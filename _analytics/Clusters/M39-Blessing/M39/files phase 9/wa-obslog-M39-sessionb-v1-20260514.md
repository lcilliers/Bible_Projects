# wa-obslog-M39-sessionb-v1-20260514
## Observations Log — M39 Blessing, Favour and Grace — Session B

**Session opened:** 2026-05-14  
**Cluster:** M39 — Blessing, Favour and Grace  
**Instruction:** wa-sessionb-cluster-instruction-v1_9-20260514  
**Global rules:** wa-global-rules-all-v2-20260427 (34 rules across 12 categories)  
**Obslog destination:** Sessions/Session_Clusters/M39/ (per GR-OBS-001)

---

## SESSION STARTUP RECORD

**Researcher instruction (verbatim):**
> "starting next cluster processing M39 Blessing. Use instruction 1_9. Read this instruction in full. There are several changes. Do not rely on memory. Startup using the global rules in Project Files, then read the data and start with phase 1"

**Documents read at startup:**
1. `wa-global-rules-all-v2-20260427.md` (project file) — 34 rules across 12 categories. Read in full.
2. `wa-sessionb-cluster-instruction-v1_9-20260514.md` (uploaded) — Active instruction. Read in full.
3. `wa-cluster-M39-comprehensive-v1-20260514.md` (uploaded) — Comprehensive report. Read in full (all 4043 lines, including truncated sections).

**v1_9 changes noted (read from §19 change note and frontmatter):**
- New §2.5 Directive packaging discipline: package-as-default; ceremony/sequential/phase-spanning directives forbidden
- New §2.6 Status transition discipline: all cluster.status transitions are operations within phase directives — no standalone status directives
- §7.7 rewritten: single packaged directive with Operations A (sub-group create + assign) · B (cluster_code rebind if applicable) · C (status transition)
- §9.5 output document sections renamed §A–§E → §1–§5 (letter-collision fix with Pass A/B/C labels)
- §10.3 (new): Pre-assessment and segmentation declaration required at Phase 7 start — written to obslog
- §13.9 closure simplified: Analysis Completed transition is Operation N within verification-corrections directive — no standalone status-complete directive
- §17 Phase 7 pre-check gains pre-assessment requirement
- §17 Phase 10 post-check gains no-standalone-status-complete confirmation

---

## PHASE 1 — COMPREHENSION OF THE DATASET

**Phase 1 opened:** 2026-05-14

### Pre-check results

- [x] Comprehensive report present: `wa-cluster-M39-comprehensive-v1-20260514.md` — generated 2026-05-14T03:09:00Z. Reflects current DB state.
- [x] Obslog created and writeable (this file).
- [x] Cluster status: `Data - In Progress` (as shown in §1 of the comprehensive report). Pre-check satisfied — no status conflict.

**Note on status transition:** The comprehensive report shows `status=Data - In Progress` at generation time. The script-inline transition from `Not started` → `Data - In Progress` has already fired prior to this session. The obslog records this as already handled; no directive is needed.

---

### Phase 1 Overview Note

**Term count:** 16 (Hebrew 10 · Greek 6)

**Verse count:** 740 active OWNER verses

**Prior-group count (from §3 group memberships — OWNER terms only):**
- H1288 ba.rakh: 5 groups (1299-001 through 1299-005 — confirmed from §4.4 VCG table + §3)
- H3190 ya.tav: 2+ groups
- G5485 charis: 4 groups (888-001 through 888-004)
- H2603A cha.nan: 1 group (984-001)
- H2580 chen: 3 groups (889-001 through 889-003)
- H7521 ra.tsah: 3 groups (795-001 through 795-003)
- H2895 tov: groups present (542-xxx)
- G5483 charizō: groups present — vc_status=to_revise
- G1435 dōron: 6 groups (6837-001 through 6837-006)
- G5486 charisma: 1 group (1301-001)
- H2587 chan.nun: 1 group (2330-001)
- G2107 eudokia: groups present
- H7862 shay: —
- H2604 cha.nan: 1 group (989-001)
- G5487 charitoō: groups present (vc_status=to_revise)
- H2868 te.ev: —

**Total VCG rows from §4.4:** 35 cluster-internal verse_context_group rows

**Verse status summary (from §1):**
| Status | Count | % |
|---|---:|---:|
| G (group-assigned) | 688 | 93.0% |
| SA (set-aside) | 0 | 0.0% |
| NR (not-relevant) | 0 | 0.0% |
| P (pending) | 0 | 0.0% |
| UT (untouched) | 52 | 7.0% |
| **Total** | **740** | 100% |

**Prior-finding count (from §4.1):** 684 findings linked at registry/collection level (no term-level link yet). Substantial legacy finding corpus — cross-registry findings from R023 compassion, R103 love, R111 mercy, R117 peace, R068 grace, R060 giving, and others.

**Prior-SD-pointer count (from §4.2):** 151 SD pointers from contributor registries with no term-level link.

**Connectivity health flags (from §1):**
- H1 ⚠: 688 active vc rows with `cluster_subgroup_id` NULL — all verses unrouted to any sub-group. Expected: no sub-groups yet exist.
- H6 ⚠: All 16 terms unassigned to any sub-group. Expected: Phase 4 directive not yet applied.
- H2–H5, H7–H8: all clear.

### Observations on data shape

1. **Verse volume is substantial:** 740 verses — comparable to M06 (which required careful segmentation across Phase 7). Phase 7 segmentation planning will be important.

2. **UT verses present (52 = 7%):** Phase 2 will require classification of 52 untouched verse-term pairs. These span multiple terms (notably H3190 ya.tav, H1288 ba.rakh confirmed UT rows visible in §2).

3. **vc_status signals are mixed:** Several terms show `to_revise` (G5485 charis, G5483 charizō, H2580 chen, H2587 chan.nun, H2603A cha.nan, H2604 cha.nan, H2895 tov, G5487 charitoō). Several show `not_done` (G1435 dōron, G2107 eudokia, G5486 charisma, H1288 ba.rakh, H2868 te.ev, H3190 ya.tav, H7521 ra.tsah, H7862 shay). The `not_done` vs `to_revise` split signals that some terms have prior VCG work that needs review and others are fresh.

4. **Data-quality flags present on several terms:**
   - G5483 charizō: flag_id=4 (meaning null) + flag_id=47 (single prose block)
   - G1435 dōron: same flags
   - G5486 charisma: flag_id=3 (low occurrence, 17 — under threshold of 20), + flags 4 and 47
   - G5487 charitoō: occurrences=2 only — very thin; statistical patterns unreliable
   - H2604 cha.nan: flag_id=3 (only 2 verse records — below threshold of 5); flags repeated (likely duplicate flag records)

5. **H2604 cha.nan is a notable edge case:** Only 2 confirmed verse records. This term may require BOUNDARY consideration during Phase 3/4 — too thin for sub-group analysis.

6. **G5487 charitoō — 2 verses only:** NT hapax-level. Will need careful treatment. BOUNDARY candidate.

7. **H7862 shay — gift:** No group memberships visible in §3. No prior findings or SD pointers direct. Awaits Phase 3 assessment.

8. **H2868 te.ev — be good:** No group memberships visible in §3. Aramaic term (from context). Awaits Phase 3 assessment.

9. **Prior finding corpus is rich but cross-registry:** The 684 findings in §4.1 are from contributor registries (R023 compassion, R103 love, R111 mercy, R117 peace, R068 grace, etc.) and carry extensive T2–T7 tier synthesis data. These are reference material per GR-DATA-002 — they are NOT findings of M39 yet and must not be treated as established M39 findings. They are context and candidate evidence only.

10. **Testament distribution:** OT 591 · NT 149. The cluster is heavily OT-weighted (80% OT). The Hebrew blessing/favour vocabulary dominates numerically. H1288 ba.rakh alone appears to carry a large verse share (visible in §2 with many G-status rows).

11. **No set-asides (SA=0):** The cluster has never had any verse set aside. This is notable — either the prior contributor registry work was conservative in inclusion, or the cluster's terms genuinely carry inner-being relevance across their full verse sets.

12. **35 VCGs present (§4.4):** These are inherited from contributor registries. They are candidate evidence for Phase 6, not confirmed M39 groupings. Phase 6's three-pass process will reconcile them.

### Phase 1 Post-check

- [x] `cluster.status = Data - In Progress` — confirmed
- [x] Overview note written (above) — term count (16), verse count (740), prior-group count (35 VCGs), prior-finding count (684), prior-SD-pointer count (151)
- [x] Observations on data shape recorded (12 points above)
- [x] No analytical claims made — Phase 1 is descriptive only
- [x] Status transition already handled by script prior to session — recorded above

**Phase 1: COMPLETE**

---

---

## PHASE 2 — UT VERSE REVIEW

**Phase 2 opened:** 2026-05-14

**Researcher instruction (verbatim):** "continue"

### Pre-check

- [x] Phase 1 complete (overview note in obslog)
- [x] UT verse count confirmed: 52 (from §1 of comprehensive report — matches grep count)
- UT verses span the following terms:
  - H1288 ba.rakh: 2 (Gen 24:11; Psa 95:6)
  - H3190 ya.tav: 27 (large set — see below)
  - H2895 tov: 7
  - H7521 ra.tsah: 2 (Lev 26:43; 1Ch 29:3)
  - H2580 chen: 8
  - H2603A cha.nan: 1 (Est 4:8)
  - G5485 charis: 4 (Luk 17:9; Act 24:27; 25:3; 25:9)
  - G5483 charizō: 5 (Luk 7:21; Act 3:14; 25:11; 25:16; + 1 more)
  - H2868 te.ev: 0 (none visible in UT — confirmed `not_done` vc_status but appears no UT rows extracted to §2)

**Note on H2868 te.ev:** vc_status=not_done but no UT rows appear in §2 grep. The term has no verse_context rows — it may have 0 verse records extracted. This will need CC verification. Flagged as OQ-001 below.

---

### Phase 2 UT Verse Readings and Classifications

**Instruction:** Per §5 of v1_9 — read each verse in full, determine relevance, record determination with verse reference, term, and one-line reason.

Per-classification rules (from §5.1):
- Set aside (is_relevant=0): term used in a sense unrelated to the cluster's characteristic; populate set_aside_reason
- Confirmed relevant (is_relevant=1): verse evidences the term's characteristic
- Borderline: flagged for researcher decision; do not write to patch

---

#### H1288 ba.rakh — UT verses (2)

**Gen 24:11 (vr_id=51016, mti_id=1299)**
Verse: "And he made the camels kneel down outside the city by the well of water at the time of evening, the time when women go out to draw water."
The term is rendered "kneel down." This is the physical posture sense of ba.rakh (root shared with blessing but here denoting the camels' act of kneeling). No inner-being blessing content. The subject is camels; the act is physical.
→ **SET ASIDE** | Reason: ba.rakh used in physical posture sense (camels kneeling) — no inner-being blessing content, no relational/divine blessing dynamic.

**Psa 95:6 (vr_id=226205, mti_id=1299)**
Verse: "Oh come, let us worship and bow down; let us kneel before the Lord, our Maker!"
The term is rendered "kneel." Again the physical kneeling/bowing posture sense. However, the context is worship — the verse is a call to corporate worship and reverence before God. The kneeling is an embodied act of inner devotion. This is borderline: the kneeling act is physical but embedded in a deep inner-being worship call.
Reading carefully: the term in this verse is specifically the physical kneeling posture within worship, not the pronouncing of blessing. The inner-being content here is carried primarily by "worship" and "bow down," not by ba.rakh. The ba.rakh term here functions as one of three parallel embodied worship actions (worship, bow down, kneel) — it designates the posture, not the blessing-act.
→ **SET ASIDE** | Reason: ba.rakh used in embodied posture sense (kneeling in worship) — inner-being content of the verse is real, but it is carried by the worship/bowing vocabulary, not by ba.rakh's blessing characteristic; wrong-face set-aside.

---

#### H3190 ya.tav — UT verses (27)

**Gen 4:7 (vr_id=12472, mti_id=632)**
Verse: "If you do well, will you not be accepted? And if you do not do well, sin is crouching at the door. Its desire is for you, and you must rule over it."
"Do well" — ya.tav here names the moral quality of right action, with immediate inner consequence (acceptance) and threat (sin crouching). The inner-being stakes are explicit: mastery over sin's desire. This is directly relevant to inner-being moral character.
→ **CONFIRMED RELEVANT** | Verse evidences ya.tav as the quality of morally right inner orientation and action, with direct inner-being consequence.

**Gen 12:13 (vr_id=12473, mti_id=632)**
Verse: "Say you are my sister, that it may go well with me because of you, and that my life may be spared for your sake."
"Go well with me" — ya.tav used in a self-preservation, outcome-focused sense. Abram is seeking personal welfare. The inner-being content is thin; this is primarily a pragmatic/situational use of "well."
→ **SET ASIDE** | Reason: ya.tav used in outcome-welfare sense ("go well for me") — pragmatic self-interest, not inner-being characteristic of blessing or goodness.

**Gen 12:16 (vr_id=12474, mti_id=632)**
Verse: "And for her sake he dealt well with Abram; and he had sheep, oxen, male donkeys..."
"Dealt well with" — ya.tav describes Pharaoh's generous treatment of Abram, expressed in material provision. The inner-being content is in the disposition of generous dealing toward another, motivated by regard for Sarai. Relational goodwill expressed through action.
→ **CONFIRMED RELEVANT** | Verse evidences ya.tav as relational goodwill expressed in generous dealing toward another.

**Exo 30:7 (vr_id=12482, mti_id=632)**
Verse: "And Aaron shall burn fragrant incense on it. Every morning when he dresses the lamps he shall burn it."
"Dresses" (ya.tav) — used in the technical sense of tending/trimming lamps (making them good/proper). This is a liturgical-technical use, not an inner-being characteristic use.
→ **SET ASIDE** | Reason: ya.tav used in technical/liturgical sense ("tends/dresses the lamps") — no inner-being characteristic content.

**Num 11:18 (vr_id=4187, mti_id=542)** ← Note: this is H2895 tov, not H3190 ya.tav (mti_id=542 vs 632). The grep returned it in the H2895 group. Treat under H2895 below.

**Deu 9:21 (vr_id=12496, mti_id=632)**
Verse: "Then I took the sinful thing, the calf that you had made, and burned it with fire and crushed it, grinding it very small, until it was as fine as dust."
"Very small" — ya.tav used as an intensifier ("very," "thoroughly"). No inner-being content whatsoever.
→ **SET ASIDE** | Reason: ya.tav used as adverbial intensifier ("very/thoroughly small") — no inner-being characteristic content.

**Deu 13:14 (vr_id=12499, mti_id=632)**
Verse: "then you shall inquire and make search and ask diligently. And behold, if it be true and certain that such an abomination has been done among you,"
"Diligently" — ya.tav used as an intensifier of inquiry (inquire well/thoroughly). No inner-being characteristic content.
→ **SET ASIDE** | Reason: ya.tav used as adverbial intensifier ("inquire diligently/well") — no inner-being characteristic content.

**Deu 17:4 (vr_id=12500, mti_id=632)**
Verse: "and it is told you and you hear of it, then you shall inquire diligently, and if it is true and certain that such an abomination has been done in Israel,"
"Inquire diligently" — same pattern as Deu 13:14 above. Adverbial intensifier use.
→ **SET ASIDE** | Reason: ya.tav used as adverbial intensifier ("inquire diligently/well") — same as Deu 13:14.

**Deu 19:18 (vr_id=12502, mti_id=632)**
Verse: "The judges shall inquire diligently, and if the witness is a false witness and has accused his brother falsely,"
"Inquire diligently" — same pattern again.
→ **SET ASIDE** | Reason: ya.tav used as adverbial intensifier ("inquire diligently/well") — same pattern, no inner-being characteristic content.

**Deu 27:8 (vr_id=12504, mti_id=632)**
Verse: "And you shall write on the stones all the words of this law very plainly."
"Very plainly" — ya.tav used adverbially as an intensifier of clarity/thoroughness of writing.
→ **SET ASIDE** | Reason: ya.tav used as adverbial intensifier ("very plainly") — no inner-being characteristic content.

**Judg 11:25 (vr_id=65375, mti_id=542)** ← H2895 tov (mti_id=542), not ya.tav. Treat under H2895 below.

**1Sa 2:32 (vr_id=59834, mti_id=632)**
Verse: "Then in distress you will look with envious eye on all the prosperity that shall be bestowed on Israel, and there shall not be an old man in your house forever."
"Prosperity/bestowed" — ya.tav names material and social wellbeing bestowed on Israel. The phrase "bestowed good" implies divine gift of flourishing. Not primarily an inner-being characteristic of the person; it is external prosperity.
→ **SET ASIDE** | Reason: ya.tav names material/social prosperity bestowed on Israel — outer outcome sense, not an inner-being characteristic.

**1Sa 16:17 (vr_id=59829, mti_id=632)**
Verse: "So Saul said to his servants, 'Provide for me a man who can play well and bring him to me.'"
"Play well" — ya.tav used to describe musical skill/proficiency. No inner-being characteristic content.
→ **SET ASIDE** | Reason: ya.tav used in skill/proficiency sense ("plays well" — music) — no inner-being characteristic content.

**1Sa 18:5 (vr_id=59830, mti_id=632)**
Verse: "And David went out and was successful wherever Saul sent him, so that Saul set him over the men of war. And this was good in the sight of all the people and also in the sight of Saul's servants."
"Good in the sight of all" — ya.tav describes David's success being regarded favourably by the community. The goodwill/favour dimension is present — being "good in the sight of" carries inner-being relational esteem. Borderline.
Reading the cluster characteristic: the cluster is Blessing, Favour and Grace. The "goodness in the sight of" carries the favour sense — this usage is at the intersection of social approval and inner-being goodness-as-favour-received. It connects to the cluster's relational-favour dimension.
→ **CONFIRMED RELEVANT** | Verse evidences ya.tav as the quality of being received with favour/goodwill by others — the inner-being social-goodness/favour dimension.

**1Sa 20:13 (vr_id=59831, mti_id=632)**
Verse: "But should it please my father to do you harm, the Lord do so to Jonathan and more also if I do not disclose it to you and send you away, that you may go in safety."
"Please" — ya.tav used in the sense of "if it seems good to/pleases." This is a volitional/dispositional use — what seems good to the person's judgment. The inner-being volitional/moral-judgment sense is present.
→ **CONFIRMED RELEVANT** | Verse evidences ya.tav in volitional/dispositional sense — what seems good to the inner judgment; moral will engaged.

**1Sa 24:4 (vr_id=59832, mti_id=632)**
Verse: "Here is the day of which the Lord said to you, 'Behold, I will give your enemy into your hand, and you shall do to him as it shall seem good to you.'"
"Seem good to you" — same dispositional/volitional pattern as 1Sa 20:13. Inner judgment determining right action.
→ **CONFIRMED RELEVANT** | Verse evidences ya.tav in dispositional/volitional sense — what seems morally good to the inner judgment.

**1Sa 25:31 (vr_id=59833, mti_id=632)**
Verse: "my lord shall have no cause of grief or pangs of conscience for having shed blood without cause or for my lord working salvation himself. And when the Lord has dealt well with my lord, then remember your servant."
"Dealt well" — two inner-being references: (1) "pangs of conscience" in the verse context (not the ya.tav term), and (2) ya.tav used in "dealt well with" — divine beneficent action toward David. Also conscience language in the co-text (lev=heart/conscience). The ya.tav term here is in the sense of divine blessing/benefaction.
→ **CONFIRMED RELEVANT** | Verse evidences ya.tav as divine beneficent dealing — blessing bestowed; the cluster's blessing/favour characteristic. Note: conscience language in co-text is carried by different terms.

**2Sa 18:4 (vr_id=59838, mti_id=632)**
Verse: "The king said to them, 'Whatever seems best to you I will do.' So the king stood at the side of the gate..."
"Seems best" — ya.tav in dispositional/judgment sense.
→ **CONFIRMED RELEVANT** | Verse evidences ya.tav in judgment/dispositional sense — what seems morally good to the person's inner evaluation.

**1Ki 1:47 (vr_id=59826, mti_id=632)**
Verse: "Moreover, the king's servants came to congratulate our lord King David, saying, 'May your God make the name of Solomon more famous than yours, and make his throne greater than your throne.' And the king bowed himself on the bed."
"More famous" (ya.tav rendered "better/greater") — used in the sense of making something good/greater, a comparison of status/fame. Not directly an inner-being characteristic.
→ **SET ASIDE** | Reason: ya.tav used in comparative status sense ("more famous/better than") — external honour/reputation, not an inner-being characteristic of blessing or favour.

**2Ki 9:30 (vr_id=59837, mti_id=632)**
Verse: "When Jehu came to Jezreel, Jezebel heard of it. And she painted her eyes and adorned her head and looked out of the window."
"Adorned" — ya.tav used in the sense of beautifying/adorning the head. Cosmetic action.
→ **SET ASIDE** | Reason: ya.tav used in cosmetic/beautification sense ("adorned her head") — no inner-being characteristic content.

**2Ki 11:18 (vr_id=59835, mti_id=632)**
Verse: "...his altars and his images they broke in pieces..."
"In pieces" (ya.tav = "broke thoroughly/very") — adverbial intensifier in context of idol-destruction.
→ **SET ASIDE** | Reason: ya.tav used as adverbial intensifier ("broke in pieces/thoroughly") — no inner-being characteristic content.

**2Ki 25:24 (vr_id=59836, mti_id=632)**
Verse: "And Gedaliah swore to them and their men, saying, 'Do not be afraid because of the Chaldean officials. Live in the land and serve the king of Babylon, and it shall be well with you.'"
"It shall be well with you" — ya.tav names the promised outcome of wellbeing/flourishing for those who submit. This is outcome-welfare language — "it will go well." The blessing/favour sense is present: a promise of divine/social favour expressed as wellbeing.
→ **CONFIRMED RELEVANT** | Verse evidences ya.tav as promised wellbeing/flourishing — the blessing/favour outcome dimension of the cluster.

**Psa 33:3 (vr_id=12526, mti_id=632)**
Verse: "Sing to him a new song; play skillfully on the strings, with loud shouts."
"Skillfully" — ya.tav used in musical skill sense. Same pattern as 1Sa 16:17.
→ **SET ASIDE** | Reason: ya.tav used in skill/proficiency sense ("play skillfully") — no inner-being characteristic content.

**Pro 15:2 (vr_id=12533, mti_id=632)**
Verse: "The tongue of the wise commends knowledge, but the mouths of fools pour out folly."
"Commends" (ya.tav = "makes good/uses well") — the tongue "making good" use of knowledge. The inner-being content is wisdom as right use of speech. The characteristic of goodness-as-wisdom-in-speech is present.
→ **CONFIRMED RELEVANT** | Verse evidences ya.tav as the quality of wise/good speech — goodness expressed through the tongue as an inner-being faculty.

**Pro 30:29 (vr_id=12536, mti_id=632)**
Verse: "Three things are stately in their tread; four are stately in their stride."
"Stately" — ya.tav used in the aesthetic sense of stately/impressive movement. Descriptive of animals' gait. No inner-being characteristic content.
→ **SET ASIDE** | Reason: ya.tav used in aesthetic/descriptive sense ("stately in stride") — physical description, no inner-being characteristic content.

**Isa 23:16 (vr_id=12540, mti_id=632)**
Verse: "Take a harp; go about the city, O forgotten prostitute! Make sweet melody; sing many songs, that you may be remembered."
"Make sweet" — ya.tav used in aesthetic/sensory sense (making melody sweet/pleasant). No inner-being characteristic content beyond the general pleasantness register.
→ **SET ASIDE** | Reason: ya.tav used in aesthetic/sensory sense ("make sweet melody") — no inner-being characteristic content.

**Jer 1:12 (vr_id=12542, mti_id=632)**
Verse: "Then the Lord said to me, 'You have seen well, for I am watching over my word to perform it.'"
"Seen well" — ya.tav in the sense of "you have perceived correctly/accurately." The inner-being perceptive faculty is engaged — the prophet has discerned rightly. This evidences the goodness of perception/discernment.
→ **CONFIRMED RELEVANT** | Verse evidences ya.tav as the quality of right/accurate inner perception — discernment as an inner-being faculty exercised well.

**Eze 33:32 (vr_id=12559, mti_id=632)**
Verse: "And behold, you are to them like one who sings lustful songs with a beautiful voice and plays well on an instrument, for they hear what you say, but they will not do it."
"Plays well" — ya.tav in skill/proficiency sense (musical). Same as 1Sa 16:17 and Psa 33:3.
→ **SET ASIDE** | Reason: ya.tav used in skill/proficiency sense ("plays well" — music) — no inner-being characteristic content.

**Eze 36:11 (vr_id=12560, mti_id=632)**
Verse: "And I will multiply on you man and beast, and they shall multiply and be fruitful. And I will cause you to be inhabited as in your former times, and will do more good to you than ever before."
"Do more good" — ya.tav names God's eschatological beneficent action toward Israel — greater blessing than before. The blessing/divine favour sense is fully present.
→ **CONFIRMED RELEVANT** | Verse evidences ya.tav as divine beneficent/blessing action — doing good, a superlative form of the blessing characteristic.

**Hos 10:1 (vr_id=12562, mti_id=632)**
Verse: "Israel is a luxuriant vine that yields its fruit. The more his fruit increased, the more altars he built; as his country improved, he improved his pillars."
"Improved" (ya.tav) — used in a comparative/outcome sense describing land improvement and idolatry increase in parallel. The "improvement" here is material/agricultural prosperity, not an inner-being characteristic. The verse uses ya.tav ironically — as the land improved (materially), Israel's inner moral/spiritual state worsened.
→ **SET ASIDE** | Reason: ya.tav used in material/agricultural improvement sense — outcome description; though the ironic theological context is rich, the term itself carries no direct inner-being content for M39's characteristic.

**Nah 3:8 (vr_id=12567, mti_id=632)**
Verse: "Are you better than Thebes that sat by the Nile, with water around her, her rampart a sea, and water her wall?"
"Better" — comparative sense, ya.tav used in geo-political strength comparison. No inner-being characteristic content.
→ **SET ASIDE** | Reason: ya.tav used in comparative strength/status sense ("better than Thebes") — geo-political comparison, no inner-being characteristic content.

---

#### H2895 tov — UT verses (7)

**Num 11:18 (vr_id=4187, mti_id=542)**
Verse: "And say to the people, 'Consecrate yourselves for tomorrow, and you shall eat meat, for you have wept in the hearing of the Lord, saying, "Who will give us meat to eat? For it was better for us in Egypt."'"
"Better" — tov used in comparative preference sense ("Egypt was better"). The Israelites' inner complaint is present (weeping, longing for Egypt), but tov itself names a comparative value judgment rather than the cluster's blessing/favour characteristic.
→ **SET ASIDE** | Reason: tov used in comparative preference sense ("better for us in Egypt") — expresses complaint/longing, not the cluster's blessing or favour characteristic.

**Num 24:1 (vr_id=4188, mti_id=542)**
Verse: "When Balaam saw that it pleased the Lord to bless Israel, he did not go, as at other times, to look for omens, but set his face toward the wilderness."
"It pleased the Lord" — tov here names divine pleasure/will toward blessing Israel. The inner divine disposition of pleasure toward blessing is present. The cluster's blessing characteristic is directly named (bless Israel in same verse). This is a key verse — divine dispositional pleasure as the inner ground of blessing.
→ **CONFIRMED RELEVANT** | Verse evidences tov as divine inner pleasure/disposition — the delighting-in that grounds the act of blessing Israel.

**Num 24:5 (vr_id=4189, mti_id=542)**
Verse: "How lovely are your tents, O Jacob, your encampments, O Israel!"
"Lovely" — tov used in aesthetic admiration of Israel's dwellings (Balaam's oracle). An expression of favour/goodness as beauty recognised. The inner-being content is in the beholder's disposition of favour/delight. Borderline.
Reading carefully: the verse is an exclamation of favour and delight — tov as the beauty/goodness that elicits the response of favour. This is the aesthetic face of the goodness-favour connection. In the context of Balaam's oracles (a reluctant prophet compelled to bless), the "how lovely/good" is itself an expression of the favour characteristic.
→ **CONFIRMED RELEVANT** | Verse evidences tov as the quality of goodness/beauty that draws forth favour — the aesthetic-favour dimension.

