# wa-099-kindness — Cross-Registry Term Extract (DIR-20260501-001)

_Generated: 2026-05-01T12:11:08Z · schema 3.17.0 · read-only extract — no DB writes._

**Directive:** [`wa-099-kindness-dir-001-crossreg-extract-v1-20260501.md`](../obslog/wa-099-kindness-dir-001-crossreg-extract-v1-20260501.md)

**Purpose:** supplementary source material for R099 kindness Stage 2b. Four kindness-cluster terms owned by other registries (H2617A chesed → R103, G5544 chrēstotēs → R067, H2623 chasid → R103, H2616A chasad → R023) extracted from the live database for analytical use alongside the R099 readiness output. OWNER assignments unchanged.

**Schema adaptations** (per directive note 3): the directive's column references `mti_terms.owning_registry_id`, `verse_context_group.dimension_id` /`dimension_confidence` /`dominant_subject` /count fields, and `verse_context.verse_ref`/`target_word` do not exist as such in v3.17.0. Adapted to: `mti_terms.owning_registry_fk` → `word_registry.id`; group counts + dimension via `wa_dimension_index` joined on `verse_context_group_id`; verse reference + target_word via `wa_verse_records` joined on `verse_context.verse_record_id`. Meaning senses keyed on `wa_meaning_sense.level_code` /`level_depth`/`parent_level_code` (not `sense_code`/`depth`).

---

## Section map

Per term (priority order: H2617A → G5544 → H2623 → H2616A):
- **A.** Term identity + lexical foundation (meaning parse, senses, root family, related words)
- **B.** Verse-context groups (group_code, dimension, counts, descriptions)
- **C.** Anchor verses (verbatim text)
- **D.** All relevant verses (verbatim text — H2617A truncated at 100 verses per directive note 4)

---

## H2617A — che.sed "kindness" (owner R103 love, priority 1)

_Rationale per directive: Primary Hebrew kindness term — 169 corpus verses — essential_

### A. Term identity and lexical foundation

### H2617A — che.sed "kindness"

**Identity:** mti=536 · ti=330 · language=Hebrew · status=extracted · md_v=1
**Owner registry:** 103 (love)

**Meaning parse** (parser v1.0.0, parsed 2026-03-28T15:13:44): 1 top sense(s) · stems=0 · causative=False · domain_tags=False

**Senses (top-level):**

- `1`: goodness, kindness, faithfulness

**Root family:** `CHESED` () — 

**Related words (14 total):**

- `H2616A` cha.sad "be kind"
- `H2616B` cha.sad "to shame"
- `H2617B` che.sed "shame"
- `H2618` che.sed "Hesed"
- `H2619` cha.sad.yah "Hasadiah"
- `H2623` cha.sid "pious"
- `H2624` cha.si.dah "stork"
- `H2616A` cha.sad "be kind"
- `H2619` cha.sad.yah "Hasadiah"
- `H2618` che.sed "Hesed"
- `H2616B` cha.sad "to shame"
- `H2623` cha.sid "pious"
- `H2617B` che.sed "shame"
- `H2624` cha.si.dah "stork"

### B. Verse-context groups

### H2617A — 3 active group(s)

**Group `536-001`** (180 related · 2 anchor · 7 set-aside · 182 total · dimension: 06 — Relational Disposition · confidence: CLAUDE_AI · dominant_subject: GOD)
  - *Term names God's steadfast love as his defining inner attribute — the covenantal faithfulness that never ceases, extends to heaven, and is the ground of Israel's hope and petition*
  - notes: SUPPLEMENTAL_VID_ASSIGNMENT_REQUIRED

**Group `536-002`** (38 related · 2 anchor · 7 set-aside · 40 total · dimension: 05 — Moral Character · confidence: CLAUDE_AI · dominant_subject: HUMAN)
  - *Term names human expressions of covenantal loyalty and kindness — the inner disposition of faithfulness between persons that mirrors divine chesed*
  - notes: SUPPLEMENTAL_VID_ASSIGNMENT_REQUIRED

**Group `536-003`** (10 related · 2 anchor · 7 set-aside · 12 total · dimension: 05 — Moral Character · confidence: CLAUDE_AI · dominant_subject: HUMAN)
  - *Term names the failure or withdrawal of chesed — its absence as the condition of moral and spiritual ruin; also the passionate demand for it as the priority above ritual*
  - notes: SUPPLEMENTAL_VID_ASSIGNMENT_REQUIRED

### C. Anchor verses (verbatim)

### H2617A — anchor verses (verbatim)

**Group `536-001`** — anchor verses (2):

- **Psa 63:3** 🔵 (✓) *target: steadfast love*
  > Psa 63:3 Because your steadfast love is better than life , my lips will praise you .
- **Lam 3:22** 🔵 (✓) *target: steadfast love*
  > Lam 3:22 The steadfast love of the Lord never ceases ; his mercies never come to an end ;

**Group `536-002`** — anchor verses (2):

- **Rut 3:10** 🔵 (✓) *target: kindness*
  > Rut 3:10 And he said , “May you be blessed by the Lord , my daughter . You have made this last kindness greater than the first in that you have not gone after young men , whether poor or rich .
