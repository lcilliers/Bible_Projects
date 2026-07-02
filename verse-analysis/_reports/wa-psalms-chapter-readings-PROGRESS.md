# Psalms — chapter-driven inner-being readings: PROGRESS TRACKER

> Living tracker for the poetic chapter-driven pipeline over the Psalter. Update after each psalm. Method: `Workflow/Instructions/wa-verse-analysis-method-v1-20260702.md` §14. Memory: `project_poetic_chapter_driven_method`, `feedback_each_chapter_first_principles_find_the_gems`.

## The pipeline (per chapter, all reusable + parameterised)
1. **Phase 0 — backfill** missing verses: `python scripts/_apply_backfill_chapter_verses_v1_20260702.py --book=Psa --chapter=N --live`
2. **Phase 1 — base lexical**: `python scripts/_apply_poetic_chapter_lexical_v1_20260702.py --book=Psa --chapter=N --live` (writes `ve_lexical`, inspection view `wa-psaN-phase1-lexical-view-*.md`)
3. **Sanity-check** the inspection view (first-principles, per-verse; find the gems — NO templating).
4. **Phase 2 — reading**: write `verse-analysis/_reports/wa-psalmN-inner-being-reading-20260702.md`.
5. **File**: `python scripts/_apply_file_chapter_lexical_prose_v1_20260702.py --book=Psa --chapter=N --story=<path> --heading="Psalm N - inner-being reading" --live` → `prose_section` type `lexical_prose_chapter`.
6. **Commit + push.**