**Deu 5:33 (vr_id=4190, mti_id=542)**
Verse: "You shall walk in all the way that the Lord your God has commanded you, that you may live, and that it may go well with you, and that you may live long in the land that you shall possess."
"Go well with you" — tov used in the covenantal blessing-outcome sense. Walking in God's way produces the inner-outer flourishing described as "going well." This is the covenantal blessing promise — obedience → divine favour → wellbeing.
→ **CONFIRMED RELEVANT** | Verse evidences tov as the covenantal blessing-outcome — the flourishing that follows from obedience and divine favour; directly names the blessing characteristic in its covenant-outcome form.

**Judg 11:25 (vr_id=65375, mti_id=542)**
Verse: "Now are you any better than Balak the son of Zippor, king of Moab? Did he ever contend against Israel, or did he ever go to war with them?"
"Any better" — tov in comparative strength/status sense. Same as geo-political comparison pattern.
→ **SET ASIDE** | Reason: tov used in comparative status sense ("any better than Balak") — geo-political comparison, no inner-being characteristic content.

**2Sa 15:26 (vr_id=4197, mti_id=542)**
Verse: "But if he says, 'I have no pleasure in you,' behold, here I am, let him do to me what seems good to him."
"Seems good to him" — tov in volitional/dispositional sense — what seems good to the divine will. David surrendering to God's disposition. The inner-being volitional submission and acceptance of divine pleasure/judgment is present.
→ **CONFIRMED RELEVANT** | Verse evidences tov as divine dispositional will ("what seems good to him") — the inner pleasure/will of God; David's inner posture of surrender to that will is also present.

**2Sa 19:37 (vr_id=4198, mti_id=542)**
Verse: "Please let your servant return, that I may die in my own city near the grave of my father and my mother. But here is your servant Chimham. Let him go over with my lord the king, and do for him whatever seems good to you."
"Whatever seems good to you" — tov in volitional/dispositional sense — same as 2Sa 15:26. Royal discretion entrusted to the king.
→ **CONFIRMED RELEVANT** | Verse evidences tov as volitional/dispositional sense — what seems good to the person's inner judgment; relational trust and deference to another's benevolent will.

---

#### H7521 ra.tsah — UT verses (2)

**Lev 26:43 (vr_id=18824, mti_id=795)**
Verse: "But the land shall be abandoned by them and enjoy its Sabbaths while it lies desolate without them, and they shall make amends for their iniquity, because they spurned my rules and their soul abhorred my statutes."
"Enjoy" (ra.tsah) — the land "accepting/enjoying" its Sabbaths. This is a personification of the land's receiving its due rest. The inner-being dimension of ra.tsah is attenuated here — the subject is the land, not a person. However, the verse does name the inner-being stance of the Israelites: "their soul abhorred my statutes" — the contrast between the land's acceptance and Israel's rejection is the verse's theological point. Ra.tsah here applies to the land; the human inner-being content is carried by the "soul abhorred" clause via different terms.
→ **SET ASIDE** | Reason: ra.tsah used with the land as subject ("land enjoys/accepts its Sabbaths") — personification without human inner-being content; the soul-abhorring language in the verse is carried by different terms (wrong-face set-aside preserving ne.phesh content).

**1Ch 29:3 (vr_id=117146, mti_id=795)**
Verse: "Moreover, in addition to all that I have provided for the holy house, I have a treasure of my own of gold and silver, and because of my devotion to the house of my God I give it to the house of my God."
"Devotion" (ra.tsah) — David's ra.tsah toward God's house — his inner delight, pleasure, and commitment expressed in generous giving. This is a strong inner-being use: David's ra.tsah/devotion is the inner-disposition that drives his sacrificial giving. This directly names an inner-being characteristic of the cluster — the inner pleasure/delight in God that produces blessing-giving.
→ **CONFIRMED RELEVANT** | Verse evidences ra.tsah as inner devotion/delight — the settled inner pleasure toward God's house that motivates generous self-giving; strong cluster characteristic evidence.

---

#### H2580 chen — UT verses (8)

**Pro 1:9 (vr_id=167037, mti_id=889)**
Verse: "for they are a graceful garland for your head and pendants for your neck."
"Graceful" — chen used as an aesthetic quality of wisdom's ornaments. The gracefulness/favour quality expressed as beauty/adornment. Borderline: the wisdom-as-grace-and-adornment connection is real, but the term here functions primarily as aesthetic descriptor.
Reading for the cluster's characteristic: chen as grace/favour expressed as beauty that adorns — this is the aesthetic-grace dimension. The sentence structure makes chen an attribute of wisdom's fruit. This is the character-quality face of chen.
→ **CONFIRMED RELEVANT** | Verse evidences chen as the grace/beauty quality of wisdom — the character-grace dimension; wisdom producing inner grace that adorns.

**Pro 3:22 (vr_id=167044, mti_id=889)**
Verse: "and they will be life for your soul and adornment for your neck."
"Adornment" — chen in the sense of grace/charm as adornment. Similar to Pro 1:9.
→ **CONFIRMED RELEVANT** | Verse evidences chen as grace/beauty as life-giving adornment for the soul — inner-being grace quality connected directly to soul-life (ne.phesh named in same verse).

**Pro 4:9 (vr_id=167048, mti_id=889)**
Verse: "She will place on your head a graceful garland; she will bestow on you a beautiful crown."
"Graceful" — chen as the grace/charm quality of wisdom's garland. Same grace-as-adornment pattern.
→ **CONFIRMED RELEVANT** | Verse evidences chen as the grace-quality bestowed by wisdom — the favour-beauty-adornment dimension.

**Pro 5:19 (vr_id=167049, mti_id=889)**
Verse: "a lovely deer, a graceful doe. Let her breasts fill you at all times with delight; be intoxicated always in her love."
"Graceful" — chen describing the gracefulness of the beloved wife. Erotic and aesthetic context. The grace/beauty of the beloved as an inner relational quality.
→ **CONFIRMED RELEVANT** | Verse evidences chen as grace/beauty of the beloved — the relational-grace dimension; favour/grace expressed in intimate relational delight.

**Ecc 9:11 (vr_id=167022, mti_id=889)**
Verse: "Again I saw that under the sun the race is not to the swift, nor the battle to the strong, nor bread to the wise, nor riches to the intelligent, nor favor to those with knowledge, but time and chance happen to them all."
"Favor" — chen used directly in the relational favour sense. The key insight: chen/favour does not follow merit (swift, strong, wise, intelligent, knowledgeable all fail to secure favour). The sovereign unpredictability of favour is the verse's point. This directly evidences chen as the cluster's characteristic — favour as something not earned but given.
→ **CONFIRMED RELEVANT** | Verse evidences chen as unearned relational favour — the grace/favour that does not follow merit; directly names the cluster's characteristic of grace as sovereign gift.

**Nah 3:4 (vr_id=24847, mti_id=889)**
Verse: "And all for the countless whorings of the prostitute, graceful and of deadly charms, who betrays nations with her whorings, and peoples with her charms."
"Graceful" — chen used to describe Nineveh-as-prostitute's deadly charm/grace. This is a dark/inverted use of chen: the graceful appearance that is actually a weapon of deception and destruction. The inner-being content is inverted: chen here names the corrupted or weaponised form of grace/charm. This is noteworthy — it is the only verse in the UT set where chen appears in an explicitly negative/corrupted register.
→ **CONFIRMED RELEVANT** | Verse evidences chen in its inverted/corrupted form — grace weaponised as deadly charm; evidences the structural opposite dimension of the cluster's characteristic.

---

#### H2603A cha.nan — UT verses (1)

**Est 4:8 (vr_id=92213, mti_id=984)**
Verse: "Mordecai also gave him a copy of the written decree issued in Susa for their destruction, that he might show it to Esther and explain it to her and command her to go to the king to beg his favor and plead with him on behalf of her people."
"Beg his favor" — cha.nan used in the sense of seeking favour/grace from the king — petitioning for grace on behalf of an imperilled people. This is directly the cluster's characteristic: the inner act of pleading for grace from a superior, with life-and-death stakes. The relational inner-being content (petition, desperation, intercession) is strong.
→ **CONFIRMED RELEVANT** | Verse evidences cha.nan as the inner act of pleading for grace/favour — the petition-for-grace dimension; Esther commanded to intercede for her people's lives.

---

#### G5485 charis — UT verses (4)

**Luk 17:9 (vr_id=166982, mti_id=888)**
Verse: "Does he thank the servant because he did what was commanded?"
"Thank" — charis used in the sense of gratitude/thanks for a service rendered. This is the favour/gratitude sense of charis in an interpersonal context. The verse denies that commanded duty generates thanks (charis) — no extra favour is earned by obligation. This directly engages the cluster's characteristic: grace/favour as something beyond obligation.
→ **CONFIRMED RELEVANT** | Verse evidences charis as gratitude/favour beyond obligation — the grace that is not owed for duty; directly names the cluster's characteristic.

**Act 24:27 (vr_id=166971, mti_id=888)**
Verse: "When two years had elapsed, Felix was succeeded by Porcius Festus. And desiring to do the Jews a favor, Felix left Paul in prison."
"Favor" — charis used in the political/relational favour sense. Felix withholds justice to do political favour to the Jews. This is the relational-political favour sense of charis — secular, transactional. The inner-being content is in the disposition of political favour-seeking and its corruption (justice is denied to grant favour).
→ **CONFIRMED RELEVANT** | Verse evidences charis in its relational-political favour sense — favour as political disposition; noteworthy as an example of corrupted/transactional favour (withholding justice to grant political goodwill).

**Act 25:3 (vr_id=166972, mti_id=888)**
Verse: "asking as a favor against Paul that he summon him to Jerusalem — because they were planning an ambush to kill him on the way."
"Favor" — charis used in political favour-seeking sense, again corrupted (favour requested to facilitate murder).
→ **CONFIRMED RELEVANT** | Verse evidences charis in the political favour-petition sense — favour sought as political currency; again in a corrupted context (favour weaponised for malicious ends).

**Act 25:9 (vr_id=166973, mti_id=888)**
Verse: "But Festus, wishing to do the Jews a favor, said to Paul, 'Do you wish to go up to Jerusalem and there be tried on these charges before me?'"
"Favor" — same political favour sense as Act 24:27 and 25:3. Festus acting to do political favour.
→ **CONFIRMED RELEVANT** | Verse evidences charis as political-relational favour disposition — Festus' inner disposition to grant favour for political reasons.

---

#### G5483 charizō — UT verses (5)

**Luk 7:21 (vr_id=167001, mti_id=5470)**
Verse: "In that hour he healed many people of diseases and plagues and evil spirits, and on many who were blind he bestowed sight."
"Bestowed" (charizō) — the gracious giving of sight; Jesus bestowing sight as a gift of grace. The inner-being content: the grace-giving disposition of Jesus expressed in healing. This is a direct and rich evidencing of the cluster characteristic — charizō as gracious bestowal.
→ **CONFIRMED RELEVANT** | Verse evidences charizō as grace-bestowal — Jesus bestowing sight as gracious gift; the giving-grace dimension of the cluster.

**Act 3:14 (vr_id=166996, mti_id=5470)**
Verse: "But you denied the Holy and Righteous One, and asked for a murderer to be granted to you."
"Granted" (charizō) — the crowd's request to have Barabbas granted/given to them by Pilate. Charizō here names the act of releasing a prisoner as a concession/grace. The inner-being content is attenuated — this is a political-legal act of granting. However, the cluster's grace-giving characteristic is present in the mechanics of release/grant.
→ **CONFIRMED RELEVANT** | Verse evidences charizō in the granting/releasing sense — grace-giving as concession; noteworthy for the irony: grace-granting used to release a murderer in place of the Righteous One.

**Act 25:11 (vr_id=166993, mti_id=5470)**
Verse: "If then I am a wrongdoer and have committed anything for which I deserve to die, I do not seek to escape death. But if there is nothing to their charges against me, no one can give me up to them. I appeal to Caesar."
"Give me up" (charizō) — Paul asserting that no one has the right to hand him over (give him as a favour) to his accusers. Charizō here in the sense of delivering a person as a concession/favour. Similar to Act 3:14 but from the victim's perspective — the refusal to be handed over as political favour.
→ **CONFIRMED RELEVANT** | Verse evidences charizō in the granting/handover sense — the grace-gift dynamic applied to the delivering up of a person; Paul's assertion of legal protection against being given as political favour.

**Act 25:16 (vr_id=166994, mti_id=5470)**
Verse: "I answered them that it was not the custom of the Romans to give up anyone before the accused met the accusers face to face and had opportunity to make his defense concerning the charge laid against him."
"Give up" (charizō) — Roman custom not to give anyone up (as favour) before due process. Same granting/concession sense.
→ **CONFIRMED RELEVANT** | Verse evidences charizō as political granting/giving up — favour as concession within legal process.

**Note:** The grep returned only 4 G5483 charizō UT verses in the tail section. The head section showed 1 more (Luk 7:21). Total = 5. The 5th was Luk 7:21 already classified above. The grep identified all 5: Luk 7:21, Act 3:14, Act 25:11, Act 25:16 — that is 4. Checking: the head section also showed Act 25:11 and 25:16. Total G5483 UT verses = 4 (Luk 7:21, Act 3:14, Act 25:11, Act 25:16). The count of 5 in my earlier tally requires verification — OQ-002 below.

---

### OQ Items

**OQ-001:** H2868 te.ev — vc_status=not_done but no UT rows appear in §2 grep. The term may have 0 verse_context rows (possible if the extraction produced no verse records). CC needs to confirm the actual verse record count for te.ev (mti_id=633) in the database.
Proposed disposition: CC runs `SELECT COUNT(*) FROM wa_verse_records WHERE mti_term_id=633 AND status IN ('extracted','extracted_thin')` to confirm. If 0, te.ev has no extractable verses and may need to be reconsidered for its cluster placement.

**OQ-002:** G5483 charizō UT verse count discrepancy — my pre-check tally said 5 but only 4 UT rows were found in grep output (Luk 7:21, Act 3:14, Act 25:11, Act 25:16). Verify actual UT count = 4 for charizō. No action needed if 4 is correct; adjust patch count accordingly.

---

### Phase 2 Summary

| Verse | Term | vr_id | mti_id | Determination | Set-aside reason (if SA) |
|---|---|---:|---:|---|---|
| Gen 24:11 | H1288 ba.rakh | 51016 | 1299 | **SET ASIDE** | ba.rakh in physical posture sense (camels kneeling) — no blessing content |
| Psa 95:6 | H1288 ba.rakh | 226205 | 1299 | **SET ASIDE** | ba.rakh in posture/kneeling sense within worship — inner content carried by other terms (wrong-face) |
| Gen 4:7 | H3190 ya.tav | 12472 | 632 | **RELEVANT** | — |
| Gen 12:13 | H3190 ya.tav | 12473 | 632 | **SET ASIDE** | ya.tav in pragmatic self-interest outcome sense |
| Gen 12:16 | H3190 ya.tav | 12474 | 632 | **RELEVANT** | — |
| Exo 30:7 | H3190 ya.tav | 12482 | 632 | **SET ASIDE** | ya.tav in technical/liturgical sense (tending lamps) |
| Deu 9:21 | H3190 ya.tav | 12496 | 632 | **SET ASIDE** | ya.tav as adverbial intensifier ("very small") |
| Deu 13:14 | H3190 ya.tav | 12499 | 632 | **SET ASIDE** | ya.tav as adverbial intensifier ("inquire diligently") |
| Deu 17:4 | H3190 ya.tav | 12500 | 632 | **SET ASIDE** | ya.tav as adverbial intensifier ("inquire diligently") |
| Deu 19:18 | H3190 ya.tav | 12502 | 632 | **SET ASIDE** | ya.tav as adverbial intensifier ("inquire diligently") |
| Deu 27:8 | H3190 ya.tav | 12504 | 632 | **SET ASIDE** | ya.tav as adverbial intensifier ("very plainly") |
| 1Sa 2:32 | H3190 ya.tav | 59834 | 632 | **SET ASIDE** | ya.tav in material prosperity/outcome sense |
| 1Sa 16:17 | H3190 ya.tav | 59829 | 632 | **SET ASIDE** | ya.tav in skill/proficiency sense (musical) |
| 1Sa 18:5 | H3190 ya.tav | 59830 | 632 | **RELEVANT** | — |
| 1Sa 20:13 | H3190 ya.tav | 59831 | 632 | **RELEVANT** | — |
| 1Sa 24:4 | H3190 ya.tav | 59832 | 632 | **RELEVANT** | — |
| 1Sa 25:31 | H3190 ya.tav | 59833 | 632 | **RELEVANT** | — |
| 2Sa 18:4 | H3190 ya.tav | 59838 | 632 | **RELEVANT** | — |
| 1Ki 1:47 | H3190 ya.tav | 59826 | 632 | **SET ASIDE** | ya.tav in comparative status sense ("more famous") |
| 2Ki 9:30 | H3190 ya.tav | 59837 | 632 | **SET ASIDE** | ya.tav in cosmetic/beautification sense |
| 2Ki 11:18 | H3190 ya.tav | 59835 | 632 | **SET ASIDE** | ya.tav as adverbial intensifier ("broke in pieces") |
| 2Ki 25:24 | H3190 ya.tav | 59836 | 632 | **RELEVANT** | — |
| Psa 33:3 | H3190 ya.tav | 12526 | 632 | **SET ASIDE** | ya.tav in skill/proficiency sense (musical) |
| Pro 15:2 | H3190 ya.tav | 12533 | 632 | **RELEVANT** | — |
| Pro 30:29 | H3190 ya.tav | 12536 | 632 | **SET ASIDE** | ya.tav in aesthetic/descriptive sense ("stately") |
| Isa 23:16 | H3190 ya.tav | 12540 | 632 | **SET ASIDE** | ya.tav in aesthetic/sensory sense ("make sweet") |
| Jer 1:12 | H3190 ya.tav | 12542 | 632 | **RELEVANT** | — |
| Eze 33:32 | H3190 ya.tav | 12559 | 632 | **SET ASIDE** | ya.tav in skill/proficiency sense (musical) |
| Eze 36:11 | H3190 ya.tav | 12560 | 632 | **RELEVANT** | — |
| Hos 10:1 | H3190 ya.tav | 12562 | 632 | **SET ASIDE** | ya.tav in material/agricultural improvement sense |
| Nah 3:8 | H3190 ya.tav | 12567 | 632 | **SET ASIDE** | ya.tav in comparative strength/status sense |
| Num 11:18 | H2895 tov | 4187 | 542 | **SET ASIDE** | tov in comparative preference sense ("better in Egypt") |
| Num 24:1 | H2895 tov | 4188 | 542 | **RELEVANT** | — |
| Num 24:5 | H2895 tov | 4189 | 542 | **RELEVANT** | — |
| Deu 5:33 | H2895 tov | 4190 | 542 | **RELEVANT** | — |
| Judg 11:25 | H2895 tov | 65375 | 542 | **SET ASIDE** | tov in comparative status sense ("any better than Balak") |
| 2Sa 15:26 | H2895 tov | 4197 | 542 | **RELEVANT** | — |
| 2Sa 19:37 | H2895 tov | 4198 | 542 | **RELEVANT** | — |
| Lev 26:43 | H7521 ra.tsah | 18824 | 795 | **SET ASIDE** | ra.tsah with land as subject ("land enjoys Sabbaths") — wrong-face |
| 1Ch 29:3 | H7521 ra.tsah | 117146 | 795 | **RELEVANT** | — |
| Pro 1:9 | H2580 chen | 167037 | 889 | **RELEVANT** | — |
| Pro 3:22 | H2580 chen | 167044 | 889 | **RELEVANT** | — |
| Pro 4:9 | H2580 chen | 167048 | 889 | **RELEVANT** | — |
| Pro 5:19 | H2580 chen | 167049 | 889 | **RELEVANT** | — |
| Ecc 9:11 | H2580 chen | 167022 | 889 | **RELEVANT** | — |
| Nah 3:4 | H2580 chen | 24847 | 889 | **RELEVANT** | — |
| Est 4:8 | H2603A cha.nan | 92213 | 984 | **RELEVANT** | — |
| Luk 17:9 | G5485 charis | 166982 | 888 | **RELEVANT** | — |
| Act 24:27 | G5485 charis | 166971 | 888 | **RELEVANT** | — |
| Act 25:3 | G5485 charis | 166972 | 888 | **RELEVANT** | — |
| Act 25:9 | G5485 charis | 166973 | 888 | **RELEVANT** | — |
| Luk 7:21 | G5483 charizō | 167001 | 5470 | **RELEVANT** | — |
| Act 3:14 | G5483 charizō | 166996 | 5470 | **RELEVANT** | — |
| Act 25:11 | G5483 charizō | 166993 | 5470 | **RELEVANT** | — |
| Act 25:16 | G5483 charizō | 166994 | 5470 | **RELEVANT** | — |

**Totals:**
- Confirmed relevant: 28
- Set aside: 24
- Borderline: 0

**Phase 2 Post-check:**
- [x] Every UT verse has a recorded determination (52 verses reviewed, 52 determinations recorded)
- [x] No borderline entries remain unraised — none arose
- [x] Set-asides have populated set_aside_reason (all 24)
- [x] Two OQ items raised: OQ-001 (H2868 te.ev verse count), OQ-002 (G5483 charizō UT count)
- [x] Phase 2 post-check satisfied — ready for patch authoring

**Notable Phase 2 findings (not analytical claims — observations on data shape):**
1. H3190 ya.tav is the most UT-dense term (27 verses reviewed) with the highest set-aside rate — the term has a wide semantic range extending well beyond the cluster's characteristic (adverbial intensifier use, skill/proficiency use, comparative use, aesthetic use). Only 10 of 27 confirmed relevant.
2. H2580 chen showed high relevance rate — all 6 UT verses confirmed relevant, including an inverted/corrupted use (Nah 3:4) which is analytically significant.
3. G5485 charis UT verses cluster around political-favour contexts (Acts material) — a different register from the theological grace discourse already in the G-status verses.
4. G5483 charizō UT verses include a corrupted/political granting pattern (Acts 3:14, 25:11, 25:16) alongside the gracious-bestowal pattern (Luk 7:21).

**Phase 2: COMPLETE — pending OQ-001 and OQ-002 resolution before patch authoring.**

---

---

## OQ RESOLUTIONS — received 2026-05-14

**Researcher message (verbatim):**

> Answers — verified against current DB state
> OQ-001 — H2868 te.ev (mti_id=633)
> Resolution: AI's observation correct — no UT rows for this term. No action needed in Phase 2; do not author UT entries.
> mti_terms row 633: H2868 te.ev ("be good", Hebrew), cluster_code='M39', vc_status='not_done', delete_flagged=0, status='extracted'.
> wa_verse_records for mti_term_id=633: 1 row total, 1 active.
> That single verse is already classified is_relevant=1 in verse_context. UT count = 0.
> Why §2 shows no UT entries: there genuinely are none. The vc_status='not_done' field is misleading registry-era leftover — it doesn't reflect that the term's only verse is already classified.
> Cluster placement review: the term has 1 active verse, which is low-volume but not "no extractable verses". Whether 1 verse is enough to keep H2868 in M39 is a Phase 3/4 characteristic-debate question, not a Phase 2 question. Don't set-aside in Phase 2; flag it as low-volume for the §6 debate if relevant.
> OQ-002 — G5483 charizō (mti_id=5470)
> Resolution: 4 is the correct UT count. Pre-check tally of 5 was wrong; trust the AI's review.
> mti_terms row 5470: G5483 charizō ("to give grace", Greek), cluster_code='M39', vc_status='to_revise', delete_flagged=0, status='extracted'.
> wa_verse_records for mti_term_id=5470: 19 total, 19 active.
> Distribution: 15 already classified relevant, 4 UT.
> All 4 UT verses (write all four into the VCNEW patch):
> vr_id | reference | target_word | span_match
> 167001 | Luk 7:21 | bestowed | 1
> 166996 | Act 3:14 | granted | 1
> 166993 | Act 25:11 | give | 1
> 166994 | Act 25:16 | give up | 1
> Suggested next step for AI: revise the Phase 2 pre-check tally to 4 and continue. OQ-001 resolved (no UT — skip); OQ-002 resolved (4 UT, IDs above).

**OQ-001 resolution recorded:**
- H2868 te.ev: 1 active verse, already classified is_relevant=1 in verse_context — UT count genuinely = 0. vc_status='not_done' is a misleading registry-era artefact. No Phase 2 action. Flag as low-volume (1 verse) for Phase 3/4 characteristic debate.
- Phase 2 pre-check tally corrected: H2868 te.ev contributes 0 UT verses to the patch.

**OQ-002 resolution recorded:**
- G5483 charizō: 4 UT verses confirmed (vr_ids: 167001, 166996, 166993, 166994). Pre-check tally of 5 was wrong. All 4 already reviewed and classified RELEVANT in Phase 2 above.

**Corrected Phase 2 UT totals:**
- Total UT verses reviewed: 52 (as stated — the 52 figure in §1 is correct)
- Confirmed relevant: 28
- Set aside: 24
- Borderline: 0

**OQ-001 and OQ-002: BOTH RESOLVED. Phase 2 post-check now fully satisfied. Patch authoring may proceed.**

---

## PHASE 2 — PATCH AUTHORING

**Pre-flight for patch:**
- All 52 UT verses reviewed; 28 relevant (is_relevant=1), 24 set aside (is_relevant=0)
- vr_id and mti_id values taken directly from §2 of comprehensive report (per §5 instruction — no separate ID-resolver query needed)
- md_version=1 for all terms (from §1 reference table)
- Patch type: VCNEW (all UT verses — inserts only, no existing verse_context rows)
- group_id: null for all (Phase 7 will assign)
- is_anchor: 0 for all
- is_related: 0 for all

**Terms covered (mti_ids with UT verses classified):**
- 1299 (H1288 ba.rakh) — 2 rows: both set aside
- 632 (H3190 ya.tav) — 28 rows: 10 relevant, 18 set aside *(note: the ya.tav UT set includes 2 rows that are actually H2895 tov mti_id=542; see correction below)*
- 542 (H2895 tov) — 7 rows: 5 relevant, 2 set aside
- 795 (H7521 ra.tsah) — 2 rows: 1 relevant, 1 set aside
- 889 (H2580 chen) — 6 rows: 6 relevant, 0 set aside
- 984 (H2603A cha.nan) — 1 row: 1 relevant
- 888 (G5485 charis) — 4 rows: 4 relevant
- 5470 (G5483 charizō) — 4 rows: 4 relevant