- **Pro 3:3** 🔵 (✓) *target: steadfast love*
  > Pro 3:3 Let not steadfast love and faithfulness forsake you; bind them around your neck ; write them on the tablet of your heart .

**Group `536-003`** — anchor verses (2):

- **Hos 6:6** 🔵 (✓) *target: steadfast love*
  > Hos 6:6 For I desire steadfast love and not sacrifice , the knowledge of God rather than burnt offerings .
- **Mic 6:8** 🔵 (✓) *target: kindness*
  > Mic 6:8 He has told you , O man , what is good ; and what does the Lord require of you but to do justice , and to love kindness , and to walk humbly with your God ?

### D. All relevant verses (verbatim)

### H2617A — all relevant verses (verbatim)

**Group `536-001`** — all relevant verses (182):

- **Gen 19:19** (✓) *target: kindness*
  > Gen 19:19 Behold , your servant has found favor in your sight , and you have shown me great kindness in saving my life . But I cannot escape to the hills , lest the disaster overtake me and I die .
- **Gen 24:12** (✓) *target: steadfast love*
  > Gen 24:12 And he said , “O Lord , God of my master Abraham , please grant me success today and show steadfast love to my master Abraham .
- **Gen 24:14** (✓) *target: steadfast love*
  > Gen 24:14 Let the young woman to whom I shall say , ‘ Please let down your jar that I may drink ,’ and who shall say , ‘ Drink , and I will water your camels ’—let her be the one whom you have appointed for your servant Isaac . By this I shall know that you have shown steadfast love to my master .”
- **Gen 24:27** (✓) *target: steadfast love*
  > Gen 24:27 and said , “ Blessed be the Lord , the God of my master Abraham , who has not forsaken his steadfast love and his faithfulness toward my master . As for me, the Lord has led me in the way to the house of my master’s kinsmen .”
- **Gen 32:10** (✓) *target: steadfast love*
  > Gen 32:10 I am not worthy of the least of all the deeds of steadfast love and all the faithfulness that you have shown to your servant , for with only my staff I crossed this Jordan , and now I have become two camps .
- **Gen 39:21** (✓) *target: steadfast love*
  > Gen 39:21 But the Lord was with Joseph and showed him steadfast love and gave him favor in the sight of the keeper of the prison .
- **Exo 15:13** (✓) *target: steadfast love*
  > Exo 15:13 “You have led in your steadfast love the people whom you have redeemed ; you have guided them by your strength to your holy abode .
- **Exo 20:6** (✓) *target: steadfast love*
  > Exo 20:6 but showing steadfast love to thousands of those who love me and keep my commandments .
- **Exo 34:6** (✓) *target: steadfast*
  > Exo 34:6 The Lord passed before him and proclaimed , “The Lord , the Lord , a God merciful and gracious , slow to anger , and abounding in steadfast love and faithfulness ,
- **Exo 34:7** (✓) *target: steadfast love*
  > Exo 34:7 keeping steadfast love for thousands , forgiving iniquity and transgression and sin , but who will by no means clear the guilty , visiting the iniquity of the fathers on the children and the children’s children, to the third and the fourth generation.”
- **Num 14:18** (✓) *target: steadfast love*
  > Num 14:18 ‘The Lord is slow to anger and abounding in steadfast love , forgiving iniquity and transgression , but he will by no means clear the guilty, visiting the iniquity of the fathers on the children , to the third and the fourth generation.’
- **Num 14:19** (✓) *target: steadfast love*
  > Num 14:19 Please pardon the iniquity of this people , according to the greatness of your steadfast love , just as you have forgiven this people , from Egypt until now .”
- **Deu 5:10** (✓) *target: steadfast love*
  > Deu 5:10 but showing steadfast love to thousands of those who love me and keep my commandments .
- **Deu 7:9** (✓) *target: steadfast love*
  > Deu 7:9 Know therefore that the Lord your God is God , the faithful God who keeps covenant and steadfast love with those who love him and keep his commandments , to a thousand generations ,
- **Deu 7:12** (✓) *target: steadfast love*
  > Deu 7:12 “And because you listen to these rules and keep and do them, the Lord your God will keep with you the covenant and the steadfast love that he swore to your fathers .
- **2Sa 2:6** (✓) *target: steadfast love*
  > 2Sa 2:6 Now may the Lord show steadfast love and faithfulness to you. And I will do good to you because you have done this thing .
- **2Sa 7:15** (✓) *target: steadfast love*
  > 2Sa 7:15 but my steadfast love will not depart from him, as I took it from Saul , whom I put away from before you.
- **2Sa 15:20** (✓) *target: steadfast love*
  > 2Sa 15:20 You came only yesterday , and shall I today make you wander about with us, since I go I know not where ? Go back and take your brothers with you, and may the Lord show steadfast love and faithfulness to you.”
- **2Sa 22:51** (✓) *target: steadfast love*
  > 2Sa 22:51 Great salvation he brings to his king , and shows steadfast love to his anointed , to David and his offspring forever .”
- **1Ki 3:6** (✓) *target: steadfast love*
  > 1Ki 3:6 And Solomon said , “ You have shown great and steadfast love to your servant David my father , because he walked before you in faithfulness , in righteousness , and in uprightness of heart toward you. And you have kept for him this great and steadfast love and have given him a son to sit on his throne this day .