## Done (prose_section ids)
| Ps | id | one-line slant |
|---|---|---|
| 1 | 399 | two ways; delight→meditation roots the tree |
| 2 | 400 | four-voice drama; defiant desire → refuge |
| 3 | 401 | encirclement→rest; assault on hope; sleep amid enemies |
| 4 | 402 | inner self-examination discipline; joy>plenty; peace-that-sleeps |
| 5 | 403 | morning prayer; inner being vs God's moral character; speech reveals corruption |
| 6 | 404 | 1st penitential; whole self undone; turn on "the LORD has heard" |
| 7 | 405 | vindication; God tests hearts; evil gestates within & recoils |
| 8 | 406 | cosmic hymn; contemplation not introspection; worth conferred by divine mindfulness |
| 9 | 407 | acrostic; memory & judgment; remembered vs blotted-out |
| 10 | 408 | interiority of the wicked; "he will never see" vs "but you do see" |
| 11 | 409 | trust as refusing to flee; the sight thread → behold his face |
| 12 | 410 | double heart vs sevenfold-refined word; speech = outflow of inner being |
| 13 | 411 | lament in miniature; fourfold "how long"; pivot on "but I have trusted" |
| 14 | 412 | fool's "no God" as heart posture corrupting conduct; God scans for seekers; universal turning-aside |
| 15 | 413 | entrance liturgy; integrity = truth in the heart, oath kept to own hurt, so never moved |
| 16 | 414 | God as the soul's portion; "no good apart from you"; whole-person joy; fullness of joy in presence |
| 17 | 415 | night-tested purposed heart; apple of eye/shadow of wings; two satisfactions (this-life portion vs "satisfied with your likeness") |
| 18 | 416 | deliverance (50v, sectioned); "I love you"; the reciprocity MIRROR (God met per the disposition brought); gentleness made me great |
| 19 | 417 | two revelations (heavens + word); the word revives/rejoices/enlightens the inner being; hidden faults vs presumptuous sins; "meditation of my heart" |
| 20 | 418 | royal/corporate; what you trust defines & decides you (name vs chariots); the heart's desire brought to God, not grasped |
| 21 | 419 | royal thanksgiving — the ANSWER to Ps 20; the trusting heart is a RECEIVING heart; joy wholly derivative; heart's desire granted; "not moved" rests on trust met by steadfast love; gifts terminate in the Presence |
| 22 | 420 | the forsaken sufferer; trust remembered/from-the-womb/mocked/vindicated; "why forsaken… you do not answer" answered by "he has NOT hidden his face… HAS HEARD" (v.24); melting heart like wax; deliverance generative — "he has done it" |
| 23 | 421 | the inner being at rest in the shepherd's keeping; rest MADE + soul RESTORED (shub nephesh); the He→You turn at the valley; fear answered by presence not removal; chesed that PURSUES (radaph) into settled dwelling |
| 24 | 422 | entrance liturgy — who may ascend + the King of glory; presses past deeds to the SOUL'S AIM ("does not lift his soul to what is false"); righteousness RECEIVED; the face-SEEKER; nasa wordplay (don't lift soul to vanity → lift head to the King) |
| 25 | 423 | acrostic — taught/forgiven/delivered, held by trust + WAITING (qavah); "I lift my soul to you" (counterpoint to 24:4); threefold "remember"; "pardon my guilt FOR IT IS GREAT"; the sod/FRIENDSHIP of the LORD (fear → intimacy); eyes ever toward while heart's troubles ENLARGE |
| 26 | 424 | the inner being that OFFERS ITSELF to be tested ("test my heart and my mind"); confidence grounded in chesed before the eyes, NOT self-righteousness — resolves into "redeem me, be gracious to me" (v.11); company defines the self; love of God's house; the two assemblies frame it |
| 27 | 425 | the ONE THING & the seeking face; fearless confidence + urgent plea held by one desire — "to gaze upon the beauty of the LORD" (v.4); the heart's dialogue "Seek my face"/"Your face I seek" (v.8, desire awakened by God's call); longing & dread of the same face; belief = assurance of future seeing; self commands its own heart to wait |
| 28 | 426 | the dread of divine SILENCE ("if you be silent, I become like those who go down to the pit") answered by "he has HEARD" (v.6); the wicked's split — peace on lips, evil in heart (v.3); the heart's cycle trusts→helped→exults→gives thanks (v.7); personal strength widens to the people's |
| 29 | 427 | storm theophany (least introspective; honestly scoped); worship as ASCRIBING glory/strength; the awed cry "Glory!" (v.9, Ps 8's self-sizing); the gem — power that shatters cedars GIVES the people strength & PEACE (v.11); storm outside → peace inside |
| 30 | 428 | the humbled heart; "not moved" as PRESUMPTION (self-claimed, v.6) vs gift (16:8/21:7) — exposed by the hidden face → dismay (v.7, disciplinary); anger-moment/favor-lifetime, weeping-night/joy-morning (v.5); life is FOR praise (v.9); mourning→dancing, "that my glory may not be silent" (v.12) |
| 31 | 429 | ENTRUSTMENT — "into your hand I commit my spirit" (v.5) + "my times are in your hand" (v.15); two-hands motif (God's vs enemy's); joy grounded in being SEEN & KNOWN (v.7); social death (broken vessel); "But I trust… You are my God" (v.14); hidden IN God's presence from the strife of tongues (v.20); panic-verdict "I am cut off" overturned by "you heard" (v.22); named by all three seats (spirit/soul/heart) |
| 32 | 430 | **[process lens on]** the MECHANICS of concealed vs confessed guilt — silence corrodes the inner being (bones waste, vv.3-4), UNcovering reverses it (you must uncover what you want God to cover, v.5); environment flips (heavy hand → surrounded by chesed); mode of guidance keyed to UNDERSTANDING (counsel vs bit-and-bridle, vv.8-9) |
| 33 | 431 | where the inner being LOCATES confidence (hymn, honestly scoped) — the heart FASHIONED & observed (yatsar+bin, v.15); misplaced confidence in strength = "false hope"/lie (vv.16-17); gladness PRODUCED by trust in the name, not the might (vv.20-22) |
| 34 | 432 | experiential knowing & the shattered inner being (acrostic) — TASTING = knowing by participation (v.8); LOOKING re-forms the face (radiant, v.5); seeking dissolves the inner being's fears (v.4); broken heart/crushed spirit = the LOCUS of nearness (v.18); boasting-faculty redirected (v.2); learnable fear driven by native desire for life (vv.11-12) |
| 35 | 433 | the wound of betrayed RECIPROCITY (imprecation as arena) — evil-for-good registered as a BEREAVEMENT of the soul (shekol, v.12); its depth = prior EMPATHY (mourned for the now-hostile as friend/brother/mother, vv.13-14) → rejoicing-at (asymmetry); praise INTEGRATES the whole self ("all my bones", v.10); two delights defined by object (ruin vs the servant's shalom, vv.25,27) |
| 36 | 434 | two inner ECONOMIES — self-enclosed wicked (transgression ORACLES in the heart v.1; self-flattery "in his own eyes" v.2; the lost "no"/rejecting-faculty gone v.4) vs open-and-fed (fountain of life outside the self; "in your light we see light" — perception DERIVATIVE, vv.7-9); self-lit vs light-receiving sight |
| 37 | 435 | a MANUAL of inner-being self-management (wisdom acrostic) — agitation over the wicked's prosperity is a SELF-KINDLING fire (fret/envy/wrath all M02) that "tends only to evil"; refuse to LIGHT it; replacement ops — DELIGHT reshapes desire (v.4), COMMIT = rolling the weight off the self (galal, v.5), be STILL + wait (v.7); internalised law steadies steps (v.31); wicked's sword recoils into own heart (v.15) |
| 38 | 436 | guilt as a CRUSHING WEIGHT — iniquities "over my head", "too heavy for me", heart in tumult (vv.3-8); drains the inner light (v.10); even the WORDLESS longing/sighing open to God — transparency below speech (v.9); the SELF-SILENCING — deaf/mute, handing the defence to God ("you will answer", vv.13-15) |
| 39 | 437 | TWO SILENCES — suppressed speech converts to inner HEAT (muzzled mouth → heart burns → erupts, vv.1-3; musing/hagah FANS the fire); grasping FINITUDE (self sized as breath/shadow) re-anchors hope (vv.4-7); suppression fails vs acceptance holds ("for it is you who have done it", v.9); plea for RESPITE from the disciplining gaze (v.13) |
| 40 | 438 | the RECEPTIVE & UN-CONCEALING inner being — sustained (doubled qavah) waiting → a GIVEN new song that propagates trust (vv.1-3); the "dug" EAR (God-worked receptivity) → delight-in-will + internalised LAW over sacrifice (vv.6-8); UN-concealing the good in the heart (fourfold, vv.9-10, inverse of guilty concealment); heart FORSAKES the self under iniquity (azab, v.12) |
| 41 | 439 | REGARD & BETRAYAL (closes Book I) — the blessed op of DISCERNING attention to the weak (sakal, v.1); the mask — heart GATHERS iniquity behind empty words (v.6, inverse of un-concealing); betrayal wounds in proportion to prior TRUST (the shared-bread friend, v.9); inferring God's DELIGHT from circumstance ("by this I know", v.11); integrity → set in the presence (v.12) |

| 42 | 440 | the DIALOGICAL inner being — an "I" stands apart from & addresses "my soul" ("why are you cast down… hope in God", vv.5,11), honest self-government (names the state, doesn't deny it); THIRST = appetitive God-desire (vv.1-2); POUR OUT the soul (self-emptying fuelled by memory, v.4); grief COMPOUNDS ("deep calls to deep", v.7); song-in-the-night coexists with the downcast state (v.8) |
| 43 | 441 | resolves 42 — the disoriented self is LED, not self-navigating (light+truth SENT as guides home, v.3); God as EXCEEDING JOY (simchat gili, the gladness of my rejoicing, v.4); the self-government refrain resolved on a destination |
| 44 | 442 | the DECOUPLING of suffering from guilt (corporate lament, scoped) — the FAITHFUL heart ("not turned back", vv.17-19) that suffers anyway [inverts penitential 32/38]; appeal to God's reading of the heart's SECRETS as vindication (v.21); soul bowed to the dust (v.25); protest unresolved = innocent suffering |
| 45 | 443 | (encomium, scoped) heart OVERFLOWS (rachash) into speech — eloquence as the heart's abundance spilling into the tongue (v.1); LOVE & HATE rightly AIMED = ordered character, producing gladness (v.7); REORIENTATION of belonging (forget the father's house, vv.10-11). aheb catch recurs |
| 46 | 444 | FEARLESSNESS decoupled from the world's stability — the self unafraid though the earth is unmade (vv.1-3), NOT MOVED while the mountains move (v.5, stability from an INDWELLING); "be STILL" (raphah = let go/cease striving) as the precondition of KNOWING God — stop → know (v.10) |

| 47 | 445 | (brief enthronement hymn, scoped) JOY enacted through body & voice (clap/shout/sing x5, vv.1,6); a CONFERRED exaltation ("pride of Jacob", gaon) grounded in being LOVED (v.4) — dignity received, not self-generated |
| 48 | 446 | (Zion hymn, scoped) knowledge matures from HEARD to SEEN (v.8); CONTEMPLATION of steadfast love as a temple practice (damah, v.9); considered OBSERVATION oriented to TRANSMISSION (vv.12-14) |
| 49 | 447 | the UN-RANSOMABLE soul — understanding is the OUTPUT of the heart's meditation (vv.3-4); no wealth buys back a life; the fool's trust has no purchase on the inner being's fate (vv.7-9); self-DECEIVES about mortality (false permanence, v.11, inverse of 39); UNDERSTANDING = the beast/man divider (vv.12,20); God RANSOMS the soul wealth could not (v.15) |
| 50 | 448 | true worship & the PROJECTED God — true offering = a POSTURE (thanksgiving + calling/dependence), not provision (vv.14-15,23); the wicked LIKENS God to itself (damah, "you thought I was one like yourself", v.21) — projecting its indifference, misreading silence as likeness; enabled by DISCARDING the word (vv.16-17); corrupt speech follows |
| 51 | 449 | **★ cornerstone** — the RE-CREATION of the inner being's core: sin owned to its ORIGIN (from birth, vv.3-5); God delights in TRUTH in the HIDDEN parts / teaches wisdom in the secret heart (v.6); CREATE (bara) a clean heart — the core cannot be self-repaired, only re-made (v.10); the spirit worked on 3 registers (holy/willing-nadib/broken, vv.11-12,17); the BROKEN & CONTRITE heart is the offering God RECEIVES (vv.16-17, w/ 34:18); re-created joy overflows into teaching/praise (vv.12-15) |

**Next: Psalm 52.**

## Cross-psalm threads emerging (for a later cross-chapter reading)
- **Refuge** as the inner being's safety — Ps 2, 3, 5, 7, 11.
- **Rest granted by God** (sleep/peace) — Ps 3, 4.
- **God sees / attentiveness** — Ps 7 (tests hearts), 10 ("but you do see"), 11 (eyes test), 9 (does not forget).
- **The inner being examined / tested** — Ps 4, 7, 11.
- **Speech reveals the inner being** — Ps 5, 10, 12 (made the whole subject).
- **Being heard** — pleaded (Ps 5) → grasped (Ps 6).
- **Right self-sizing (enosh)** — Ps 8 ("what is man"), 9 ("but men").
- **Behold God's face / satisfaction in presence** — Ps 11:7, 16:11 (fullness of joy), 17:15 ("satisfied with your likeness"), 21:6 (the gifts terminate in "the joy of your presence").
- **What you trust defines & decides you** — Ps 20:7 (name vs chariots), 21:7 (the king trusts → not moved); trust as the inner posture that receives (21) and stands (20). Ties to the "not moved" thread (Ps 15:5, 16:8).
- **The heart's desire brought to God, then granted** — Ps 20:4 (petition: "may he grant you your heart's desire") → 21:2 (answer: "you have given him his heart's desire"); the inner longing entrusted, not grasped, and answered/exceeded (21:4).
- **The word/law acts on the inner being** — Ps 19:7–8 (revives the soul, rejoices the heart, enlightens the eyes); 12:6 (the sevenfold-refined word); inner light rekindled (13:3, 18:28).
- **Hidden vs presumptuous sin; the inner watch on the self** — Ps 19:12–14 ("hidden faults", "presumptuous sins", "the meditation of my heart"); self-examination (Ps 4:4, 17:3).
- **The inner being tested/examined — and *inviting* it** — Ps 7 (God tests hearts), 11 (eyes test), 17:3 (night-tested), 26:2 ("test my heart and my mind" — the self *offered* for assay); teachability (25:4–5,9,12).
- **The fixed gaze — eyes toward God** — Ps 16:8 ("I have set the LORD always before me"), 25:15 ("eyes ever toward the LORD"), 26:3 ("your steadfast love is before my eyes"); attentiveness/dependence.
- **Integrity/penitence both resting on grace** — Ps 25:11 (penitent: "pardon my guilt, for it is great") and 26:11 (integrous: "I shall walk in my integrity; redeem me, be gracious") — opposite postures, same ground: grace, not merit.
- **Fear of the LORD → intimacy, not distance** — Ps 25:14 (the *sod*/friendship of the LORD for those who fear him; he makes known his covenant); the reverent inner being taken into God's confidence.
- **The soul's *aim* / what it lifts itself toward** — Ps 24:4 ("does not lift his soul to what is false") vs 25:1 ("to you I lift up my soul"); the direction of longing defines the inner being (nasa nephesh).
- **Company/"sitting" shapes the inner being** — Ps 1:1 (seat of scoffers), 26:4–5 ("I do not sit with men of falsehood… the assembly of evildoers"); vs the "great assembly" of blessing (26:12).
- **Deliverance is generative; private rescue → public/universal worship** — Ps 22:22–31 ("from you comes my praise"; the afflicted satisfied; ends of the earth turn; "he has done it").
- **Love/longing for God's dwelling-place** — Ps 26:8 ("I love the habitation of your house… where your glory dwells"); 27:4 ("one thing… to dwell in the house of the LORD… to gaze upon the beauty of the LORD") — the peak; 31:20 (hidden IN the cover of God's presence).
- **The seeking/beholding of God's face — its peak & its dread** — Ps 27:4 ("gaze upon the beauty"), 27:8 (the heart's dialogue "Seek my face"/"Your face I seek"); the FACE dreaded hidden (27:9, 30:7) and pleaded to SHINE (31:16, the Aaronic light); the panic "I am cut off from your sight" overturned (31:22).
- **"He has heard" — the dread of silence answered** — Ps 22:24, 28:6 ("he has heard"), 28:1 (dread of God's silence = the pit); the panic-verdict corrected by "you heard" (31:22).
- **"Not moved" — gift vs presumption** — grounded in trust (16:8, 21:7 GIFT) vs self-claimed complacency (30:6 PRESUMPTION), exposed by the hidden face → dismay (30:7).
- **The inner being commits itself / its times into God's hand** — Ps 31:5 ("into your hand I commit my spirit") + 31:15 ("my times are in your hand"); the two-hands motif (God's keeping vs the enemy's grip).
- **Life is FOR praise; the self restored to sing / not be silent** — Ps 30:9,12 ("will the dust praise you?"→"that my glory may not be silent"); 28's non-silence vs God's dreaded silence.
- **The self / community exhorted to be strong, take courage, WAIT** — Ps 27:14 (self-address) → 31:24 (to all the saints); waiting words qavah (25,27) / yachal (31); the heart taking courage.
- **God SEES/KNOWS the inner being's distress — the ground of joy** — Ps 31:7 ("you have known the distress of my soul"); with the God-sees thread (7,10,11).
- **Storm/majesty contemplated → not terror but strength & peace** — Ps 29:11 (the voice that shatters cedars blesses with shalom); 8 (majesty → right self-sizing).
- **[PROCESS LENS from Ps 32]** — the inner-being OPERATION is the finding, God-relation the arena (memory `feedback_lens_is_inner_being_process_not_god_relation`). Operations catalogued so far:
- **Concealment corrodes; uncovering releases** — Ps 32:3-5 (silence → bones waste; you must UNcover what you want covered); the mechanics of suppressed vs confessed guilt.
- **Where the inner being LOCATES confidence determines its state** — Ps 33:16-22 (external strength = "false hope"; gladness produced by trust in the NAME), 20:7, 31:6; misplaced vs relocated confidence.
- **Experiential knowing — the inner being verifies by participation** — Ps 34:8 ("taste and see"); knowing-by-tasting grounds knowing-about.
- **The gaze/attention has a visible output** — Ps 34:5 (looking → radiant face); the direction of attention lights the countenance; sight self-enclosed (36:2 "his own eyes") vs received (36:9 "in your light we see light").
- **The heart is a space that is ADDRESSED; the "no" can be lost** — Ps 36:1 (transgression oracles in the heart where the fear of God should speak), 36:4 (the rejecting-faculty gone, "does not reject evil"); corruption as a SUBTRACTED refusal.
- **The shattered inner being is the LOCUS of nearness** — Ps 34:18 (broken heart/crushed spirit drawn near), with 51:17 (coming); brokenness not distance.
- **Empathy and its betrayal; reciprocity betrayed wounds as bereavement** — Ps 35:12-16 (mourned for the now-hostile as family → rejoicing-at; evil-for-good = shekol of the soul).
- **Delight/desire is defined by its object** — Ps 35:25,27 (soul-desire for ruin vs the LORD's delight in the servant's shalom); 37:4 (coming).
- **Praise integrates the WHOLE self** — Ps 35:10 ("all my bones"), 34 (whole-person); worship not partial.
- **The inner being is fed from OUTSIDE itself** — Ps 36:8-9 (fountain of life, river of delights; life-source external), 23 (led/restored); vs the self-enclosed wicked.
- **God as portion / supreme good vs earthly portion** — Ps 16 ("no good apart from you", "my portion"), 17:14–15 (portion in this life vs God's face).
- **The heart quoted / practical atheism** — Ps 10:4,11 (wicked's heart), 14:1 (fool's "no God"), inverted in 16:7 (heart instructs by night), 4:4 (ponder in your heart).
- **God met per the disposition brought (reciprocity mirror)** — Ps 18:25–27.
- **The inner light rekindled** — Ps 13:3 ("light up my eyes"), 18:28 ("you light my lamp").

## Learned rules now in the Phase-1 script (continuous learning)
- **Role rule:** gate-1 tagged term functioning adverbially (manner/coupling) → process-qualifier, not characteristic.
- **Stop-list (`STOPLIST_NOT_CHARACTERISTIC`):** superscription metadata (*mizmor* H4210, *shir* H7892, *menatseach* H5329) + external-entity adversaries (*enemy* H0341, *foe* H6862) → standalone. Lemma-level (M44 is mixed). Extend as verified lemmas appear.
- **Recurring sanity-check reclassification (NOT rule-ified):** "holy of place" (*holy* H6944 modifying hill/temple) → standalone; left to sanity-check because *holy* can be a genuine inner-being quality elsewhere.

## ⚠ Known Phase-1 residuals (pending script fixes — flagged Ps 21–26, do NOT re-flag from scratch each psalm)
- **`prohibition=forbidden` over-stamp** — fires on *any* negated clause, conflating four cases: plain **negation** ("you do not answer"), **descriptive** ("without wavering"), **habitual resolve** ("I do not sit"), and **jussive-petition** ("remember not"). None but a true imperative-prohibition should set it. **Fix:** gate on verb mood, not the neg particle. (Rule-adjustment candidate.)
- **`bearer=LORD/David` bleed (D11)** — nearest-proper-noun heuristic mis-assigns the bearer to the closest proper noun (usually the LORD) when the true bearer is the speaker/enemy/congregation. Pervasive; subject-agreement not parsed. Readings take bearers from the text.
- **Backfill fragmentary `verse_text`** — Phase-0 backfilled verses store `verse_text` as space-joined word-fragments (Ps 21:12, 22:7/12/21, 24:2, 25:4). Spans intact → readings unaffected, but the verse rows should be repaired (backfill verse_text assembly). Also stray footnote markers (e.g. "^" in 25:21).
- **`nasa` (H5375) grain blur** — single M19 tag spans distinct senses: *lift the soul* (long/aim), *receive/carry*, *lift the head*. Grain-split candidate (memory `project_term_is_sense_not_lemma`).
- **Intensity over-stamp** — *all*/*many*/*very* auto-stamped from quantifier spans; cosmetic.
- **Genuine per-psalm sanity catches still ARE flagged** (e.g. Ps 26:8 *love/aheb* mis-tagged standalone → should be a characteristic). The list above is only the *systemic* residuals to reference compactly, not repeat in full.

## ⚠ SPECIAL HANDLING — Psalm 119 (watch out)
176 verses, 22 acrostic stanzas (8 verses each), the Bible's longest chapter. **Do NOT run the standard single-pass reading.** Plan: backfill + Phase 1 as normal (the mechanical steps scale), but the **Phase-2 reading must be stanza-aware** — read the 22 stanzas (aleph…taw), each turning on the Torah/word vocabulary (law, testimonies, precepts, statutes, commandments, word, promise), and produce a **structured reading** (per-stanza movements → the whole), not one flat essay. Flag to researcher before doing it. Other long psalms to note: Ps 78 (72v), 89 (52v), 105/106/107 (~40+v), 18/104/144 (long).

## Notes
- The `verse`/measure layer is term-sparse (~23,600 of ~31,100 verses); Phase 0 backfill fills chapter gaps from STEP. Many psalms have 1–2 missing verses (often the hinge).
- Each reading is filed DB-canonical (prose_section) + as an .md in `verse-analysis/_reports/`.