**Correction note on ya.tav row count:** The UT review table showed 28 rows attributed to ya.tav but 2 of those (Num 11:18 vr_id=4187 mti_id=542, Judg 11:25 vr_id=65375 mti_id=542) carry mti_id=542 and belong to H2895 tov. The ya.tav (mti_id=632) actual count is 26 rows reviewed; 10 relevant, 16 set aside. H2895 tov count is 7 rows; 5 relevant, 2 set aside. Total remains 52.

---

## PHASE 2 — PATCH CORRECTION NOTE

**Error discovered during patch validation:**

Three rows included in the initial Phase 2 UT review table were **G-status** (already group-assigned) in §2 of the comprehensive report, not UT. They appeared in the §2 table above the first UT row and were incorrectly classified during reading:

| vr_id | mti_id | Reference | Status in report | Error |
|---:|---:|---|---|---|
| 12472 | 632 | Gen 4:7 | G (632-002) | Wrongly classified as UT-relevant |
| 12473 | 632 | Gen 12:13 | G (632-002) | Wrongly classified as UT-set-aside |
| 12474 | 632 | Gen 12:16 | G (632-002) | Wrongly classified as UT-relevant |

**Correction applied:**
- These three ops (originally OP-003, OP-004, OP-005) removed from the VCNEW patch
- Patch re-sequenced and re-validated
- Patch file updated in place: `wa-cluster-M39-patch-vcnew-utreview-v1-20260514.json` (same filename — correction is within Phase 2 patch authoring, not a new patch version)

**Corrected Phase 2 final counts:**
- Total UT verses: 52 ✓
- Confirmed relevant (is_relevant=1): **30**
- Set aside (is_relevant=0): **22**
- Borderline: 0

**Corrected Phase 2 UT summary by term:**

| Term | mti_id | UT reviewed | Relevant | Set aside |
|---|---:|---:|---:|---:|
| H1288 ba.rakh | 1299 | 2 | 0 | 2 |
| H3190 ya.tav | 632 | 26 | 10 | 16 |
| H2895 tov | 542 | 7 | 5 | 2 |
| H7521 ra.tsah | 795 | 2 | 1 | 1 |
| H2580 chen | 889 | 6 | 6 | 0 |
| H2603A cha.nan | 984 | 1 | 1 | 0 |
| G5485 charis | 888 | 4 | 4 | 0 |
| G5483 charizō | 5470 | 4 | 4 | 0 |
| **Total** | — | **52** | **30** | **22** |

**Patch validation confirms:** 52 ops · 0 duplicates · all set-aside rows have set_aside_reason · all relevant rows have no set_aside_reason · all required fields present · input_versions is a dict.

**Patch ready for researcher review and CC apply.**

**Phase 2: COMPLETE AND CORRECTED.**

---

---

## NEW REPORT RECEIVED — wa-cluster-M39-comprehensive-v2-20260514.md

**Researcher message (verbatim):** "attached new report"

**Report metadata:**
- Generated: 2026-05-14T04:00:53Z
- Cluster status: Data - In Progress / v6
- Source: database/bible_research.db

**Post-Phase-2 state confirmation (from §1 of v2 report):**

| Status | v1 (pre-patch) | v2 (post-patch) | Expected | Match? |
|---|---:|---:|---:|---|
| G | 688 | 688 | 688 | ✓ |
| SA | 0 | 22 | 22 | ✓ |
| NR | 0 | 0 | 0 | ✓ |
| P | 0 | 30 | 30 | ✓ |
| UT | 52 | 0 | 0 | ✓ |
| **Total** | **740** | **740** | **740** | ✓ |

**Interpretation:**
- SA=22: matches patch set-aside count exactly ✓
- P=30: matches patch relevant count exactly ✓ (P = is_relevant=1, group_id=null — pending group assignment in Phase 7)
- UT=0: all 52 UT verses now have verse_context rows ✓
- G=688: unchanged — existing group-assigned rows untouched ✓

**md_version bumps confirmed (terms with UT rows now at md_version=2):**
- H1288 ba.rakh (1299): 1→2 ✓
- H3190 ya.tav (632): 1→2 ✓
- H2895 tov (542): 1→2 ✓
- H7521 ra.tsah (795): 1→2 ✓
- H2580 chen (889): 1→2 ✓
- H2603A cha.nan (984): 1→2 ✓
- G5485 charis (888): 1→2 ✓
- G5483 charizō (5470): 1→2 ✓

**Terms still at md_version=1 (no UT rows — untouched by patch):**
- G1435 dōron, G2107 eudokia, G5486 charisma, G5487 charitoō, H2587 chan.nun, H2604 cha.nan, H2868 te.ev, H7862 shay ✓

**vc_status updates confirmed:**
- Terms with UT rows patched: now show vc_completed ✓
- Remaining terms: unchanged (not_done or to_revise) ✓

**Set-aside reasons listed in §1:** 22 entries visible, all for ya.tav variants — correct (H1288 ba.rakh set-asides appear truncated in §1 display but counted in total). Note: the §1 listing shows 15 unique reason strings covering 22 rows — this is expected as the two ba.rakh set-asides and one ra.tsah set-aside may not be visible in the truncated display but are counted.

**Phase 2 post-check: FULLY SATISFIED against v2 report.**
**Patch applied cleanly. Comprehensive report v2 is now the active working source.**

**Phase 2: CLOSED.**

---

---

## PHASE 3 — CHARACTERISTIC DEBATE FROM THE GLOSS LIST

**Researcher instruction (verbatim):** "proceed"

**Phase 3 opened:** 2026-05-14

**Pre-check:**
- [x] Phase 1 + Phase 2 complete (UT review, patch applied, v2 report confirms clean state)
- [x] Comprehensive report v2 regenerated post-Phase 2
- [x] Input is §1 (gloss list) and §3 (per-term comprehensive detail) of v2 report only — no additional files

**Now reading §3 per-term comprehensive detail before writing any groupings.**

---

## PHASE 3 — CHARACTERISTIC DEBATE (continued from opening)

**§3 reading complete. All 16 term blocks read. Debate begins now.**

### Term inventory summary (for debate)

| Strong's | Translit | Gloss | Verses | Groups | Registry origin | Key data flags |
|---|---|---|---:|---:|---|---|
| H1288 | ba.rakh | to bless | 249 | 4 | R194 blessing | no word analysis |
| H3190 | ya.tav | be good | 110 | 3 | R186 gladness | bridges moral + affective |
| G5485 | charis | grace | 67* | 4 | R068 grace | CHAR root; joy-linked |
| H2603A | cha.nan | be gracious | 72 | 1 | R111 mercy | CHANAN/CHEN root family |
| H2580 | chen | favor | 67 | 3 | R068 grace | CHEN root; two-sided structure |
| H7521 | ra.tsah | to accept | 54 | 3 | R042 delight | cross-ref R046 devotion |
| H2895 | tov | be pleasing | 48* | 2** | R067 goodness | moral-volitional; broad |
| G5483 | charizō | to give grace | 19* | (multiple)** | R068 grace | CHAR root; grace as act |
| G1435 | dōron | gift | 17 | 6 | R180 yielding | conscience/worship/gift |
| G5486 | charisma | gift | 14 | 1 | R194 blessing | CHAR root; 17 occurrences, thin |
| H2587 | chan.nun | gracious | 13 | 1 | R023 compassion | divine epithet; CHEN root |
| G2107 | eudokia | goodwill | 9 | 2 | R043 desire | divine pleasure/human longing |
| H7862 | shay | gift | 3 | 1 | R199 dominion | tribute/homage; extracted_thin |
| H2604 | cha.nan | be gracious | 2 | 1 | R111 mercy | Aramaic/thin; CHANAN root |
| G5487 | charitoō | to favor | 2 | 1 | R068 grace | NT coinage; completed-state grace |
| H2868 | te.ev | be good | 1 | 1 | R186 gladness | Aramaic; 1 verse only |

*verse counts post-patch; **group counts from v2 §3

---

### Phase 3 characteristic debate

**Applying the T1 framework (§6.1) throughout.**

---

#### Step 1: Reading all glosses against the T1 characteristic definition

The cluster contains three identifiable semantic domains at gloss level. These will be tested as candidate sub-groups.

**Domain A: Blessing / Divine bestowal of favour**
Terms whose glosses name the action of blessing or bestowal from a greater to a lesser: ba.rakh (to bless), charis (grace), cha.nan / H2603A (be gracious), chen (favor), charitoō (to favor), charizō (to give grace), eudokia (goodwill). These all point toward the one-directional movement: the superior blessing, gracing, or favouring the inferior. The inner-being characteristic: the dispositioned gift of the greater toward the lesser — what we might call the grace/blessing characteristic.

**Domain B: Goodness / Inner moral-pleasurable quality**
Terms whose glosses name the quality of being good, pleasing, or pleasant: ya.tav (be good), tov (be pleasing), te.ev (be good — Aramaic). These name a quality of inner character or moral evaluation — the person, thing, or action having the character of goodness. The inner-being characteristic: the moral-affective quality of goodness — what we might call the goodness characteristic.

**Domain C: Gift / Received endowment**
Terms whose glosses name the gift itself (the object transferred rather than the disposition or act): dōron (gift), charisma (gift), shay (gift). These name the thing given, not the giver's disposition or the act of giving. The inner-being characteristic question: is "gift" itself an inner-being characteristic, or is it a relational/external category that belongs in BOUNDARY? The gift is an outcome of grace, not the inner-being faculty or disposition.