- **1Ki 8:23** (✓) *target: steadfast love*
  > 1Ki 8:23 and said , “O Lord , God of Israel , there is no God like you, in heaven above or on earth beneath, keeping covenant and showing steadfast love to your servants who walk before you with all their heart ;
- **1Ch 16:34** (✓) *target: steadfast love*
  > 1Ch 16:34 Oh give thanks to the Lord , for he is good ; for his steadfast love endures forever !
- **1Ch 16:41** (✓) *target: steadfast love*
  > 1Ch 16:41 With them were Heman and Jeduthun and the rest of those chosen and expressly named to give thanks to the Lord , for his steadfast love endures forever .
- **1Ch 17:13** (✓) *target: steadfast love*
  > 1Ch 17:13 I will be to him a father , and he shall be to me a son . I will not take my steadfast love from him, as I took it from him who was before you,
- **2Ch 1:8** (✓) *target: steadfast love*
  > 2Ch 1:8 And Solomon said to God , “ You have shown great and steadfast love to David my father , and have made me king in his place .
- **2Ch 5:13** (✓) *target: steadfast love*
  > 2Ch 5:13 and it was the duty of the trumpeters and singers to make themselves heard in unison in praise and thanksgiving to the Lord ), and when the song was raised , with trumpets and cymbals and other musical instruments , in praise to the Lord , “ For he is good , for his steadfast love endures forever ,” the house , the house of the Lord , was filled with a cloud ,
- **2Ch 6:14** (✓) *target: steadfast love*
  > 2Ch 6:14 and said , “O Lord , God of Israel , there is no God like you, in heaven or on earth , keeping covenant and showing steadfast love to your servants who walk before you with all their heart ,
- **2Ch 6:42** (✓) *target: steadfast love*
  > 2Ch 6:42 O Lord God , do not turn away the face of your anointed one ! Remember your steadfast love for David your servant .”
- **2Ch 7:3** (✓) *target: steadfast love*
  > 2Ch 7:3 When all the people of Israel saw the fire come down and the glory of the Lord on the temple , they bowed down with their faces to the ground on the pavement and worshiped and gave thanks to the Lord , saying, “ For he is good , for his steadfast love endures forever .”
- **2Ch 7:6** (✓) *target: steadfast love*
  > 2Ch 7:6 The priests stood at their posts ; the Levites also, with the instruments for music to the Lord that King David had made for giving thanks to the Lord — for his steadfast love endures forever —whenever David offered praises by their ministry ; opposite them the priests sounded trumpets , and all Israel stood .
- **2Ch 20:21** (✓) *target: steadfast love*
  > 2Ch 20:21 And when he had taken counsel with the people , he appointed those who were to sing to the Lord and praise him in holy attire , as they went before the army , and say , “Give thanks to the Lord , for his steadfast love endures forever .”
- **Ezr 3:11** (✓) *target: steadfast love*
  > Ezr 3:11 And they sang responsively , praising and giving thanks to the Lord , “ For he is good , for his steadfast love endures forever toward Israel .” And all the people shouted with a great shout when they praised the Lord , because the foundation of the house of the Lord was laid.
- **Ezr 7:28** (✓) *target: steadfast love*
  > Ezr 7:28 and who extended to me his steadfast love before the king and his counselors , and before all the king’s mighty officers . I took courage , for the hand of the Lord my God was on me, and I gathered leading men from Israel to go up with me .
- **Ezr 9:9** (✓) *target: steadfast love*
  > Ezr 9:9 For we are slaves . Yet our God has not forsaken us in our slavery , but has extended to us his steadfast love before the kings of Persia , to grant us some reviving to set up the house of our God , to repair its ruins , and to give us protection in Judea and Jerusalem .
- **Neh 1:5** (✓) *target: steadfast love*
  > Neh 1:5 And I said , “ O Lord God of heaven , the great and awesome God who keeps covenant and steadfast love with those who love him and keep his commandments ,
- **Neh 9:17** (✓) *target: steadfast love*
  > Neh 9:17 They refused to obey and were not mindful of the wonders that you performed among them, but they stiffened their neck and appointed a leader to return to their slavery in Egypt . But you are a God ready to forgive , gracious and merciful , slow to anger and abounding in steadfast love , and did not forsake them .
- **Neh 9:32** (✓) *target: steadfast love*
  > Neh 9:32 “ Now , therefore, our God , the great , the mighty , and the awesome God , who keeps covenant and steadfast love , let not all the hardship seem little to you that has come upon us, upon our kings , our princes , our priests , our prophets , our fathers , and all your people , since the time of the kings of Assyria until this day .
- **Neh 13:22** (✓) *target: steadfast love*
  > Neh 13:22 Then I commanded the Levites that they should purify themselves and come and guard the gates , to keep the Sabbath day holy . Remember this also in my favor, O my God , and spare me according to the greatness of your steadfast love .
- **Job 10:12** (✓) *target: life*
  > Job 10:12 You have granted me life and steadfast love, and your care has preserved my spirit .
- **Job 37:13** (✓) *target: love*
  > Job 37:13 Whether for correction or for his land or for love , he causes it to happen .
- **Psa 5:7** (✓) *target: steadfast love*
  > Psa 5:7 But I , through the abundance of your steadfast love , will enter your house . I will bow down toward your holy temple in the fear of you.
