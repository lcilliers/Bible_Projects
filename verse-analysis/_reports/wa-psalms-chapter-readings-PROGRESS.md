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

**Next: Psalm 27.**

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
- **Love/longing for God's dwelling-place** — Ps 26:8 ("I love the habitation of your house… where your glory dwells"); anticipates the "one thing" of Ps 27:4.
- **God as portion / supreme good vs earthly portion** — Ps 16 ("no good apart from you", "my portion"), 17:14–15 (portion in this life vs God's face).
- **The heart quoted / practical atheism** — Ps 10:4,11 (wicked's heart), 14:1 (fool's "no God"), inverted in 16:7 (heart instructs by night), 4:4 (ponder in your heart).
- **God met per the disposition brought (reciprocity mirror)** — Ps 18:25–27.
- **The inner light rekindled** — Ps 13:3 ("light up my eyes"), 18:28 ("you light my lamp").

## Learned rules now in the Phase-1 script (continuous learning)
- **Role rule:** gate-1 tagged term functioning adverbially (manner/coupling) → process-qualifier, not characteristic.
- **Stop-list (`STOPLIST_NOT_CHARACTERISTIC`):** superscription metadata (*mizmor* H4210, *shir* H7892, *menatseach* H5329) + external-entity adversaries (*enemy* H0341, *foe* H6862) → standalone. Lemma-level (M44 is mixed). Extend as verified lemmas appear.
- **Recurring sanity-check reclassification (NOT rule-ified):** "holy of place" (*holy* H6944 modifying hill/temple) → standalone; left to sanity-check because *holy* can be a genuine inner-being quality elsewhere.

## ⚠ SPECIAL HANDLING — Psalm 119 (watch out)
176 verses, 22 acrostic stanzas (8 verses each), the Bible's longest chapter. **Do NOT run the standard single-pass reading.** Plan: backfill + Phase 1 as normal (the mechanical steps scale), but the **Phase-2 reading must be stanza-aware** — read the 22 stanzas (aleph…taw), each turning on the Torah/word vocabulary (law, testimonies, precepts, statutes, commandments, word, promise), and produce a **structured reading** (per-stanza movements → the whole), not one flat essay. Flag to researcher before doing it. Other long psalms to note: Ps 78 (72v), 89 (52v), 105/106/107 (~40+v), 18/104/144 (long).

## Notes
- The `verse`/measure layer is term-sparse (~23,600 of ~31,100 verses); Phase 0 backfill fills chapter gaps from STEP. Many psalms have 1–2 missing verses (often the hinge).
- Each reading is filed DB-canonical (prose_section) + as an .md in `verse-analysis/_reports/`.