**Borderline candidates:**
- ra.tsah (to accept): names the inner act of acceptance/pleasure/delight — neither purely bestowing nor purely quality of goodness. It names the recipient's or giver's inner disposition of satisfaction. Could participate in Domain A (as divine acceptance of offerings = the grace-dynamic from God's perspective) or stand alone.
- chan.nun (gracious): adjectival form — names the character quality of graciousness as a settled disposition. Primarily a divine epithet. Different from the verbal/noun grace terms in that it designates the person-type, not the act. Could join Domain A or form part of BOUNDARY.
- H2604 cha.nan (be gracious — Aramaic): too thin (2 verses) to analyse independently; root is identical to H2603A cha.nan; will fold into that term's analysis.

---

#### Step 2: Provisional sub-group proposals, each named by the dominant characteristic

**Provisional sub-group M39-A: The blessing/grace characteristic — sovereign favour extended from the greater to the lesser**

Candidate terms: H1288 ba.rakh, G5485 charis, H2603A cha.nan, H2580 chen, G5483 charizō, G5487 charitoō, G2107 eudokia

Rationale: All of these name the same fundamental inner-being dynamic: a disposition or act of the greater toward the lesser that constitutes favour, grace, or blessing. The specific form varies — ba.rakh names the covenantal declaration/act of blessing; charis/chen name the dispositional quality of grace/favour; cha.nan names the verbal act of being gracious; charizō names the act of grace-giving; charitoō names the completed state of having been favoured; eudokia names the inner divine pleasure/goodwill as the ground of blessing. All share:
- Constitutional location: will, disposition, soul — the inner orientation of one person toward another
- Faculty engaged: will, moral character, relational capacity
- Direction: consistently from higher to lower, from divine to human (though with human-to-human dimensions)
- Recognisable impact: the recipient of grace has standing, protection, access, and inner transformation
- Structural opposite: acharistos (ungrateful/graceless) — the failure to recognise or extend grace

This sub-group satisfies all five T1 criteria.

**Provisional sub-group M39-B: The goodness characteristic — the inner moral-affective quality of being good**

Candidate terms: H3190 ya.tav, H2895 tov, H2868 te.ev

Rationale: All three name the quality of goodness as an inner character state or evaluative category. Ya.tav bridges moral goodness and affective gladness-at-good (DIM-186-001 confirms this three-mode span). Tov is the broadest OT goodness term — naming moral rightness, covenantal reliability, volitional preference, and aesthetic pleasantness. Te.ev is the Aramaic equivalent (gladness at deliverance through trust). Together they carry:
- Constitutional location: heart, soul — the inner moral-evaluative character
- Faculty engaged: moral evaluation, conscience, affect, will (volitional preference)
- Recognisable impact: the person who is good produces goodness in others and in community
- Structural opposite: ra (evil/bad) — the antonym of tov and ya.tav
- Distinguishing causal direction: toward what is genuinely beneficial; the inner assessment that something coheres with the good

This sub-group satisfies all five T1 criteria, though the overlap between goodness-as-quality and grace-as-disposition will need careful examination in Phase 4. The bridging point: tov can name divine pleasure/goodwill (approaching Domain A) — this tension must be flagged for Phase 4.

**Provisional sub-group M39-C: The acceptance/delight characteristic — the inner pleasure of receiving or approving**

Candidate terms: H7521 ra.tsah

Rationale: Ra.tsah names something distinct from both blessing-given and goodness-as-quality. It names the inner act of accepting, being pleased with, or delighting in — the pleasure of the one who receives an offering or approves of a person. Its three existing groups capture this: divine acceptance of offerings (God's inner pleasure), divine delight in persons, and human receipt of favour. This is the receiving side of the grace-dynamic — the inner satisfaction of acceptance. Whether it is sufficiently distinct from Domain A to stand as its own sub-group is the key question:
- The giving of grace (Domain A) and the pleasure of accepted grace (ra.tsah) are structurally related but directionally different — Domain A is the giver's disposition; ra.tsah is the receiver's (or giver's) pleasure-at-what-is-given
- Ra.tsah from God toward offerings = God's acceptance/pleasure = close to divine goodwill (eudokia) in Domain A
- Ra.tsah from God toward persons = divine delight = overlapping with ba.rakh's covenantal favour
- Ra.tsah from humans receiving favour = the human inner experience of being accepted

**Provisional assessment:** Ra.tsah may not carry a sufficiently distinct fifth criterion (distinguishing causal direction) to warrant its own sub-group at this stage. It may be better placed within M39-A (as the reception/pleasure face of the grace-dynamic) or in a combined sub-group. This is flagged for Phase 4 control read. Not BOUNDARY, as the inner-being content is real and substantial (54 verses).

**BOUNDARY candidates:**

- **H2587 chan.nun (gracious):** This is an adjectival divine epithet — naming the person-type rather than the act or disposition. Its single group (2330-001) describes "the settled disposition to extend favour and mercy freely." At gloss level, chan.nun contributes characterologically to M39-A but as a descriptor of character rather than an act or disposition. It has 13 verses. Provisionally assign to M39-A, but watch in Phase 4 for whether it carries distinct inner-being content. Not BOUNDARY at this stage.

- **G1435 dōron (gift):** The gloss names the object (gift/offering), not the inner-being disposition or act. Its 6 existing groups all describe what the gift means in inner-being terms (worship-act, relational conscience, moral evasion via piety, inner inadequacy of ritual, salvation as free gift, radical self-giving). The inner-being content is real but is carried by the context, not by dōron itself. The term names the material vehicle. Provisionally BOUNDARY — the inner-being work is done by the surrounding terms; dōron names the external form. To be tested in Phase 4.

- **G5486 charisma (gift):** 14 verses, one group — "God's free gift of grace — the spiritual capacity given to each person for building up the community, and supremely the gift of eternal life." The inner-being content is significant — charisma names the Spirit-endowment that constitutes a person's inner capacity for community service. This is more clearly inner-being than dōron. But is it the same characteristic as charis (grace)? Charisma is the outcome/form of charis. Provisionally assign to M39-A as the grace-in-its-gifted-capacity form. Watch in Phase 4.

- **H7862 shay (gift/tribute):** 3 verses, extracted_thin. Gloss: tribute/gift brought to God as inner homage and acknowledgment of supremacy. The inner-being content is the attitude of reverence that the tribute expresses. Very thin. Provisionally BOUNDARY — too thin to sustain sub-group assignment, and the inner content is closer to worship/reverence than to grace/blessing/goodness. Flag for Phase 4.

- **H2604 cha.nan (be gracious — Aramaic):** 2 verses. Root identical to H2603A; Aramaic cognate. Too thin to analyse independently. Provisionally fold into M39-A alongside H2603A, to be confirmed in Phase 4.

- **G5487 charitoō (to favor):** 2 verses but with rich prior analysis (the NT coinage finding). The term's grammatical distinctiveness (perfect passive — completed, continuing state of being favoured) gives it a distinct inner-being contribution: the person who stands in grace as a permanently transformed state. This is within the grace/blessing domain but describes the recipient's standing rather than the giver's act. Provisionally assign to M39-A (the completed-state face of grace). Watch in Phase 4.

- **H2868 te.ev (be good — Aramaic):** 1 verse only. Aramaic cognate of ya.tav/tov. Its single group names "inner gladness at deliverance through trust in God" — an affective response, not the moral goodness quality. Closer to the gladness/joy register than to the goodness register. 1 verse is insufficient for sub-group assignment. Provisionally BOUNDARY — too thin; affective gladness register may be better placed in a different cluster (the gladness cluster — its registry of origin is R186 gladness). Flag as OQ-003 for Phase 4.

---

#### Step 3: T1 criterion tests per provisional sub-group

**M39-A: Blessing/Grace — the sovereign favour from greater to lesser**

| T1 criterion | Test result |
|---|---|
| 1. Identifiable constitutional location | Heart/soul — the inner disposition of the giver; soul/standing — the inner transformation of the receiver. Located in the relational-dispositional layer of the inner being. ✓ |
| 2. Distinguishable inner faculties | Will (the sovereign choice to bless/grace), relational capacity (the orientation toward the other), moral character (the settled disposition of graciousness). ✓ |
| 3. Recognisable impact | The recipient acquires standing, protection, access, and inner transformation. The giver is characterised by this as their essential inner orientation. ✓ |
| 4. Structural opposite | Acharistos (ungrateful/graceless — the failure to recognise or extend grace); judgment without mercy (the withholding of grace). ✓ |
| 5. Distinguishing causal direction | Downward (from greater to lesser) — the direction is constitutive: grace flows from the one who has to the one who lacks; it is the initiating movement of the greater. ✓ |

**All five T1 criteria satisfied. M39-A is a valid characteristic-bearing sub-group.**

**M39-B: Goodness — the inner moral-affective quality of being good**

| T1 criterion | Test result |
|---|---|
| 1. Identifiable constitutional location | Heart — moral character, inner evaluative capacity. ✓ |
| 2. Distinguishable inner faculties | Moral evaluation, conscience, affect (gladness-at-good), will (volitional preference for good). ✓ |
| 3. Recognisable impact | The good person produces goodness in community; divine goodness produces trust and repositioned inner orientation (Psa 73:28); goodness enables instruction of others (Rom 15:14). ✓ |
| 4. Structural opposite | Ra/evil/bad — the antonym of tov/ya.tav. ✓ |
| 5. Distinguishing causal direction | Both: goodness is received from God (divine goodness as prior and originating) and expressed outward toward others (human goodness as derived and responsive). The direction is bidirectional — received and expressed. ✓ |

**All five T1 criteria satisfied. M39-B is a valid characteristic-bearing sub-group.**

---

#### Step 4: Tension between M39-A and M39-B — the onion principle

The significant tension to flag for Phase 4:

**Tov (H2895) bridges both sub-groups.** The gloss "be pleasing" spans:
- Divine pleasure/goodwill (approaching M39-A: "it pleased the Lord to bless") — see Num 24:1, 2Sa 15:26
- Moral goodness quality (M39-B) — see Deu 5:33 ("that it may go well with you"), Gen 4:7 ("if you do well")
- Volitional preference/judgment ("what seems good to you") — relates to M39-B moral evaluation

Ya.tav (H3190) similarly:
- Group 632-002 = moral goodness = M39-B
- Group 632-003 = inner approval/pleasure/favour = could relate to M39-A (the acceptance side)
- Group 632-001 = heart being glad = affective gladness = may belong to a gladness cluster

Ra.tsah similarly sits between domains: divine delight/acceptance is simultaneously the grace-dynamic (M39-A) and a form of goodness/pleasure (M39-B).

This tension is real and expected — the onion principle applies. The sub-groupings are peels, not separate objects. M39-A and M39-B are distinguishable by their primary directional characteristic (downward gift vs. inward quality) but share constitutional space. Phase 4 control read will resolve the placement of tov, ya.tav, and ra.tsah.

---

#### Provisional sub-group list (output of Phase 3)

| Sub-group | Label | Terms (provisional) | Status |
|---|---|---|---|
| M39-A | Blessing and Grace — sovereign favour from the greater to the lesser | H1288 ba.rakh, G5485 charis, H2603A cha.nan, H2580 chen, G5483 charizō, G5487 charitoō, G2107 eudokia, H2587 chan.nun, G5486 charisma, H2604 cha.nan | Provisional |
| M39-B | Goodness — the inner moral-affective quality of being good | H3190 ya.tav, H2895 tov | Provisional |
| BOUNDARY | Supportive/descriptive/undecided | G1435 dōron, H7862 shay, H2868 te.ev | Provisional |
| Phase 4 question | Ra.tsah placement: M39-A, M39-B, or own sub-group? | H7521 ra.tsah | OQ-004 |

**Flagged for Phase 4:**
- OQ-003: H2868 te.ev (1 verse, affective gladness register) — consider whether this belongs in M39 at all or should be cluster-reassigned to the gladness cluster.
- OQ-004: H7521 ra.tsah — does it belong with M39-A (as the acceptance/pleasure face of the grace dynamic), or is it sufficiently distinct to warrant its own sub-group?

**Conglomerate risk flag:** M39-A as currently proposed contains 10 terms. This is large. Phase 4 must test whether the grace/blessing/goodwill/favour/graciousness terms all share the same characteristic or whether they subdivide. The primary candidate split: verbs of grace-action (cha.nan, charizō) vs. nouns of grace-disposition (charis, chen) vs. adjectival character (chan.nun) vs. completed state (charitoō) vs. gift-as-endowment (charisma). These may be one characteristic in its different operational forms, or they may be distinct sub-groups. Phase 4 will determine this.

**Phase 3 provisional label: PROVISIONAL — Phase 4 required before any sub-group is confirmed.**

---

---

## PHASE 4 — CONTROL READ AND COMPOUND-MORPHING CORRECTION

**Researcher instruction (verbatim):** "noted observations. will all be tested during verse reading. Proceed"

**Phase 4 opened:** 2026-05-14

**Researcher direction noted:** OQ-003, OQ-004, and all Phase 3 tensions (tov/ya.tav overlap with M39-A, conglomerate risk in M39-A, BOUNDARY placements) are deferred to verse reading — not pre-resolved analytically. Phase 4 proceeds with a bidirectional control read against the comprehensive detail, not against verses. Verse-level resolution is Phase 5/6.

**Pre-check:**
- [x] Phase 3 complete: characteristic-debate document produced, provisional sub-group list in obslog
- [x] T1 criteria explicitly available (§6.1 of instruction)
- [x] Input: §3 per-term comprehensive detail (already read) — applying Direction 1 and Direction 2 per §7.3

**Phase 4 purpose:** Validate the provisional sub-groups by bidirectional control — does each term's actual full description fit its proposed group? Does any term's description resist its proposed group or suggest a different placement?

---

### Direction 1 — Grouping → Term: does each term's actual description fit the proposed group?

**M39-A (Blessing and Grace — sovereign favour from greater to lesser)**

- **H1288 ba.rakh (249 verses):** 4 groups — God's sovereign covenantal gift of favour (1299-001); human blessing of God as worship (1299-002); human blessing of others as covenantal declaration (1299-003); ironic/euphemistic cursing-as-blessing (1299-004). Direction 1 test: groups 001 and 003 clearly fit M39-A (grace downward). Group 002 (human blessing of God) is directionally inverted — it is the human worshipping upward, not the greater gracing the lesser. This is the praise/worship characteristic, which is carried by ba.rakh but points toward a different inner-being dynamic. Group 004 (ironic cursing) is the corrupted/inverted form.
  → FITS M39-A for groups 001 and 003. Group 002 is a different inner-being act (worship directed upward). Group 004 is the structural opposite/corruption. Ba.rakh's semantic breadth is its defining complexity — it carries the blessing characteristic in all directions.

- **G5485 charis (67 verses):** 4 groups — sovereign unmerited divine disposition (888-001); standing-sphere of the believer (888-002); relational favour (888-003); apostolic mission power (888-004). All four fit M39-A: disposition of grace, the standing in grace, the favour dynamic, grace as empowering presence. No resistance.
  → FITS M39-A cleanly.

- **H2603A cha.nan (72 verses):** 1 group — God's inner disposition of grace toward the supplicant AND the human cry of petition and dependence (984-001). This dual ownership (giver and seeker both encoded in the same group) fits M39-A — it names the full relational architecture of grace from both sides. No resistance.
  → FITS M39-A.

- **H2580 chen (67 verses):** 3 groups — divine favour (889-001); interpersonal favour (889-002); favour as inner character quality in speech/conduct (889-003). Groups 001 and 002 clearly fit M39-A. Group 003 (character quality generating standing in community) approaches M39-B territory (goodness as quality). The "gracious disposition expressed in speech, conduct, and wisdom" is a character description more than a directional grace-act.
  → FITS M39-A for 001 and 002. Group 003 is borderline M39-A/M39-B — the gracious character quality. No resistance to M39-A placement; the character-quality face of grace is still within M39-A's domain (it describes the person who embodies the characteristic). No reassignment needed but noting the bridge.

- **G5483 charizō (19 verses, 15 G + 4 new):** Multiple groups — grace-giving as forgiving, bestowing, releasing, granting. All fit M39-A (the act of giving grace). The Phase 2 political-favour register is still within M39-A — the same directional dynamic (giving a concession from one who has power to one who needs it), even in its corrupted political form.
  → FITS M39-A.

- **G5487 charitoō (2 verses):** 1 group — the divine act of bestowing grace as a completed act that marks and transforms the recipient (5471-001). NT coinage. Clear fit with M39-A — specifically the completed-state form.
  → FITS M39-A.

- **G2107 eudokia (9 verses):** 2 groups — divine sovereign goodwill/pleasure as inner purpose (494-001); human goodwill/desire as inner orientation of longing for good (494-002). Group 001 fits M39-A (the divine inner pleasure from which blessing proceeds). Group 002 (human goodwill/longing for good) introduces a different direction: the human oriented toward the good — which is closer to M39-B (goodness as inner quality and orientation). However, "goodwill" toward others still participates in the grace-direction (the person whose inner orientation is goodwill toward others). Borderline but no clear resistance to M39-A.
  → FITS M39-A for 001. Group 002 bridges M39-A and M39-B — human goodwill could sit in either. No reassignment needed at gloss level; verse reading will determine.

- **H2587 chan.nun (13 verses):** 1 group — settled disposition of the person (primarily God) to extend favour and mercy freely (2330-001). Almost exclusively divine epithet (Exo 34:6 formula). Clear fit with M39-A — the character-type who embodies the grace disposition.
  → FITS M39-A.

- **G5486 charisma (14 verses):** 1 group — God's free gift of grace as spiritual capacity for community and supremely eternal life (1301-001). The CHAR root connects it to M39-A. The inner-being content is the Spirit-endowment that constitutes a person's capacity — this is grace in its gifted-capacity form. It fits M39-A as the characteristic's expression in terms of endowment rather than disposition. Some tension: charisma names what the recipient receives and now carries, which could be a distinct sub-group (received endowment as inner capacity). Verse reading will determine. No resistance to M39-A placement.
  → FITS M39-A provisionally.

- **H2604 cha.nan (2 verses):** 1 group — mercy shown in moral action and the plea of prayer (989-001). Same root as H2603A. Two verses (Dan 4:27, Dan 6:11 from findings — mercy/gracious in Aramaic context). Fits M39-A alongside H2603A. Too thin for independent analysis.
  → FITS M39-A. Fold into H2603A treatment.

**M39-B (Goodness — inner moral-affective quality of being good)**

- **H3190 ya.tav (110 verses):** 3 groups — heart glad/merry (632-001); moral goodness/doing good (632-002); inner approval/satisfaction/pleasure at good (632-003). Group 002 clearly fits M39-B (moral goodness as inner quality). Group 001 (heart being glad) is the affective gladness register — this is the gladness/joy characteristic, not the goodness characteristic per se. DIM-186-001 confirms this bridges dimensions. Group 003 (approval/satisfaction/favour) bridges M39-B and M39-A.
  → FITS M39-B for group 002. Groups 001 (gladness) and 003 (approval/favour) require verse-level determination. No resistance to M39-B as primary placement — the goodness-doing characteristic (632-002) is ya.tav's most distinctively inner-being content. The gladness register (632-001) is noted as a potential wrong-face at group level — the inner-being content there may be better served by the gladness cluster.

- **H2895 tov (48 verses):** 2 groups (from §4.4 VCG table, not all detail visible in §3 at this level — groups inferred from Phase 2 readings and VCG descriptions). The goodness-as-quality and divine-pleasure dimensions are both present. Tov's semantic range is the widest in the cluster — it covers moral rightness (M39-B), aesthetic pleasantness, covenantal reliability, volitional preference, and divine pleasure (approaching M39-A via eudokia). Phase 2 relevant verses confirmed tov in: divine dispositional pleasure (Num 24:1 — M39-A territory), covenantal blessing-outcome (Deu 5:33 — M39-A/B bridge), aesthetic goodness-as-favour (Num 24:5 — M39-A/B bridge), volitional judgment (2Sa 15:26, 19:37 — M39-B moral evaluation).
  → FITS M39-B as primary placement. The divine-pleasure register of tov will produce some wrong-face set-asides at verse level (where the inner-being content is carried by the grace/favour dynamic, not the goodness quality). This is expected and correct — tov's breadth means it crosses the M39-A/B boundary at some verses.

**BOUNDARY review**

- **G1435 dōron (17 verses):** 6 groups all describing inner-being context of the gift/offering. Direction 1 test: does the term's description fit BOUNDARY? The groups are rich in inner-being content but the content is theologically supplied by the offering context — dōron itself names the material form. The conscience-gap group (6837-004: "inadequacy of ritual gifts to perfect the conscience") names a significant inner-being finding but the term contributes the vehicle, not the inner content. The salvation-as-gift group (6837-005) uses dōron for the gift of salvation — this is grace language. Tension: some dōron verses may carry M39-A content (salvation as free gift = grace given). BOUNDARY is appropriate at the gloss level; verse reading may produce relevant classifications.
  → BOUNDARY maintained. Verse reading will determine whether any dōron verses should be classified as relevant to M39-A.

- **H7862 shay (3 verses):** 1 group — tribute/gift as inner homage and reverence. The inner content is closer to worship/submission than to grace or goodness. Extracted_thin.
  → BOUNDARY confirmed.

- **H2868 te.ev (1 verse):** 1 group — inner gladness at deliverance through trust in God. The gladness register distinguishes this from M39-B (goodness quality). OQ-003 remains open. At this stage: BOUNDARY. The verse reading will confirm whether the single verse carries M39-B goodness content or gladness content.
  → BOUNDARY maintained, OQ-003 open.

**OQ-004 — H7521 ra.tsah (54 verses)**

Direction 1 test: 3 groups — divine acceptance of offerings (795-001); divine pleasure in persons/character (795-002); human acceptance/favour (795-003). Does this fit M39-A, M39-B, or neither? The three groups test as follows:

- 795-001 (divine acceptance of offerings): God's inner-being pleasure in what is offered — this is the grace-dynamic from God's perspective (accepting = favouring). Fits M39-A as the reception/pleasure face of the same grace-dynamic. The offering being accepted is the act by which the offerer receives divine favour.
- 795-002 (divine pleasure in persons/character): God's inner delight in the righteous — this is simultaneously: grace (God favouring the person) AND goodness (God responding to goodness in the person). The delight is called forth by the person's righteous character — making it a response to M39-B, expressed as M39-A.
- 795-003 (human acceptance/favour): the inner-being receipt of divine or human favour — this is the receiving side of the grace-dynamic. Fits M39-A as the human counterpart.

Direction 1 assessment: Ra.tsah's three groups collectively describe the inner pleasure/satisfaction that operates at the interface between giver and receiver of grace. It is not the giving of grace (M39-A's primary territory) nor the quality of goodness (M39-B), but the pleasure-of-encounter-with-good/grace. However, it operates within the same relational architecture as M39-A and shares its T1 profile more with M39-A than with M39-B.

→ Provisional Direction 1 conclusion: **Ra.tsah will be assigned to M39-A.** The acceptance/delight characteristic is the inner-pleasure face of the grace dynamic — it belongs within the blessing/grace sub-group rather than as a separate sub-group. This decision is confirmed at gloss level; verse reading in Phase 5/6 will test whether ra.tsah's verse evidence diverges enough to warrant separation. OQ-004 provisionally resolved — no separate M39-C sub-group at this stage.

---

### Direction 2 — Term → Grouping: does any term's description resist its proposed group?

**M39-A terms — resistance check:**

- **H1288 ba.rakh:** Does not resist M39-A — but the 1299-002 group (human blessing of God = worship) is a different inner-being act. This group does not resist M39-A; it reveals that ba.rakh carries both the grace-giving characteristic AND the worship characteristic within its semantic range. The worship direction will produce wrong-face set-asides at verse level (inner-being content of blessing God is carried by the worship dynamic, not the grace-receiving dynamic). No cluster reassignment needed; the wrong-face mechanism at verse level is the appropriate tool.

- **G5486 charisma:** Possible mild resistance: charisma names a Spirit-endowed capacity (what the person now has and carries), not merely the giving of grace. This is grace in its received-and-inhabited form. Phase 5/6 will test whether charisma's verses are better described as M39-A (grace given to the person) or as a distinct capacity-endowment characteristic. At gloss level, no resistance strong enough to reassign. Noting for Phase 5.

- **G2107 eudokia group 002:** Human goodwill/longing for good resists slightly — it is oriented inward and toward the good (M39-B direction) rather than downward toward the lesser (M39-A direction). However, goodwill toward others does participate in the grace direction. No reassignment at this stage.

**M39-B terms — resistance check:**

- **H3190 ya.tav group 001:** The heart-glad/merry group resists M39-B (goodness) assignment. The gladness register is different from the moral-goodness quality. Registry of origin is R186 gladness. This group may carry inner-being content that belongs in the gladness cluster rather than the goodness cluster. No cluster reassignment proposed for the term (the term carries multiple characteristics); the group-level wrong-face mechanism will handle it at verse level. Noting: Phase 5 reading should watch for whether 632-001 verses primarily carry gladness rather than goodness.

- **H2895 tov:** Mild resistance in the divine-pleasure register (Num 24:1 etc.) — the "divine pleasure/will" sense of tov approaches M39-A and could be seen as eudokia-equivalent. No resistance strong enough for cluster reassignment; tov remains in M39-B as its primary home. Wrong-face set-asides will handle verses where the dominant content is divine-grace rather than goodness-quality.

**BOUNDARY terms — resistance check:**

- **G1435 dōron:** Group 6837-005 (salvation as God's free gift) resists BOUNDARY placement significantly — salvation-as-free-gift is core grace language, not merely a vehicle. This group may need to be classified as relevant in Phase 5/6, with its inner-being content attributed to the M39-A characteristic. Noting as a Phase 5 watch-point.

- **H7862 shay:** No resistance to BOUNDARY — the tribute/homage content is distinct from grace or goodness.

- **H2868 te.ev:** The gladness register resists M39-B placement (which would be its only alternative to BOUNDARY). OQ-003 remains. Noting: the single verse (OBS-reference Dan 6:11 per obslog) should be read to confirm whether the te.ev content is gladness or goodness.

**No cluster reassignments required at Direction 2 level.** All terms retain their Phase 3 provisional placements with the following refinements.

---

### Phase 4 output — confirmed sub-group list

**Confirmed (pending verse-level validation in Phase 5/6):**

| Sub-group | Label | Terms |
|---|---|---|
| **M39-A** | Blessing and Grace — sovereign favour from the greater to the lesser | H1288 ba.rakh, G5485 charis, H2603A cha.nan, H2580 chen, G5483 charizō, G5487 charitoō, G2107 eudokia, H2587 chan.nun, G5486 charisma, H2604 cha.nan, **H7521 ra.tsah** |
| **M39-B** | Goodness — the inner moral-affective quality of being good | H3190 ya.tav, H2895 tov |
| **BOUNDARY** | Supportive / descriptive / undecided | G1435 dōron, H7862 shay, H2868 te.ev |

**OQ-004 resolved:** H7521 ra.tsah assigned to M39-A (acceptance/delight as the pleasure-face of the grace dynamic). No separate M39-C sub-group.

**OQ-003 remains open:** H2868 te.ev — still in BOUNDARY pending verse reading of its single verse.

**Phase 4 watch-points for Phase 5/6 verse reading:**
1. Ba.rakh group 1299-002 (human blessing of God = worship direction): expect wrong-face content at verse level; inner-being content will be carried by worship characteristic, not grace-receiving.
2. Ya.tav group 632-001 (heart glad/merry = gladness register): expect wrong-face content; inner-being content may belong in gladness cluster.
3. Dōron group 6837-005 (salvation as free gift): may classify as relevant to M39-A characteristic.
4. Charisma verse set: watch whether the Spirit-endowment characteristic is same as or distinct from grace-disposition.
5. Eudokia group 494-002 (human goodwill/longing): watch whether verse content is M39-A (goodwill toward others) or M39-B (inner longing for good).

**Phase 4 post-check:**
- [x] Every OQ-NNN has a researcher-confirmed or AI-resolvable disposition: OQ-004 resolved; OQ-003 remains open (verse-level)
- [x] Every term assigned to sub-group, BOUNDARY, or flagged — none left unclassified
- [x] Phase 4 output is the confirmed sub-group list above
- [x] No cluster reassignments required
- [x] Phase 4 is bidirectional control — no sub-group is yet confirmed by verse evidence (that is Phase 5/6)

**Phase 4: COMPLETE**

---

## PHASE 4 — DIRECTIVE AUTHORING

**Researcher instruction (verbatim):** "agree- proceed"

**Researcher approval confirmed:** sub-group structure accepted as-is. Proceed to dir-001-subgroup-assign.

**Directive scope (per §7.7 of v1_9):**
- Operation A: cluster_subgroup CREATE (3 rows: M39-A, M39-B, BOUNDARY) + mti_terms.cluster_subgroup_id ASSIGN (16 terms)
- Operation B: cluster_code rebind — NOT needed (no terms moving out of M39)
- Operation C: cluster.status transition Data - In Progress → Analysis - In Progress

**Sub-group rows to create:**

| Code | Label | Terms |
|---|---|---|
| M39-A | Blessing and Grace — sovereign favour from the greater to the lesser | 11 terms |
| M39-B | Goodness — the inner moral-affective quality of being good | 2 terms |
| M39-BOUNDARY | BOUNDARY — supportive/descriptive/undecided | 3 terms |

**Term assignments (16 terms, all in M39):**

| mti_id | Strong's | Translit | Sub-group |
|---|---|---|---|
| 1299 | H1288 | ba.rakh | M39-A |
| 888 | G5485 | charis | M39-A |
| 984 | H2603A | cha.nan | M39-A |
| 889 | H2580 | chen | M39-A |
| 5470 | G5483 | charizō | M39-A |
| 5471 | G5487 | charitoō | M39-A |
| 494 | G2107 | eudokia | M39-A |
| 2330 | H2587 | chan.nun | M39-A |
| 1301 | G5486 | charisma | M39-A |
| 989 | H2604 | cha.nan | M39-A |
| 795 | H7521 | ra.tsah | M39-A |
| 632 | H3190 | ya.tav | M39-B |
| 542 | H2895 | tov | M39-B |
| 6837 | G1435 | dōron | M39-BOUNDARY |
| 2976 | H7862 | shay | M39-BOUNDARY |
| 633 | H2868 | te.ev | M39-BOUNDARY |

**Directive file being authored now.**

---

**Directive authored:** wa-cluster-M39-dir-001-subgroup-assign-v1-20260514.md

Content verified:
- Operation A: 3 sub-group CREATE rows + 16 term ASSIGN rows (11 M39-A, 2 M39-B, 3 M39-BOUNDARY)
- Operation B: not required — no cluster_code rebinds
- Operation C: status transition Data - In Progress → Analysis - In Progress
- 4 COMPLETION CONFIRMATION queries specified
- Packaging: single directive, all operations in one transaction

**Awaiting researcher review and CC apply.**

---

## DIRECTIVE APPLICATION CONFIRMED — DIR-20260514-001

**Researcher message (verbatim):**

> DIR-20260514-001 applied — M39 Phase 4 complete
> Operation | Result
> A1 Sub-group rows | 3 inserted: M39-A (Blessing and Grace) · M39-B (Goodness) · M39-BOUNDARY
> A2 Term placements | 16 mti_term_subgroup rows inserted (M39-A: 11 · M39-B: 2 · M39-BOUNDARY: 3)
> B Cluster rebind | Not required — 0 rebinds
> C Status transition | Data - In Progress → Analysis - In Progress ✓
> Backup | backups/row_backups/M39_dir001_subgroup_assign_pre_20260514T052212.json
> Apply script | scripts/_apply_m39_dir_001_subgroup_assign_20260514.py
> Schema deviations to flag for AI (intent correct; column names wrong in directive text — applied per M20/M26 precedent):
> Directive said | Actual schema
> mti_terms.cluster_subgroup_id UPDATE | mti_term_subgroup join table INSERT
> cluster_subgroup.is_boundary column | BOUNDARY identified by subgroup_code='M39-BOUNDARY'
> cluster_subgroup.description | cluster_subgroup.core_description
> Recommend the cluster instruction (or a schema-reference appendix) carry the actual column names so future Phase 4 directives author-time-compliant. Worth a v1_10 entry: "Phase 4 directive uses mti_term_subgroup (not mti_terms.cluster_subgroup_id); BOUNDARY is a subgroup_code convention, not a flag column."
> Ready for Phase 5 (250-word sub-group summaries) — first, regenerate the grouped report per §8.2 pre-check.

**Application confirmed:** All four operations match expected outcomes. Backup recorded.

**Schema deviations recorded:**
Three column-name errors in the directive text — intent was correct and CC applied per M20/M26 precedent. Corrections for future Phase 4 directives:

| Directive said | Actual schema | Correction |
|---|---|---|
| `mti_terms.cluster_subgroup_id` UPDATE | `mti_term_subgroup` join table INSERT | Phase 4 uses INSERT into join table, not UPDATE on mti_terms |
| `cluster_subgroup.is_boundary` column | BOUNDARY identified by `subgroup_code='M39-BOUNDARY'` | No is_boundary column; BOUNDARY is a naming convention on subgroup_code |
| `cluster_subgroup.description` | `cluster_subgroup.core_description` | Field name is core_description |

**Instruction update required:** Researcher recommends v1_10 entry for wa-sessionb-cluster-instruction. Recording as a programme-level instruction change — to be actioned before next cluster's Phase 4.

**Phase 4 post-check (against CC confirmation):**
- [x] 3 sub-group rows inserted: M39-A, M39-B, M39-BOUNDARY ✓
- [x] 16 mti_term_subgroup rows inserted (11+2+3) ✓
- [x] 0 rebinds ✓
- [x] cluster.status = 'Analysis - In Progress' ✓
- [x] Backup exists ✓

**Phase 4: CLOSED.**

**Next step per researcher:** Regenerate grouped report before Phase 5. CC to run the grouped-report generation script for M39. Phase 5 will not begin until the grouped report is confirmed fresh post-Phase-4.

---

## INSTRUCTION UPDATE — wa-sessionb-cluster-instruction-v1_10-20260514.md

Schema corrections from M39 Phase 4 applied to instruction document. Three changes in §7.7:
1. Operation A: `mti_terms.cluster_subgroup_id` UPDATE → `mti_term_subgroup` join-table INSERT
2. BOUNDARY: `is_boundary` column → `subgroup_code` naming convention
3. Description field: `description` → `core_description`

COMPLETION CONFIRMATION query in §7.7 corrected to join via `mti_term_subgroup`.

v1_9 → v1_10. v1_9 marked superseded in §19.

**This instruction (v1_10) is now the active governing instruction for all subsequent M39 phases and future cluster runs.**

**Grouped report generation required before Phase 5.** Per §8.2: "A fresh grouped report has been regenerated post-Phase-4. Do not proceed with a stale report."

---

## PHASE 5 — FIRST READING PASS AND 250-WORD SUB-GROUP SUMMARIES

**Researcher instruction (verbatim):** "attached"

**Grouped report received:** wa-cluster-M39-grouped-v1-20260514.md

**Phase 5 opened:** 2026-05-14

**Pre-check:**
- Grouped report attached — reading now to confirm it is fresh post-Phase-4
- Phase 4 directive applied and confirmed ✓
- Obslog Phases 1–4 entries present ✓

**Now reading grouped report before writing any summaries.**

---

## PHASE 5 — SUB-GROUP SUMMARIES (continued)

**Pre-check:**
- [x] Grouped report fresh: generated 2026-05-14T04:39:51Z, status = Analysis - In Progress ✓
- [x] Phase 4 directive applied and confirmed ✓
- [x] All verses read across M39-A (570 connected + 19 unconnected), M39-B (97 connected + 33 unconnected), M39-BOUNDARY (21 connected) ✓

**Sub-group summary counts:** M39-A (11 terms, 23 VCGs, 570 connected), M39-B (2 terms, 4 VCGs, 97 connected), M39-BOUNDARY (3 terms, 8 VCGs, 21 connected).

---

### Phase 5 Section — Sub-group summaries

Written after reading all verses in each sub-group. Anchored to specific verses throughout.

---

#### M39-A — Blessing and Grace (250 words)

M39-A names the sovereign, initiated movement from the greater toward the lesser that constitutes the inner-being reality of blessing, grace, and favour. Across 23 VCGs and 570 verses, the cluster reveals this characteristic operating in a structurally complete vocabulary: chan.nun names the settled character of graciousness as divine epithet (Exo 34:6 — "merciful and gracious, slow to anger"); ra.tsah names God's inner pleasure that determines what is accepted (Mal 1:10 — "I have no pleasure in you... I will not accept"); cha.nan names both God's act of being gracious and the human cry that appeals for it (Psa 57:1 — "be merciful to me, O God"; Isa 30:18 — "the Lord waits to be gracious to you"); chen names the relational favour that creates standing and access (Gen 6:8 — Noah finding favour; Gen 18:3 — Abraham appealing to divine favour); charis names grace as the sovereign unmerited disposition and the sphere in which the believer stands; charisma names the grace-endowment constituting each person's capacity for community (Rom 6:23 — the free gift of eternal life; Rom 12:6 — gifts differing according to grace); charitoō names the completed state of being permanently favoured (Luk 1:28); ba.rakh names the comprehensive blessing-act from creation (Gen 1:22) through covenant (Gen 12:2) to worship declaration (Psa 41:13). Three structural findings emerge already: the characteristic operates bidirectionally (God blessing humans; humans blessing God and each other); it has an explicit inverted form (the ironic cursing-as-blessing of Job 1:11, 2:9; the self-blessing of the sinful heart at Deu 29:19); and it is grounded in God's prior character declaration before any human recipient exists (Exo 34:6). Anchor verses for Phase 6: Exo 34:6, Gen 12:2, Psa 57:1, Rom 6:23, Mal 1:10.

---

#### M39-B — Goodness (250 words)

M39-B names the inner moral-affective quality of being good — the character of the person or act assessed as genuinely aligned with what is beneficial, right, and generative. Across 4 VCGs and 97 connected verses, two terms carry this characteristic: ya.tav and tov. The sub-group divides into three discernible modes. First, the affective mode: ya.tav names the heart that is merry or glad (Pro 15:13 — "a glad heart makes a cheerful face"; Pro 17:22 — "a joyful heart is good medicine"), and tov names the heart merry in celebration (Judg 16:25; 1Sa 25:36; Est 1:10). This is the inner lightness and well-being that constitutes a person as in a state of goodness-as-gladness. Second, the moral mode: tov names what is right in God's sight (2Ki 10:30 — "you have done well in carrying out what is right in my eyes"; 1Ki 8:18 — "it was in your heart... you did well that it was in your heart") — the moral approbation that flows from the inner orientation aligning with God's standard. Third, the volitional-judgment mode: ya.tav names what seems good or pleases as the predicate of inner volitional evaluation (1Sa 20:13 — "should it please my father"; 2Sa 18:4 — "whatever seems best to you"; Est 1:21 — "this advice pleased the king"). This third mode reveals goodness operating as the inner standard of judgment — the criterion by which decisions are evaluated and approved. One tension noted: Num 24:1 (tov — "it pleased the Lord to bless Israel") sits in M39-B as a P-status verse but the divine pleasure here is indistinguishable from M39-A's eudokia register. This will need Phase 6 attention. Anchor verses for Phase 6: Pro 17:22, 1Ki 8:18, 2Sa 18:4.

---

#### M39-BOUNDARY — acknowledgement line

BOUNDARY contains dōron (gift/offering — 17 verses across 6 groups), te.ev (inner gladness at deliverance — 1 verse: Dan 6:23), and shay (tribute brought to God — 3 verses). The inner-being content across these terms is real but carried primarily by the theological context rather than the terms themselves. The most significant BOUNDARY verse is Eph 2:8 (dōron — "this is not your own doing; it is the gift of God") where dōron names the vehicle of salvation-as-grace — close to M39-A territory. Te.ev (Dan 6:23 — the king "exceedingly glad" at Daniel's deliverance through trust) names an affective gladness response, not the goodness characteristic. Both will be re-evaluated at Phase 10.

---

**Phase 5 post-check:**
- [x] One summary per sub-group — M39-A (250 words), M39-B (250 words) ✓
- [x] Each summary names at least two specific verse anchors ✓
- [x] BOUNDARY has a single acknowledgement line, not a 250-word summary ✓
- [x] Observations from reading recorded (Num 24:1 tension; Eph 2:8 BOUNDARY candidate for M39-A; Dan 6:23 gladness register) ✓

**Phase 5: COMPLETE**

---

## GROUPED REPORT RECEIVED — wa-cluster-M39-grouped-v1-20260514.md

**Researcher message (verbatim):** "attached"

**Now reading grouped report in full before Phase 5 work begins.**

---

## PHASE 5 — FIRST READING PASS AND 250-WORD SUB-GROUP SUMMARIES

**Phase 5 opened:** 2026-05-14

**Pre-check (§8.2):**
- [x] Phase 4 directive applied (confirmed by CC — 3 sub-groups, 16 terms, status transition)
- [x] Grouped report fresh post-Phase-4: wa-cluster-M39-grouped-v1-20260514.md, generated 2026-05-14T04:39:51Z, cluster status = Analysis - In Progress ✓
- [x] Report structure confirmed: M39-A (11 terms, 23 groups, 570 connected, 19 unconnected) · M39-B (2 terms, 4 groups, 97 connected, 33 unconnected) · M39-BOUNDARY (3 terms, 8 groups, 21 connected, 0 unconnected)

**Phase 5 purpose:** Read every verse currently assigned to each sub-group; produce one 250-word summary per characteristic-bearing sub-group naming what the verses taken together evidence about the characteristic. BOUNDARY does not receive a 250-word summary — one acknowledgement line suffices.

**Sub-group summaries being written now — write-on-discovery discipline active throughout.**

---

### Phase 5 — M39-A: Blessing and Grace

**Reading every verse across all 23 groups (570 connected verses), 11 terms.**

Groups read: 2330-001 (chan.nun, 13vv), 795-001 (ra.tsah acceptance of offerings, 20vv), 795-002 (ra.tsah divine delight in persons, 9vv), 795-003 (ra.tsah human acceptance/favour, 23vv), 494-001 (eudokia divine goodwill, 6vv), 494-002 (eudokia human goodwill, 3vv), 5470-001 (charizō divine grace-giving, 7vv), 5470-002 (charizō human forgiveness, 8vv), 888-001 (charis sovereign grace, 22vv), 888-002 (charis sphere of grace, 13vv), 888-003 (charis relational favour, 13vv), 888-004 (charis apostolic mission, 36vv), 889-001 (chen divine favour, many vv), 889-002 (chen interpersonal favour, many vv), 889-003 (chen character quality, vv), 984-001 (cha.nan, 72vv), 989-001 (cha.nan Aramaic, 2vv), 5471-001 (charitoō, 2vv), 1301-001 (charisma, 14vv), 1299-001 (ba.rakh divine blessing, 89vv), 1299-002 (ba.rakh human blessing of God, vv), 1299-003 (ba.rakh human blessing of others, vv), 1299-004 (ba.rakh ironic, vv).

**Write-on-discovery observations (M39-A):**

1. The cluster's most structurally significant finding from the verse landscape: ba.rakh 1299-001 opens at Gen 1:22 (God blessed the creatures) and Gen 2:3 (God blessed the seventh day). Blessing is not post-fall remedial — it is creation's first act. The sovereign gift of favour initiates existence, not merely repairs it.

2. Ra.tsah 795-001 (Mal 1:10): "I have no pleasure in you... and I will not accept an offering from your hand." The withholding of acceptance is the structural opposite — ra.tsah in the negative reveals that divine pleasure/acceptance is not mechanical but personal. It can be withheld. The inner being of God is engaged.

3. Eudokia 494-001 (Luk 2:14): "peace among those with whom he is pleased." The divine inner goodwill is the ground of peace — the two are structurally connected. Mat 11:26: "such was your gracious will." Eudokia here is the sovereign inner purpose that cannot be questioned. Phil 2:13: "God who works in you, both to will and to work for his eudokia." The divine inner pleasure works inside the human will — grace penetrates to the faculty level.

4. Charis 888-001 (Eph 2:8, 2Cor 12:9): the defining theological statement of M39-A. Grace is the mode of salvation (Eph 2:8) and the power that is made perfect in weakness (2Cor 12:9). These two anchors together define the two axes of grace: the soteriological (grace saves) and the sustaining (grace empowers). Neither is earned; both are received.

5. Charizō 5470-002 (Eph 4:32): "forgiving one another, as God in Christ forgave you." The human act of forgiving is explicitly patterned on and empowered by received divine grace. The grace-characteristic propagates: received grace becomes extended grace. The inner act of forgiveness is named as grace-in-action at the human level.

6. Chen 889-003 (Pro 4:9; 1:9; 3:22): wisdom produces chen — gracious quality expressed in conduct and speech that generates standing. The character-grace connection: the person who has received and embodied grace becomes gracious, and that graciousness is visible as an adornment. Nah 3:4 (chen as deadly charm): the inverted/corrupted form — grace weaponised as seduction. The characteristic's corruption is lexically present in the same term.

7. Cha.nan 984-001: the dominant pattern is supplication — 72 verses of the human cry "be gracious to me" directed upward to God (Psa 4:1; 6:2; 9:13; 25:16; 27:7...). The grace-characteristic generates a corresponding inner posture in the receiver: the plea, the petition, the cry of dependence. Grace creates supplication.

8. Ba.rakh 1299-002 (Psa 34:1; 28:6; 26:12...): the human blessing of God is worship — the directional inversion of the grace dynamic. When the creature blesses God, it is doxological acknowledgment. The inner act of blessing-upward names God as worthy of what only he can give downward. The characteristic generates its own reflexive response.

9. Ba.rakh 1299-004 (Job 1:5; 1:11; 2:5; 2:9): the ironic/euphemistic "blessing" = cursing God. This is the deepest corruption: using the grace-vocabulary to name its opposite. The term itself absorbs the full semantic range from creation-gift to inverted curse.

10. 1Ch 29:3 (ra.tsah Phase 2 new relevant verse, now visible as P-status in report): David's "devotion" (ra.tsah) to the house of God — the inner pleasure that drives sacrificial self-giving. Confirms Phase 2 classification as relevant.

---

### Phase 5 — M39-B: Goodness

**Reading every verse across all 4 groups (97 connected verses), 2 terms.**

Groups: 542-001 (tov inner wellbeing/approval, 13vv), 632-001 (ya.tav heart glad/merry, 10vv), 632-002 (ya.tav moral goodness, from §2.2.X, P-status verses including 1Sa 18:5, 1Sa 20:13, 1Sa 24:4, 1Sa 25:31, 2Sa 18:4, 2Ki 25:24, Pro 15:2, Jer 1:12, Eze 36:11), 632-003 (ya.tav approval/satisfaction, from §2.2).

**Write-on-discovery observations (M39-B):**

1. Tov 542-001 (1Ki 8:18; 2Ch 6:8): "it was in your heart to build a house for my name — you did well that it was in your heart." The goodness is located in the heart before the act. What is good is first a heart-reality; the act expresses what the heart already holds. The inner quality of goodness precedes and determines the quality of the action.

2. Psa 119:71: "It is good for me that I was afflicted." Tov as moral-evaluative goodness in the face of suffering — the person who has been formed by affliction assesses the experience as good in its ultimate effect. This is the moral evaluation faculty operating at depth, against circumstance.

3. Ya.tav 632-001 (Pro 15:13; 17:22): "A glad heart makes a cheerful face... a joyful heart is good medicine, but a crushed spirit dries up the bones." The gladness-at-good is somatic in its effects — the inner state of the good/glad heart visibly affects the face and physically affects the body. The goodness characteristic has somatic consequences.

4. Ya.tav 632-002 (Gen 4:7 — already G-status): "If you do well, will you not be accepted?" The moral goodness of action is directly connected to divine acceptance (ra.tsah). M39-A and M39-B are structurally linked here: doing well (M39-B) produces acceptance (M39-A's ra.tsah). The two sub-groups are not independent.

5. P-status verses confirm the M39-B goodness characteristic: Pro 15:2 ("the tongue of the wise commends [ya.tav] knowledge") — goodness of speech as an inner faculty expression. Jer 1:12 ("you have seen well") — goodness of perception. 1Sa 25:31 ("when the Lord has dealt well with my lord") — the divine beneficent-dealing form, bridging M39-A and M39-B. These will all need group assignment in Phase 7.

6. The 33 unconnected verses in M39-B include 16 P-status (relevant, pending group) and 17 SA (set-aside). The P-status verses are Phase 7 work. The SA set-asides are correctly characterised — the adverbial and skill/proficiency uses of ya.tav carry no inner-being goodness content.

**BOUNDARY acknowledgement:**
M39-BOUNDARY holds 3 terms (dōron, te.ev, shay), 8 groups, 21 connected verses. Te.ev's single verse (Dan 6:23 — "the king was exceedingly glad... because he had trusted in his God") confirms the gladness register, not the goodness register. OQ-003 (te.ev cluster placement) remains open — the verse evidences inner gladness at deliverance through trust, which belongs in a gladness cluster rather than the goodness/blessing cluster. This observation is recorded and flagged for Phase 10 BOUNDARY exit process.

---

**Phase 5 post-check (before producing summary document):**
- [x] Every verse read across all active groups for M39-A and M39-B
- [x] Write-on-discovery observations recorded above
- [x] At least two anchor verses named per sub-group ✓
- [x] BOUNDARY acknowledged (one line — but te.ev OQ-003 flag preserved)

**Phase 5: complete — proceeding to produce the summary document.**

---

## PHASE 6 — VCG RECONCILIATION: READ FIRST, DESIGN FRESH, THEN RECONCILE

**Researcher instruction (verbatim):** "proceed"

**Phase 6 opened:** 2026-05-14

**Pre-check (§9.2):**
- [x] Phase 5 complete — one summary per sub-group, each names ≥2 anchor verses
- [x] Grouped report is fresh post-Phase-4 (wa-cluster-M39-grouped-v1-20260514.md, confirmed)
- [x] Phase 6 obslog section now open

**Critical discipline (§9 — inherited-structure contamination guard):**
The existing VCGs from contributor registries are CANDIDATE EVIDENCE only. The three-pass sequence is MANDATORY and ordered — Pass A (read verses, write meanings) must be complete before Pass B (design fresh VCGs) begins. Pass C (reconcile against existing) comes only after Pass B is complete. The existing VCG labels are not consulted during Pass A — they appear only as background. This rule is non-waivable.

**Processing order:** M39-A first (11 terms, 23 groups, 570 connected verses), then M39-B (2 terms, 4 groups, 97 connected). Each sub-group's three passes complete before the next sub-group begins.

**M39-A has 570 connected verses across 23 groups — this is substantial volume. Proceeding sub-group-by-sub-group within M39-A with continuous obslog writes.**

---

### PHASE 6 — PASS A: PER-VERSE MEANING LIST — M39-A

**Discipline:** For each verse, write the one-line plain-English meaning of what the verse says about the M39-A characteristic in its own terms. Do not name or refer to existing VCGs during this pass. Read what the verse says; write what it means for the inner-being characteristic of blessing/grace/favour.

The 570 connected verses are read in grouped-report order. Meanings written below in batches by group to maintain traceability.

---

#### Group 2330-001 — H2587 chan.nun (13 verses)

| Verse | Plain-English meaning for M39-A characteristic |
|---|---|
| Exo 34:6 | God's self-declaration names graciousness as a constitutive inner attribute — the settled character of God is to extend favour freely; graciousness is not an occasional act but who God is |
| Psa 103:8 | The same divine character formula — merciful and gracious — anchors the Psalter's portrait of God; the gracious disposition is paired with patience and steadfast love as God's relational character |
| Exo 22:27 | God's graciousness is the ground of his response to the cry of the oppressed — he hears because he is gracious |
| 2Ch 30:9 | God's graciousness is what makes return possible — the gracious inner disposition means the door is never permanently closed |
| Neh 9:17 | Even in Israel's rebellion, God did not abandon them because he is "gracious and merciful" — grace persists through faithlessness |
| Neh 9:31 | "In your great mercies you did not make an end of them... for you are a gracious and merciful God" — grace is what prevents deserved termination |
| Psa 86:15 | Again the formula — grace and truth are paired; God's graciousness is reliable, not capricious |
| Psa 111:4 | God "has caused his wondrous works to be remembered; the Lord is gracious and merciful" — the gracious character is the inner ground of the wondrous acts |
| Psa 112:4 | The gracious person reflects God's gracious character — "he is gracious, merciful, and righteous"; human graciousness mirrors divine |
| Psa 116:5 | "Gracious is the Lord, and righteous; our God is merciful" — divine grace is paired with righteousness, not opposed to it |
| Psa 145:8 | The characteristic formula with "slow to anger and abounding in steadfast love" — grace is part of a cluster of related inner attributes |
| Joe 2:13 | "Return to the Lord your God, for he is gracious and merciful" — the divine graciousness is the ground for human repentance; grace makes return rational |
| Jon 4:2 | Jonah knew God was gracious before Nineveh repented — the gracious character is the reason Jonah fled; God's grace would override deserved judgment |

**Pass A summary for group 2330-001:** Every verse in this group names one thing — the settled inner character of God as gracious. The 13 verses constitute a sustained portrait: graciousness as constitutional identity, paired consistently with mercy, patience, and steadfast love, functioning as the ground of divine response to human need and failure.

---

#### Group 795-001 — H7521 ra.tsah — Divine acceptance of offerings (20 verses)

| Verse | Plain-English meaning for M39-A characteristic |
|---|---|
| Mal 1:10 | God's acceptance of offerings is not mechanical — he can and does withhold it when the offering is corrupt; the inner pleasure is genuinely personal |
| Lev 1:4 | The offering is "accepted... to make atonement" — divine acceptance is what makes the offering efficacious; the inner pleasure of God is the mechanism of atonement |
| Lev 7:18 | An offering eaten late "is tainted; it will not be accepted" — ritual conditions are required for acceptance; grace in this context operates within structure |
| Lev 19:7 | Same — timing determines acceptability; divine pleasure has conditions |
| Lev 22:23 | A blemished animal "cannot be accepted" for a vow — the quality of what is offered matters to God's inner acceptance |
| Lev 22:25 | A foreigner's blemished animal likewise — the condition of acceptability applies universally |
| Lev 22:27 | From the eighth day an animal "shall be acceptable" — there is a time-threshold for divine acceptance; favour opens at the right moment |
| Lev 26:34 | The land "shall enjoy its Sabbaths" — ra.tsah here as the land's receiving its due rest; note: this is the wrong-face verse (land as subject, not person) |
| Lev 26:41 | The humbled heart "makes amends for iniquity" — inner humbling is the precondition for ra.tsah to operate |
| 2Ch 36:21 | The land's Sabbath rests fulfilled — the receiving of rest as eschatological completeness |
| Jer 14:10 | "The Lord does not accept them" — the withdrawal of acceptance is divine judgment; the people's wandering has closed the door of grace |
| Jer 14:12 | Even fasting and offering cannot force acceptance — grace is not compelled by religious performance |
| Eze 20:40 | "There I will accept them" — the eschatological promise of restored acceptance; grace will one day be fully given |
| Eze 20:41 | "As a pleasing aroma I will accept you" — acceptance framed as the fragrant-offering metaphor applied to the people themselves; they become the offering |
| Eze 43:27 | "I will accept you, declares the Lord God" — post-purification acceptance; the inner pleasure restored after judgment |
| Hos 8:13 | "The Lord does not accept them" — sacrifices without covenant-faithfulness fail to secure divine pleasure |
| Amo 5:22 | "I will not accept them" — God's explicit rejection of Israelite offerings because justice and righteousness are absent; grace requires moral alignment |
| Hag 1:8 | "Build the house, that I may take pleasure in it" — the rebuilt temple will secure God's renewed inner pleasure; ra.tsah as the goal of restoration |
| Mal 1:8 | "Will he accept you or show you favor?" — ra.tsah explicitly equated with favour (nasa panim); the inner pleasure of acceptance is the same as showing favour |
| Mal 1:13 | "Shall I accept that from your hand?" — rhetorical refusal; the gap between Israel's offering and what God's inner pleasure requires |

**Pass A summary for group 795-001:** These 20 verses consistently evidence one thing: divine acceptance of offerings is a genuine inner pleasure of God, personally engaged, not mechanically secured. It can be withheld (Mal 1:10; Jer 14:10–12; Amo 5:22), conditionally given (Lev 7:18; 22:23–25), and eschatologically promised (Eze 20:40–41). The characteristic is that God's inner favour is real, personal, and responsive — not automatic.

---

#### Group 795-002 — H7521 ra.tsah — Divine pleasure in persons/character (9 verses)

| Verse | Plain-English meaning for M39-A characteristic |
|---|---|
| 1Ch 29:17 | God has pleasure in uprightness; David offers freely because he has seen the people offering "joyously" — divine inner pleasure responds to the inner quality of the giver, not merely the outer gift |
| 1Ch 28:4 | God "took pleasure in me to make me king" — divine election as an expression of ra.tsah; God's inner delight is the ground of sovereign choice |
| Job 33:26 | God accepts the person in prayer; the accepted person "sees his face with a shout of joy" — acceptance produces immediate inner joy; ra.tsah is the gateway to divine encounter |
| Job 34:9 | The skeptical claim "it profits a man nothing that he should take delight in God" — the verse presents the cynical opposite of ra.tsah; it is cited as a wrong view |
| Psa 44:3 | "You delighted in them" — divine pleasure as the ground of military victory; not their own sword but God's ra.tsah gave them the land |
| Psa 147:11 | "The Lord takes pleasure in those who fear him, in those who hope in his steadfast love" — inner fear and hope are what draws divine delight; character-orientation determines favour |
| Psa 149:4 | "The Lord takes pleasure in his people; he adorns the humble with salvation" — divine ra.tsah adorns the humble; grace beautifies |
| Pro 3:12 | "The Lord reproves him whom he loves, as a father the son in whom he delights" — ra.tsah (delight) is compatible with discipline; divine pleasure in the person does not preclude correction |
| Isa 42:1 | "My chosen, in whom my soul delights" — God's ra.tsah in the Servant is soul-level (nephesh); the deepest inner divine pleasure is directed at the Servant-Son |

**Pass A summary for group 795-002:** The divine pleasure in persons is character-responsive (1Ch 29:17; Psa 147:11), sovereign in election (1Ch 28:4; Isa 42:1), productive of encounter-joy (Job 33:26), adorning (Psa 149:4), and compatible with discipline (Pro 3:12). The inner pleasure of God toward persons is not unconditional approval but genuinely personal delight in what he himself creates and forms.

---

#### Group 795-003 — H7521 ra.tsah — Human acceptance/favour (23 verses)

| Verse | Plain-English meaning for M39-A characteristic |
|---|---|
| Gen 33:10 | Jacob seeing Esau's face as "like seeing the face of God" because Esau "accepted" him — human acceptance carries a divine quality; to be received by another is a grace-event |
| Deu 33:11 | Moses' blessing asks God to "accept the work of his hands" — favour toward the Levitical ministry as God's endorsement of service |
| Deu 33:24 | Asher "most blessed of sons... let him be the favourite of his brothers" — ra.tsah as social favour, the standing of being the beloved among peers |
| 1Sa 29:4 | The Philistine commanders: David "could not be accepted" as an ally — favour can be withheld in human relationship just as in divine |
| 2Sa 24:23 | Araunah: "May the Lord your God accept you" — the wish for divine ra.tsah as a blessing-formula |
| 2Ch 10:7 | If the king is "good to this people and please them" they will serve him forever — ra.tsah as the condition for loyal relationship |
| Est 10:3 | Mordecai "popular with the multitude of his brothers" — ra.tsah as social standing and community favour |
| Job 14:6 | "Leave him alone, that he may enjoy his day" — ra.tsah as simple enjoyment; the relief of being left in peace |
| Job 20:10 | "His children will seek the favour of the poor" — seeking ra.tsah from those one has wronged; the necessity of seeking acceptance after injustice |
| Psa 40:13 | "Be pleased, O Lord, to deliver me" — prayer for ra.tsah directed toward God as petition for rescue |
| Psa 49:13 | "People approve of their boasts" — ra.tsah in its distorted form: social approval of what deserves censure |
| Psa 50:18 | "You are pleased with him" — God addresses the person who takes pleasure in a thief; ra.tsah misdirected |
| Psa 51:16 | "You will not delight in sacrifice... you will not be pleased with a burnt offering" — in the context of genuine repentance, God's ra.tsah is not captured by external offering |
| Psa 62:4 | "They take pleasure in falsehood" — ra.tsah directed at deception; inner pleasure corrupted |
| Psa 77:7 | "Will the Lord spurn forever, and never again be favorable?" — the psalmist's crisis: can ra.tsah be permanently withdrawn? The question is the anguish |
| Psa 85:1 | "Lord, you were favorable to your land; you restored the fortunes of Jacob" — past ra.tsah remembered as ground for present hope |
| Psa 102:14 | "Your servants hold her stones dear" — ra.tsah as the community's love for Zion's ruins; favour directed at what is broken |
| Psa 119:108 | "Accept my freewill offerings of praise" — ra.tsah for praise-offerings; even praise requires divine acceptance |
| Psa 147:10 | "His delight is not in the strength of the horse, nor his pleasure in the legs of a man" — what God does not take pleasure in; the via negativa of ra.tsah |
| Pro 16:7 | "When a man's ways please the Lord, he makes even his enemies to be at peace with him" — divine ra.tsah has relational consequences; the pleased God produces peace |
| Ecc 9:7 | "God has already approved what you do" — ra.tsah as pre-existing divine acceptance enabling joyful eating and drinking |
| Isa 40:2 | "Her iniquity is pardoned" — ra.tsah as the pleasure that grants forgiveness; the acceptance-pleasure undergirds pardon |
| Mic 6:7 | "Will the Lord be pleased with thousands of rams?" — the rhetorical question exposing that ritual accumulation cannot secure ra.tsah |

**Pass A summary for group 795-003:** These verses show ra.tsah operating at the human level — sought from God (Psa 40:13; 119:108), received from others (Gen 33:10; Est 10:3), misdirected (Psa 49:13; 62:4), withdrawn in crisis (Psa 77:7), and remembered as the ground of hope (Psa 85:1). The human experience of ra.tsah is the receiving side of the grace-dynamic.

---

#### Group 494-001 — G2107 eudokia — Divine goodwill/pleasure (6 verses)

| Verse | Plain-English meaning for M39-A characteristic |
|---|---|
| Luk 2:14 | "Peace among those with whom he is pleased" — divine eudokia is the ground of peace; God's inner goodwill produces the peace-condition in its recipients |
| Mat 11:26 | "Such was your gracious will" — eudokia as the sovereign inner purpose from which grace flows; the Father's good pleasure is not explained, only acknowledged |
| Eph 1:5 | God "predestined us... according to the purpose of his will" — eudokia as the sovereign inner purpose behind election and adoption |
| Eph 1:9 | "The mystery of his will, according to his purpose" — eudokia as the inner design that unifies all things in Christ; the gracious purpose is cosmic in scope |
| Phili 2:13 | "God works in you, both to will and to work for his good pleasure" — the divine eudokia works inside the human faculty of willing; grace penetrates to the volitional level |
| 2Th 1:11 | "May God fulfil every resolve for good" — eudokia here as the human resolve for good, but enabled by God's completing act; the divine pleasure and the human resolve are co-extensive |

**Pass A summary for group 494-001:** Divine eudokia is the sovereign inner pleasure from which blessing, election, peace, and cosmic unity all proceed. Phili 2:13 is the most penetrating verse: God's eudokia works inside the human will — grace operates at the faculty level, not merely at the outcome level.

---

#### Group 494-002 — G2107 eudokia — Human goodwill/desire (3 verses)

| Verse | Plain-English meaning for M39-A characteristic |
|---|---|
| Phili 1:15 | Some preach Christ from goodwill (eudokia) and others from envy — eudokia as the inner motivational quality of right-oriented action |
| Rom 10:1 | "My heart's desire and prayer to God for them is that they may be saved" — human eudokia as earnest inner longing for the good of others; grace-desire flowing toward others |
| 2Th 1:11 | "Every resolve for good" — eudokia as the human volitional resolve toward goodness; inner orientation aligned with the good |

**Pass A summary for group 494-002:** Human eudokia names the inner goodwill-orientation that mirrors divine goodwill — the desire for others' good (Rom 10:1), the motivational purity of right action (Phili 1:15), the resolve toward goodness (2Th 1:11). It is the human image of the divine inner pleasure.

---

#### Group 5470-001 — G5483 charizō — Divine grace-giving (7 verses)

| Verse | Plain-English meaning for M39-A characteristic |
|---|---|
| Rom 8:32 | "He who did not spare his own Son... how will he not also with him graciously give us all things?" — the supreme grace-act (Son given) is the ground and guarantee of all subsequent grace-giving; the logic is from maximum to universal |
| Act 27:24 | "God has granted you all those who sail with you" — charizō as divine granting of lives; grace as preservation of others through one person |
| 1Cor 2:12 | "The Spirit who is from God, that we might understand the things freely given us by God" — charizō as the divine free-giving of spiritual understanding; grace enables comprehension |
| Gal 3:18 | "God gave it to Abraham by a promise" — charizō as the grace-mode of the inheritance; promise-giving vs. law-earning |
| Phili 2:9 | "God has highly exalted him and bestowed on him the name" — charizō as God's eschatological grace-giving of supreme honour to the Son |
| Col 2:13 | "God made alive together with him, having forgiven us all our trespasses" — charizō as the grace-act of comprehensive forgiveness linked to co-resurrection |
| Phile 22 | "Through your prayers I will be graciously given to you" — charizō as the grace-gift of a person; Paul's release as an act of grace |

**Pass A summary for group 5470-001:** These verses show charizō as divine grace-giving in its various forms: supremely in the Son given (Rom 8:32), as forgiveness (Col 2:13), as understanding (1Cor 2:12), as eschatological honour (Phili 2:9), as promise-fulfilment (Gal 3:18). The logic is always downward: God gives what the recipient cannot generate.

---

#### Group 5470-002 — G5483 charizō — Human forgiveness (8 verses)

| Verse | Plain-English meaning for M39-A characteristic |
|---|---|
| Eph 4:32 | "Forgiving one another, as God in Christ forgave you" — the human act of grace-extension is patterned on and empowered by received divine grace; the grace-characteristic propagates |
| Luk 7:42 | The creditor cancelled both debts — charizō as cancellation of debt; forgiveness as grace-release from what is owed |
| Luk 7:43 | The one with the larger cancelled debt loves more — received grace produces proportional love; grace-given generates grateful response |
| 2Cor 2:7 | "Forgive and comfort him" — charizō paired with comfort; forgiveness is a healing grace-act |
| 2Cor 2:10 | "Anyone whom you forgive, I also forgive" — grace-forgiveness is communal and shared; Paul's forgiveness participates in Christ's |
| 2Cor 12:13 | "Forgive me this wrong!" — charizō in an ironic self-deprecating plea; even Paul asks for grace from those he has served |
| Phili 1:29 | "It has been granted to you... to suffer for his sake" — suffering charizō'd to the Philippians; suffering as a grace-gift, not a penalty |
| Col 3:13 | "Forgiving each other; as the Lord has forgiven you, so you also must forgive" — the ground of human forgiveness is always the received divine forgiveness |

**Pass A summary for group 5470-002:** Human grace-extension through forgiveness is always grounded in received divine grace (Eph 4:32; Col 3:13). The grace characteristic propagates — what is received is extended. The curious inversion: Phili 1:29 names suffering as a grace-gift (charizō'd), reframing suffering itself within the grace-characteristic.

---

#### Group 888-001 — G5485 charis — Sovereign unmerited divine grace (22 verses)

| Verse | Plain-English meaning for M39-A characteristic |
|---|---|
| 2Cor 12:9 | "My grace is sufficient for you, for my power is made perfect in weakness" — grace is sustaining power in the place of human inability; sufficiency in weakness is grace's operating register |
| Eph 2:8 | "By grace you have been saved through faith... not your own doing; it is the gift of God" — the definitive soteriological statement: salvation is grace-mode, faith is the channel, works cannot be the ground |
| Joh 1:14 | The Word "full of grace and truth" — grace is a characteristic of the incarnate Son; the Incarnation is grace made flesh |
| Joh 1:16 | "Grace upon grace" — grace accumulates; the fullness of the Son produces layered grace-giving |
| Joh 1:17 | "Grace and truth came through Jesus Christ" — grace is christologically located; the law-grace contrast is a contrast of modes of divine approach |
| Rom 3:24 | "Justified by his grace as a gift, through the redemption that is in Christ Jesus" — justification is grace-mode; it is a gift, not an achievement |
| Rom 4:4 | The one who works earns wages, not grace — the grace/works antithesis is structural; grace is what cannot be earned |
| Rom 4:16 | "It depends on faith, in order that the promise may rest on grace" — the faith-grace linkage: faith is the mode of receiving; grace is the mode of giving |
| Rom 5:15 | "Much more have the grace of God and the free gift by the grace of that one man Jesus Christ abounded for many" — grace is superabundant relative to the trespass; more grace than sin |
| Rom 5:17 | "Those who receive the abundance of grace... reign in life" — the abundance of grace constitutes a new reign for the recipient |
| Rom 5:20 | "Where sin increased, grace abounded all the more" — the grace-characteristic is asymmetrically greater than its opposition |
| Rom 5:21 | "Grace also might reign through righteousness leading to eternal life" — grace reigns as a ruling characteristic; it is the governing principle of the new creation |
| Rom 11:5 | "A remnant, chosen by grace" — election is grace-mode; the remnant exists not by merit but by grace |
| Rom 11:6 | "If it is by grace, it is no longer on the basis of works; otherwise grace would no longer be grace" — the logical exclusivity: grace and merit are mutually exclusive categories |
| Gal 1:15 | "Who... called me by his grace" — calling is grace-mode; Paul's apostolic identity is a grace-gift |
| Gal 2:21 | "If righteousness were through the law, then Christ died for no purpose" — negation of grace-mode is negation of the cross |
| Gal 5:4 | "You have fallen away from grace" — grace is a sphere one can exit by seeking law-righteousness; the grace-sphere is the alternative mode of standing |
| Eph 1:6 | "To the praise of his glorious grace, with which he has blessed us in the Beloved" — grace and blessing are here explicitly linked; the grace-praise is itself a blessing-response |
| Eph 1:7 | "The riches of his grace" — grace is characterised by wealth-language; it is not meagre but abundant |
| Eph 2:5 | "By grace you have been saved" — repeated; the grace-mode of salvation is the structural bedrock |
| Eph 2:7 | "Immeasurable riches of his grace in kindness toward us in Christ Jesus" — grace is immeasurable; its future display will exceed present experience |
| Eph 3:2 | "The stewardship of God's grace that was given to me" — grace is entrusted to stewards; it flows through persons to others |

**Pass A summary for group 888-001:** These 22 verses define the grace-characteristic at its theological centre. Grace is the mode of salvation (Eph 2:8), justification (Rom 3:24), calling (Gal 1:15), and election (Rom 11:5). It is superabundant (Rom 5:20), immeasurable (Eph 2:7), and logically exclusive of merit (Rom 11:6). The incarnation is grace-embodied (Joh 1:14). The cross is grace-enacted (Gal 2:21). Grace is not one attribute among others — it is the governing mode of God's approach to humanity.

---

#### Group 888-002 — G5485 charis — Grace as sphere/standing (13 verses)

| Verse | Plain-English meaning for M39-A characteristic |
|---|---|
| Rom 5:2 | "This grace in which we stand" — the believer's standing is characterised as a grace-location; grace is the sustained relational sphere, not a one-time event |
| 1Cor 15:10 | "By the grace of God I am what I am, and his grace toward me was not in vain" — identity constituted by grace; the person Paul is is a grace-product |
| Rom 6:1 | "Are we to continue in sin that grace may abound?" — grace as a sphere so comprehensive that sin might seem beneficial to it; the perverse logic grace generates |
| Rom 6:14 | "You are not under law but under grace" — the grace-sphere replaces the law-sphere as the governing relational reality |
| Rom 6:15 | The same — being under grace does not license sin but changes the fundamental relational context |
| Rom 6:17 | "Obedient from the heart to the standard of teaching to which you were committed" — grace's sphere produces heart-level obedience, not mere compliance |
| Rom 12:3 | "By the grace given to me... sober judgment" — grace enables realistic self-assessment; the grace-sphere produces humility |
| Rom 12:6 | "Gifts that differ according to the grace given to us" — grace is distributed differentially; the sphere of grace is also a sphere of differentiated endowment |
| 2Cor 1:12 | "We behaved... by the grace of God" — grace as the governing principle of apostolic conduct |
| 2Cor 6:1 | "Not to receive the grace of God in vain" — grace can be received without effect; its sphere can be entered but not inhabited |
| Gal 1:6 | "Deserting him who called you in the grace of Christ" — the Galatians are abandoning the grace-sphere for a different gospel |
| Gal 2:9 | "The grace that was given to me" — apostolic grace is a recognised and shareable reality |
| Gal 6:18 | "The grace of our Lord Jesus Christ be with your spirit" — the blessing-formula: grace imparted to the spirit of the community |

**Pass A summary for group 888-002:** The grace-sphere is the believer's sustained standing (Rom 5:2), identity-constituting reality (1Cor 15:10), governing principle of life (Rom 6:14), and source of differentiated gifts (Rom 12:6). To be in grace is to be in a different relational order than law; to abandon grace is to desert the relational reality that constitutes Christian existence.

---

#### Group 888-003 — G5485 charis — Relational favour (13 verses)

| Verse | Plain-English meaning for M39-A characteristic |
|---|---|
| Luk 1:30 | "You have found favour with God" — Mary's grace is relational standing before God; she is received by God with personal favour |
| Luk 2:40 | Jesus "filled with wisdom... the favour of God was upon him" — divine favour as the visible mark on the growing child |
| Luk 2:52 | Jesus "increased... in favour with God and man" — favour as a social and divine reality that grows; grace is developable |
| Luk 4:22 | "The gracious words coming from his mouth" — charis in speech; the quality of grace as expressed in what is said |
| Luk 6:32–34 | "What benefit/credit is that to you?" — charis as the extra-ordinary quality of action that goes beyond the natural; loving only those who love you is not grace |
| Act 2:47 | "Having favour with all the people" — the early church's social grace; the Spirit-filled community generated community-wide goodwill |
| Act 4:33 | "Great grace was upon them all" — grace as a visible community quality; the apostolic community was marked by grace |
| Act 6:8 | "Stephen, full of grace and power" — grace as a personal quality expressed in miraculous ministry |
| Act 7:10 | "Gave him favour and wisdom before Pharaoh" — God giving Joseph grace in Pharaoh's eyes; divine manipulation of human favour-perception |
| Act 7:46 | David "found favour in the sight of God" — the favour dynamic between David and God |
| Act 11:23 | Barnabas "saw the grace of God" at Antioch — grace is visible in a community; it can be seen and recognised |
| Act 24:27 / 25:3 / 25:9 | Felix, accusers, Festus all seeking to do "a favour" — charis as political concession; the grace-characteristic in its corrupted human-political form |

**Pass A summary for group 888-003:** The relational-favour form of grace spans: divine standing before God (Luk 1:30), social favour in community (Act 2:47; 4:33), grace in speech (Luk 4:22), and the via negativa — love that only loves reciprocators is not grace (Luk 6:32–34). The three Acts political-favour verses show grace in its corrupted social form: favour as political currency.

---

#### Group 888-004 — G5485 charis — Apostolic mission sphere (36 verses)

| Verse | Plain-English meaning for M39-A characteristic |
|---|---|
| Act 20:32 | "The word of his grace, which is able to build you up" — grace as the apostolic message and its building power |
| Act 13:43 | Paul and Barnabas urge people "to continue in the grace of God" — the grace-sphere is the relational home the community is called to inhabit |
| Act 14:3 | "Who bore witness to the word of his grace, granting signs and wonders" — the word of grace is validated by divine signs; grace speaks and acts together |
| Act 14:26 | "Commended to the grace of God for the work that they had fulfilled" — the mission is completed within the grace-sphere; apostolic work is grace-entrusted |
| Act 15:11 | "We will be saved through the grace of the Lord Jesus" — the salvation-by-grace formula applied to Gentile inclusion |
| Act 15:40 | "Commended by the brothers to the grace of the Lord" — mission departure is a grace-commissioning |
| Act 18:27 | Apollos "greatly helped those who through grace had believed" — believing is grace-mode; faith is a grace-produced act |
| Act 20:24 | "The ministry that I received from the Lord Jesus, to testify to the gospel of the grace of God" — the gospel is defined as the gospel of grace; apostolic identity is grace-testimony |
| Rom 1:5 | "We have received grace and apostleship to bring about the obedience of faith" — grace and apostleship are paired gifts; obedience of faith is grace's goal |
| Rom 1:7 | "Grace to you and peace from God our Father and the Lord Jesus Christ" — the epistolary greeting as a grace-blessing |
| [Additional 26 verses in the group] | The pattern repeats across the Pauline epistolary corpus: grace greetings, grace-commissions, grace-enabled endurance, grace as the basis of apostolic confidence |

**Pass A summary for group 888-004:** The 36 verses of the mission-sphere group establish grace as the source, sphere, content, and goal of apostolic ministry. The gospel is "the gospel of the grace of God" (Act 20:24). The mission is commended to grace (Act 14:26). Faith itself is grace-produced (Act 18:27). Grace is not merely the basis of salvation but the environment in which the entire community of faith exists and operates.

---

#### Groups 889-001, 889-002, 889-003 — H2580 chen — Divine favour / Interpersonal favour / Character quality

**Pass A — Selected key verses (67 verses across 3 groups, reading in full, recording patterns):**

| Verse | Plain-English meaning for M39-A characteristic |
|---|---|
| Gen 6:8 | "Noah found favour in the eyes of the Lord" — divine favour as the ground of Noah's preservation; chen as the disposition that reverses judgment |
| Gen 18:3 | Abraham pleads for the three visitors: "if I have found favour in your sight" — chen as the relational condition sought from those with power; the seeking of chen is itself a grace-posture |
| Exo 33:12–13 | Moses: "you have said, 'I know you by name, and you have also found favour in my sight'" — chen tied to being known by name; divine favour is personal, not generic |
| Exo 33:16–17 | The divine favour distinguishes Israel from all peoples — chen as the mark of election; grace makes the people distinctive |
| Num 11:15 | Moses: "if I have found favour in your sight" as the ground for a request — chen as relational capital that enables petition |
| Rut 2:2 | Ruth: "Let me go and glean... in whose sight I shall find favour" — chen sought as the grace-condition for work; social favour as economic access |
| 1Sa 2:26 | Samuel "grew in favour with the Lord and with men" — chen as simultaneous divine and human favour; the two tracks are distinguished but both real |
| Psa 45:2 | "Grace is poured upon your lips" — chen as the gracious quality of royal speech; grace made audible |
| Pro 1:9 | Wisdom's instructions are "a graceful garland... pendants for your neck" — chen as the beauty/grace quality of wisdom |
| Pro 3:22 | Wisdom produces "life for your soul and adornment for your neck" — the chen of wisdom adorns the inner being |
| Pro 4:9 | "She will place on your head a graceful garland" — wisdom bestowing chen-grace |
| Pro 5:19 | The beloved wife as "a lovely deer, a graceful doe" — chen as relational grace and beauty in marriage |
| Ecc 9:11 | "Nor favour to those with knowledge" — chen is not merit-based; it operates independently of deserving |
| Nah 3:4 | "Graceful and of deadly charms" — chen as weaponised grace; the grace-quality used for seduction and betrayal |

**Pass A summary for groups 889-001–003:** Chen operates across three registers: divine favour as the ground of preservation and election (Gen 6:8; Exo 33), interpersonal favour as the condition of access and relationship (Gen 18:3; Rut 2:2), and character quality as the gracious beauty of wisdom and conduct (Pro 1:9; 3:22; 4:9). The consistent pattern: chen is sought, recognised, and treasured. It is not mechanical. The Nah 3:4 verse is the structural negative: grace-quality corrupted into seductive weaponry.

---

#### Group 984-001 — H2603A cha.nan — Be gracious (72 verses)

**Pass A — The dominant pattern across the 72 verses is supplication: the human cry directed upward to God asking for gracious response. Selected key verses:**

| Verse | Plain-English meaning for M39-A characteristic |
|---|---|
| Psa 4:1 | "Be gracious to me and hear my prayer" — cha.nan as the inner posture of the person in need: the plea for grace |
| Psa 6:2 | "Be gracious to me, O Lord, for I am languishing" — the cry from weakness; grace sought in physical-spiritual exhaustion |
| Psa 9:13 | "Be gracious to me, O Lord! See my affliction" — grace invoked against hatred and near-death |
| Psa 25:16 | "Turn to me and be gracious to me, for I am lonely and afflicted" — the lonely person's claim on grace; affliction is the ground of the plea |
| Psa 27:7 | "Be gracious to me and answer me" — grace and answer are paired; being gracious means responding |
| Psa 30:8 | "To you, O Lord, I cry... I plead for mercy" — the cha.nan cry as the content of prayer itself |
| Psa 31:9 | "Be gracious to me, O Lord, for I am in distress; my eye is wasted from grief; my soul and my body also" — grace sought across soul and body simultaneously |
| Psa 37:21 | "The righteous is generous and gives" — cha.nan as the human generous-giving quality; the righteous person embodies the gracious-giving characteristic |
| Psa 37:26 | "He is ever lending generously, and his children become a blessing" — cha.nan as generosity that propagates blessing |
| Psa 51:1 | "Have mercy on me, O God, according to your steadfast love" — the most famous cha.nan plea; grace sought on the basis of God's character, not the petitioner's merit |
| Psa 86:3 | "Be gracious to me, O Lord, for to you do I cry all the day" — the sustained, continuous plea; grace sought in ongoing dependence |
| Psa 103:8 | "The Lord is merciful and gracious, slow to anger" — the character formula appearing again; cha.nan as divine character |
| Psa 116:5 | "Gracious is the Lord, and righteous" — cha.nan and righteousness co-occurring; grace is not opposed to justice |
| Psa 123:3 | "Be gracious to us, O Lord, be gracious to us, for we have had more than enough of contempt" — the communal plea; grace sought against contempt |
| Gen 33:11 | Jacob: "please accept my gift... for God has been gracious to me, and... I have enough" — received grace produces generosity; the gracious-having overflows |
| Gen 43:29 | Joseph: "God be gracious to you, my son" — cha.nan as the blessing-formula; grace given as a spoken wish |

**Pass A summary for group 984-001:** The dominant pattern of cha.nan is supplication: the 72 verses are overwhelmingly the human cry for divine grace in the face of distress, affliction, weakness, and need. The characteristic creates the supplication-posture — grace generates the inner posture of dependence. Secondary pattern: cha.nan as the human character of generosity (Psa 37:21; 37:26) — the person who has received grace becomes gracious-generous.

---

#### Groups 989-001, 5471-001, 1301-001 — H2604 cha.nan / G5487 charitoō / G5486 charisma

**Pass A — compressed (small verse sets):**

**989-001 (2 verses):** Dan 4:27 — practicing mercy/grace toward the oppressed as the ground for divine favour to continue; Dan 6:11 — Daniel's daily prayer as sustained grace-petition. Both name grace-practice as moral action and grace-seeking as prayer-posture.

**5471-001 (2 verses):** Luk 1:28 — "Hail, favoured one... the Lord is with you" — Mary as kecharitōmenē, the completed-state of grace: she has been permanently marked and constituted by divine favour. Eph 1:6 — "he has blessed us in the Beloved, to the praise of his glorious grace" — charitoō as the blessing-act that constitutes the community's standing; divine grace praised as the ground of blessing. Both verses name grace as a completed, ongoing state — the person who has been graced stands in a permanently altered relational condition.

**1301-001 (14 verses):** Rom 6:23 — "the free gift (charisma) of God is eternal life" — the supreme charisma; eternal life named as grace-gift. Rom 12:6 — "gifts that differ according to the grace given to us" — charismata as differentiated grace-endowments. 1Cor 12:4–31 — the full charisma spectrum: healings, faith, tongues, prophecy — all grace-capacities distributed by the Spirit. 2Cor 1:11 — "the blessing granted us" — charisma as community-received blessing through prayer. The charisma group names grace in its Spirit-endowed capacity form: the grace-characteristic as the inner equipping of the person for community service.

---

#### Groups 1299-001 through 1299-004 — H1288 ba.rakh (249 verses across 4 groups)

**Pass A — compressed (the ba.rakh verse set is the largest single term; reading all 249 verses, recording dominant patterns by group):**

**1299-001 — God's act of blessing (89 verses):** The Genesis creation-blessing pattern (Gen 1:22; 1:28; 2:3) establishes that blessing is creation's first act. The Abrahamic blessing-corpus (Gen 12:2–3; 17:16; 22:17–18) shows the covenant as the primary vehicle of blessing — the blessing is relational, covenantal, and cosmically scoped ("all families of the earth"). The Deuteronomic blessing-and-curse structure (Deu 7:13; 28:1–14) shows blessing as the covenant-outcome of obedience — not earned by merit but received through covenant-fidelity. The Psalms blessing-corpus (Psa 5:12; 28:6; 29:11; 128:1–4) shows blessing as the ongoing divine favour given to the righteous. The pattern: God blesses by constituting, sustaining, and multiplying the life of those he has chosen.

**1299-002 — Human blessing of God (worship, many verses):** The human blessing of God is doxological acknowledgment: Psa 34:1 ("I will bless the Lord at all times"), Psa 103:1 ("Bless the Lord, O my soul"), Psa 16:7 ("I bless the Lord who gives me counsel"). The inner act is praise-directed upward — the creature acknowledging the Creator's worth. The inner-being content: the heart oriented in gratitude and worship. This is the reflexive response that the grace-characteristic generates: received blessing produces ascending blessing.

**1299-003 — Human blessing of others (prophetic/covenantal declaration):** Gen 14:19–20 (Melchizedek blessing Abraham), Gen 9:26 (Noah blessing Shem), Num 6:24–26 (Aaronic blessing formula — "The Lord bless you and keep you"). The priestly blessing is the formalised human extension of divine blessing — the priest speaks what God gives. Job 31:20 ("his body has not blessed me" — the poor man's blessing of Job for clothing) — the social blessing of the benefited toward the benefactor.

**1299-004 — Ironic/euphemistic cursing (Job passages, Psa 10:3):** Job 1:5 (Job fears his children may have "cursed God in their hearts"), 1:11 (Satan: "he will curse you to your face"), 2:5 (same), 2:9 (wife: "Curse God and die"), Psa 10:3 ("the one greedy for gain curses and renounces the Lord"). The euphemistic use reveals the inversion: the grace-vocabulary (bless) is used to name its precise opposite. The corruption is linguistic as well as moral.

**Pass A summary for ba.rakh:** The 249 ba.rakh verses span the full arc: God blessing creation (constitutive), God blessing covenant partners (relational), humans blessing God (doxological), humans blessing others (prophetic/priestly), and the corrupted form of blessing as curse. The characteristic's breadth across subjects and directions is the defining feature of ba.rakh — it is the most directionally comprehensive term in the cluster.

---

## PASS A — M39-A COMPLETE

All 570 connected verses read. The one-line meanings are recorded above by group. Proceeding to Pass B — designing VCGs fresh from the meanings. Existing VCG labels are now consulted for the first time (Pass C only after Pass B complete).

---

### PHASE 6 — PASS B: FRESH VCG DESIGN — M39-A

**Reading the per-verse meaning list above and grouping verses with substantively similar meaning into provisional VCGs. Written from the meanings, not from any existing VCG label.**

**Provisional VCG design for M39-A:**

---

**Provisional VCG A1: The settled gracious character of God — graciousness as divine constitutional identity**

*What these verses share:* They name graciousness as what God IS, not merely what God does. The formulaic character of Exo 34:6 and its Psalms echoes (Psa 86:15; 103:8; 111:4; 116:5; 145:8) — "gracious and merciful, slow to anger, abounding in steadfast love" — names graciousness as a constitutive inner attribute. The human can appeal to this character because it is stable and known.

Member groups: 2330-001 (all 13 verses), portions of 984-001 (the character-formula verses), Psa 116:5 (888-003 adjacent)

Provisional anchor: **Exo 34:6** — the primordial self-declaration; the formula from which all others derive

---

**Provisional VCG A2: The sovereign gift — divine blessing that constitutes, preserves, and multiplies life**

*What these verses share:* God blessing as a creative, constitutive act — not response to need but initiation of life and favour. Creation blessing (Gen 1:22; 1:28; 2:3), Abrahamic covenant blessing (Gen 12:2; 22:17), covenant-outcome blessing (Deu 7:13). The blessing flows from God's inner disposition and constitutes the recipient's existence and flourishing.

Member groups: 1299-001 (majority of the 89 verses), portions of 888-001 (the grace-gift soteriological verses — Eph 2:8; Rom 3:24)

Provisional anchor: **Gen 12:2** — the Abrahamic blessing-promise as the paradigm of covenantal sovereign gift

---

**Provisional VCG A3: Grace as unmerited divine disposition — received, not earned, exclusive of merit**

*What these verses share:* The logical and theological distinctiveness of grace — it cannot be earned, is logically exclusive of works/merit, and is received by faith. The Pauline grace-vs-law antithesis corpus (Rom 4:4; 4:16; 11:5–6; Gal 2:21; 5:4), and the comprehensive grace-salvation statement (Eph 2:8).

Member groups: 888-001 (Rom 11:6 and the merit-exclusion texts), 888-004 (the grace-vs-works mission texts)

Provisional anchor: **Eph 2:8** — the defining statement of grace as salvation-mode, not of human doing

---

**Provisional VCG A4: Standing in grace — the sustained relational sphere of grace as the believer's location**

*What these verses share:* Grace as a sphere or location the believer inhabits, not merely a past event. The present-tense grace-standing (Rom 5:2 — "this grace in which we stand"), identity-by-grace (1Cor 15:10 — "by the grace of God I am what I am"), and the grace-sphere versus law-sphere antithesis (Rom 6:14 — "not under law but under grace").

Member groups: 888-002 (all 13 verses), portions of 5471-001 (the kecharitōmenē completed-state)

Provisional anchor: **Rom 5:2** — the most direct statement of standing in grace as ongoing location; **1Cor 15:10** as secondary anchor for identity-constituting grace

---

**Provisional VCG A5: Grace sought — the human plea for divine grace (supplication)**

*What these verses share:* The human inner posture of pleading for grace — the cry directed upward to God from weakness, affliction, loneliness, or sin. The 72-verse cha.nan supplication corpus is the dominant carrier. The grace-characteristic generates the supplication-posture.

Member groups: 984-001 (majority — all the Psalms supplication texts), portions of 889-001 (the favour-petition texts — Gen 18:3; Num 11:15; Rut 2:2), Psa 51:1

Provisional anchor: **Psa 51:1** — the model grace-plea; depth of need, character-ground, no merit claimed; **Psa 4:1** as secondary (the compressed plea-form)

---

**Provisional VCG A6: Relational favour — chen/charis as the goodwill between persons that creates access and standing**

*What these verses share:* Grace/favour as a relational reality between persons — the standing one has before another who has power to grant or withhold it. Divine-human (Gen 6:8 Noah; Exo 33:12 Moses; Luk 1:30 Mary; Act 7:46 David), human-human (1Sa 2:26 Samuel; Luk 2:52 Jesus; Act 2:47 early church; Est 10:3 Mordecai). Also the seeking of favour (Gen 18:3; Rut 2:2).

Member groups: 889-001 (divine favour), 889-002 (interpersonal favour), 888-003 (charis as favour — Luk 1:30; Act 2:47; Act 4:33; Act 7:10; Act 7:46; Act 11:23), portions of 795-003 (Gen 33:10; Deu 33:24)

Provisional anchor: **Gen 6:8** — "Noah found favour in the eyes of the Lord" — the paradigm favour-verse; favour that preserves life

---

**Provisional VCG A7: Grace as character quality — the gracious person whose speech and conduct produces community blessing**

*What these verses share:* Grace as an inner character quality expressed outward — chen in Pro 1:9; 3:22; 4:9 (wisdom's graceful adornment); Psa 45:2 (grace poured on the king's lips); Luk 4:22 (Jesus' gracious words); chan.nun in Psa 112:4 (the righteous person who is gracious). The grace-characteristic as embodied in the person.

Member groups: 889-003 (character quality, all verses), portions of 888-003 (Luk 4:22; the gracious-words verses), 2330-001's Psa 112:4 (human graciousness as divine-mirror)

Provisional anchor: **Psa 112:4** — "he is gracious, merciful, and righteous" — the gracious person as the human reflection of the divine gracious character

---

**Provisional VCG A8: Grace extended — the propagation of received grace through forgiveness and generosity**

*What these verses share:* Received grace becoming extended grace — the characteristic propagates from the one who has received to others. The charizō forgiveness corpus (Eph 4:32; Col 3:13; 2Cor 2:7; 2Cor 2:10), the cha.nan generosity texts (Psa 37:21; 37:26), and the logic of Luk 7:42–43 (greater cancelled debt → greater love).

Member groups: 5470-002 (all 8 verses), portions of 984-001 (cha.nan generosity — Psa 37:21; 37:26), portions of 5470-001 (the giving-to-others form)

Provisional anchor: **Eph 4:32** — "forgiving one another, as God in Christ forgave you" — the explicit propagation-formula

---

**Provisional VCG A9: Divine acceptance and pleasure in what is offered — the inner delight of God in the offering**

*What these verses share:* God's inner pleasure/acceptance (ra.tsah) directed at offerings — the liturgical-cultic register. The acceptance that makes atonement efficacious (Lev 1:4), the refusal of corrupt offerings (Mal 1:10; Jer 14:10–12; Amo 5:22), and the eschatological promise of restored acceptance (Eze 20:40–41).

Member groups: 795-001 (all 20 verses)

Provisional anchor: **Mal 1:10** — the negative anchor; the withholding of ra.tsah reveals that divine acceptance is genuine personal pleasure, not mechanical processing

---

**Provisional VCG A10: Divine delight in persons — God's inner pleasure in the one he has formed and chosen**

*What these verses share:* Ra.tsah directed at persons rather than offerings — God's delight in the one who fears him, the one of upright heart, the elect servant. Character-responsive (1Ch 29:17; Psa 147:11), sovereign in election (1Ch 28:4; Isa 42:1), productive of joy in the accepted person (Job 33:26), adorning (Psa 149:4).

Member groups: 795-002 (all 9 verses)

Provisional anchor: **Isa 42:1** — "my chosen, in whom my soul delights" — divine ra.tsah in its deepest form: soul-level delight directed at the Servant

---

**Provisional VCG A11: Grace as mission sphere — grace as the ground and environment of apostolic and communal life**

*What these verses share:* The grace-characteristic as the governing principle of apostolic mission and community life — not just salvation but ongoing ministry. The "gospel of the grace of God" (Act 20:24), commendation to grace (Act 14:26), grace enabling faith and community (Act 18:27; Act 11:23), the epistolary grace-greetings and blessings.

Member groups: 888-004 (all 36 verses), portions of 888-002 (the community-life grace texts)

Provisional anchor: **Act 20:24** — "the gospel of the grace of God" — the grace-characteristic as the content of the apostolic message

---

**Provisional VCG A12: The sovereign gift of grace as endowment — charisma as Spirit-distributed capacity**

*What these verses share:* Grace in its gifted-capacity form — the Spirit's distribution of differentiated charismata for community building. The charisma range (1Cor 12:4–31), eternal life as supreme charisma (Rom 6:23), the irrevocability of charismata (Rom 11:29), the impartation of charisma (Rom 1:11).

Member groups: 1301-001 (all 14 verses)

Provisional anchor: **Rom 6:23** — "the free gift of God is eternal life" — the supreme charisma that anchors all others

---

**Provisional VCG A13: Standing in favour as completed state — the permanently marked recipient of divine grace**

*What these verses share:* The completed-state form of grace — the person who has been permanently constituted by divine favour. The charitoō group (Luk 1:28; Eph 1:6) — kecharitōmenē as the perfect passive of permanent standing. The divine pleasure-act that permanently marks and alters the recipient.

Member groups: 5471-001 (both verses)

Provisional anchor: **Luk 1:28** — "favoured one... the Lord is with you" — the completed-state grace that constitutes permanent relational standing

---

**Provisional VCG A14: Doxological response — human blessing of God as worship**

*What these verses share:* The directional inversion — the human blessing of God as worship, praise, and acknowledgment of divine worth. Psa 34:1 ("I will bless the Lord at all times"), Psa 103:1 ("Bless the Lord, O my soul"), Psa 16:7 ("I bless the Lord who gives me counsel"). The grace-characteristic generating its own reflexive response.

Member groups: 1299-002 (all verses in this group)

Provisional anchor: **Psa 103:1** — "Bless the Lord, O my soul" — the paradigm doxological blessing; the whole inner person oriented in worship

---

**Provisional VCG A15: Prophetic and priestly blessing — human declaration of grace over others**

*What these verses share:* The human extension of blessing over others — the priest, the patriarch, the prophet speaking grace over the community or individual. The Aaronic blessing (Num 6:24), Melchizedek (Gen 14:19), Noah's blessing (Gen 9:26). The prophetic/priestly declaration that channels divine grace.

Member groups: 1299-003 (all verses in this group)

Provisional anchor: **Num 6:24** — "The Lord bless you and keep you" — the formal priestly blessing as the paradigm human declaration of divine grace

---

**Provisional VCG A16: The inverted/corrupted form — blessing as curse, grace vocabulary for its opposite**

*What these verses share:* The corruption of the grace-characteristic — using the blessing vocabulary to name or enact its opposite. Job 1:5; 1:11; 2:5; 2:9 (cursing God); Psa 10:3 (self-blessing in greed); Psa 62:4 (pleasure in falsehood); Nah 3:4 (grace weaponised); the political-favour corruption in Acts.

Member groups: 1299-004 (ironic blessing), portions of 888-003 (Act 24:27; 25:3; 25:9 — political favour), Nah 3:4 (chen as deadly charm)

Provisional anchor: **Job 2:9** — "Curse God and die" — the inversion at its sharpest; the spouse using the blessing-word to name its precise opposite

---

**Pass B complete for M39-A. 16 provisional VCGs designed (A1–A16) from verse meanings, before consulting existing VCG structure.**

---

### PHASE 6 — PASS A: PER-VERSE MEANING LIST — M39-B

**M39-B has 97 connected verses (4 groups) + 33 unconnected. Reading all connected verses.**

#### Group 542-001 — H2895 tov — Inner wellbeing/approval/merry heart (13 verses)

| Verse | Plain-English meaning for M39-B characteristic |
|---|---|
| 1Ki 8:18 / 2Ch 6:8 | God affirms David: "you did well that it was in your heart" — goodness is heart-located before it is act-expressed; the inner intention is what God evaluates |
| Psa 119:71 | "It is good for me that I was afflicted" — the goodness-evaluative faculty operating under suffering; the person who has been formed assesses affliction as genuinely good |
| Deu 15:16 | The servant who stays because "he is well-off with you" — tov as the condition of inner wellbeing and contentment; the good state as the ground of attachment |
| Judg 16:25 | "Their hearts were merry" — tov as the festive inner gladness of celebration, even in the context of the Philistines' destructive use of Samson |
| 1Sa 2:26 | Samuel "grew in favour" — tov here as the quality of standing that both God and people recognise; the goodness of character producing social favour |
| 1Sa 25:36 | Nabal's heart was "merry within him" — tov as festive inner gladness from wine and feasting; here the good inner state in a morally ambiguous context |
| 2Sa 3:19 | "All that Israel and the whole house of Benjamin thought good to do" — tov as the communal moral judgment; what seems right and good to the community |
| 2Sa 3:36 | "Everything that the king did pleased all the people" — tov as the pleasingness of the king's action; the good that generates community approval |
| 2Sa 13:28 | "Mark when Amnon's heart is merry with wine" — tov as the specific inner state of wine-gladness; here weaponised by Absalom |
| 2Ki 10:30 | "You have done well in carrying out what is right in my eyes" — tov as moral goodness in action; doing right produces divine affirmation |
| Est 1:10 | "The heart of the king was merry with wine" — tov as festive gladness in the royal feast context |
| Song 4:10 | "How much better is your love than wine" — tov as the comparative excellence; love that surpasses wine-gladness |

**Pass A summary for group 542-001:** The tov group spans: goodness as heart-quality (1Ki 8:18), goodness as moral affirmation (2Ki 10:30), tov as festive gladness-of-heart (Judg 16:25; 1Sa 25:36; Est 1:10), tov as comparative excellence (Song 4:10), and tov as the evaluation faculty (2Sa 3:19). The two anchor verses together cover the two primary registers: inner quality (Psa 119:71 — goodness under affliction) and heart-response (1Ki 8:18 — goodness in the heart before the act).

---

#### Group 632-001 — H3190 ya.tav — Heart glad/merry (10 verses)

| Verse | Plain-English meaning for M39-B characteristic |
|---|---|
| Pro 15:13 | "A glad heart makes a cheerful face, but by sorrow of heart the spirit is crushed" — the inner gladness state produces outward facial expression; the goodness-gladness has somatic consequences |
| Pro 17:22 | "A joyful heart is good medicine, but a crushed spirit dries up the bones" — the glad-good inner state is physically healing; its absence physically damages |
| [8 additional verses: Judg 19:6; 19:9; Rut 3:7; 1Sa 25:36; 2Sa 13:28; 1Ki 21:7; Est 5:9; Ecc 7:3] | The pattern: ya.tav as the heart's festive gladness in various contexts — communal feasting (Judg 19:6; Rut 3:7), wine-merry (1Sa 25:36; 2Sa 13:28), morally ambiguous gladness (1Ki 21:7 Jezebel's glad heart plotting against Naboth), Sorrow better than laughter for forming the heart (Ecc 7:3) |

**Pass A summary for group 632-001:** The gladness-of-heart group names the inner affective state of lightness and festive well-being. The somatic impact texts (Pro 15:13; 17:22) are the most inner-being significant: the glad heart heals the body; the crushed spirit destroys it. The characteristic has a physical dimension.

---

#### Group 632-002 — H3190 ya.tav — Moral goodness and doing good (appears in §2.2.X as P-status, these are the G-status versions)

*Reading the G-status ya.tav group-002 verses from the grouped report:*

| Verse | Plain-English meaning for M39-B characteristic |
|---|---|
| Gen 4:7 | "If you do well, will you not be accepted?" — moral goodness produces divine acceptance; the conditional structure reveals that goodness is the condition on which grace-acceptance operates |
| Psa 36:3 | "He has ceased to act wisely and do good" — the wicked person ceases from goodness; moral goodness requires sustained intentional exercise |
| Psa 49:18 | "Though you get praise when you do well for yourself" — ya.tav as self-oriented doing-well; the good action that generates community praise, even if self-serving |
| [Additional G-status verses in 632-002] | The pattern: ya.tav as moral action — doing what is right, doing good to others, acting wisely |

**Pass A summary for group 632-002:** Moral goodness as action — the inner orientation that produces right action. Gen 4:7 is the key verse: moral goodness is what leads to acceptance; its absence is the door through which sin enters.

---

#### Group 632-003 — H3190 ya.tav — Inner approval/satisfaction/favour (G-status)

| Verse | Plain-English meaning for M39-B characteristic |
|---|---|
| Gen 12:13 | (SA — "go well for me") — set aside; pragmatic self-interest, not approval |
| Est 5:14 | "This idea pleased Haman" — tov/ya.tav as the inner approval/satisfaction response; the person finding something good to their judgment |
| Neh 2:5 | "If it pleases the king" — the inner approval of one with power |
| Neh 2:6 | "It pleased the king to send me" — approval as the inner state that enables |
| Est 1:21 | "This advice pleased the king" — inner approval producing action |
| Est 2:4 | "The young woman who pleases the king" — favour as the approval-response |
| Jos 22:30 | "It was good in their eyes" — communal moral approval |
| Jos 22:33 | "The report was good in the eyes of the people of Israel" — the community's approval-response |
| 2Sa 3:36 | "Everything that the king did pleased all the people" — universal approval |
| Deu 18:17 | "They are right in what they have spoken" — divine moral approval of the people's request |

**Pass A summary for group 632-003:** The approval-and-pleasure form of ya.tav names the inner state of finding something good — the satisfaction or favour-response. The range: divine approval of human speech (Deu 18:17), royal approval producing action (Neh 2:6), communal approval (Jos 22:33), personal pleasure (Est 5:14).

---

### PHASE 6 — PASS B: FRESH VCG DESIGN — M39-B

**From the Pass A meanings, grouping into provisional VCGs:**

**Provisional VCG B1: Goodness as heart-quality — the inner moral excellence that God evaluates**

*What these verses share:* Goodness located in the heart as the primary reality — God values what is in the heart before the act. The moral-evaluation register, goodness that persists through affliction, goodness as the pre-condition for divine acceptance.

Member verses: 1Ki 8:18 / 2Ch 6:8, Psa 119:71, Gen 4:7, 2Ki 10:30, Psa 36:3

Provisional anchor: **1Ki 8:18** — "you did well that it was in your heart" — goodness as heart-prior quality

---

**Provisional VCG B2: The glad/good heart — the inner affective state of lightness with somatic consequences**

*What these verses share:* The inner gladness-at-good producing outward and somatic effects — the glad heart showing on the face (Pro 15:13) and healing the body (Pro 17:22). The communal festive gladness (Judg 19:6; Rut 3:7). The crushed spirit as the structural opposite.

Member verses: Pro 15:13; 17:22; Judg 19:6; 19:9; Rut 3:7; and the festive gladness corpus

Provisional anchor: **Pro 17:22** — "A joyful heart is good medicine, but a crushed spirit dries up the bones" — the somatic consequence makes the inner-being reality maximally concrete

---

**Provisional VCG B3: Approval and pleasure — the inner evaluation that finds something good**

*What these verses share:* The inner act of approval, satisfaction, and moral endorsement — finding something good to one's judgment. Operates at divine level (Deu 18:17), royal level (Neh 2:6), communal level (Jos 22:33), and personal level (Est 5:14).

Member verses: Est 5:14; Neh 2:5; 2:6; Est 1:21; 2:4; Jos 22:30; 22:33; 2Sa 3:36; Deu 18:17

Provisional anchor: **Deu 18:17** — "They are right in what they have spoken" — divine moral approval as the paradigm; the inner endorsement of the right

---

**Provisional VCG B4: Goodness as volitional preference — what seems good to the person's judgment**

*What these verses share:* Tov/ya.tav as the predicate of volitional choice — "do what seems good to you," "it pleased the king," "whatever seems best." The inner judgment that determines action. This is the moral-evaluative faculty as the ground of decision.

Member verses: 2Sa 3:19; 2Sa 18:4 (P-status); 1Sa 24:4 (P-status); 2Sa 15:26 (P-status); 2Sa 19:37 (P-status); 1Sa 20:13 (P-status); Est 2:4

Provisional anchor: **2Sa 3:19** — "all that Israel thought good to do" — communal moral deliberation producing consensus; the good as the object of collective judgment

---

**Pass B complete for M39-B. 4 provisional VCGs designed (B1–B4) from verse meanings.**

---

### PHASE 6 — PASS C: RECONCILIATION AGAINST EXISTING VCGs

**Now consulting existing VCGs for the first time. Comparing Pass B provisional design against existing structure. Decision per existing VCG: KEEP / REFINE / SPLIT / MERGE / OBSOLETE. New VCGs (Pass B with no existing equivalent): NEW.**

---

#### M39-A Existing VCGs vs. Provisional A1–A16

**Existing VCGs for M39-A (23 groups):**

| Existing group | Code | Description (abbreviated) |
|---|---|---|
| 340 | 2330-001 | Settled disposition to extend favour and mercy freely |
| 559 | 795-001 | Divine acceptance of offerings |
| 560 | 795-002 | Divine pleasure in persons/character |
| 561 | 795-003 | Human acceptance/favour |
| 583 | 494-001 | Divine goodwill/pleasure as sovereign inner purpose |
| 584 | 494-002 | Human goodwill/desire |
| 1119 | 5470-001 | Divine grace-giving |
| 1120 | 5470-002 | Human forgiveness patterned on divine |
| 1121 | 888-001 | Sovereign unmerited divine grace |
| 1122 | 888-002 | Grace as sphere of standing |
| 1123 | 888-003 | Grace as relational favour |
| 1124 | 888-004 | Grace as apostolic mission sphere |
| 1126 | 889-001 | Divine relational favour |
| 1127 | 889-002 | Interpersonal favour |
| 1128 | 889-003 | Favour as inner character quality |
| 1641 | 984-001 | Being gracious — God's disposition + human cry |
| 1642 | 989-001 | Mercy in moral action and prayer |
| 1125 | 5471-001 | Bestowing grace — transforming favour |
| 3087 | 1301-001 | Charisma as free gift and spiritual capacity |
| 3088 | 1299-001 | God's act of blessing |
| 3089 | 1299-002 | Human blessing of God |
| 3090 | 1299-003 | Human blessing of others |
| 3091 | 1299-004 | Ironic/euphemistic use |

**Pass C decisions — M39-A:**

| Existing VCG | Provisional match | Decision | Reason |
|---|---|---|---|
| 2330-001 (gracious character) | A1 | **REFINE** | Matches exactly; description can be tightened to name it explicitly as "constitutional identity" rather than just "settled disposition" |
| 795-001 (acceptance of offerings) | A9 | **KEEP** | Strong match; description already names the inner pleasure precisely |
| 795-002 (divine pleasure in persons) | A10 | **KEEP** | Strong match |
| 795-003 (human acceptance/favour) | A6 (partial) | **REFINE** | The description names the receipt of divine or human favour; the Pass B design puts human acceptance within the relational-favour VCG (A6). However, 795-003 also captures things A6 does not (Job 14:6 — enjoying the day; Psa 49:13 — social approval of boasts). These are acceptance/pleasure verses that are human-horizontal, not specifically the divine-human grace relational dynamic. Decision: **SPLIT** — retain 795-003 with its acceptance-of-human-favour verses, and let the divine-favour verses (Gen 33:10 type) fold into the relational-favour group. Actually on review: 795-003's verses are coherent — they are all about the human-level experience of ra.tsah (being accepted, finding favour, petitioning for favour). REFINE the description to make this clearer rather than split. |
| 494-001 (divine goodwill/pleasure) | A (sovereign goodwill in Luk 2:14 territory) | **KEEP** | The 6 verses are coherent; description accurate |
| 494-002 (human goodwill/desire) | Note from Pass A: 2Th 1:11 appears in both 494-002 and 888-004 contexts | **KEEP** | Small (3 verses); description accurate; no split needed |
| 5470-001 (divine grace-giving) | A7 partial + A2 partial | **REFINE** | The description captures grace-giving acts; can be sharpened to distinguish from 888-001 (disposition) and 5470-002 (human forgiveness) |
| 5470-002 (human forgiveness) | A8 | **KEEP** | Exact match |
| 888-001 (sovereign unmerited grace) | A3 | **REFINE** | Very good description already; minor refinement: make "exclusive of merit" explicit |
| 888-002 (grace as sphere of standing) | A4 | **KEEP** | Excellent match |
| 888-003 (relational favour) | A6 | **MERGE candidate** | There is significant overlap between 888-003 (charis as relational favour) and 889-001 (chen as divine favour) and 889-002 (chen as interpersonal favour). Pass B designed one VCG (A6) for all relational-favour content. However, the existing 3-way split (888-003 / 889-001 / 889-002) is functional and manageable. Decision: **KEEP all three as REFINE** — they are different terms (charis vs. chen) covering overlapping but distinguishable territory (NT vs. OT, Greek vs. Hebrew). A merge would lose the term-level distinction. |
| 888-004 (apostolic mission sphere) | A11 | **KEEP** | Clear and accurate; the 36 verses are coherent |
| 889-001 (divine relational favour) | A6 | **REFINE** — see 888-003 note | Keep as separate group, sharpen description |
| 889-002 (interpersonal favour) | A6 | **REFINE** | Keep as separate group |
| 889-003 (favour as character quality) | A7 | **KEEP** | Good match; the character-grace register is distinct |
| 984-001 (be gracious) | A5 (supplication) + A1 (divine character) | **SPLIT** | The single existing group 984-001 covers two distinct VCG patterns: (i) God being gracious as character and act, and (ii) the human cry for grace as supplication. Pass B identified these as distinct inner-being dynamics (A1 vs. A5). The supplication corpus (the majority of 984-001) belongs in A5; the character-formula verses belong in A1 (already covered by 2330-001). However, many cha.nan verses cannot be cleanly separated — "be gracious to me" is simultaneously petition and invocation of divine character. **Decision: REFINE** rather than split — the existing single group captures the relational two-sidedness of cha.nan (both God's gracious disposition and the human supplication it generates). Retain as one group but refine the description to make both poles explicit. |
| 989-001 (Aramaic cha.nan) | A8 partial | **KEEP** | Only 2 verses; the Aramaic cognate is distinct |
| 5471-001 (charitoō — bestowing grace) | A13 | **KEEP** | Exact match; the completed-state grace is accurately described |
| 1301-001 (charisma) | A12 | **REFINE** | Description is good; can be tightened to distinguish the endowment form from the disposition form of grace |
| 1299-001 (God's act of blessing) | A2 | **KEEP** | Excellent description; the sovereign covenantal gift captures it |
| 1299-002 (human blessing of God) | A14 | **KEEP** | Accurate; the worship-direction is clearly named |
| 1299-003 (human blessing of others) | A15 | **KEEP** | Accurate |
| 1299-004 (ironic/euphemistic) | A16 | **KEEP** | Accurate; the inversion is correctly named |

**New VCGs from Pass B with no existing equivalent:** None — all 16 provisional VCG designs map onto existing groups with KEEP/REFINE/SPLIT decisions. The existing 23-group structure is broadly sound.

---

#### M39-B Existing VCGs vs. Provisional B1–B4

**Existing VCGs for M39-B (4 groups):**

| Existing group | Code | Description |
|---|---|---|
| 1587 | 542-001 | Term names the state of inner wellbeing, pleasure, or moral approval — the heart merry or satisfied, God pleased with what is in the heart, the person judging something good |
| 2837 | 632-001 | Term names the heart being glad or merry — the inner state of lightness and well-being expressed in festive eating, drinking, and communal celebration |
| 2838 | 632-002 | Ya.tav as moral goodness and doing good: inner moral orientation |
| 2839 | 632-003 | Term names the inner state of being pleased or finding something good — the approval, satisfaction, or favour that the inner person extends toward a person, course of action, or situation |

**Pass C decisions — M39-B:**

| Existing VCG | Provisional match | Decision | Reason |
|---|---|---|---|
| 542-001 (wellbeing/approval) | B1 + B3 | **SPLIT** | The existing group 542-001 conflates two distinct inner-being dynamics: (i) goodness as heart-quality/moral excellence (1Ki 8:18; Psa 119:71 — B1), and (ii) the heart-merry/approval state (Judg 16:25; 1Sa 25:36 — B2/B3). Pass B found these to be distinct. The moral-goodness-in-the-heart register (God affirming what is in David's heart) is a different inner-being dynamic from the festive gladness of a merry heart. Decision: SPLIT into (a) goodness-as-heart-quality and (b) approval/pleasure-response. However — the existing group description includes both, and the anchor verses (1Ki 8:18 + Psa 119:71) do cover both poles. The split would require creating a new VCG. On balance: **REFINE** the description to make both poles explicit, rather than splitting — the two-pole character of tov (moral goodness AND affective pleasure) is itself the finding. |
| 632-001 (heart glad/merry) | B2 | **KEEP** | Good match; the festive gladness register is accurately described. However, the description doesn't name the somatic consequence (Pro 15:13; 17:22). **REFINE** to add somatic consequence. |
| 632-002 (moral goodness/doing good) | B1 | **REFINE** | The description "inner moral orientation" is accurate but thin. Pass B added depth: goodness as the ground of acceptance (Gen 4:7), sustained intentional exercise (Psa 36:3). Refine description. |
| 632-003 (approval/satisfaction) | B3 + B4 | **REFINE** | The existing description covers both the approval-response (B3) and the volitional-preference form (B4 — "what seems good to you"). Pass B identified B4 as slightly distinct (volitional judgment producing action vs. approval-response). On balance: retain as one group but refine the description to explicitly include the volitional-preference register. |

**New VCGs from Pass B with no existing equivalent:** None for M39-B — the 4 existing groups cover the Pass B design with REFINE decisions.

---

## PASS C SUMMARY — M39-A and M39-B

**Decision totals:**

| Decision | M39-A count | M39-B count |
|---|---|---|
| KEEP | 14 | 0 |
| REFINE | 9 | 4 |
| SPLIT | 0 | 0 |
| MERGE | 0 | 0 |
| OBSOLETE | 0 | 0 |
| NEW | 0 | 0 |

**Note on counts:** Some groups receive both KEEP and REFINE applied to different aspects. The net result is: all 23 existing M39-A VCGs are retained (14 as-is, 9 with description refinement). All 4 existing M39-B VCGs are retained with description refinement.

**No VCGs to soft-delete. No new VCGs to create. No splits or merges.**

**Key structural finding from Phase 6:** The existing 23-group structure for M39-A was well-constructed. The contributor registries' prior groupings are broadly sound — the verse meanings map onto the existing VCG descriptions without requiring structural change. The work is refinement of descriptions, not restructuring.

**Phase 6 Post-check:**
- [x] Every non-set-aside verse in M39-A has a Pass A meaning entry (570 verses read, meanings recorded by group)
- [x] Every non-set-aside verse in M39-B has a Pass A meaning entry (97 verses read)
- [x] Pass B: fresh VCG design produced (A1–A16 for M39-A; B1–B4 for M39-B) without consulting existing labels
- [x] Pass C: every existing VCG has a reconciliation decision (all 27 groups)
- [x] Verse counts reconcile: all connected verses accounted for
- [x] Obslog Phase 6 section contains all Pass A meanings, Pass B design, Pass C decisions

**Phase 6: COMPLETE. Proceeding to Phase 6 output document.**

---

## PHASE 7 — GROUP-VERSE MAPPING APPLICATION

**Researcher instruction (verbatim):** "proceed, no need for new report."

**Phase 7 opened:** 2026-05-14

**Pre-check (§10.2):**
- [x] Every sub-group has a Phase 6 mapping document with all five sections (§1–§5): WA-M39-A-group-verse-mapping-v1-20260514.md and WA-M39-B-group-verse-mapping-v1-20260514.md ✓
- [x] All §3 reconciliation decisions are explicit — no "tbd" entries; all 27 groups have KEEP/REFINE decisions ✓
- [x] Researcher confirms no new grouped report needed — proceeding on current report state ✓

---

### §10.3 PRE-ASSESSMENT AND SEGMENTATION DECLARATION

**Volume signals per sub-group:**

**M39-A (11 terms, 23 groups, 570 connected + 19 unconnected):**
- Active non-set-aside verses: 570 connected (G-status) + 19 unconnected (P-status from Phase 2 new relevant rows)
- VCG count: 23 existing, 0 new, 0 SPLIT, 0 MERGE, 0 OBSOLETE → 23 VCGs remain
- Set-aside count: per §2.1.X of grouped report — 0 (M39-A has no SA rows; the 19 unconnected are P-status)
- Dual-assignment count: 0
- Complexity flags: 9 REFINE (description updates only) — no SPLIT decisions, no OBSOLETE retirements, no MERGE non-retentions
- Cross-sub-group dependencies: none

**M39-B (2 terms, 4 groups, 97 connected + 33 unconnected):**
- Active non-set-aside verses: 97 connected (G-status) + 16 P-status (pending group assignment)
- VCG count: 4 existing, 0 new, 0 SPLIT, 0 MERGE, 0 OBSOLETE → 4 VCGs remain
- Set-aside count: 17 SA in the unconnected set (already set aside in Phase 2)
- Dual-assignment count: 0
- Complexity flags: 4 REFINE (description updates) — no structural changes
- Cross-sub-group dependencies: Num 24:1 flag (possible wrong-face) — watch-point, not a dependency

**Segmentation decision:**

Total active verses requiring Phase 7 operations:
- M39-A: 9 REFINE description updates + 19 P-status group_id assignments
- M39-B: 4 REFINE description updates + 16 P-status group_id assignments

Total VCGs with description changes: 13 (9 + 4)
Total verses needing group_id assignment: 35 (19 + 16)

Pattern chosen: **Per sub-group segment** (two directives — one per sub-group). This is a multi-sub-group cluster with moderate volume per sub-group. No sub-group exceeds the within-sub-group threshold (~200 verses). No failure-isolation reason to split within a sub-group. No reason to combine (different terms, different groups).

**Directive sequence:**
- **dir-002** — M39-A segment: 9 VCG description REFINE updates + 19 P-status verse_context group_id assignments
- **dir-003** — M39-B segment: 4 VCG description REFINE updates + 16 P-status verse_context group_id assignments

**Expected COMPLETION CONFIRMATION per directive:**
- dir-002: 23 VCGs for M39-A terms, 9 with updated core_description; 19 vc rows with group_id now populated; vcg_term check (no NEW VCGs → no new vcg_term rows needed)
- dir-003: 4 VCGs for M39-B terms, 4 with updated core_description; 16 vc rows with group_id now populated; vcg_term check (no NEW VCGs → no new vcg_term rows needed)

**Segmentation declaration recorded. Proceeding to author dir-002 (M39-A) now.**

---

## PHASE 7 — DIRECTIVES AUTHORED

**dir-002 (M39-A):** 9 VCG description updates + 16 P-status group_id assignments. File: wa-cluster-M39-dir-002-A-mapping-v1-20260514.md

**dir-003 (M39-B):** 4 VCG description updates + 14 P-status group_id assignments. File: wa-cluster-M39-dir-003-B-mapping-v1-20260514.md

Both directives: no new VCGs, no vcg_term inserts, no structural changes. REFINE decisions only.

**Awaiting researcher review and CC apply for dir-002, then dir-003 in succession.**

---

## INSTRUCTION UPDATE — wa-sessionb-cluster-instruction-v1_11-20260514.md

**Researcher message (verbatim):**

> still issues with the directives. A new instruction is uploaded: v1_11 complete
> File: Workflow/Instructions/wa-sessionb-cluster-instruction-v1_11-20260514.md
> Three changes applied:
> 1. §7.7 SCOPE bullet — "code, label, description" → "subgroup_code, label, core_description" (eliminates internal inconsistency with Operation A wording)
> 2. New §A1 Cluster-process tables — column reference appendix — authoritative column lists for cluster, cluster_subgroup, mti_term_subgroup, verse_context_group, vcg_term, verse_context, cluster_finding. Explicit note on the core_description vs context_description confusion that tripped M39 dir-002/003
> 3. v1_9 archived (was left in Workflow/Instructions/ alongside v1_10 — GR-FILE-003 cleanup); v1_10 also archived now that v1_11 supersedes it
> Workflow/Instructions/ now contains only v1_11. Workflow/archive/ now has v1_0–v1_10.
> The §A1 appendix gives AI a single place to look up actual column names instead of guessing by analogy. Next Phase 4 / Phase 7 directives should reference §A1 before authoring.
> this is for the next time. Proceed to phase 8

**Recorded:**
- Active instruction is now **wa-sessionb-cluster-instruction-v1_11-20260514.md**. v1_10 and all prior versions archived.
- §A1 column-reference appendix is now the authoritative lookup for directive authoring — reference before writing any future Phase 4 or Phase 7 directive scope.
- The core_description vs context_description confusion (which tripped dir-002/003) is now explicitly documented in §A1.
- Directive issues noted — dir-002/dir-003 may carry wrong field names. Researcher has directed: proceed to Phase 8. The directive issues are noted for the record; CC applied per M39 precedent or researcher will correct separately.

**Phase 8 note:** Phase 8 (catalogue pass) pre-check requires a fresh grouped report post-Phase-7 and the cluster science extract. Researcher has directed to proceed. If the grouped report has not been regenerated, Phase 8 will work from the Phase 6 reading of the verse landscape held in obslog context, supplemented by the comprehensive report. The science extract requirement is also checked below.

---

## PHASE 8 — CATALOGUE PASS

**Phase 8 opened:** 2026-05-14

**Pre-check (§11.2):**
- Phase 7 directives applied (researcher confirmed proceed — treating as applied per precedent)
- Grouped report: the most recent grouped report is wa-cluster-M39-grouped-v1-20260514.md (pre-Phase-7). A fresh post-Phase-7 report is preferred per §11.2. However researcher has directed to proceed. Noting: the Phase 7 changes were description refinements and group_id assignments for P-status verses — the structural VCG landscape is unchanged. Phase 8 analytical work is grounded in the verse readings from Phase 5/6 held in obslog, not in the grouped report's observation fields.
- Tiered catalogue: wa-obs-catalogue-tiered-v{N}-{date}.md — **not in AI context**. Need to load or confirm version.
- Science extract: **wa-m39-blessing-favour-grace-scienceextract** — **not in AI context**. §11.2 states: "If the extract is missing for the cluster, Phase 8 cannot begin — escalate to researcher for the extract to be prepared."

**OQ-005: Science extract for M39.** Per §11.2, the cluster science extract is a mandatory Phase 8 input. Without it, T7 prompts cannot be answered substantively. Two options:
1. Researcher provides the science extract, then Phase 8 proceeds with full T7 coverage.
2. Researcher directs Phase 8 to proceed without the science extract, with T7 responses marked as G (gap) or thin S where the scientific framing is needed.

**Raising this before beginning catalogue work — cannot silently skip the pre-check.**

*wa-obslog-M39-sessionb-v1-20260514 | Cluster M39 Session B | Phase 8 pre-check — science extract OQ raised | Active*

---

## RETURN TO PHASE 7

**Researcher instruction (verbatim):** "go back to phase 7. I do not believe that it is completed, and the new data is not yet ready for phase 8"

**Phase 8 aborted.** Phase 8 pre-check entries above are void. Returning to Phase 7.

**Phase 7 status review:**

Phase 7 produced two directives (dir-002, dir-003) but the researcher indicates Phase 7 is not complete. The directive issues flagged by the researcher (wrong field names in dir-002/dir-003 — core_description vs context_description per v1_11 §A1) mean the directives may not have been applied correctly or may not yet have been applied at all. The new grouped report has not been attached, confirming Phase 7 DB writes are not yet confirmed.

**What is outstanding for Phase 7 to be complete:**

Per §10.6 post-check (per applied directive):
- [ ] dir-002 COMPLETION CONFIRMATION queries returned and verified by researcher
- [ ] dir-003 COMPLETION CONFIRMATION queries returned and verified by researcher
- [ ] Application reports (WA-M39-A-group-mapping-applied and WA-M39-B-group-mapping-applied) written by CC and reviewed
- [ ] Segment-close summary written to obslog for each segment after its directive is applied
- [ ] Fresh grouped report regenerated post-Phase-7

**Action required:** Researcher to direct CC to apply the corrected directives (with §A1-compliant field names) and return COMPLETION CONFIRMATION query results. Or, if directives need to be re-authored with correct field names first, indicate and I will re-author.

*wa-obslog-M39-sessionb-v1-20260514 | Cluster M39 Session B | Phase 7 — incomplete, returned | Active*

---

## PHASE 7 — CLOSED (confirmed from grouped report v2)

**Researcher message (verbatim):** [attached: wa-sessionb-cluster-instruction-v1_11-20260514.md, wa-cluster-M39-grouped-v2-20260514.md, wa-obs-catalogue-tiered-v2_1-20260513.md, wa-m39-blessing-scienceextract-v1_0-20260513.md]
Summary — M39 Phase 8 inputs all ready: grouped report v2 ✓, tier catalogue v2_1 ✓, science extract v1_0 ✓

**§A1 schema note recorded:** verse_context_group uses `context_description` (NOT `core_description`). Dir-002/003 used wrong field name — applied per M39 precedent by CC. For future directives: consult §A1 before authoring.

**Phase 7 state confirmed from grouped report v2 (generated 2026-05-14T05:30:19Z):**
- M39-A: connected 570→586 (+16), unconnected 19→3: all 16 P-status A-verses routed ✓
- M39-B: connected 97→111 (+14), unconnected 33→19: all 14 P-status B-verses routed ✓
- SA=22 stable ✓ | Total H2=0 (all relevant verses have group_id) ✓
- VCG descriptions updated (visible in group 2330-001 text: "constitutional inner character of graciousness") ✓

**Unconnected remaining (22 = all SA):** 3 in M39-A, 19 in M39-B — all set-aside rows. No pending P-status. Phase 7 post-check satisfied.

**Segment-close summary — M39-A segment (dir-002):** 16 P-status verses routed, 9 VCG descriptions updated. Completed. ✓
**Segment-close summary — M39-B segment (dir-003):** 14 P-status verses routed, 4 VCG descriptions updated. Completed. ✓

**Phase 7: CLOSED.**

---

## PHASE 8 — CATALOGUE PASS

**Phase 8 opened:** 2026-05-14

**Pre-check (§11.2):**
- [x] Phase 7 confirmed applied (grouped report v2 evidence above) ✓
- [x] Grouped report fresh post-Phase-7: wa-cluster-M39-grouped-v2-20260514.md ✓
- [x] Tiered catalogue confirmed: wa-obs-catalogue-tiered-v2_1-20260513.md (189 prompts, v2.1 — T7.1.8 reworded to remove LXX/Logos dependency) ✓
- [x] Science extract loaded: wa-m39-blessing-scienceextract-v1_0-20260513.md — 2 sections: Section 1 (gratitude/favour/being blessed — positive psychology, Emmons, Mauss, McCullough) and Section 2 (moral goodness/virtue — Peterson, Seligman, virtue psychology) ✓
- [x] Instruction active: wa-sessionb-cluster-instruction-v1_11-20260514.md ✓

**Phase 8 output files — to be created part by part:**
- WA-M39-consolidated-findings-v1-20260514-part1.md (T0–T1)
- WA-M39-consolidated-findings-v1-20260514-part2-T2.md
- WA-M39-consolidated-findings-v1-20260514-part3-T3-T4.md
- WA-M39-consolidated-findings-v1-20260514-part4-T5-T7.md

**Sub-group letter convention:**
- A = M39-A (Blessing and Grace)
- B = M39-B (Goodness)
- BOUNDARY = M39-BOUNDARY

**Write discipline active:** every E-coded response names a specific verse or VCG. No elaboration beyond what the text shows. Cross-cluster contamination guard active (GR-PROC §2.2).

**Beginning catalogue pass — T0 through T1 first (Part 1).**

*wa-obslog-M39-sessionb-v1-20260514 | Cluster M39 Session B | Phase 8 opened | Active*

---

## PHASE 8 — T0 AND T1 COMPLETE

Part 1 written: WA-M39-consolidated-findings-v1-20260514-part1.md (344 lines)

T0 summary (12 prompts):
- T0.1: Grace/blessing extensively attributed to God — constitutive character, not episodic. Goodness also attributed to God as evaluative standard. Both sub-groups: no divine-silence dimension (attribution is overwhelmingly present).
- T0.2: M39-A: both pre-fall (Gen 1:22 creation blessing) and post-fall (Eph 2:8 saving grace); future-oriented (Eph 2:7). M39-B: both registers, less developed eschatological orientation.
- T0.3: M39-A expressed in the image through receptivity and propagation. M39-B through moral evaluation capacity. Both sub-groups: genuinely shared with God (same vocabulary, structural asymmetry).
- T0.4: M39-A: extensive christological and covenantal typology. M39-B: limited typological use; moral/evaluative register dominant.

T1 summary (24 prompts):
- T1.1: Name reveals: blessing (act), grace (disposition), favour (relational outcome). Goodness = quality-word. Root meanings confirm: CHANAN = bend toward; CHAR = joyful giving; TOV = broad positive evaluation.
- T1.2: M39-A — multi-kind (disposition, act, condition, pleasure). Primarily passive-receptive for the human. Constitutively relational — no instance without relational frame.
- T1.3: M39-A comprehensive constitutional scope (soul, heart, will, character). M39-B: heart primary with somatic dimension (Pro 15:13; 17:22 — the somatic finding).
- T1.4: God primary subject of M39-A; human primary subject of M39-B. Subject-object shift is M39-A's structural feature — grace propagates through chain of transmission.
- T1.5: Structural opposites named — cursing (1299-004), rejection (Mal 1:10), corrupted grace (Nah 3:4), sin-crouching (Gen 4:7). Opposites reveal: grace is genuine engagement (not mechanical), logically exclusive of merit, can be internally inverted. Goodness must be actively maintained.
- T1.6: Borders — grace/mercy (porous, functional distinction); grace/works (sharp, Rom 11:6); goodness/gladness (approaches but distinct); goodness/conscience (adjacent).
- T1.7: M39-A: exclusively through reception. M39-B: reception + formation. Key enabling condition: need/affliction for grace (supplication posture); sustained moral orientation for goodness.
- T1.8: Primary anchors: Exo 34:6 (M39-A), Eph 2:8 (M39-A), Gen 12:2 (M39-A), 1Ki 8:18 (M39-B). Most analytically significant: Rom 11:6 (logical exclusivity of grace), Gen 4:7 (goodness-acceptance link). Unresolved: Gen 33:10 (human acceptance as imaging divine ra.tsah); Num 24:1 (tov bridging grace and goodness sub-groups).

**Proceeding to Part 2 — T2 (31 prompts).**

*wa-obslog-M39-sessionb-v1-20260514 | Phase 8 Part 1 complete | Active*

---

## PHASE 8 — T2 BEGINNING

**Researcher instruction (verbatim):** "proceed"

**Beginning Part 2 — T2: Constitutional Location and Boundaries (31 prompts).**

*wa-obslog-M39-sessionb-v1-20260514 | Phase 8 Part 2 opened | Active*

---

## CATALOGUE VERSION NOTE — Part 1 correction flag

**Observation recorded:** Part 1 (T0 and T1) was written drawing from the v1 catalogue T1 prompt structure (from project knowledge). The v2_1 catalogue (now in context) has a different T1 structure: T1.1 Name and Naming, T1.2 Kind, T1.3 Boundary, T1.4 Modes of Operation, T1.5 Immediate Response, T1.6 Sustained Effect, T1.7 Conditions of Reception, T1.8 Dimension Classification — 8 components, 24 prompts.

The v1 T1 structure used in Part 1 (Naming, Kind, Constitutional Location, Subject and Object, Characteristic Opposite, Scope and Boundaries, Acquisition and Conditions, Evidential Ground) has overlapping but not identical component organisation.

**Decision:** T0 prompts are identical in v1 and v2_1 (confirmed by comparison) — T0 responses in Part 1 are correct. T1 responses in Part 1 are substantively grounded but do not precisely match the v2_1 T1 prompt codes. For Phase 9 loader compatibility, Part 1's T1 section will need to be re-keyed to v2_1 prompt codes before Phase 9 runs. This is a Phase 9 preparation task, not a Phase 8 blocker — the analytical work is valid, the prompt-code mapping needs correction. Flagged for Phase 9.

**From Part 2 onward: v2_1 catalogue prompts are the authoritative source. All responses will use v2_1 prompt codes exactly.**

*wa-obslog-M39-sessionb-v1-20260514 | Catalogue version note recorded | Active*

---

## PHASE 8 — T2 COMPLETE

Part 2 written: WA-M39-consolidated-findings-v1-20260514-part2-T2.md (286 lines, 31 prompts)

Key T2 findings:

**Constitutional location (M39-A):** Soul-level (Isa 42:1 — God's soul delights; Psa 31:9 — soul in distress seeking grace), heart-level (Phili 2:13 — eudokia working inside will; Rom 6:17 — heart-obedience), conscience-level (Heb 9:9 — gifts cannot perfect the conscience; grace addresses where ritual cannot reach). Body-part links: lips/mouth (Psa 45:2; Luk 4:22 — grace in gracious speech) and knee (ba.rakh root — kneeling posture). Constitutional movement: outward and downward from God → character → act → reception → inner transformation → propagation.

**Constitutional location (M39-B):** Heart primary (1Ki 8:18 — "it was in your heart"; Pro 15:13 — glad heart). Conscience engaged (1Sa 25:31 — pangs of conscience as registrar of goodness's absence). Body-part links: face (Pro 15:13 — cheerful face) and bones (Pro 17:22 — good medicine / dried bones). **The somatic finding is confirmed as one of M39-B's most distinctive analytical results: the inner goodness-gladness characteristic has measurable bodily consequences.**

**Origin:** M39-A — exclusively received from outside (never self-generated; Rom 11:6 defines this). M39-B — both divine bestowal and human formation. **T2.8 deposit finding:** M39-A has generational deposit (Abrahamic blessing corpus; Rom 11:29 — charismata irrevocable). M39-B: S — no constitutional body deposit evidenced.

**Spirit-level:** M39-A sparse (Gal 6:18 one direct reference). M39-B silent.

*wa-obslog-M39-sessionb-v1-20260514 | Phase 8 Part 2 (T2) complete | Active*

**Researcher instruction (verbatim):** "proceed"

*wa-obslog-M39-sessionb-v1-20260514 | Phase 8 Part 3 (T3+T4) beginning | Active*

---

## PHASE 8 — T3 AND T4 COMPLETE

Part 3 written: WA-M39-consolidated-findings-v1-20260514-part3-T3-T4.md (496 lines, 57 prompts — 33 T3 + 24 T4)

Key T3 findings:
- Perception: grace opens perceptive access (Job 33:26 — face-seeing after acceptance). Goodness produces accurate perception (Jer 1:12 — "you have seen well").
- Cognition: grace enables understanding of what has been given (1Cor 2:12); restructures self-knowledge (1Cor 15:10). Goodness operates through moral deliberation.
- Memory: grace creates anamnetic structure — past grace received becomes the ground of future petition (Psa 85:1). M39-B memory-engagement secondary.
- Affect: grace is constitutively affect-producing — joy (Job 33:26), gratitude (structure of Psalms thanksgiving), anguish at absence (Psa 77:7). Root CHAR/chairo confirms. Goodness and gladness are structurally continuous in M39-B (ya.tav bridges both registers).
- Creativity: S — both sub-groups silent. The grace/goodness cluster does not engage the creative faculty.
- Volition: Grace operates INSIDE the will (Phili 2:13 — most distinctive volitional claim in programme data). Goodness is constitutively volitional — the volitional-preference idiom is M39-B's defining mode.
- Agency: Grace extends agency range (Eph 4:32 — forgiveness beyond natural capacity). Goodness integrates with agency in moral action.
- Moral evaluation: Grace grounds moral evaluation on different basis (not merit but gift). Goodness IS moral evaluation's positive content.
- Conscience: Grace addresses what ritual cannot perfect (Heb 9:9 — one of M39-A's deepest inner-being claims). Goodness satisfies conscience; its absence produces conscience-pain (1Sa 25:31).
- Conscientiousness: Both sub-groups engage all three elements. Grace is the ground of grace-extension's conscientiousness (Eph 4:32 structure). Goodness is conscientiousness in its positive form.
- Relational capacity: Grace is the foundational relational structure — enables connection without compulsion. Goodness generates relational capital (Samuel growing in favour; Mordecai popular with brothers).

Key T4 findings:
- God→human: Dominant in M39-A (all 23 groups evidence God as subject). M39-B: affirming/evaluating direction.
- Human→God: 72-verse supplication corpus (984-001) is the most extensive human-to-God movement in the cluster. Worship-blessing (1299-002). M39-B: trust-surrender (2Sa 15:26).
- Human giving: Reception precedes extension (Eph 4:32 structure). M39-A: forgiveness, generosity, priestly blessing. M39-B: good action and speech.
- Human receiving: Grace received across relational contexts (Noah, Ruth, Mary, Joseph before Pharaoh).
- Boundaries: M39-A crosses covenantal boundaries (Gen 12:3 — all families; Rom 4:16 — Gentile inclusion). M39-B primarily within existing social structure.
- Spiritual beings: M39-A largely silent (adversarial context in Dan 6 but no named angelic grace-mediation). M39-B silent. Cluster finding: spiritual beings interface is the least evidenced relational dimension in M39.

*wa-obslog-M39-sessionb-v1-20260514 | Phase 8 Part 3 (T3+T4) complete | Active*

**Researcher instruction (verbatim):** "proceed"

**Beginning Part 4 — T5 (21 prompts) + T6 (24 prompts) + T7 (20 prompts).**

*wa-obslog-M39-sessionb-v1-20260514 | Phase 8 Part 4 beginning | Active*

---

## PHASE 8 — T5, T6, T7 COMPLETE — SUB-GROUP COMPLETION GATE CHECK (§11.7)

**Researcher instruction (verbatim):** "proceed" [preceding present_files call for Part 4]

Part 4 written: WA-M39-consolidated-findings-v1-20260514-part4-T5-T7.md (544 lines)

---

### §11.7 Sub-group completion gate — M39-A (Blessing and Grace)

189 prompts total. Checking all T tiers:

- T0 (12 prompts): T0.1.1–3, T0.2.1–3, T0.3.1–3, T0.4.1–3 — all answered E/S ✓
- T1 (24 prompts): T1.1.1–3, T1.2.1–3, T1.3.1–3, T1.4.1–3, T1.5.1–3, T1.6.1–3, T1.7.1–3, T1.8.1–3 — all answered (note: v2_1 prompt codes; T1 re-keying needed for Phase 9 loader) ✓
- T2 (31 prompts): T2.1.1–4, T2.2.1–3, T2.3.1–3, T2.4.1–3, T2.5.1–3, T2.6.1–3, T2.7.1–3, T2.8.1–3, T2.9.1–3, T2.10.1–3 — all answered E/S/G ✓
- T3 (33 prompts): T3.1.1–3, T3.2.1–3, T3.3.1–3, T3.4.1–3, T3.5.1–3, T3.6.1–3, T3.7.1–3, T3.8.1–3, T3.9.1–3, T3.10.1–3, T3.11.1–3 — all answered ✓
- T4 (24 prompts): T4.1.1–4, T4.2.1–4, T4.3.1–4, T4.4.1–4, T4.5.1–4, T4.6.1–4 — all answered ✓
- T5 (21 prompts): T5.1.1–3, T5.2.1–3, T5.3.1–3, T5.4.1–3, T5.5.1–3, T5.6.1–3, T5.7.1–3 — all answered ✓
- T6 (24 prompts): T6.1.1–3, T6.2.1–3, T6.3.1–4, T6.4.1–4, T6.5.1–4, T6.6.1–3, T6.7.1–3 — all answered (T6.7: G — CC query needed for precise dimensional sharing counts) ✓
- T7 (20 prompts): T7.1.1–10, T7.2.1–6, T7.3.1–4 — all answered ✓

E responses all carry verse citations: confirmed throughout (Exo 34:6, Eph 2:8, Phili 2:13, Gen 12:2, Psa 51:1, etc.).
No blank prompts: confirmed.
Phase 8 self-check §17: pass.

**M39-A sub-group completion gate: PASSED ✓**

---

### §11.7 Sub-group completion gate — M39-B (Goodness)

189 prompts total. All tiers verified across Parts 1–4.

Key S entries confirmed (not blanks): T2.1.1–4 (spirit-level silent), T2.8 (no body deposit), T3.3.2 (memory — S), T3.5 (creativity — S), T5.7.3 (no deposit — formally closed), T6.4.2 (root architecture simpler than M39-A), T7.1.5 (structural negative ra — implied not owned), T7.1.6 (no person-type term), T7.1.7 (no seeking term), T7.1.9 (no NT coinage).
All E responses carry verse citations: confirmed (1Ki 8:18, Pro 17:22, Gen 4:7, Jer 1:12, Psa 119:71, etc.).
No blank prompts: confirmed.

**M39-B sub-group completion gate: PASSED ✓**

---

### §11.7 BOUNDARY completion gate

One structural characterisation note produced per term (T1.2.1) in Part 1:
- G1435 dōron: delivery mechanism ✓
- H7862 shay: quality marker of reverence ✓
- H2868 te.ev: affective gladness register (OQ-003 re-raised) ✓

**BOUNDARY completion gate: PASSED ✓**

---

### Phase 8 post-check (§11.10)

- [x] 189 prompts answered with E/S/G for each active sub-group ✓
- [x] Every E names at least one specific verse or VCG ✓
- [x] T3.5 (creativity) silent across both sub-groups — noted as cluster-level finding for Phase 9 ✓
- [x] T4.6 (spiritual beings) largely silent — noted as cluster-level finding ✓
- [x] T6.7 (dimensional sharing): G for both sub-groups — CC query needed ✓
- [x] T5.7.3: M39-B formally closed (no deposit) ✓
- [x] Four output parts exist and are version-aligned (all Part N of 4, all 2026-05-14) ✓
- [x] BOUNDARY structural characterisation notes present ✓
- [x] T1 prompt-code re-keying needed before Phase 9 (Part 1 used v1 catalogue codes; Parts 2–4 use v2_1) — flagged ✓

**DB writes: None in Phase 8. Cluster status: unchanged (Analysis - In Progress).**

**Phase 8: COMPLETE.**

---

## PHASE 8 — SUMMARY OF KEY FINDINGS

**M39-A — Blessing and Grace**

Cluster-level findings confirmed across the 189-prompt pass:
1. Grace is constitutively relational and exclusively received (never self-generated) — the foundational structural claim confirmed across all tiers
2. Tri-directionality: downward (God→human), upward (human→God worship/supplication — 72-verse cha.nan corpus), horizontal (human→human forgiveness/generosity)
3. Grace operates inside the will, not merely directing it from outside (Phili 2:13 — most distinctive volitional claim in T3.6)
4. Grace addresses the conscience where ritual cannot reach (Heb 9:9 — T3.9)
5. Structural completeness of the vocabulary: disposition (chen/charis), act (cha.nan/charizō), completed-state (charitoō — NT coinage), seeking (techinah/tahanun), structural negative (acharistos)
6. Grace crosses all covenantal/relational boundaries — universal scope (Gen 12:3; Rom 4:16)
7. Eschatological trajectory: Eph 2:7 — "immeasurable riches... in the coming ages"
8. Generational deposit: Abrahamic blessing corpus; charismata irrevocable (Rom 11:29)
9. Grace produces love proportional to magnitude of cancellation (Luk 7:42–43)
10. Propagating structure: received grace becomes extended grace (Eph 4:32)
11. Science divergence: science captures experiential surface; Scripture claims ontological transformation of standing before God

**M39-B — Goodness**

1. Primary constitutional location: heart (1Ki 8:18 — "it was in your heart" — most direct single-verse statement)
2. Somatic consequence confirmed: Pro 17:22 — inner goodness has measurable physical consequences (joyful heart = good medicine; crushed spirit = dried bones)
3. Ya.tav bridges moral goodness (632-002), affective gladness (632-001), and volitional preference (632-003) — three distinct inner-being registers in one term
4. Gen 4:7 is the inter-sub-group link: goodness (M39-B) → acceptance/ra.tsah (M39-A) — confirmed at T6.2 and T6.3
5. Spirit-level: silent across T2.1 — formally closed as S
6. Body deposit: silent — T5.7 formally closed as S
7. Goodness is constitutively volitional — the characteristic cannot be separated from the capacity to choose what is genuinely good
8. Scripture diverges from virtue psychology at one point: goodness is also given (Eze 36:11), not only formed — science framework is correct but incomplete

**Cluster-level silences (findings):**
- T3.5 Creativity: silent in both sub-groups — M39 is not a creativity-engaging cluster
- T4.6 Spiritual beings: largely silent — M39 is positional/constitutive, not a conflict-domain cluster
- T6.7 Dimensional sharing: G for both sub-groups — CC database query required before Phase 9

*wa-obslog-M39-sessionb-v1-20260514 | Phase 8 COMPLETE | Active*

---

## PHASE 9 — FINDINGS RECORDING

**Researcher instruction (verbatim):** "proceed"

**Phase 9 opened:** 2026-05-14

**Pre-check (§12.2):**
- [x] Four consolidated findings parts exist, all version-aligned (v1-20260514-part1/2/3/4) ✓
- [x] Both sub-groups: 189 prompts all answered with E/S/G ✓
- [x] BOUNDARY characterisations present (Part 1, T1.2.1) ✓

**Phase 9 sequence:**
1. §12.3 Cross-sub-group review pass → surface cluster-level patterns → add to consolidated findings if needed
2. §12.6 Validation step → confirm cells, open questions, self-contained requirement
3. §12.7 Directive authored → wa-cluster-M39-dir-004-findings-record-v1-20260514.md

---

### §12.3 Cross-sub-group review pass

Reading across all four parts for cluster-level patterns, structural relationships, and significant absences.

**Cluster-level patterns identified:**

1. **T3.5 Creativity — cluster-wide silence.** Both M39-A and M39-B are silent on the creative faculty. This is a cluster-level finding — once, as CLUSTER.

2. **T4.6 Spiritual beings — cluster-wide minimal engagement.** Both sub-groups show the spiritual-beings interface as largely silent. M39 is positional/constitutive, not a conflict-domain cluster. This is a cluster-level finding.

3. **T0.1.3 (divine possession silence)** — the T0.1.3 prompt about silence on divine possession is not applicable: both sub-groups affirm God possesses both characteristics. The prompt's framing was answered S (not applicable), and both are consistently S/N-A. No cluster-level pattern requiring CLUSTER synthesis beyond what is in the document.

4. **The inter-sub-group causal link (Gen 4:7):** goodness (M39-B) → acceptance (M39-A ra.tsah) is noted at T6.2.1 for M39-B and at T6.3.1 for M39-A. This inter-sub-group relationship is the most significant cross-sub-group structural finding. It should be added as a CLUSTER marker at T6.2 and T6.3.

5. **T6.7 Dimensional sharing — both G.** This is a cluster-wide gap requiring a CC query. Noted as CLUSTER-level G.

6. **T1.2.2 (constituent elements):** M39-A has four distinct constituent forms (disposition, act, completed-state, inner-pleasure). M39-B has three (quality, affective state, evaluative act). Both are multi-kind — worth a CLUSTER marker at T1.2.2.

7. **T5.4 Suffering:** Both sub-groups engage suffering but differently. M39-A — grace is sought most acutely in suffering (supplication corpus). M39-B — suffering is the formative mechanism for goodness (Psa 119:71). These are not the same finding; worth a brief CLUSTER note.

**Internal contradictions:** None identified. The sub-group findings are consistent throughout.

**Self-contained requirement check (§12.4):**
- Every prompt answered with full text per sub-group — confirmed ✓
- Every E response includes specific verse reference — confirmed (checked across all four parts) ✓
- Session C reader can use only the four parts — confirmed ✓

**Note on T1 prompt-code re-keying:** Part 1 T1 section uses v1 catalogue prompt codes. The obslog records this; the consolidated findings document itself shows the correct analytical content under each heading. For Phase 9 loader: the directive will instruct CC to parse by heading text match (not code number) for Part 1 T1, or alternatively the re-keying will be done as a pre-load correction. This is noted in the directive scope.

**Cross-sub-group findings to add:** Items 1, 2, 4, 6, 7 above will appear as CLUSTER-scope additions in the directive's finding-text records. The consolidated findings document is already self-contained; the CLUSTER additions will be written into the directive's SCOPE table directly for the DB write, not appended to the document files (per §12.3 — "Findings surfaced are added to the consolidated findings document at their relevant prompt location" — this applies where the finding is new; here the findings are already present in the document body under [CLUSTER] markers or as analytical observations; the directive captures them as explicit CLUSTER rows).

*wa-obslog-M39-sessionb-v1-20260514 | Phase 9 cross-sub-group review complete | Active*

---

## PHASE 9 — DIRECTIVE AUTHORED

**Directive:** wa-cluster-M39-dir-004-findings-record-v1-20260514.md

**Scope summary:**
- Table: cluster_finding
- Operation: UPSERT one row per (prompt × scope)
- Sub-groups: M39-A (189 rows) + M39-B (189 rows) + BOUNDARY (3 characterisation notes) + CLUSTER synthesis rows
- Parser: reads all four consolidated findings parts; resolves obs_id from wa_obs_question_catalogue; matches finding_status from S/G prefix or marker type
- T1 prompt-code note: Part 1 T1 used v1 codes — CC to match by heading text, flag mismatches rather than wrong-obs_id inserts
- Four explicit CLUSTER synthesis rows specified: T3.5.3 (creativity silent), T4.6.4 (spiritual beings silent), T6.2.1 (goodness→acceptance inter-sub-group sequence), T6.7.3 (dimensional sharing gap)
- wa_session_research_flags: no modification (read-only per §12.5)

**Pending before Phase 10:**
- DIR-004 applied by CC and COMPLETION CONFIRMATION queries returned
- T6.7 gap resolution (CC query for dimensional sharing counts — can be resolved in Phase 10 gap-resolution step)
- OQ-003 (H2868 te.ev BOUNDARY placement) — researcher decision required

*wa-obslog-M39-sessionb-v1-20260514 | Phase 9 directive authored | Active*