- **Psa 6:4** (✓) *target: steadfast love*
  > Psa 6:4 Turn , O Lord , deliver my life ; save me for the sake of your steadfast love .
- **Psa 13:5** (✓) *target: steadfast love*
  > Psa 13:5 But I have trusted in your steadfast love ; my heart shall rejoice in your salvation .
- **Psa 17:7** (✓) *target: steadfast love*
  > Psa 17:7 Wondrously show your steadfast love , O Savior of those who seek refuge from their adversaries at your right hand .
- **Psa 18:50** (✓) *target: steadfast love*
  > Psa 18:50 Great salvation he brings to his king , and shows steadfast love to his anointed , to David and his offspring forever .
- **Psa 21:7** (✓) *target: steadfast love*
  > Psa 21:7 For the king trusts in the Lord , and through the steadfast love of the Most High he shall not be moved .
- **Psa 23:6** (✓) *target: mercy*
  > Psa 23:6 Surely goodness and mercy shall follow me all the days of my life , and I shall dwell in the house of the Lord forever .
- **Psa 25:6** (✓) *target: steadfast love*
  > Psa 25:6 Remember your mercy , O Lord , and your steadfast love , for they have been from of old .
- **Psa 25:7** (✓) *target: steadfast love*
  > Psa 25:7 Remember not the sins of my youth or my transgressions ; according to your steadfast love remember me, for the sake of your goodness , O Lord !
- **Psa 25:10** (✓) *target: steadfast love*
  > Psa 25:10 All the paths of the Lord are steadfast love and faithfulness , for those who keep his covenant and his testimonies .
- **Psa 26:3** (✓) *target: steadfast love*
  > Psa 26:3 For your steadfast love is before my eyes , and I walk in your faithfulness .
- **Psa 31:7** (✓) *target: steadfast love*
  > Psa 31:7 I will rejoice and be glad in your steadfast love , because you have seen my affliction ; you have known the distress of my soul ,
- **Psa 31:16** (✓) *target: steadfast love*
  > Psa 31:16 Make your face shine on your servant ; save me in your steadfast love !
- **Psa 31:21** (✓) *target: steadfast love*
  > Psa 31:21 Blessed be the Lord , for he has wondrously shown his steadfast love to me when I was in a besieged city .
- **Psa 32:10** (✓) *target: steadfast love*
  > Psa 32:10 Many are the sorrows of the wicked , but steadfast love surrounds the one who trusts in the Lord .
- **Psa 33:5** (✓) *target: steadfast love*
  > Psa 33:5 He loves righteousness and justice ; the earth is full of the steadfast love of the Lord .
- **Psa 33:18** (✓) *target: steadfast love*
  > Psa 33:18 Behold , the eye of the Lord is on those who fear him, on those who hope in his steadfast love ,
- **Psa 33:22** (✓) *target: steadfast love*
  > Psa 33:22 Let your steadfast love , O Lord , be upon us, even as we hope in you .
- **Psa 36:5** (✓) *target: steadfast love*
  > Psa 36:5 Your steadfast love , O Lord , extends to the heavens , your faithfulness to the clouds .
- **Psa 36:7** (✓) *target: steadfast love*
  > Psa 36:7 How precious is your steadfast love , O God ! The children of mankind take refuge in the shadow of your wings .
- **Psa 36:10** (✓) *target: steadfast love*
  > Psa 36:10 Oh, continue your steadfast love to those who know you, and your righteousness to the upright of heart !
- **Psa 40:10** (✓) *target: steadfast love*
  > Psa 40:10 I have not hidden your deliverance within my heart ; I have spoken of your faithfulness and your salvation ; I have not concealed your steadfast love and your faithfulness from the great congregation .
- **Psa 40:11** (✓) *target: steadfast love*
  > Psa 40:11 As for you , O Lord , you will not restrain your mercy from me; your steadfast love and your faithfulness will ever preserve me !
- **Psa 42:8** (✓) *target: steadfast love*
  > Psa 42:8 By day the Lord commands his steadfast love , and at night his song is with me, a prayer to the God of my life .
- **Psa 44:26** (✓) *target: steadfast love*
  > Psa 44:26 Rise up ; come to our help ! Redeem us for the sake of your steadfast love !
- **Psa 48:9** (✓) *target: steadfast love*
  > Psa 48:9 We have thought on your steadfast love , O God , in the midst of your temple .
- **Psa 51:1** (✓) *target: steadfast love*
  > To the choirmaster . A Psalm of David , when Nathan the prophet went to him, after he had gone in to Bathsheba . Psa 51:1 Have mercy on me, O God , according to your steadfast love ; according to your abundant mercy blot out my transgressions .
- **Psa 52:1** (✓) *target: steadfast love*
  > To the choirmaster . A Maskil of David , when Doeg , the Edomite , came and told Saul , “ David has come to the house of Ahimelech .” Psa 52:1 Why do you boast of evil , O mighty man ? The steadfast love of God endures all the day .
- **Psa 52:8** (✓) *target: steadfast love*
  > Psa 52:8 But I am like a green olive tree in the house of God . I trust in the steadfast love of God forever and ever .
- **Psa 57:3** (✓) *target: steadfast love*
  > Psa 57:3 He will send from heaven and save me; he will put to shame him who tramples on me. Selah God will send out his steadfast love and his faithfulness !
- **Psa 57:10** (✓) *target: steadfast love*
  > Psa 57:10 For your steadfast love is great to the heavens , your faithfulness to the clouds .
- **Psa 59:10** (✓) *target: steadfast love*
  > Psa 59:10 My God in his steadfast love will meet me; God will let me look in triumph on my enemies .
- **Psa 59:16** (✓) *target: steadfast love*
  > Psa 59:16 But I will sing of your strength ; I will sing aloud of your steadfast love in the morning . For you have been to me a fortress and a refuge in the day of my distress .
- **Psa 59:17** (✓) *target: steadfast love*
  > Psa 59:17 O my Strength , I will sing praises to you, for you, O God , are my fortress , the God who shows me steadfast love .
- **Psa 61:7** (✓) *target: steadfast love*
  > Psa 61:7 May he be enthroned forever before God ; appoint steadfast love and faithfulness to watch over him !
- **Psa 62:12** (✓) *target: steadfast love*
  > Psa 62:12 and that to you, O Lord , belongs steadfast love . For you will render to a man according to his work .
- **Psa 63:3** 🔵 (✓) *target: steadfast love*
  > Psa 63:3 Because your steadfast love is better than life , my lips will praise you .
- **Psa 66:20** (✓) *target: steadfast love*
  > Psa 66:20 Blessed be God , because he has not rejected my prayer or removed his steadfast love from me !
- **Psa 69:13** (✓) *target: steadfast love*
  > Psa 69:13 But as for me , my prayer is to you, O Lord . At an acceptable time , O God , in the abundance of your steadfast love answer me in your saving faithfulness .
- **Psa 69:16** (✓) *target: steadfast love*
  > Psa 69:16 Answer me, O Lord , for your steadfast love is good ; according to your abundant mercy , turn to me .
- **Psa 77:8** (✓) *target: steadfast love*
  > Psa 77:8 Has his steadfast love forever ceased ? Are his promises at an end for all time ?
- **Psa 85:7** (✓) *target: steadfast love*
  > Psa 85:7 Show us your steadfast love , O Lord , and grant us your salvation .
- **Psa 85:10** (✓) *target: Steadfast love*
  > Psa 85:10 Steadfast love and faithfulness meet ; righteousness and peace kiss each other.
- **Psa 86:5** (✓) *target: steadfast love*
  > Psa 86:5 For you , O Lord , are good and forgiving , abounding in steadfast love to all who call upon you .
- **Psa 86:13** (✓) *target: steadfast love*
  > Psa 86:13 For great is your steadfast love toward me; you have delivered my soul from the depths of Sheol .
- **Psa 86:15** (✓) *target: steadfast love*
  > Psa 86:15 But you , O Lord , are a God merciful and gracious , slow to anger and abounding in steadfast love and faithfulness .
- **Psa 88:11** (✓) *target: steadfast love*
  > Psa 88:11 Is your steadfast love declared in the grave , or your faithfulness in Abaddon ?
- **Psa 89:1** (✓) *target: steadfast love*
  > A Maskil of Ethan the Ezrahite . Psa 89:1 I will sing of the steadfast love of the Lord forever ; with my mouth I will make known your faithfulness to all generations .
- **Psa 89:2** (✓) *target: love*
  > Psa 89:2 For I said , “Steadfast love will be built up forever ; in the heavens you will establish your faithfulness .”
- **Psa 89:14** (✓) *target: steadfast love*
  > Psa 89:14 Righteousness and justice are the foundation of your throne ; steadfast love and faithfulness go before you .
- **Psa 89:24** (✓) *target: steadfast love*
  > Psa 89:24 My faithfulness and my steadfast love shall be with him, and in my name shall his horn be exalted .
- **Psa 89:28** (✓) *target: steadfast love*
  > Psa 89:28 My steadfast love I will keep for him forever , and my covenant will stand firm for him .
- **Psa 89:33** (✓) *target: steadfast love*
  > Psa 89:33 but I will not remove from him my steadfast love or be false to my faithfulness .
- **Psa 89:49** (✓) *target: steadfast love*
  > Psa 89:49 Lord , where is your steadfast love of old , which by your faithfulness you swore to David ?
- **Psa 90:14** (✓) *target: steadfast love*
  > Psa 90:14 Satisfy us in the morning with your steadfast love , that we may rejoice and be glad all our days .
- **Psa 92:2** (✓) *target: steadfast love*
  > Psa 92:2 to declare your steadfast love in the morning , and your faithfulness by night ,
- **Psa 94:18** (✓) *target: steadfast love*
  > Psa 94:18 When I thought , “My foot slips ,” your steadfast love , O Lord , held me up .
- **Psa 98:3** (✓)
  > He has remembered his steadfast love and faithfulness
- **Psa 100:5** (✓)
  > For the LORD is good;
- **Psa 101:1** (✓)
  > I will sing of steadfast love and justice;
_… truncation at 100 verses per directive note 4. Group `536-001` has 82 more relevant verse(s); subsequent groups (if any) not rendered. Full set available on request._


---

## G5544 — chrēstotēs "kindness" (owner R067 goodness, priority 1)

_Rationale per directive: Primary Greek abstract kindness noun — 7 corpus verses — essential_

### A. Term identity and lexical foundation

### G5544 — chrēstotēs "kindness"

**Identity:** mti=886 · ti=925 · language=Greek · status=extracted · md_v=2
**Owner registry:** 067 (goodness)

**Meaning parse** (parser v1.0.0, parsed 2026-03-28T14:07:31): 1 top sense(s) · stems=0 · causative=False · domain_tags=False

**Senses (top-level):**

- `1`: kindness, goodness 
primarily goodness, kindness, gentleness, Rom. 2:4; 11:22(3x); 2Cor. 6:6; Gal. 5:22; Col. 3:12; Tit. 3:4; kindness shown, beneficence, Eph. 2:7; goodness, virtue, Rom. 3:12*

**Root family:** `CHRĒSTO` (Greek) — kindness · _Backfilled 2026-04-09 from wa_term_related_words clustering_

**Related words (3 total):**

- `G5541` chrēsteuomai "be kind"
- `G5542` chrēstologia "smooth talk"
- `G5543` chrēstos "good/kind"

### B. Verse-context groups

### G5544 — 2 active group(s)

**Group `886-001`** (2 related · 1 anchor · 0 set-aside · 3 total · dimension: 11 — Divine-Human Correspondence · confidence: KEYWORD_STRONG · dominant_subject: —)
  - *Term names kindness as God's inner disposition of generous goodwill toward humanity — the divine attribute that leads to repentance, governs judgment and mercy, and is displayed supremely in Christ*

**Group `886-002`** (3 related · 1 anchor · 0 set-aside · 4 total · dimension: 05 — Moral Character · confidence: KEYWORD_WEAK · dominant_subject: —)
  - *Term names kindness as a Spirit-produced inner quality of the believer — the disposition to act with goodness toward others, listed as fruit of the Spirit and garment of the renewed person*

### C. Anchor verses (verbatim)

### G5544 — anchor verses (verbatim)

**Group `886-001`** — anchor verses (1):

- **Rom 11:22** 🔵 (✓) *target: kindness*
  > Rom 11:22 Note then the kindness and the severity of God : severity toward those who have fallen , but God’s kindness to you , provided you continue in his kindness . Otherwise you too will be cut off .

**Group `886-002`** — anchor verses (1):

- **Gal 5:22** 🔵 (✓) *target: kindness*
  > Gal 5:22 But the fruit of the Spirit is love , joy , peace , patience , kindness , goodness , faithfulness ,

### D. All relevant verses (verbatim)

### G5544 — all relevant verses (verbatim)

**Group `886-001`** — all relevant verses (3):

- **Rom 2:4** (✓) *target: kindness*
  > Rom 2:4 Or do you presume on the riches of his kindness and forbearance and patience , not knowing that God’s kindness is meant to lead you to repentance ?
- **Rom 11:22** 🔵 (✓) *target: kindness*
  > Rom 11:22 Note then the kindness and the severity of God : severity toward those who have fallen , but God’s kindness to you , provided you continue in his kindness . Otherwise you too will be cut off .
- **Eph 2:7** (✓) *target: kindness*
  > Eph 2:7 so that in the coming ages he might show the immeasurable riches of his grace in kindness toward us in Christ Jesus .

**Group `886-002`** — all relevant verses (4):

- **Rom 3:12** (✓) *target: good*
  > Rom 3:12 All have turned aside ; together they have become worthless ; no one does good , not even one .”
- **2Cor 6:6** (✓) *target: kindness*
  > 2Cor 6:6 by purity , knowledge , patience , kindness , the Holy Spirit , genuine love ;
- **Gal 5:22** 🔵 (✓) *target: kindness*
  > Gal 5:22 But the fruit of the Spirit is love , joy , peace , patience , kindness , goodness , faithfulness ,
- **Col 3:12** (✓) *target: kindness*
  > Col 3:12 Put on then , as God’s chosen ones , holy and beloved , compassionate hearts , kindness , humility , meekness , and patience ,

---

## H2623 — cha.sid "pious" (owner R103 love, priority 2)

_Rationale per directive: Person characterised by chesed — 33 corpus verses — strongly recommended_

### A. Term identity and lexical foundation

### H2623 — cha.sid "pious"

**Identity:** mti=540 · ti=333 · language=Hebrew · status=extracted · md_v=1
**Owner registry:** 103 (love)

**Meaning parse** (parser v1.0.0, parsed 2026-03-28T15:13:44): 1 top sense(s) · stems=0 · causative=False · domain_tags=False

**Senses (top-level):**

- `1`: faithful, kind, godly, holy one, saint, pious

**Sub-senses (depth > 1): 3 entries**

- `1a` (parent `—`): kind
- `1b` (parent `—`): pious, godly
- `1c` (parent `—`): faithful ones (subst)

**Root family:** `CHESED` () — 

**Related words (12 total):**

- `H2616A` cha.sad "be kind"
- `H2616B` cha.sad "to shame"
- `H2617A` che.sed "kindness"
- `H2617B` che.sed "shame"
- `H2619` cha.sad.yah "Hasadiah"
- `H2624` cha.si.dah "stork"
- `H2616A` cha.sad "be kind"
- `H2619` cha.sad.yah "Hasadiah"
- `H2616B` cha.sad "to shame"
- `H2617B` che.sed "shame"
- `H2617A` che.sed "kindness"
- `H2624` cha.si.dah "stork"

### B. Verse-context groups

### H2623 — 1 active group(s)

**Group `540-001`** (31 related · 2 anchor · 0 set-aside · 33 total · dimension: 05 — Moral Character · confidence: CLAUDE_AI · dominant_subject: HUMAN)
  - *Term names the godly or pious person — one whose inner character is shaped by covenantal faithfulness toward God, set apart for his purposes and preserved by him*

### C. Anchor verses (verbatim)

### H2623 — anchor verses (verbatim)

**Group `540-001`** — anchor verses (2):

- **Psa 4:3** 🔵 (✓) *target: godly*
  > Psa 4:3 But know that the Lord has set apart the godly for himself; the Lord hears when I call to him .
- **Psa 16:10** 🔵 (✓) *target: holy one*
  > Psa 16:10 For you will not abandon my soul to Sheol , or let your holy one see corruption .

### D. All relevant verses (verbatim)

### H2623 — all relevant verses (verbatim)

**Group `540-001`** — all relevant verses (33):

- **Deu 33:8** (✓) *target: godly*
  > Deu 33:8 And of Levi he said , “Give to Levi your Thummim , and your Urim to your godly one , whom you tested at Massah , with whom you quarreled at the waters of Meribah ;
- **1Sa 2:9** (✓) *target: faithful ones*
  > 1Sa 2:9 “He will guard the feet of his faithful ones , but the wicked shall be cut off in darkness , for not by might shall a man prevail .
- **2Sa 22:26** (✓) *target: merciful*
  > 2Sa 22:26 “ With the merciful you show yourself merciful ; with the blameless man you show yourself blameless ;
- **2Ch 6:41** (✓) *target: saints*
  > 2Ch 6:41 “And now arise , O Lord God , and go to your resting place , you and the ark of your might . Let your priests , O Lord God , be clothed with salvation , and let your saints rejoice in your goodness .
- **Psa 4:3** 🔵 (✓) *target: godly*
  > Psa 4:3 But know that the Lord has set apart the godly for himself; the Lord hears when I call to him .
- **Psa 12:1** (✓) *target: godly*
  > To the choirmaster : according to The Sheminith . A Psalm of David . Psa 12:1 Save , O Lord , for the godly one is gone ; for the faithful have vanished from among the children of man .
- **Psa 16:10** 🔵 (✓) *target: holy one*
  > Psa 16:10 For you will not abandon my soul to Sheol , or let your holy one see corruption .
- **Psa 18:25** (✓) *target: merciful*
  > Psa 18:25 With the merciful you show yourself merciful ; with the blameless man you show yourself blameless ;
- **Psa 30:4** (✓) *target: saints*
  > Psa 30:4 Sing praises to the Lord , O you his saints , and give thanks to his holy name .
- **Psa 31:23** (✓) *target: saints*
  > Psa 31:23 Love the Lord , all you his saints ! The Lord preserves the faithful but abundantly repays the one who acts in pride .
- **Psa 32:6** (✓) *target: godly*
  > Psa 32:6 Therefore let everyone who is godly offer prayer to you at a time when you may be found ; surely in the rush of great waters , they shall not reach him.
- **Psa 37:28** (✓) *target: saints*
  > Psa 37:28 For the Lord loves justice ; he will not forsake his saints . They are preserved forever , but the children of the wicked shall be cut off.
- **Psa 43:1** (✓) *target: ungodly*
  > Psa 43:1 Vindicate me, O God , and defend my cause against an ungodly people , from the deceitful and unjust man deliver me !
- **Psa 50:5** (✓) *target: faithful ones*
  > Psa 50:5 “ Gather to me my faithful ones , who made a covenant with me by sacrifice !”
- **Psa 52:9** (✓) *target: godly*
  > Psa 52:9 I will thank you forever , because you have done it. I will wait for your name , for it is good , in the presence of the godly .
- **Psa 79:2** (✓) *target: faithful*
  > Psa 79:2 They have given the bodies of your servants to the birds of the heavens for food , the flesh of your faithful to the beasts of the earth .
- **Psa 85:8** (✓) *target: saints*
  > Psa 85:8 Let me hear what God the Lord will speak , for he will speak peace to his people , to his saints ; but let them not turn back to folly .
- **Psa 86:2** (✓) *target: godly*
  > Psa 86:2 Preserve my life , for I am godly ; save your servant , who trusts in you— you are my God .
- **Psa 89:19** (✓) *target: godly one*
  > Psa 89:19 Of old you spoke in a vision to your godly one , and said : “I have granted help to one who is mighty ; I have exalted one chosen from the people .
- **Psa 97:10** (✓) *target: saints*
  > Psa 97:10 O you who love the Lord , hate evil ! He preserves the lives of his saints ; he delivers them from the hand of the wicked .
- **Psa 116:15** (✓) *target: saints*
  > Psa 116:15 Precious in the sight of the Lord is the death of his saints .
- **Psa 132:9** (✓) *target: saints*
  > Psa 132:9 Let your priests be clothed with righteousness , and let your saints shout for joy .
- **Psa 132:16** (✓) *target: saints*
  > Psa 132:16 Her priests I will clothe with salvation , and her saints will shout for joy .
- **Psa 145:10** (✓) *target: saints*
  > Psa 145:10 All your works shall give thanks to you, O Lord , and all your saints shall bless you !
- **Psa 145:13** (✓) *target: kind*
  > Psa 145:13 Your kingdom is an everlasting kingdom , and your dominion endures throughout all generations . [The Lord is faithful in all his words and kind in all his works . ]
- **Psa 145:17** (✓) *target: kind*
  > Psa 145:17 The Lord is righteous in all his ways and kind in all his works .
- **Psa 148:14** (✓) *target: saints*
  > Psa 148:14 He has raised up a horn for his people , praise for all his saints , for the people of Israel who are near to him. Praise the Lord !
- **Psa 149:1** (✓) *target: godly*
  > Psa 149:1 Praise the Lord ! Sing to the Lord a new song , his praise in the assembly of the godly !
- **Psa 149:5** (✓) *target: godly*
  > Psa 149:5 Let the godly exult in glory ; let them sing for joy on their beds .
- **Psa 149:9** (✓) *target: godly ones*
  > Psa 149:9 to execute on them the judgment written ! This is honor for all his godly ones . Praise the Lord !
- **Pro 2:8** (✓) *target: saints*
  > Pro 2:8 guarding the paths of justice and watching over the way of his saints .
- **Jer 3:12** (✓) *target: merciful*
  > Jer 3:12 Go , and proclaim these words toward the north , and say , “‘ Return , faithless Israel , declares the Lord . I will not look on you in anger , for I am merciful , declares the Lord ; I will not be angry forever .
- **Mic 7:2** (✓) *target: godly*
  > Mic 7:2 The godly has perished from the earth , and there is no one upright among mankind ; they all lie in wait for blood , and each hunts the other with a net .

---

## H2616A — cha.sad "be kind" (owner R023 compassion, priority 2)

_Rationale per directive: Verbal root of chesed — 2 corpus verses — recommended_

### A. Term identity and lexical foundation

### H2616A — cha.sad "be kind"

**Identity:** mti=1635 · ti=4102 · language=Hebrew · status=extracted_thin · md_v=1
**Owner registry:** 023 (compassion)

**Meaning parse** (parser v1.0.0, parsed 2026-03-26T14:01:11): 1 top sense(s) · stems=0 · causative=False · domain_tags=False

**Senses (top-level):**

- `1`: to be good, be kind

**Sub-senses (depth > 1): 1 entries**

- `1a` (parent `—`): (Hithpael) to show kindness to oneself

**Root family:** `CHASAD` (Hebrew) — shame · _Backfilled 2026-04-09 from wa_term_related_words clustering_

**Related words (6 total):**

- `H2616B` cha.sad "to shame"
- `H2617A` che.sed "kindness"
- `H2617B` che.sed "shame"
- `H2619` cha.sad.yah "Hasadiah"
- `H2623` cha.sid "pious"
- `H2624` cha.si.dah "stork"

### B. Verse-context groups

### H2616A — 1 active group(s)

**Group `1635-001`** (1 related · 1 anchor · 0 set-aside · 2 total · dimension: 11 — Divine-Human Correspondence · confidence: CLAUDE_AI · dominant_subject: NONE)
  - *Term names the responsive quality of inner covenantal mercy — the faithfulness of character that draws out corresponding faithfulness from God*

### C. Anchor verses (verbatim)

### H2616A — anchor verses (verbatim)

**Group `1635-001`** — anchor verses (1):

- **2Sa 22:26** 🔵 (✓) *target: merciful*
  > 2Sa 22:26 “ With the merciful you show yourself merciful ; with the blameless man you show yourself blameless ;

### D. All relevant verses (verbatim)

### H2616A — all relevant verses (verbatim)

**Group `1635-001`** — all relevant verses (2):

- **2Sa 22:26** 🔵 (✓) *target: merciful*
  > 2Sa 22:26 “ With the merciful you show yourself merciful ; with the blameless man you show yourself blameless ;
- **Psa 18:25** (✓) *target: merciful*
  > Psa 18:25 With the merciful you show yourself merciful ; with the blameless man you show yourself blameless ;

---

## Completion Confirmation

**Query 1 — term identity confirmed (OWNER row, status IN ('extracted','extracted_thin')):**

| Strong's | Owner reg | Word | Status |
|---|---:|---|---|
| H2617A | 103 | love | extracted |
| G5544 | 067 | goodness | extracted |
| H2623 | 103 | love | extracted |
| H2616A | 023 | compassion | extracted_thin |

**Query 2 — group counts per term (active groups; counts via wa_dimension_index):**

| Strong's | Active groups | Total related | Total anchors |
|---|---:|---:|---:|
| H2617A | 3 | 228 | 6 |
| G5544 | 2 | 5 | 2 |
| H2623 | 1 | 31 | 2 |
| H2616A | 1 | 1 | 1 |

**Query 3 — anchor verse rows per term (verse_context.is_anchor=1, not delete_flagged):**

| Strong's | Anchor verse rows |
|---|---:|
| H2617A | 6 |
| G5544 | 2 |
| H2623 | 2 |
| H2616A | 1 |

**Query 4 — file written:** see footer for path + byte size.

