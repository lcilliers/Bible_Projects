# Narrative claim changes

*Published from iba.db on 2026-10-13. Edit the register in the database (`Narrative-Register.ps1`); changes made only in this file are not kept.*

## 2026-10-13 — Psa 116:9 and 1Sa 17:19 removed from the narrative

**Researcher:** just remove 1 Sam 17:19 from the narative, it has no relevance;  Ps 116:9 is also not relevant and can be removed.

**Method:** Ch 2: the Psalm 116 citation ends at verse 8; the quoted words of 116:9 ('I will walk before the Lord in the land of the living') are removed with it. Ch 4: '(17:17-20)' becomes '(17:17-18, 20)'.

**Original claims changed:** No claim text changed.

**Refs:** escalation 2138


## 2026-10-13 — Citation format: Ch 3 Mark and Luke named (#2136)

**Researcher:** 2136 confirm that the citation references has a consistent format throughout the narative that is consistent with the config and verse table

**Method:** After update 132 named Matthew 22:37, the bare (12:30) and (10:27) that follow it took Matthew; the prose names Mark and Luke. Both now name their book. Found by the book-named-between scan after the update.

**Original claims changed:** No claim text changed. Only reference wording.

**Refs:** escalation 2136


## 2026-10-13 — Citation format made consistent (#2136)

**Researcher:** 2136 confirm that the citation references has a consistent format throughout the narative that is consistent with the config and verse table

**Method:** Audit (iba/app/tools/temp_2136_citation_format_audit.py) against style guide section 5, narrative.book_alias_map and the verse table. Corrected: 26 abbreviated or variant book names written in full as the narrative spells them elsewhere (Ch 4, 10.1, 10.10, 12, 14; most in Held sections, reference wording only); the first bare follow-on of 23 paragraphs given its book (Ch 2, 3, 5, 10.4, 10.5, 10.6, 10.7, 10.9, 10.13, 11, 13.1, 14), so the 54 follow-ons that cited nothing in the register now resolve.

**Sources:** outputs/narrative-register/narrative-citation-format-audit-2136-v1-20261013.md

**Scripts:** iba/app/tools/temp_2136_citation_format_audit.py

**Original claims changed:** No claim text changed. Only reference wording.

**Notes:** 'Psalm' (single psalm) and 'Song of Songs' are the narrative's standard forms and are kept.

**Refs:** escalation 2136


## 2026-10-13 — Citations linked to two verses added to the verse table (#2138)

**Researcher:** 2138  add the two verses to the verse table. the link to strong_verse should also be set.

**Method:** Psa 116:9 and 1Sa 17:19 were added to the verse table (iba/app/tools/temp_2138_add_gap_verses.py). Ch 2 and Ch 4 are re-read at their current version (from_version = to_version) so their citations take the new verse ids. No chapter text changed.

**Scripts:** iba/app/tools/temp_2138_add_gap_verses.py

**Original claims changed:** No claim or chapter text changed.

**Refs:** escalation 2138


## 2026-10-13 — Citation corrections (#2136): section pointers and follow-on books

**Researcher:** fix the citation errors in 2136

**Method:** 1. Reference parser (lib/narrativeregister.py _BODY): a chained part followed by '.digit' is a narrative section pointer ('; 10.1'), not a chapter; 49 false whole-chapter citations in 19 chapters are dropped. 2. Bare follow-ons that took the book of the previous reference while the prose named another book: the book is now named in the reference. Found by the unresolved list, a scan for a book named in the prose between a reference and its follow-on, and a check of each follow-on's quote against its resolved verse. Chapters whose text is unchanged are re-read at their current version (from_version = to_version).

**Original claims changed:** No claim text changed. Only reference wording in five chapters.

**Notes:** Text changes: Ch 2 v19 (1 Corinthians 15:45, 15:54, 15:55); Ch 9 v3 (Ephesians 4:23, Ecclesiastes 3:21); 10.10 v24 (Nehemiah 6:8, was read as Acts 6:8); Ch 11 v32 (Proverbs 15:28); 13.1 v24 (Matthew 12:14, Acts 4:28, Matthew 23:38-39, was read as Luke 23:38-39). Not changed: Psa 116:9 (Ch 2) and 1Sa 17:19 (Ch 4) have no verse row (governance.verse_gap_by_design); the references are correct.

**Refs:** escalation 2136


## 2026-10-13 — Strand updates — anger (M02) pairings with strands already read: 14 gaps woven, two corrections (2026-10-13, OT-29/OT-30/OT-51)

**Strand:** anger

**Sources:** ../../Clusters/M02 - anger-wrath/m02-pairing-done-strands-check-v1-20261013.md

**Scripts:** m02-pairing-gaps-weave-v1-20261013.py

**Original claims changed:** **Original claims changed:** two. The 10.13 working note said that the life-and-death verses were "kept for Chapter 2, where that placement is on hold". OT-08 was closed on 2026-10-09 and Chapter 2 already carries Jonah 4:9, so the note is removed. Chapter 5 said that Chapter 2 takes up Proverbs 20:2, but Chapter 2 does not cite it. The pointer now names 10.13 *Other parties*, where the verse is placed.

**Not woven:** **Not woven:** Ezekiel 20:13 and 20:21 are forwarded to OT-01 (life by the statutes), which holds Ezekiel 20:11.

**Notes:** **Researcher, verbatim:** *"proceed as recommended"*, then *"weave the 14 gaps and make the two fixes"*.

**Source:** `../../Clusters/M02 - anger-wrath/m02-pairing-done-strands-check-v1-20261013.md`. The 90 verses that M02 shares with M01, M20, M25 and M64 were checked against the narrative. A verse counted as carried only where the narrative carries the anger and the paired word together. 14 were not carried; each was read in its passage (section 3) and is woven here. Script: `m02-pairing-gaps-weave-v1-20261013.py`.

**Original claims changed:** two. The 10.13 working note said that the life-and-death verses were "kept for Chapter 2, where that placement is on hold". OT-08 was closed on 2026-10-09 and Chapter 2 already carries Jonah 4:9, so the note is removed. Chapter 5 said that Chapter 2 takes up Proverbs 20:2, but Chapter 2 does not cite it. The pointer now names 10.13 *Other parties*, where the verse is placed.

| Section | Added or changed | Verdict |
|---|---|---|
| 10.13 (v8) | *Reading the ruin*: Deu 31:17, God's side beside the people's question. *How it is provoked*: **Known beforehand** (Deu 31:27, 29). *Bearing it*: Lam 2:20, 22 (terrors summoned as to a festival). *How it ends*: **The cup taken back** (Isa 51:17–22). *Shelter, and who can stand*: Zep 2:3; Pro 11:4; Psa 76:7–9. *How it is answered*: Pro 29:8, 11. *Other parties*: Pro 20:2–3 with the ruler's anger; **Those who pursue another** (Job 19:25, 28–29); **The nations** (Rev 11:18). Working note on Chapter 2 "on hold" removed | Added; I read marked; one note removed |
| 10.9 (v22) | *When God hides his face*: the **Sin** bullet widened with Deu 31:16–18 and the people's question; **Time is weighed against it** (Psa 89:46–47); Jer 33:5–6, the hidden face followed at once by healing | Added; I read marked |
| 10.12 (v8) | *Fear before God*: Psa 76:7–9 (fear as stillness); Rev 11:18 (those who fear his name rewarded). *Fear between people*: Pro 20:2–3 | Added |
| 10.4 (v13) | *Where thoughts come from*: a thought answered by God (Eze 20:1, 32–33) | Added |
| 13.1 (v23) | *Ruling*: **His rule answers a thought** (Eze 20:32–37); **His reign, and the nations' rage** (Rev 11:17–18) | Added |
| Ch 2 (v18) | *What death is*: Psa 89:46–47 beside 89:48 | Added |
| Ch 5 (v6) | Pointer for Pro 20:2 corrected from Chapter 2 to 10.13 *Other parties* | Restated |

**Not woven:** Ezekiel 20:13 and 20:21 are forwarded to OT-01 (life by the statutes), which holds Ezekiel 20:11.

**Quote check:** every inserted quotation was checked against the ESV in iba.db: 52 parts, 0 failures.

[Chapter versions, from the narrative index] 02 v18: Psa 89:46–47, M02 pairing gaps, OT-29/30/51; 05 v6: Pro 20:2 pointer corrected to 10.13, M02 pairing gaps, OT-29/30/51; 10.4 v13: Eze 20:32–33, M02 pairing gaps, OT-29/30/51; 10.9 v22: Deu 31:16–18; Psa 89:46–47; Jer 33:5–6, M02 pairing gaps, OT-29/30/51; 10.12 v8: Psa 76:7–9; Rev 11:18; Pro 20:2–3, M02 pairing gaps, OT-29/30/51; 10.13 v8: Deu 31:17, 27–29; Lam 2:20–22; Isa 51:17–22; Zep 2:3; Pro 11:4; Psa 76:7–9; Pro 29:8; Pro 20:2; Job 19:29; Rev 11:18; Chapter 2 hold note removed, M02 pairing gaps, OT-29/30/51; 13.1 v23: *Ruling* gains Eze 20:32–37 and Rev 11:17–18, M02 pairing gaps, OT-29/30/51

**Refs:** thread OT-29, thread OT-30, thread OT-51


## 2026-10-12 — v30: §7 *Authority as a standing* (first reading; title under question, OT-100), M72 group B, #1998

**Notes:** [Chapter versions, from the narrative index] 11 v30: v30: §7 *Authority as a standing* (first reading; title under question, OT-100), M72 group B, #1998

**Refs:** escalation 1998, thread OT-100


## 2026-10-12 — Psa 49:14, 16, M72 group B, #1998

**Notes:** [Chapter versions, from the narrative index] 02 v17: Psa 49:14, 16, M72 group B, #1998; 04 v15: the heart watching power (Ecc 8:9); the boast (Dan 4:30); Act 8:21–22; Judg 9:3; Jer 30:21, M72 group B, #1998; 05 v5: Psa 103:22, M72 group B, #1998; 07 v8: kin used to win rule; Eph 6:12; Jude 8–10, M72 group B, #1998; 08 v7: 1Co 8:9; Rom 13:1 beside 13:5, M72 group B, #1998; 10.1 v20: joy turned (Luk 10:17–21), M72 group B, #1998; 10.3 v7: Num 16:13; Tit 3:3; Gen 42:9, M72 group B, #1998; 10.4 v12: Mat 21:25–27, M72 group B, #1998; 10.6 v22: Simon (Act 8:18–23); Ecc 5:19–20; Gen 37:8, M72 group B, #1998; 10.7 v27: *Convinced that I ought*; *Rule offered, refused, and sought*, M72 group B, #1998; 10.9 v21: new *Kept from what would rule*, *Under rule, and longing for his*, *Knowing who rules*, M72 group B, #1998; 10.10 v23: new *Holding authority over another* and *A right set aside for another*; Lev 25:46–55; 2Sa 23:3; Eph 6:9; Est 9:1, M72 group B, #1998; 10.11 v8: Mat 21:27, M72 group B, #1998; 10.12 v7: Lev 26:17; Luk 12:5; Pilate; fear of the crowd; Jer 51:46; Dan 6:26, M72 group B, #1998; 10.13 v7: Num 16:15; Act 26:10–11, M72 group B, #1998; 12 v20: Dan 4:30 beside 5:20, M72 group B, #1998; 13.1 v22: new section *Ruling*, M72 group B, #1998; 13.2 v5: angels with authority; Jude 6, 9; Hos 12:4; 1Co 11:10, M72 group B, #1998; 13.3 v3: authorities that are not human (Eph 6:12); Luk 10:17–20; Act 19:16; Luk 22:53; Rev 13, M72 group B, #1998; 13.4 v5: lights that rule; creatures under man's dominion, M72 group B, #1998; 14 v15: new *Sin's rule ended* (Rom 6:12–16), M72 group B, #1998

**Refs:** escalation 1998


## 2026-10-12 — Strand updates — desire (M18), group C: will, willing, acceptance, read by role (2026-10-12, #1993 item F)

**Strand:** desire

**Method:** **Method:** `Workflow/Instructions/wa-verse-reading-by-role-guide-v1-20261011.md` (rule 73). Of the 280 verses left after the pull filter, 164 are read in 23 phenomenon groups, 48 are already carried, 29 are marked forward (OT-97), 14 whose act carries no M-code are read by their acts, and 25 are data. Records: `../../Clusters/M18 - desire-longing/m18-group-C-reading-batch1-v1-20261012.md`, `m18-group-C-reading-batch2-3-v1-20261012.md`, `m18-group-C-role-triage-v2-20261012.csv`.

**Sources:** Workflow/Instructions/wa-verse-reading-by-role-guide-v1-20261011.md
../../Clusters/M18 - desire-longing/m18-group-C-reading-batch1-v1-20261012.md
m18-group-C-reading-batch2-3-v1-20261012.md
m18-group-C-role-triage-v2-20261012.csv

**Original claims changed:** **Original claims changed:** none.

**Notes:** **Researcher, verbatim:** *"remove the worktree, then proceed to group C"*; *"continue with batches 2 and 3, then weave all"*.

**Method:** `Workflow/Instructions/wa-verse-reading-by-role-guide-v1-20261011.md` (rule 73). Of the 280 verses left after the pull filter, 164 are read in 23 phenomenon groups, 48 are already carried, 29 are marked forward (OT-97), 14 whose act carries no M-code are read by their acts, and 25 are data. Records: `../../Clusters/M18 - desire-longing/m18-group-C-reading-batch1-v1-20261012.md`, `m18-group-C-reading-batch2-3-v1-20261012.md`, `m18-group-C-role-triage-v2-20261012.csv`.

**Original claims changed:** none.

| Section | Added or changed | Verdict |
|---|---|---|
| 10.7 (v25) | *Willing*: the will asked for; a will redirected; refusals extended (feast, plea, reign, threat, urging; the gall; a finger not lifted; being gathered; a light for a while); wanting to go back; content to stay; Pilate, Felix and Festus; Herod's oath; the will to harm stopped short, Hos 5:11; the willing heart extended (1Ch 29, Ezra, Judg 5:2, Neh 11:2, 2Co 8:10–12, 19); the will made absolute seen from below (Dan 11, Neh 9, Mat 17:12); a will that cannot carry itself out (Rom 7:15–21); doing the will of God. *Planning*: Luk 14:28; Paul's plans under God's will. *What follows a choice*: Esau too late (Heb 12:16–17) | Added; I read marked |
| 10.6 (v20) | *Aimed at God*: wanting to see Jesus; *Unmet*: Luk 16:26; *Wanting and death*: Job 6:8–10 | Added |
| 10.9 (v20) | Psa 145:19; the leper's plea to the will (Mat 8:2–3) | Added |
| 10.10 (v22) | another's will met by giving, and the golden rule (Mat 5:40–42; 7:12; Luk 6:31); Act 14:13–15; Luk 9:53–56; Job 6:28–29 | Added; I read marked |
| 10.11 (v6) | Jesus not able to be hidden (Mar 7:24–25; 9:30–31) | Added |
| 10.12 (v6) | *"Fear not"*: Mar 6:48–50; Joh 6:21 | Added |
| 10.5 (v20) | Mat 27:43 beside Psa 22:8; 1Ti 1:5–7 | Added |
| 10.2 (v16) | willing to receive a word (Mat 11:14–15; Act 17:11–12; 1Ti 1:15); 2Pe 3:3, 5 | Added; I read marked |
| 13.1 (v20) | *Choosing*: Mar 3:13–14; *Willing*: the Son's will in its own words (the leper, Jerusalem, Luk 12:49–50, Joh 17:24, Mat 20:14–15), the Father's will (Rev 4:11, 1Co 12:18, Col 1:27, Gal 1:4, 1Ti 2:4, Mat 18:14); *Delight*: Mat 9:13 and 12:7 with Hos 6:6, what makes an offering accepted, his favor | Added; I read marked |
| 13.2 (v4) | Psa 103:20–21 | Added |
| 13.3 (v2) | first content: the devil's will (Luk 4:6–8; 2Ti 2:25–26) | Added |
| Ch 11 (v28) | §4 *What changes the character*: Whose will, and whether it can carry itself out | Added |

**Quote check:** 201 inserted quotations checked against the ESV in iba.db, 0 failures.

[Chapter versions, from the narrative index] 10.2 v16: willing to receive a word; 2Pe 3:5, M18 group C (will) by role, #1993; 10.5 v20: Mat 27:43; 1Ti 1:5–7, M18 group C (will) by role, #1993; 10.6 v20: wanting to see Jesus; Luk 16:26; Job 6:8–10, M18 group C (will) by role, #1993; 10.7 v25: *Willing* widened (Rom 7:15–21; doing the will of God; the will asked; redirected; going back; Herod; willing heart), Paul's plans, M18 group C (will) by role, #1993; 10.9 v20: Psa 145:19; the leper's plea, M18 group C (will) by role, #1993; 10.10 v22: golden rule; Act 14:13; Luk 9:54; Job 6:28, M18 group C (will) by role, #1993; 10.11 v6: Jesus not able to be hidden, M18 group C (will) by role, #1993; 10.12 v6: Mar 6:48–50; Joh 6:21, M18 group C (will) by role, #1993; 11 v28: §4 whose will, M18 group C (will) by role, #1993; 13.1 v20: the Son's and the Father's will; offerings accepted; his favor, M18 group C (will) by role, #1993; 13.2 v4: Psa 103:20–21, M18 group C (will) by role, #1993; 13.3 v2: first content, the devil's will, M18 group C (will) by role, #1993; **new**, empty

**Refs:** escalation 1993


## 2026-10-12 — Strand updates — desire (M18) × authority (M72): the 51 never-read shared verses, read by role (2026-10-12, #1993 item H)

**Strand:** desire

**Method:** **Method:** `Workflow/Instructions/wa-verse-reading-by-role-guide-v1-20261011.md` (rule 73). Of the 182 shared verses, 131 were decided earlier in the M18 strand. The 51 never read: 6 read, 8 carried, 8 read by their acts, 23 forward (OT-97; seven to M72 itself, OT-98), 6 data. Records: `../../Clusters/M18 - desire-longing/m18-m72-shared-reading-v1-20261012.md`, `m18-m72-shared-triage-v2-20261012.csv`.

**Sources:** Workflow/Instructions/wa-verse-reading-by-role-guide-v1-20261011.md
../../Clusters/M18 - desire-longing/m18-m72-shared-reading-v1-20261012.md
m18-m72-shared-triage-v2-20261012.csv

**Original claims changed:** **Original claims changed:** none.

**Notes:** **Researcher, verbatim:** *"next the M18 strand overview, item F, lists M72 (Authority & Dominion), which shares 182 verses with M18, as recorded so it isn't lost."*; *"weave §9 as proposed"*.

**Method:** `Workflow/Instructions/wa-verse-reading-by-role-guide-v1-20261011.md` (rule 73). Of the 182 shared verses, 131 were decided earlier in the M18 strand. The 51 never read: 6 read, 8 carried, 8 read by their acts, 23 forward (OT-97; seven to M72 itself, OT-98), 6 data. Records: `../../Clusters/M18 - desire-longing/m18-m72-shared-reading-v1-20261012.md`, `m18-m72-shared-triage-v2-20261012.csv`.

**Original claims changed:** none.

| Section | Added or changed | Verdict |
|---|---|---|
| 10.7 (v26) | *Whose measure*: "The king's pleasure, asked for" (Neh 2:4–8; Est 1:17–19; 5:3–4; 9:12–13; 7:3); *Others around a choice*: Mal 2:17–3:2 beside Isa 58:2 | Added; I read marked |
| 13.1 (v21) | *Delight*: "His delight claimed for evildoers" (Mal 2:17; 3:3) | Added |
| 10.6 (v21) | *Coveting*: David (2Sa 11:1–4; 12:9), no desire word named; *Wanting speaks, and drives thinking*: 2Sa 18:27, 29, 33 | Added; I read marked |
| 10.11 (v7) | *Hiding what I hold*: "It can all be shown" (Isa 39:2–6; 2Ki 20:13; 2Ch 32:31) | Added |
| 10.2 (v17) | a refusal to hear standing on a reading of the past (Jer 44:16–18) | Added; I read marked |
| 10.4 (v11) | *It reckons*: Amos 6:1–3 | Added |
| 10.5 (v21) | *Speech is heard*: the chief baker (Gen 40:16, 19); *The oath*: Shimei (1Ki 2:38, 43) | Added |
| Ch 11 (v29) | §1 *Others steal, sway and turn hearts*: Absalom's words (2Sa 15:3) with 15:6 | Changed (words added) |

**Quote check:** 36 inserted quotations checked against the ESV in iba.db, 0 failures.

[Chapter versions, from the narrative index] 10.2 v17: Jer 44:16–18, M18 × M72, #1993 item H; 10.4 v11: Amos 6:2, M18 × M72, #1993 item H; 10.5 v21: Gen 40:16; Shimei 1Ki 2:38, M18 × M72, #1993 item H; 10.6 v21: David 2Sa 11:2–4; 2Sa 18:27, M18 × M72, #1993 item H; 10.7 v26: the king's pleasure, asked for; Mal 3:1, M18 × M72, #1993 item H; 10.11 v7: Hezekiah shows all, M18 × M72, #1993 item H; 11 v29: 2Sa 15:3, M18 × M72, #1993 item H; 13.1 v21: his delight claimed for evildoers (Mal 2:17; 3:3), M18 × M72, #1993 item H

**Refs:** escalation 1993


## 2026-10-12 — Strand updates — authority (M72), group B: current thoughts into Ch 11 §7, and the faculty and other-being parts placed (2026-10-12, #1998)

**Strand:** authority

**Sources:** ../../Clusters/M72 - authority-dominion/m72-group-B-reading-v1-20261012.md
m72-group-B-weave-record-v1-20261012.md

**Original claims changed:** **Original claims changed:** Ch 11 §7's opening, *"Scripture takes the words it uses for ruling … and turns them inward"*, is restated as *"In some verses Scripture takes …"*. The M72 reading found ruling turned inward in a few verses only (Pro 16:32, Gen 4:7, 1Co 7:37, 1Co 6:12), and those join the rule to another act.

**Notes:** **Researcher, verbatim:** *"I suggest you add the current thoughts coming out of the M72 reading to ch_11 and place the parts that is specific to the heart, flesh, divine etc. into those sections. from what I can see at the moment rule, authority, giving or having power is more of a state or status that works in collaboration with other characteristics and parties, but this is not yet strongly emerging from the material you are providing."*

**Source:** `../../Clusters/M72 - authority-dominion/m72-group-B-reading-v1-20261012.md` (275 verses triaged; 81 read in 9 groups). Record: `m72-group-B-weave-record-v1-20261012.md`. The 10.x activity sections are not touched (not instructed).

**Original claims changed:** Ch 11 §7's opening, *"Scripture takes the words it uses for ruling … and turns them inward"*, is restated as *"In some verses Scripture takes …"*. The M72 reading found ruling turned inward in a few verses only (Pro 16:32, Gen 4:7, 1Co 7:37, 1Co 6:12), and those join the rule to another act.

| Section | Added or changed | Verdict |
|---|---|---|
| Ch 11 (v30) | §7: new subsection *Authority as a standing*. Authority given before it is held; what moves inside it (fear, pride, wanting, hatred, conviction and fury, faith, care for another, joy, the fear of God, knowing who rules); Saul and Paul compared; turned round; its limits and whose the ruled are; offered, sought, refused; living under it; ruling within. Held as a first reading; working note (OT-100) | Added; I read marked; opening restated |
| Ch 2 (v17) | Psa 49:14, 16 beside 49:15 | Added |
| Ch 4 (v15) | Ecc 8:9 (the heart watching power); Dan 4:30–31, 26 under *A heart lifted up*; Act 8:19–22; Judg 9:2–3; Jer 30:21 | Added; I read marked |
| Ch 5 (v5) | Psa 103:22 | Added |
| Ch 7 (v8) | Kin used to win rule (Judg 9:2–3, 5); flesh and blood beside the powers (Eph 6:12); Jude 8–10 beside 2Pe 2:10 | Added |
| Ch 8 (v7) | 1Co 8:9 in the weak-conscience bullet; Rom 13:1 beside 13:5 | Added; I read marked |
| 13.1 (v22) | New section *Ruling*: he rules over all; his rule to be known; he gives and takes authority; the Son's authority; the Father's own authority (Act 1:7); the ruler to come, with peace; the soul's answer | Added |
| 13.2 (v5) | Angels with authority, and those who did not keep it (Jude 6); Michael (Jude 9); Hos 12:4; 1Co 11:10 recorded without explanation | Added |
| 13.3 (v3) | Eph 6:12–13; Luk 10:17–20; Act 19:16; Luk 22:53; Rev 13:2, 4; Col 2:15 | Added |
| 13.4 (v5) | Lights that rule (Gen 1:16; Psa 136:8–9); creatures under man's dominion (Gen 1:26; Psa 8:6–7) | Added |

**Quote check:** every inserted quotation was checked against the ESV in iba.db, 0 failures. Three were checked by hand: Pro 16:32, the existing bracketed line; Psa 8:6–7, joined at a comma; and the researcher's own words in the working note.

[Chapter versions, from the narrative index] 11 v31: **retitled *Other sides of the inner being*** and opening restated (a gathering of what has no other home), #1998

**Refs:** escalation 1998


## 2026-10-12 — Strand updates — authority (M72), group B: Ch 11 retitled, and the remaining placements written (2026-10-12, #1998)

**Strand:** authority

**Sources:** ../../Clusters/M72 - authority-dominion/m72-group-B-weave-record-v1-20261012.md

**Scripts:** m72-group-B-weave-activities-v1-20261012.py

**Original claims changed:** **Original claims changed:** Ch 11's title and opening. The title was *"Patterns of the inner life"*, and the opening said *"certain patterns kept coming back"*. Both claimed a link between the sections that the chapter does not establish. They are restated as a gathering of what has no other home.

**Notes:** **Researcher, verbatim:** *"Ch 11 as a whole — the title should not carry any weight in the analysis, it is almost a collection of different inner being elements that does not have another home."* Then: *"'11. Other sides of the inner being' and update the opening paragraph.  you can proceed with writing to the narrative any outstanding parts of M72"*.

**Placement rule:** each verse goes where the act that moves in it belongs. Authority is the standing that act moves in (`../../Clusters/M72 - authority-dominion/m72-group-B-weave-record-v1-20261012.md` §2). Script: `m72-group-B-weave-activities-v1-20261012.py`.

**Original claims changed:** Ch 11's title and opening. The title was *"Patterns of the inner life"*, and the opening said *"certain patterns kept coming back"*. Both claimed a link between the sections that the chapter does not establish. They are restated as a gathering of what has no other home.

| Section | Added or changed | Verdict |
|---|---|---|
| Ch 11 (v31, renamed `11-other-sides-of-the-inner-being`) | Title *Other sides of the inner being*; opening restated; §7 working note updated | Restated |
| 10.10 (v23) | *The fear of God and the weak*: Lev 25:46, 53, 55; 2Sa 23:3; Eph 6:9. *Fear that arrives with a person*: Est 9:1–2. New **Holding authority over another** (at its worst: Eze 34, Pro 28:15–16, Ecc 8:9; from money, a decree, given to each other; in the church, 1Ti 2:11–14; turned round, Luk 22:24–27, 1Pe 5:2–5, 2Co 1:23–24; under it, Tit 3:1–4, Judg 15:11–12). New **A right set aside for another** (1Co 9:4–19; 2Th 3:9; 1Co 8:9–13; 2Co 10:8–9; 13:9–10) | Added; I read marked |
| 10.9 (v21) | New **Kept from what would rule** (Psa 19:12–13; 119:133–134); **Under rule, and longing for his** (Neh 9:27–28; Psa 106:41, 44; Lam 5:8; Hab 1:13–14; Isa 63:19); **Knowing who rules** (Mat 8:9–10; Hos 8:2, 4; Dan 4:26–27; Psa 8:4, 9; Jer 30:21; Hos 12:4, 6) | Added |
| 10.12 (v7) | Lev 26:16–17; Luk 12:5, 7; Pilate's fear and his claim (Joh 19:8–12); fear of the crowd (Mat 21:25–27; Luk 20:6); Jer 51:46; Psa 49:16; Dan 6:23, 26 | Added; I read marked |
| 10.7 (v27) | *Convinced that I ought* (Act 26:9–10, 14); *Rule offered, refused, and sought* (Judg 8:22–23; Dan 5:17; Judg 9:2–3, 5) | Added |
| 10.6 (v22) | Simon (Act 8:18–23); Ecc 5:19–20; Gen 37:8; 42:6, 9 | Added |
| 10.4 (v12) | answers weighed by their cost (Mat 21:25–27) | Added |
| 10.11 (v8) | an answer held back (Mat 21:27) | Added |
| 10.3 (v7) | Num 16:13; Tit 3:1, 3; Gen 42:9 | Added |
| 10.1 (v20) | joy turned (Luk 10:17, 20–21) | Added |
| 10.13 (v7) | Num 16:15; Act 26:10–11 | Added |
| Ch 12 (v20) | Dan 4:30–31, 26 beside 5:20 | Added |
| Ch 14 (v15) | New **Sin's rule ended** (Rom 6:12–14, 16) | Added; I read marked |

**Quote check:** every inserted quotation was checked against the ESV in iba.db, 0 failures.

**Refs:** escalation 1998


## 2026-10-11 — Strand updates — desire (M18), group B: the 94 remaining bucket-1 verses, read by role (2026-10-11, #1993 item F)

**Strand:** desire

**Method:** **Method:** `Workflow/Instructions/wa-verse-reading-by-role-guide-v1-20261011.md` (rule 73). Triage: 24 read in depth, 43 marked forward (OT-97), 15 whose act carries no M-code read by their acts and placed, 12 data only. Records: `../../Clusters/M18 - desire-longing/m18-group-B-remaining-role-reading-v2-20261011.md`, `m18-group-B-no-carrier-reading-v1-20261011.md`, `m18-group-B-remaining-role-triage-v2-20261011.csv`.

**Sources:** Workflow/Instructions/wa-verse-reading-by-role-guide-v1-20261011.md
../../Clusters/M18 - desire-longing/m18-group-B-remaining-role-reading-v2-20261011.md
m18-group-B-no-carrier-reading-v1-20261011.md
m18-group-B-remaining-role-triage-v2-20261011.csv

**Original claims changed:** **Original claims changed:** none. **Correction in the record:** the reading v1 said Isa 58:13 uses one word twice with opposite objects; "pleasure" is *ḥēpheṣ* and the Sabbath "delight" is *ʿōneg*. Corrected in reading v2; nothing woven from it.

**Notes:** **Researcher, verbatim:** *"you will not blanketly read every verse, but will optimise the reading by first assessing the status of the M18 M-code, if it is supportive, for another cluster's reading then the reading is marked forward for when that cluster is read, else if the M-code is central to the verse, then read in in deapth and in context."* Then: *"read the 15 now as recommended, then proceed with the weave"*.

**Method:** `Workflow/Instructions/wa-verse-reading-by-role-guide-v1-20261011.md` (rule 73). Triage: 24 read in depth, 43 marked forward (OT-97), 15 whose act carries no M-code read by their acts and placed, 12 data only. Records: `../../Clusters/M18 - desire-longing/m18-group-B-remaining-role-reading-v2-20261011.md`, `m18-group-B-no-carrier-reading-v1-20261011.md`, `m18-group-B-remaining-role-triage-v2-20261011.csv`.

**Original claims changed:** none. **Correction in the record:** the reading v1 said Isa 58:13 uses one word twice with opposite objects; "pleasure" is *ḥēpheṣ* and the Sabbath "delight" is *ʿōneg*. Corrected in reading v2; nothing woven from it.

| Section | Added or changed | Verdict |
|---|---|---|
| 10.1 (v19) | *On God's word*: beside meditating (Psa 1:1–2), under pressure (Psa 119:23–24, 92–93, 143), joined to doing (Psa 40:6–8); *In a person*: Psa 16:2–4; measure table +12 rows | Added; I read marked |
| 10.5 (v19) | the vow and the mouth (Ecc 5:2–7) | Added; I read marked |
| 10.6 (v19) | the good eye (Pro 22:9; 23:6); life itself pleasant (Ecc 11:7–9); concern that stops at death (Job 21:19–21); coveting as a fair offer (1Ki 21:2–4); passions in prayer (Jam 4:2–3) | Added; I read marked |
| 10.7 (v24) | Eli yielding (1Sa 3:17–18); Balaam turning (Num 24:1–2); *Whose measure*: 1Sa 14:36–40, Est 3:9–11 and 8:8; *Choosing together*: 1Ch 13:2–4; *A choice that is honoured*: Gen 20:15–16; *Fear and choosing*: 2Ki 10:4–6 | Added |
| 10.9 (v19) | *Waiting, and pleading*: Psa 90:13–17 | Added |
| 10.10 (v21) | *Loyalty and honour*: 2Sa 3:36–37; 2Sa 19:18–30; Gen 19:7–9 | Added; I read marked |
| 10.11 (v5) | *Hiding what I hold*: 1Sa 11:9–11 | Added; I read marked |
| 13.1 (v19) | *Purposing*: his purpose spoken and carried out by another (Isa 44:26–28; 46:9–11; 48:14, referent crux recorded); *Delight*: not from those who put something else in the place of hearing (1Sa 15:21–22; Mal 1:6–10; Ecc 5:4), Psa 135:5–6, Balaam (Num 24:1), delight at creation (Pro 8:22, 29–31) | Added; I read marked |
| Ch 11 (v27) | §4 *Delight*: *ḥēpheṣ* as purpose and as what a man cares for; new face *Good, said of the eye*; *Whose eyes, and whose delight*: "what seems good to you" across six settings | Added |

**Quote check:** 86 inserted quotations checked against the ESV in iba.db, 0 failures.

[Chapter versions, from the narrative index] 10.1 v19: delight beside meditating, under pressure, joined to doing; Psa 16:3; measure table +12, M18 group B remaining 94 by role, #1993; 10.5 v19: the vow and the mouth (Ecc 5:2–7), M18 group B remaining 94 by role, #1993; 10.6 v19: good eye; Ecc 11:7–9; Job 21:21; 1Ki 21:2; Jam 4:3, M18 group B remaining 94 by role, #1993; 10.7 v24: Eli; Balaam; 1Sa 14; Esther 3 and 8; 1Ch 13; Gen 20:15; 2Ki 10:5, M18 group B remaining 94 by role, #1993; 10.9 v19: Psa 90:13–17, M18 group B remaining 94 by role, #1993; 10.10 v21: 2Sa 3:36; 2Sa 19:18–30; Gen 19:8, M18 group B remaining 94 by role, #1993; 10.11 v5: words of surrender (1Sa 11:9–11), M18 group B remaining 94 by role, #1993; 11 v27: §4 delight faces; "what seems good to you", M18 group B remaining 94 by role, #1993; 13.1 v19: *Purposing* Isa 44, 46, 48; *Delight* 1Sa 15:22, Mal 1:10, Ecc 5:4, Psa 135:6, Num 24:1, Pro 8:30–31, M18 group B remaining 94 by role, #1993

**Refs:** escalation 1993


## 2026-10-09 — Structure: 10.6 gains the section *Coveting* (after *Through the eye*). No other structure change.

**Strand:** desire (M18), group A (#1993 item F)

**Refs:** escalation 1993


## 2026-10-09 — Structure: 10.6 given section headings (Through the eye; Aimed at nothing, and enjoyment given; As heat; Wantin

**Strand:** desire (M18) × life and death (M25), and the held items (#1993, #1942)

**Refs:** escalation 1993, escalation 1942


## 2026-10-09 — Jonathan's delight (1Sa 19); the avenger's heat (Deu 19:6); new *Friends, company and care*, #1993, #1942

**Notes:** [Chapter versions, from the narrative index] 10.10 v15: Jonathan's delight (1Sa 19); the avenger's heat (Deu 19:6); new *Friends, company and care*, #1993, #1942

**Refs:** escalation 1993, escalation 1942


## 2026-10-09 — the heart awake (Song 5:2–6); the heart hot (Psa 39:1–4); teaching that speaks on waking (Pro 6:21–22); Hos 7:7, #1993

**Notes:** [Chapter versions, from the narrative index] 04 v14: the heart awake (Song 5:2–6); the heart hot (Psa 39:1–4); teaching that speaks on waking (Pro 6:21–22); Hos 7:7, #1993; 04 v13: Pro 21:1 a heart directed, not a state; Mat 5:28, #1993; 05 v4: M18 × M47 read-back: "exhaustion" restated, each death-wish with its own ground; a life precious; the ransom; the want before God, #1993; 06 v11: 1Sa 16:16, 23; the Spirit instructs, leads and carries (Neh 9:20; Psa 143:10; 2Pe 1:21), #1993; 07 v7: what is done with the desires of the flesh; flesh as an outward mark, #1993; 08 v6: Heb 13:18, #1993; 10.1 v17: *Delight*: **new** *What is found pleasant*; willing because it could not be borne (1Th 3:1), M18 group B set 2, #1993; 10.1 v15: Pro 6:34–35 "tender/hard" restated as a reading, #1993; 10.1 v14: Ecc 7:2; Pro 15:15, #1993; 10.2 v14: hearing stopped at one word (Act 22:18–22); goads and nails (Ecc 12:10–12), #1993; 10.2 v13: the word rare in Samuel's days (1Sa 3:1–9), #1993; 10.2 v12: a famine of hearing (Amo 8:11–13), #1993; 10.2 v11: Pro 17:4, #1993; 10.3 v6: Joh 2:17; Gen 37:11, #1993; 10.4 v10: the centurion (Luk 7:4–9), #1993; 10.4 v9: the lordly price (Zec 11:13; Mat 27:9), #1993; 10.5 v17: long prayers for a pretense, and the widow (Mar 12:38–44), #1993; 10.5 v15: Job 6:2–3, weight and rash words, #1993; 10.5 v13: Psa 45:1; Pro 16:24, #1993; 10.6 v17: Paul’s wish (Act 26:28–29), #1993; 10.6 v12: M18 × M02: Phinehas beside Elijah; Psa 37 and Pro 24 envy answered; jealousy as infancy (1Co 3); Rom 13; where desire ends; Lam 2:4, #1993; 10.7 v22: aims (Rom 15:20; 2Co 5:9; 1Th 4:11), #1993; 10.7 v21: Naaman in *Whose measure*; Luk 15:28; Dan 11:36, #1993; 10.7 v20: Mat 19 (Isaiah 1 "one place" sentence restated); Joh 5:40–44; Ruth's redeemer; 2Ti 3:12; Joh 21:18; 2Ch 19:3; Pro 14:14; Isa 47:13–14, #1993; 10.7 v19: Jer 6:16; Act 7:38-39; willing gifts with joy; a will under another, #1993; 10.8 v6: pressure toward wrong (Psa 125:3–4), #1993; 10.9 v17: sought and not far (Act 17:27); recognised and gone to (Joh 21:7–8), #1993; 10.10 v19: the father and the son’s self-rating (Luk 15:19–22), #1993; 10.10 v18: the visit kept seldom (Pro 25:16–17), #1993; 10.10 v16: Pro 14:35; 2Co 12:20, #1993; 10.11 v4: the guards’ report covered with money (Mat 28:11–15), #1993; 10.12 v5: Exo 14:12, #1993; 11 v26: §4 delight faces: thanks and taunt, an offering refused then delighted in, being well pleased; two *What changes the character* entries, #1993; 11 v23: §4 *tĕšûqāh* and panting, #1993; 11 v20: §2 Ecc 9:7, #1993; 12 v18: Eze 28:13–17, #1993; 12 v17: Eze 31:9–10, #1993; 12 v16: Psa 5:9; Isa 44:9, #1993; 12 v15: the idol-maker warmed and deceived (Isa 44:15–20; 47:14), #1993; 12 v14: Pro 16:19, #1993; 13.1 v17: *Delight*: the voice on the mountain; his good pleasure gives; not pleased though they shared it all; Heb 10:5–10, #1993; 13.1 v13: *What he desires*; Deu 7:7, 10:15, #1993; 13.1 v12: *Jealousy* widened from the M18 × M02 read-back; Mic 7:18, Isa 60:10, Rom 9:22, #1993; 13.2 v2: first content, 1Pe 1:12, #1993; **new**, empty; 13.4 v3: Joe 1:20; Ecc 1:5, #1993

**Refs:** escalation 1993


## 2026-10-09 — "not far from the kingdom" (Mar 12:34), #1993; was Ch 2, renumbered 2026-10-02, #1936

**Notes:** [Chapter versions, from the narrative index] 03 v3: "not far from the kingdom" (Mar 12:34), #1993; was Ch 2, renumbered 2026-10-02, #1936

**Refs:** escalation 1993, escalation 1936


## 2026-10-09 — Hezekiah's plea; "see good" (Psa 34:12, Job 7:7); Exo 14:12; Pro 8:35–36. OT-08 closed, #1993

**Notes:** [Chapter versions, from the narrative index] 02 v15: Hezekiah's plea; "see good" (Psa 34:12, Job 7:7); Exo 14:12; Pro 8:35–36. OT-08 closed, #1993

**Refs:** escalation 1993, thread OT-08


## 2026-10-09 — Strand updates — desire (M18) × life and death (M25), and the held items (2026-10-09, #1993, #1942)

**Strand:** desire

**Sources:** ../../Clusters/M18 - desire-longing/m18-m25-validation-register-v1-20261009.csv
m18-m25-inner-being-reading-v1-20261009.md
m18-held-items-reading-v1-20261009.md

**Original claims changed:** **Original claims changed:** none. **Narrative sentences restated:**
- **10.7 *Willing*: Restated.** "Isaiah 1 is the one place in these verses where the will is invited with an 'if'" is no longer true. Mat 19:17, 21 is a second place.
- **13.1 *Willing*: Restated.** "the one place in these verses where two wills are named side by side" is no longer true. Joh 6:38 names the same thing, outside Gethsemane.
- **10.9 *Calling on God to wake*: Restated** from a summary ("In Psalms 7, 35, 44 and 59 the call comes where the psalmist's life is sought") into the ground each call gives (innocence, a cause, suffering for his sake, no fault, his office, his past). Each ground is quoted.

**Notes:** **Researcher, verbatim:** *"always remember that the narration must be done from the perspective of the inner being workings - merely restating the verse is not a proper narration, thinking about the item and asking probing questions in important : compare, why different, what lies behind it; does the relationships make a difference; and other probing; it is especially important to not just restate figurative speach but explore it."* Then: *"OT-08 is no longer relavant … OT-95 just read these verses … OT-15 why are you holding this? … why is H5782 not properly completed. complete all these accumulating outstanding items, then update M25-M18 findings into the narrative as per your findings and then proceed with M02"*.

**Source:**
- the 89 M18 × M25 verses not already done with M47, one decision per verse: `../../Clusters/M18 - desire-longing/m18-m25-validation-register-v1-20261009.csv` (report `.md`)
- the probing reading: `m18-m25-inner-being-reading-v1-20261009.md`
- the held items: `m18-held-items-reading-v1-20261009.md`. These are jealousy (10 verses), *ṭôb* (10), H2552 (19) and H5782/H6974 (50).

**Decisions (M25 read-back):** missed and added 26 · new perspective added 12 · error realigned 0 · confirmed 21 · carried by a parallel 8 · no inner-being bearing (route C) 22 · held 0.

**Original claims changed:** none. **Narrative sentences restated:**
- **10.7 *Willing*: Restated.** "Isaiah 1 is the one place in these verses where the will is invited with an 'if'" is no longer true. Mat 19:17, 21 is a second place.
- **13.1 *Willing*: Restated.** "the one place in these verses where two wills are named side by side" is no longer true. Joh 6:38 names the same thing, outside Gethsemane.
- **10.9 *Calling on God to wake*: Restated** from a summary ("In Psalms 7, 35, 44 and 59 the call comes where the psalmist's life is sought") into the ground each call gives (innocence, a cause, suffering for his sake, no fault, his office, his past). Each ground is quoted.

| Section | Added or changed | Verdict |
|---|---|---|
| 10.6 *Wanting* (v11) | sectioned. Through the eye (Gen 2:9; 3:6; Ecc 7:25–26); enjoyment given, set against the rich fool (Ecc 3:11–13; 5:10, 12, 17–20; 6:12; 8:14–15; Luk 12:19–20); heat (Isa 57:4–5); wanting that owns (Tit 3:3–5; 2:11–14; Luk 8:7, 13–15; Pro 23:33–35); unmet (Hag 1:4–6, 14; Isa 29:8; Exo 17:3, 7; Judg 15:18–19; Eze 23:21–22); shaped by fear (Jer 42:11–22; Exo 14:10–13; Num 11:18); wanting life (Psa 34:10–14; 1Pe 3:9–10; Job 7:7); aimed at God (Psa 27:1–10; 16:2–11; 119:37, 40); thirst answered (Joh 4:13–15; 6:26, 34–35; Jer 2:13); a person (Song 2:5, 7; 3:4–5; 5:2–6; 8:1–7); jealousy and envy (1Ki 19:10–18; Num 11:28–29; Psa 73:1–3, 16–22; Pro 23:17–18; Jam 3:13–16; pointers to Pro 14:30, Job 5:2, Pro 6:34–35, 27:4); taken away (Joe 1:5); possessions (Mat 19:20–22; Pro 15:27); delight (Psa 119:75–77; 68:29–31) | Widened; I read marked |
| 13.1 *Divine* (v11) | Delight: no pleasure in death, to accusers and to the despairing (Eze 18:23, 25, 31–32; 33:10–11); death precious (Psa 116:3, 8, 15); Eli's sons (1Sa 2:25–26), tension with Eze 18:32 left standing; favour by finding (Pro 8:34–36). Willing: Joh 5:21; 6:38–40; 21:22–23. **New *Jealousy*** (Eze 36:5–6; Isa 42:13–14; Jam 4:4–6; Eze 8:3–4; Deu 6:15). **New *Stirring*** (Ezr 1:1, 5; 2Ch 36:22; Isa 45:13; 41:25; Hag 1:12–14; 1Ch 5:25–26; 2Ch 21:12–16; Jer 51:1, 11; 50:9; Eze 23:22; Zec 9:13; Joe 3:7; Isa 13:17; Zec 2:13; Psa 78:38). He is good (Lam 3:24–25; Psa 125:4) | Widened; new sections |
| 13.4 *Nature* (v2) | **first content:** God's look on what he made (Gen 1:21, 25, 31); the creatures' thirst met (Psa 104:10–15, 27–28; 42:1; 145:16); the ostrich (Job 39:14–17); Job 39:9 | New |
| 13.2 *Angels* (v3) | an angel wakes a prophet to see (Zec 4:1–2) | Widened |
| 10.7 (v20) | Mat 19:16–26; Joh 5:39–44; Rut 3:10–13, 4:4–6; 2Ti 3:11–12; Joh 21:18–22; 2Ch 19:2–3; Pro 14:13–14; Dan 11:25; Isa 47:13–14 | Widened; one sentence restated |
| 10.9 (v16) | Psa 73:3, 20; new *Waiting, and pleading* (Lam 3:24–26; Isa 38:2–5; 2Ki 20:2–3); calling on God to wake (Psa 7:4–6; 35:23; 44:22–23; 59:4; 80:1–2, 18; Isa 51:9–10, 17; 52:1; 64:7–8; Job 8:6; Psa 57:6–8; Judg 5:12) | Widened; one paragraph restated |
| 10.10 (v15) | 1Sa 19:1–7 with 18:1, 8–9; Deu 19:6; new *Friends, company and care* (Job 6:15–18; Ecc 4:9–11; Job 31:19–20, 29–30; 17:8–9; Pro 10:12; Song 2:7) | Widened |
| Ch 2 (v15) | Isa 38:3, 5; Psa 34:12 with Job 7:7; Exo 14:12; Pro 8:35–36. **OT-08 closed by the researcher; no block on Ch 2** | Widened |
| Ch 4 (v14) | Song 5:2–6; Psa 39:1–4; Pro 6:21–22; Hos 7:7 | Widened |
| Ch 6 (v12) | the stirred spirit: Ezr 1:5; Hag 1:6, 12–14; 1Ch 5:25–26; Jer 51:11 | Widened |
| 10.2 (v10) | Isa 50:4–6; Zec 4:1–2; Jos 23:14–15 | Widened |
| 10.5 (v14) | Psa 39:1–4 | Widened |
| 10.8 (v6) | Psa 125:3–4 | Widened |
| 10.12 (v5) | Exo 14:12 | Widened |
| Ch 11 (v21) | §4: eat, drink, be merry; jealousy; rousing oneself; the redeemer's will; whom the need is spoken to; Haggai's order. §5: Lam 3:24; Psa 57:8; Pro 6:22 | Widened |
| Ch 12 (v15) | Isa 44:15–20; 47:14 | Widened |

**Closed:**
- OT-08, OT-15, OT-95 and OT-96, in the open threads register.
- #1942: all H5782 inner-being hits from unit 4 §E are read and placed, with LD-149 and LD-155.

**Cross-reference note:** two verses counted as "not cited" were already quoted as bare citations (Psa 119:40 in Ch 2; Exo 17:3 in 10.5). Every "not cited" verse was checked by a direct text search before weaving.

**Quote check:** every new quotation was checked against the ESV in iba.db. The only failures left are:
- section titles
- glosses
- the literal Hebrew "while his heart is hot", marked as such
- quotations that span two verses, each of which was checked separately
- flags that were already there before this pass

[Chapter versions, from the narrative index] 06 v12: the stirred spirit, toward building and destroying (Haggai 1), #1942; 10.2 v10: the woken ear (Isa 50:4–6; Zec 4:1–2); knowing in heart and soul (Jos 23:14–15), #1993, #1942; 10.5 v14: silence held too long, the heart hot (Psa 39:1–4), #1993; 10.6 v11: **sectioned**; M18 × M25 read-back and the held items: through the eye (Gen 3:6), enjoyment given against the rich fool, wanting that owns, shaped by fear, wanting life, aimed at God, thirst answered, a person (Song), **jealousy and envy**, possessions, #1993; 10.9 v16: envy undone in the sanctuary (Psa 73); new *Waiting, and pleading*; *Calling on God to wake* given its grounds and Isaiah's answer, #1993, #1942; 10.13 v6: Gamaliel held in honour (Act 5:34), #1993; 13.1 v11: *Delight* widened (no pleasure in death; Psa 116:15; 1Sa 2:25; Pro 8:35); *Willing* (Joh 5:21; 6:38–40, Gethsemane sentence restated; 21:22); **new *Jealousy* and *Stirring***, #1993, #1942; 13.2 v3: an angel wakes a prophet to see (Zec 4:1–2), #1942

**Refs:** escalation 1993, escalation 1942


## 2026-10-09 — Strand updates — desire (M18) × anger (M02) (2026-10-09, #1993)

**Strand:** desire

**Sources:** ../../Clusters/M18 - desire-longing/m18-m02-validation-register-v1-20261009.csv
m18-m02-inner-being-reading-v1-20261009.md

**Notes:** **Researcher, verbatim:** *"... then proceed with M02"*.

**Source:** 51 M18 × M02 verses, the 59 less 8 done with M47 and M25. They were read beside the anger ledgers (units 1–5, overview v2). Files: `../../Clusters/M18 - desire-longing/m18-m02-validation-register-v1-20261009.csv` (report `.md`) and the reading `m18-m02-inner-being-reading-v1-20261009.md`. **OT-19 closed.**

**Decisions:** missed and added 23 · new perspective 9 · error realigned 1 · confirmed 10 · carried 2 · route C 6 · held 0.

**Narrative sentence restated:**
- **10.1 *When feeling changes character*: Restated.** "Grief makes it tender; jealousy makes it hard" was stated as if the verses said it. They do not. The two joinings are now quoted (Mar 3:5; Pro 6:34–35), and the comparison is marked "I read".

| Section | Added or changed | Verdict |
|---|---|---|
| 13.1 (v12) | *Jealousy*: Deu 32:15–18, 21; Psa 78:58; Eze 16:38, 42–43; 23:25; 5:13; Deu 29:19–20; Zec 8:2–3; Zep 1:18; 3:8–9; Eze 38:19–20; Nah 1:2–3; Psa 79:5–6; Num 25:11. *Delight*: Mic 7:18; Isa 60:10. *Willing*: Rom 9:22–23 | Widened |
| 10.6 (v12) | Num 25:11–13 beside Elijah; Psa 37:1–7; Pro 24:17–20; 1Co 3:1–4 with 1Pe 2:2; Rom 13:11–14; Pro 11:23; Psa 112:9–10; Lam 2:4–5 | Widened |
| 10.7 (v21) | 2Ki 5:11–14 (*Whose measure*); Luk 15:28; Dan 11:36 | Widened |
| 10.10 (v16) | Pro 14:35 with 19:12; 2Co 12:20 | Widened |
| 10.5 (v15) | Job 6:2–3 (listed by the anger ledger as narrated; it was not) | Widened |
| 10.1 (v15) | Pro 6:34–35 restated | Restated |
| Ch 11 (v22) | §6: 2Co 9:2 | Widened |

**Quote check:** every new quotation was checked against the ESV in iba.db. The only failures left are quotations that span two verses (each part checked separately), glosses and headings.

**Refs:** escalation 1993


## 2026-10-09 — Strand updates — desire (M18), group A: desire, craving, longing (2026-10-09, #1993 item F)

**Strand:** desire

**Sources:** ../../Clusters/M18 - desire-longing/m18-group-A-register-v1-20261009.csv
m18-group-A-reading-v1-20261009.md

**Scripts:** m18-group-A-decisions-v1-20261009.py

**Original claims changed:** **Original claims changed:** none.

**Notes:** **Researcher, verbatim:** *"first do a session close and then proceed with F"*; *"10.6 is fine for M18"*.

**Source:** the 258 group A hits, less the verses already decided in the three read-backs, which leaves 151 verses. Files: `../../Clusters/M18 - desire-longing/m18-group-A-register-v1-20261009.csv` (reasons in `m18-group-A-decisions-v1-20261009.py`) and the reading `m18-group-A-reading-v1-20261009.md`.

**Decisions:** missed and added 103 · new perspective 7 · confirmed 12 · carried 5 · route C 24 · held 0.

**Original claims changed:** none.

| Section | Added or changed | Verdict |
|---|---|---|
| 10.6 (v13) | **New *Coveting*** (Exo 20:17; Deu 5:21; Rom 13:9; Jos 7:21 with Gen 3:6; Mic 2:1–2; Rom 7:7–8; Deu 7:25; Pro 12:12; Act 20:33–35). *Through the eye*: Deu 21:11; Eze 23:12, 14; Isa 53:2–4. *As heat*: Jer 5:7–8. *Delight*: Pro 1:22. *Wanting that owns*: the verbs of desire (Rom 6:12; Jude 16; 2Pe 3:3–4; 2Ti 4:3–4; 3:6–7; Eph 4:22; Jam 1:14; Pro 11:6; Gen 4:7; Joh 8:44), and what is set against it (1Th 4:5; 1Pe 1:14; Eph 4:23–24; 1Pe 4:2–3; 1Jo 2:16–17; 2Pe 1:4). *Unmet*: Luk 16:21; 15:16–17; Psa 106:13–15; 78:29–30; Num 11:34; 1Co 10:6. *Evil desire*: Pro 10:24; 18:1; 21:26. *Wanting and death*: Heb 11:15–16; Ecc 12:5. *Aimed at God*: Psa 119:131, 173–174; 19:10; 38:9; Mat 13:17; Luk 17:22–23; Amo 5:18–19; Jer 17:16. *A person*: Paul's longing (2Ti 1:4; Phi 1:7–8; 2:26; 4:1; 1Th 3:6–7; 2Co 9:14; 7:6–7; Rom 15:23); Gen 31:30–31; Song 2:3; 5:16; Pro 19:22; *tĕšûqāh* (Gen 3:16; 4:7; Song 7:10). *Jealousy and envy*: Pro 24:1–2. *Taken away*: Eze 24:16–18; Lam 1:10; Isa 64:11–12; 32:11–12; Amo 5:11; Deu 28:32; Psa 39:11. *Possessions*: 1Ti 6:10; Psa 52:7; Hab 2:9–10; Eze 22:12; Job 20:20; Jer 6:13–14; Pro 23:2–7; 21:20 | Widened; new section; I read marked |
| 13.1 (v13) | *Delight*: new item *What he desires* (Psa 132:13–14; 68:16; Jer 3:19–20; 12:10–11; Isa 27:2–4; Psa 91:14; Exo 34:24; Hag 2:7–8; Hos 10:10; Luk 22:15; Job 14:15). *Choosing*: Deu 7:7–8; 10:15–16 | Widened |
| 13.4 (v3) | Joe 1:20; Ecc 1:5 | Widened |
| 10.7 (v22) | *Setting the heart*: aims (Rom 15:20; 2Co 5:9–10; 1Th 4:11; 1Ti 3:1) | Widened |
| Ch 11 (v23) | §4: *tĕšûqāh*; panting (Job 7:2; 5:5; Ecc 1:5; Jer 2:24; Psa 119:131; Isa 42:14) | Widened |
| Ch 12 (v16) | Psa 5:9 with Pro 11:6; Isa 44:9 | Widened |
| Ch 2 (v16) | 2Ch 21:20; Job 36:20; Job 7:2–3 | Widened |
| 10.2 (v11) | Pro 17:4 | Widened |

**Quote check:** every new quotation was checked against the ESV in iba.db. The only failures left are quotations that span two verses (each part checked separately), glosses and headings.

[Chapter versions, from the narrative index] 02 v16: 2Ch 21:20; Job 36:20; Job 7:2, M18 group A, #1993; 10.6 v13: M18 group A: **new *Coveting***; the verbs of desire; Paul's longing; *tĕšûqāh*; craving filled and unsatisfied; greed's reasons; what is taken, #1993

**Refs:** escalation 1993


## 2026-10-09 — Strand updates — desire (M18), group D: jealousy, zeal (2026-10-09, #1993 item F)

**Strand:** desire

**Sources:** ../../Clusters/M18 - desire-longing/m18-group-D-register-v1-20261009.csv
m18-group-D-reading-v1-20261009.md

**Scripts:** m18-group-D-decisions-v1-20261009.py

**Original claims changed:** **Original claims changed:** none.

**Notes:** **Researcher, verbatim:** *"proceed with the next section of 1993"*.

**Source:** the 112 group D hits, less the verses already decided in the three read-backs and group A, which leaves 51 verses. Files: `../../Clusters/M18 - desire-longing/m18-group-D-register-v1-20261009.csv` (reasons in `m18-group-D-decisions-v1-20261009.py`) and the reading `m18-group-D-reading-v1-20261009.md`.

**Decisions:** missed and added 37 · confirmed 5 · carried 5 · route C 4 ("Simon the Zealot") · held 0.

**Original claims changed:** none.

| Section | Added or changed | Verdict |
|---|---|---|
| 10.6 (v14) | *Jealousy and envy*: zeal read in (the same words). Zeal that consumes (Psa 69:8–9; 119:139, 141; Joh 2:16–17); zeal without knowledge (Rom 10:1–3; Gal 1:13–16; Phi 3:6–7; Act 22:3–4; 21:20–21); zeal on show and zeal that set aside an oath (2Ki 10:16, 31; 2Sa 21:1–2); jealousy that is God's in a man (2Co 11:2–3); zeal for others and for good (Col 4:12–13; 1Pe 3:13–14; Tit 2:14). New *Jealousy against a person* (Gen 37:4, 11; 26:12–16; Psa 106:16–17 with Num 16:3; Act 5:17–18; 13:45; Eze 31:9–10; Isa 11:12–13). Ecc 9:6. New *A husband's jealousy with no witness* (Num 5:14–15, 30–31; Pro 6:35) | Widened; I read marked |
| 13.1 (v14) | *Jealousy*: his name in the commandment (Exo 20:5–6; Deu 5:9–10; Exo 34:14; Deu 4:23–24); 1Ki 14:22; Zec 1:12–16; roused by prayer, joined to pity (Joe 2:17–18; Eze 39:25–26); zeal that does the work (Isa 9:7; 2Ki 19:30–31; Isa 37:31–32); put on when no one stood (Isa 59:16–17); Heb 10:26–27; missed and asked to be seen (Isa 63:15; 26:11). Closing reading widened | Widened |
| 10.3 (v6) | Joh 2:17; Gen 37:11 | Widened |
| Ch 11 (v24) | §4 *Whose jealousy, and for whom*: zeal faces and jealousy against a person | Widened |
| Ch 12 (v17) | *Pride*: Eze 31:9–10 | Widened |

**Quote check:** 66 inserted quotations checked against the ESV in iba.db, 0 failures. Two bare citations that followed an Acts citation now name Philippians and Galatians.

[Chapter versions, from the narrative index] 10.6 v14: M18 group D: zeal read into *Jealousy and envy*; **new** *Jealousy against a person* and *A husband's jealousy with no witness*, #1993; 11 v24: §4 zeal and jealousy against a person, #1993; 11 v22: §6 zeal passes on (2Co 9:2), #1993; 13.1 v14: *Jealousy* widened from M18 group D: his name in the commandment, roused by prayer, zeal that does the work, put on as a cloak, #1993

**Refs:** escalation 1993


## 2026-10-09 — Strand updates — desire (M18), group E: thirst, hunger (2026-10-09, #1993 item F)

**Strand:** desire

**Sources:** ../../Clusters/M18 - desire-longing/m18-group-E-register-v1-20261009.csv
m18-group-E-reading-v1-20261009.md

**Scripts:** m18-group-E-decisions-v1-20261009.py

**Original claims changed:** **Original claims changed:** none.

**Notes:** **Researcher, verbatim:** *"proceed with group E"*.

**Source:** the 45 group E hits, less the verses already decided in the three read-backs and groups A and D, which leaves 30 verses. Files: `../../Clusters/M18 - desire-longing/m18-group-E-register-v1-20261009.csv` (reasons in `m18-group-E-decisions-v1-20261009.py`) and the reading `m18-group-E-reading-v1-20261009.md`.

**Decisions:** missed and added 24 · confirmed 3 · carried 1 · route C 2 · held 0.

**Original claims changed:** none.

| Section | Added or changed | Verdict |
|---|---|---|
| 10.6 (v15) | *Thirst answered*: rivers out of the heart (Joh 7:37–39); "I thirst" (Joh 19:28–30; Psa 69:20–21); Mat 5:6; God's answer and its reasons (Isa 41:17; 49:10; Rev 7:16–17); met and forgotten (Neh 9:15–17; Isa 48:21–22); thirst as judgment with its inner ground (Deu 28:47–48; Isa 65:12–14; 5:11–13); want borne for others (1Co 4:11–12; 2Co 11:27–28); Act 10:10–12 | Widened; I read marked |
| 10.10 (v17) | *Friends, company and care*: another's thirst met, refused or used (Mat 25:35, 37, 40, 44; Rut 2:9–10; Jdg 4:19, 21; Lam 4:3–4; Job 24:11–12) | Widened |
| 10.2 (v12) | A famine of hearing (Amo 8:11–13) | Widened |

**Quote check:** 32 inserted quotations checked against the ESV in iba.db, 0 failures.

[Chapter versions, from the narrative index] 10.6 v15: M18 group E: *Thirst answered* widened (rivers out of the heart; "I thirst"; thirst answered, forgotten, and as judgment; want borne for others), #1993; 10.10 v17: another's thirst met, refused or used (Mat 25; Rut 2:9; Jdg 4:19; Lam 4:4; Job 24:11), #1993; 13.4 v2: **first content**: God's look on what he made; the creatures' thirst met; the ostrich, #1993; **new**, empty

**Refs:** escalation 1993


## 2026-10-09 — Strand updates — desire (M18), group F: precious (2026-10-09, #1993 item F)

**Strand:** desire

**Sources:** ../../Clusters/M18 - desire-longing/m18-group-F-register-v1-20261009.csv
m18-group-F-reading-v1-20261009.md

**Scripts:** m18-group-F-decisions-v1-20261009.py

**Original claims changed:** **Original claims changed:** none.

**Notes:** **Researcher, verbatim:** *"proceed with group F"*.

**Source:** the 60 group F hits, less the verses already decided in the three read-backs and groups A, D and E, which leaves 44 verses. Files: `../../Clusters/M18 - desire-longing/m18-group-F-register-v1-20261009.csv` (reasons in `m18-group-F-decisions-v1-20261009.py`) and the reading `m18-group-F-reading-v1-20261009.md`.

**Decisions:** missed and added 27 (Pro 3:15 and Act 5:34 were cited, but their M18 word was not carried, #1987) · confirmed 2 · carried 1 · route C 14 (stones, cargo, building material, the city's radiance, "cold", people made "rare") · held 0.

**Original claims changed:** none.

| Section | Added or changed | Verdict |
|---|---|---|
| 10.6 (v16) | **New** *Precious*: wisdom above every desire, its worth not known (Pro 3:15; Job 28:13, 16); faith tested (1Pe 1:6–8); the farmer's waiting and the fattened hearts (Jam 5:3–8); the cornerstone and the refuge of lies (Isa 28:15–16; 1Pe 2:6–7); what is honoured shows in what is given (1Ch 29:2–3; Dan 11:37–38); the queen of Sheba (1Ki 10:1–13); honour held (Heb 13:4–5; 1Sa 18:29–30); splendour that entices, passes and covers (Job 31:24–28; Psa 37:1, 20; Rev 17:4). *Aimed at God*: Psa 36:7–8. *Possessions*: two ways to fill a house (Pro 1:13; 24:1–4; 12:27). *Taken away*: the cargo that ends in human souls (Rev 18:11–17) | Widened; new section; I read marked |
| 10.4 (v9) | *It reckons*: the lordly price (Zec 11:12–13; Mat 27:3, 9) | Widened |
| 13.1 (v15) | *Delight*: Ephraim held dear while spoken against (Jer 31:19–20); the price paid (1Pe 1:18–19) | Widened |
| Ch 12 (v18) | *Pride*: the king of Tyre's given splendour (Eze 28:13–17) | Widened |
| 10.2 (v13) | The word rare in Samuel's days; hearing learned (1Sa 3:1–9) | Widened |
| 10.10 (v18) | *Friends, company and care*: the visit kept seldom (Pro 25:16–17) | Widened |
| 10.5 (v16) | *From the heart to the mouth*: utter what is precious (Jer 15:18–19) | Widened |
| 10.13 (v6) | Gamaliel "held in honor by all the people" (Act 5:34) | Wording widened in place |
| Ch 11 (v25) | §4 *Precious*: worth, rarity, splendour, esteem, price, dearness | Widened |

**Quote check:** 64 inserted quotations checked against the ESV in iba.db, 0 failures. The Gamaliel phrase in 10.13 has no citation after it on its line; it was checked by hand against Acts 5:34.

[Chapter versions, from the narrative index] 10.5 v16: utter what is precious (Jer 15:18–19), #1993; 10.6 v16: M18 group F: **new** *Precious*; Psa 36:7–8 in *Aimed at God*; two ways to fill a house in *Possessions*; Babylon's cargo in *Taken away*, #1993; 11 v25: §4 precious, #1993

**Refs:** escalation 1993


## 2026-10-09 — Strand updates — desire (M18), group G: gloss away from desire (2026-10-09, #1993 item F)

**Strand:** desire

**Sources:** ../../Clusters/M18 - desire-longing/m18-group-G-register-v1-20261009.csv
m18-group-G-reading-v1-20261009.md

**Scripts:** m18-group-G-decisions-v1-20261009.py

**Original claims changed:** **Original claims changed:** none.

**Notes:** **Researcher, verbatim:** *"proceed with G"*.

**Source:** the 23 group G hits, less the verses already decided in the three read-backs and groups A, D, E and F, which leaves 21 verses. The M18 words here are glossed "far, long", "collection, gathering" and "untroubled"; each verse was read in its passage for what it carries. Files: `../../Clusters/M18 - desire-longing/m18-group-G-register-v1-20261009.csv` (reasons in `m18-group-G-decisions-v1-20261009.py`) and the reading `m18-group-G-reading-v1-20261009.md`.

**Decisions:** missed and added 12 (Mar 12:34 was cited, but "not far from the kingdom" was not carried, #1987) · confirmed 1 · carried 1 · route C 7 (gathered waters, the collection for the saints, thick clouds, a far country) · held 0.

**Original claims changed:** none.

| Section | Added or changed | Verdict |
|---|---|---|
| Ch 14 (v14) | **New** *Brought near*: far off and without hope, brought near; the hostility killed; peace to far and near (Eph 2:12–18) | New section; I read marked |
| 10.9 (v17) | *Sought, and not far* (Act 17:27–28); *Recognised, and gone to* (Joh 21:7–8) | Widened; I read marked |
| 10.10 (v19) | The son's self-rating set aside by the father (Luk 15:19–22) | Widened; I read marked |
| 10.4 (v10) | *It reckons*: the centurion reckoned worthy by others, not by himself (Luk 7:4–9) | Widened |
| 10.6 (v17) | *A person*: Paul's wish for Agrippa and his hearers (Act 26:28–29) | Widened |
| 10.2 (v14) | Hearing that stops at one word (Act 22:18–22); words as goads and nails (Ecc 12:10–12) | Widened; I read marked |
| 10.5 (v17) | *When mouth and heart part*: long prayers for a pretense, and the widow (Mar 12:38–44) | Widened |
| 10.11 (v4) | *Hiding another*: what the guards told, covered with money and a story (Mat 28:11–15) | Widened |
| Ch 3 (v3) | "You are not far from the kingdom of God" added to the cited Mark 12:33–34 | Wording widened in place |

**Quote check:** 28 inserted quotations checked against the ESV in iba.db, 0 failures.

[Chapter versions, from the narrative index] 14 v14: **new** *Brought near* (Eph 2:12–18), M18 group G, #1993

**Refs:** escalation 1993


## 2026-10-09 — Strand updates — desire (M18), group B set 1: the delight verbs (2026-10-09, #1993 item F)

**Strand:** desire

**Sources:** ../../Clusters/M18 - desire-longing/m18-group-B1-register-v1-20261009.csv
m18-group-B1-delight-reading-v1-20261009.md

**Scripts:** m18-group-B1-decisions-v1-20261009.py
m18-group-B1-narrative-weave-v1-20261009.py

**Original claims changed:** **Original claims changed:** none.

**Notes:** **Researcher, verbatim:** *"split the 77 between delight related words and pleasant related words. and read them in two separate sessions."* At the weave: *"delight associated with God goes to 13.1, separate section; HIB delight goes into 10.1"*.

**Source:** group B (delight, pleasure) after the filter leaves 448 verses. Of these, 171 hold a bucket-1 (inner-being candidate) hit. The 77 whose hit is a verb were split by Strong's number, and set 1 is the 56 delight verses: H2654A *ḥāpēṣ*, H6026 *ʿānag*, H8173B *šāʿaʿ*, G4913 *synēdomai*. Files: `../../Clusters/M18 - desire-longing/m18-group-B1-register-v1-20261009.csv` (reasons in `m18-group-B1-decisions-v1-20261009.py`), reading `m18-group-B1-delight-reading-v1-20261009.md`, weave `m18-group-B1-narrative-weave-v1-20261009.py`.

**Decisions:** a 46 · carried 6 · confirmed 3 (Isa 65:12, 66:4, 56:4) · route C 1 (Jer 6:2) · held 0.

**Structure changed:** a person's delight now has one account, in 10.1. The 10.6 section *Delight* was moved there whole, and 10.6 keeps a pointer.

**Original claims changed:** none.

| Section | Added or changed | Verdict |
|---|---|---|
| 10.1 (v16) | **New** *Delight*: the 10.6 section moved in, plus *On God's word, and on God*; *When it looks right, and when it is missing*; *In a person*; *Wishing*; *A child's delight*; *God's delight in a person's hands*. Delight added to *When feeling changes character* and to the opening | New section; I read marked |
| 10.6 (v18) | *Delight* replaced by a pointer to 10.1; the Deu 21:11 pointer redirected | Moved |
| 13.1 (v16) | *Delight* widened: *Not strength, and truth within* (Jer 9:23–24; Psa 147:10–11; 51:5–6); *Whom he delights in, and why* (2Sa 22:20; Isa 62:4–5; Psa 37:23–24; 1Ki 10:7–9); *His delight in people's mouths* (Num 14:8–10; Psa 41:9–11; 22:8–9; 2Sa 15:26); *Not the offering itself* (Isa 1:11–13; Psa 40:6–8; 51:16–19; Hos 6:4–6); *He does what pleases him* widened (Psa 115:2–5; Isa 42:20–21; 55:11) | Widened; I read marked |

**Quote check:** 82 inserted quotations checked against the ESV in iba.db, 0 failures. The *ḥesed* identity in Hos 6:4 and 6:6 was checked in verse_lexical (H2617A).

[Chapter versions, from the narrative index] 10.1 v16: **new** *Delight* (a person’s delight; the 10.6 section moved in), M18 group B set 1, #1993; 10.6 v18: *Delight* moved to 10.1, pointer kept, #1993; 13.1 v16: *Delight* widened: strength refused, truth within; whom he delights in; his delight in people’s mouths; not the offering itself; does what pleases him, #1993; 13.1 v15: *Delight*: Ephraim my dear son (Jer 31:20); the price paid (1Pe 1:18–19), #1993

**Refs:** escalation 1993


## 2026-10-09 — Strand updates — desire (M18), group B set 2: the pleasant and pleased verbs (2026-10-09, #1993 item F)

**Strand:** desire

**Sources:** ../../Clusters/M18 - desire-longing/m18-group-B2-register-v1-20261009.csv
m18-group-B2-pleasant-reading-v1-20261009.md

**Scripts:** m18-group-B2-decisions-v1-20261009.py
m18-group-B2-narrative-weave-v1-20261009.py

**Original claims changed:** **Original claims changed:** none.

**Notes:** **Researcher, verbatim:** *"proceed with set 2"*. Placement as ruled for set 1: *"delight associated with God goes to 13.1, separate section; HIB delight goes into 10.1"*.

**Source:** the 21 bucket-1 verb verses of H5276 *nāʿēm* (be pleasant) and G2106 *eudokeō* (to be well pleased). Files: `../../Clusters/M18 - desire-longing/m18-group-B2-register-v1-20261009.csv` (reasons in `m18-group-B2-decisions-v1-20261009.py`), reading `m18-group-B2-pleasant-reading-v1-20261009.md`, weave `m18-group-B2-narrative-weave-v1-20261009.py`.

**Decisions:** a 15 · carried 3 · confirmed 2 (2Co 5:8, 2Th 2:12) · route C 1 (Eze 32:19) · held 0.

**Original claims changed:** none.

| Section | Added or changed | Verdict |
|---|---|---|
| 10.1 (v17) | *Delight*: **new** *What is found pleasant* (Gen 49:14–15; Song 7:5–6; 2Sa 1:26; Pro 9:17–18; Psa 141:4–6; Pro 24:24–25; 2Co 12:8–10); *Wishing* widened (1Th 3:1–3) | New subsection; I read marked |
| 13.1 (v17) | *Delight*: **new** *The voice again, on the mountain* (Mat 17:4–7; 2Pe 1:16–19); **new** *His good pleasure gives* (Luk 12:30–32; 1Co 1:21; Col 1:19–21); not pleased though they shared it all (1Co 10:3–6); Hebrews reads Psalm 40 of Christ (Heb 10:5–10) | Widened |

**Quote check:** 28 inserted quotations checked against the ESV in iba.db, 0 failures.

**Refs:** escalation 1993


## 2026-10-09 — Strand updates — desire (M18), group B: three Ch 11 §4 faces (2026-10-09, #1993 item F)

**Strand:** desire

**Sources:** m18-group-B1-delight-reading-v1-20261009.md
m18-group-B2-pleasant-reading-v1-20261009.md

**Scripts:** ../../Clusters/M18 - desire-longing/m18-group-B-ch11-faces-weave-v1-20261009.py

**Original claims changed:** **Original claims changed:** none.

**Notes:** **Researcher, verbatim:** *"proceed with Ch 11"*. These are the faces proposed in `m18-group-B1-delight-reading-v1-20261009.md` §12 and `m18-group-B2-pleasant-reading-v1-20261009.md` §6. Weave: `../../Clusters/M18 - desire-longing/m18-group-B-ch11-faces-weave-v1-20261009.py`.

**Original claims changed:** none.

| Section | Added or changed | Verdict |
|---|---|---|
| Ch 11 (v26) | §4 after *Delight*: *God's delight in a person* (Psa 18:19 / 22:8–9); *An offering* (Psa 51:16–19); *Being well pleased* (Mat 3:17 / 2Co 12:9–10). *What changes the character*: *Whose mouth it is in*; *What the one who brings it brings first* | Widened |

**Quote check:** 9 inserted quotations checked against the ESV in iba.db, 0 failures.

[Chapter versions, from the narrative index] 11 v21: §4 five new faces (eat-drink-be-merry, jealousy, rousing oneself, the redeemer's will, whom the need is spoken to); §5 three voices, #1993

**Refs:** escalation 1993


## 2026-10-09 — Strand updates — desire (M18), group B sets 1 and 2 corrected: read by the main operation (2026-10-09, #1993 item F)

**Strand:** desire

**Sources:** ../../Clusters/M18 - desire-longing/m18-group-B-correction-reread-v1-20261009.md

**Original claims changed:** **Original claims changed:** none.

**Notes:** **Researcher, verbatim (on 2Pe 2:13):** *"making something of this verse with pleasure as an entry point will lead to distorted views"*; then *"yes, re-read and correct your work."*

**What was wrong:** sets 1 and 2 were read with delight as the way in. Twenty-six verses were placed under *Delight* although the delight word only measures or qualifies another act. Each is now placed with the act the verse is about. Record: `../../Clusters/M18 - desire-longing/m18-group-B-correction-reread-v1-20261009.md`.

**Original claims changed:** none.

| Section | Added or changed | Verdict |
|---|---|---|
| 10.1 (v18) | *Delight*: four subsections removed; new table *When delight is only the measure* (26 rows, each pointing to its home) | Corrected |
| 10.2 (v15) | Jer 6:10–11: ears that cannot listen | Moved in |
| 10.5 (v18) | Psa 109:16–18 cursing put on; Psa 22:7–9 mockery before words | Moved in; I read marked |
| 10.7 (v23) | Gen 49:14–15 and Pro 9:13–18 (*What draws it*); 2Sa 15:25–26 (*Choosing before God*); Isa 58:2 (*An inner act weighed*); Psa 141:4–8 (*Setting the heart*); 2Sa 24:3–4, 10 (*Choices weighed by another*) | Moved in; I read marked |
| 10.8 (v7) | Pro 24:23–25 judging without partiality | Moved in |
| 10.9 (v18) | *Comforted as by a mother* (Isa 66:11–13); *Told to depart* (Job 21:13–16); *Returned to* (Job 22:21–27); Job 9:2–3, 13:3–4, 15 contending; Num 14:8–10 not fearing; Job 27:9–10 calling in distress | Moved in; I read marked |
| 10.10 (v20) | 1Sa 18:21–22 snare; Deu 25:7–10 refused duty; 2Sa 20:9–13 following past a body; Ecc 8:2–5 before a king; 1Th 3:1–5, Job 33:30–32, Psa 41:9–11 | Moved in; I read marked |
| Ch 12 (v19) | *Pride*: Haman's designed honour and fall (Est 6:6–13) | Moved in; I read marked |
| 13.1 (v18) | Isa 55:10–11 moved from *Delight* to *Purposing*; *His delight in people's mouths* now points to the acts | Corrected |
| 13.4 (v4) | *Harm ended* (Isa 11:6–9) | Moved in |

**Quote check:** 88 inserted quotations checked against the ESV in iba.db, 0 failures.

[Chapter versions, from the narrative index] 10.1 v18: *Delight* corrected: table *When delight is only the measure*, M18 group B correction by main operation, #1993; 10.2 v15: ears that cannot listen (Jer 6:10–11), M18 group B correction by main operation, #1993; 10.5 v18: cursing put on (Psa 109:16–18); mockery (Psa 22:7–9), M18 group B correction by main operation, #1993; 10.7 v23: Gen 49:15, Pro 9:13–18, 2Sa 15:26, Isa 58:2, Psa 141:4–8, 2Sa 24:3, M18 group B correction by main operation, #1993; 10.8 v7: judging without partiality (Pro 24:23–25), M18 group B correction by main operation, #1993; 10.9 v18: comforted as by a mother; told to depart; returned to; contending; not fearing; calling in distress, M18 group B correction by main operation, #1993; 10.10 v20: snare; refused duty; following past a body; before a king; Timothy sent; Elihu; betrayal, M18 group B correction by main operation, #1993; 12 v19: *Pride*: Haman (Est 6:6–13), M18 group B correction by main operation, #1993; 13.1 v18: Isa 55:10–11 to *Purposing*, M18 group B correction by main operation, #1993; 13.4 v4: *Harm ended* (Isa 11:6–9), M18 group B correction by main operation, #1993

**Refs:** escalation 1993


## 2026-10-09 — Strand updates — desire (M18) × M47: read-back of the narrated cluster (2026-10-09, #1993)

**Strand:** desire

**Sources:** ../../Clusters/M18 - desire-longing/m18-m47-validation-register-v1-20261009.csv
m18-m47-validation-register-v1-20261009.md

**Scripts:** m18-m47-narrative-weave-v1-20261009.py

**Original claims changed:** **Original claims changed:** none. One narrative reading is restated:
- **Ch 5, "Loving and hating one's own soul": Restated.** Ch 5 v3 called Job 10:1, Ecc 2:17 and Jon 4:3 "exhaustion rather than discipleship". The verses give their own ground: bitterness of soul (Job 10:1), "what is done under the sun was grievous to me" (Ecc 2:17), and anger that God spared Nineveh (Jon 4:1–4). Faintness comes only with the second wish (Jon 4:8). The "exhaustion" frame came from M47 batch G §6.

**Notes:** **Researcher, verbatim:** *"yes M02, proceed with M47 first. I want to stress how important the reading back of clusters already narrated are. This is about checking : a) why would the verse not be narrated in the first place, is it because something was missed - fix it; b) does the new reading add new perspective to the narration, maybe from a different angle - validate this new perspective and add it c) is there a fundamental error that need to be re-alligned. It is very important to work with the analysis already generated in the cluster work to avoid re-doing investigatory work alraedy done."*

**Source:** the 208 verses that carry both an M18 and an M47 word, read in their passages beside the M47 batch C reading (§1, "Desire and longing") and the narrative. One decision per verse: `../../Clusters/M18 - desire-longing/m18-m47-validation-register-v1-20261009.csv` (report: `m18-m47-validation-register-v1-20261009.md`).

**Decisions:** missed and added 94 · new perspective added 9 · error realigned 4 · confirmed 54 · carried by a parallel 8 · held for the jealousy account 8 (OT-95) · held as generic "good/better" until the #1993 filter decision 10 (OT-96) · no inner-being bearing (route C) 21.

**Original claims changed:** none. One narrative reading is restated:
- **Ch 5, "Loving and hating one's own soul": Restated.** Ch 5 v3 called Job 10:1, Ecc 2:17 and Jon 4:3 "exhaustion rather than discipleship". The verses give their own ground: bitterness of soul (Job 10:1), "what is done under the sun was grievous to me" (Ecc 2:17), and anger that God spared Nineveh (Jon 4:1–4). Faintness comes only with the second wish (Jon 4:8). The "exhaustion" frame came from M47 batch G §6.

| Section | Added or changed | Verdict |
|---|---|---|
| 10.6 *Wanting* (v10) | desire in the heart through the eye, and held there (Mat 5:28–29; Pro 6:25; 1Co 7:37; 2Ti 2:22); the Preacher: envy, quietness, having without enjoying, enjoyment as God's gift (Ecc 4:4, 6; 6:2–3; 2:24–26); desire as an unrestrained drive (Jer 2:24–25); delight, its objects, its end and its misreading (Psa 119:70; Isa 55:2; 58:3; Pro 18:2; Psa 40:14; 70:2; Deu 21:14; Est 6:6); the wilderness craving (Num 11:4, 18, 20) and Rom 1:24; evil desire and desire thwarted (Pro 21:10; Psa 10:3; Mic 7:3; Pro 10:3; 13:4; 19:2); wanting God (Isa 26:8; Psa 119:20; 2Ch 15:15; 1Pe 2:2–3; 1Co 14:12; Psa 10:17; 21:2; Pro 13:19); wanting a person (Gen 34:8; 1Th 2:17, 8; Rom 1:11); what is desired taken away (Eze 24:21, 25; Rev 18:14; Isa 21:4); greed takes life (Pro 1:19; Eze 22:27) | Widened |
| 13.1 *Delight* (v10, **new section**) | what he delights in (Pro 11:20; 1Ch 29:17; 1Ki 8:18–19; 2Ch 6:8–9; Act 13:22; 2Ki 10:30–31; Isa 43:4; 38:17; 58:5); whom he is pleased with (Luk 3:22; Mat 12:18; Gal 1:16; Heb 10:38); he does what pleases him (Pro 21:1–2; Job 23:13, 15; Jon 1:14, 16; Isa 53:10) | Widened |
| Ch 5 (v4) | the want before God, and the idiom for the reach of a rule (Deu 14:26; 1Ki 11:37; 2Sa 3:21; 1Sa 23:20); Psa 119:20; Isa 26:8; the costly ransom (Psa 49:7–8); a life precious in someone's eyes (1Sa 26:21; 2Ki 1:13–15; Psa 72:14; Pro 6:26); the soul entrusted (1Pe 4:19); Mat 16:25 and parallels; Act 20:24; the death-wishes restated above | Restated |
| Ch 4 (v13) | Pro 21:1 taken out of the "states of the heart" list: a heart directed where the Lord pleases; lust in the heart (Mat 5:28) | Restated |
| Ch 6 (v11) | the harmful spirit and the lyre (1Sa 16:16, 23); the Spirit instructs and leads (Neh 9:20; Psa 143:10) and carries those who speak (2Pe 1:21) | Widened |
| Ch 7 (v7) | what is done with the desires of the flesh (Gal 5:16, 24; Rom 13:14; 1Pe 4:2); the desires used on others (2Pe 2:18, 10); flesh as an outward mark (Gal 6:12–13) | Widened |
| 10.7 *Willing* (v19) | rest refused (Jer 6:16); the living oracles refused (Act 7:38–39); willing gifts with joy (1Ch 29:9, 17; Judg 5:9; Rom 15:27); a will under another (Joh 1:13; Psa 143:10; Col 1:9; Eph 6:6) | Widened |
| 10.1 (v14) | Ecc 7:2 beside 7:3; Pro 15:15 beside 15:13 | Widened |
| 10.5 (v13) | Psa 45:1; Pro 16:24 | Widened |
| Ch 8 (v6) | Heb 13:18 | Widened |
| Ch 11 §2 (v20) | the merry heart with God's approval as its reason (Ecc 9:7) | Widened |
| Ch 12 (v14) | Pro 16:19 beside 16:18 | Widened |
| 13.2 *Angels* (v2) | first content: angels long to look (1Pe 1:12) | Widened |

**Already carried, no change:** 54 verses confirmed in place (see the register CSV).
**Cross-reference note:** the citation parser does not carry a bare citation such as "(4:4)" across a quotation, so a cross-reference run undercounts. 19 placements from this pass, and Isa 58:5 in 10.7, were confirmed by direct search.
**Quote check:** 136 fragments, 0 failures (`m18-m47-narrative-weave-v1-20261009.py`). A deliberately wrong fragment was caught as a test.

[Chapter versions, from the narrative index] 10.6 v10: M18 × M47 read-back: desire in the heart and held there, the Preacher, delight, the wilderness craving, evil desire, wanting God and people, what is desired taken away, greed, #1993; 13.1 v10: **new section *Delight***, God's delight and pleasure, from the M18 × M47 read-back, #1993

**Refs:** escalation 1993


## 2026-10-08 — Structure: No structure change. 6 were already carried (Isa 42:1 in 13.1 through Mat 12:18, with no 10.7 placem

**Strand:** the 18 include verses (#1992, from #1987)

**Refs:** escalation 1992, escalation 1987


## 2026-10-08 — Structure: No structure change. Seven citations corrected to what the verse says. Jer 8:3 (Ch 2): "wished for a

**Strand:** citations to check (#1991, from #1987)

**Refs:** escalation 1991, escalation 1987


## 2026-10-08 — Structure: No structure change. Three citations corrected to their setting. 2Sa 14:14 (Ch 2, 10.4, 13.1): set i

**Strand:** citations needing attention (#1990, from #1987)

**Refs:** escalation 1990, escalation 1987


## 2026-10-08 — Structure: No structure change. 13.1 *Choosing* gains two paragraphs on the researcher's instruction: his eyes 

**Strand:** the 29 M64 × M47 verses: 13.1 (#1989)

**Refs:** escalation 1989


## 2026-10-08 — Structure: No structure change. The will reading carried into the chapters it touches: Ch 4 (the heart named be

**Strand:** willing (M64): the touched chapters (#1986)

**Refs:** escalation 1986


## 2026-10-08 — Structure: Two new sections, no new file, no renumbering. 10.7 *Willing*, after *Planning*: the will meets what

**Strand:** willing (M64): 10.7 and 13.1 (#1986)

**Refs:** escalation 1986


## 2026-10-08 — Structure: Two new sections, no new file, no renumbering. 10.7 *Planning* is the account of looking ahead: weig

**Strand:** planning (M64): the 77 inner-being verses (#1986)

**Refs:** escalation 1986


## 2026-10-08 — Structure: 13.1 *Purposing* gains "The Spirit intercedes according to the will of God" (Rom 8:26-27), placed be

**Strand:** planning (M64): 13.1, the Spirit (#1986)

**Refs:** escalation 1986


## 2026-10-08 — Structure: 13.1 gains the section *Purposing*, after *Choosing*: how God's plans operate, from the 30 verses on

**Strand:** planning (M64): 13.1 (#1986)

**Refs:** escalation 1986, escalation 1987, thread OT-94


## 2026-10-08 — Structure: Ch 11 §4 gains three faces ("Desire beside a choice"; "Despising"; "Knowing that a choice was made")

**Strand:** choosing (M64), §2c: Ch 11 §4 and 13.1 (#1978)

**Refs:** escalation 1978


## 2026-10-08 — Structure: 10.7 gains the section *Others around a choice*, after *Being chosen* (the place the working note re

**Strand:** choosing (M64), §2c (#1978)

**Refs:** escalation 1978


## 2026-10-08 — Structure: Ch 11 §4 gains two faces ("Choosing a person": God before anything in the person, people by what is 

**Strand:** choosing (M64), §2b: Ch 11 §4 and 13.1 (#1978)

**Refs:** escalation 1978


## 2026-10-08 — Structure: 10.7 gains the section *Being chosen*, after *Choosing before God* (the place the v10 working note r

**Strand:** choosing (M64), §2b (#1978)

**Refs:** escalation 1978


## 2026-10-08 — Structure: 10.6 gains a paragraph on wanting beside choosing (2Sa 19:38, where "desire" renders the choosing ve

**Strand:** choosing (M64), §2a: 10.6 and 13.1 (#1978)

**Refs:** escalation 1978


## 2026-10-08 — Structure: Ch 11 §4 gains the five faces of choosing (good or evil in your eyes; knowing good and evil; refusin

**Strand:** choosing (M64), §2a, change of character (#1978, #1919)

**Refs:** escalation 1978, escalation 1919


## 2026-10-08 — Structure: 10.7 reframed around the account of choosing. The section now opens from Joshua 24, where the choice

**Strand:** choosing (M64), §2a (#1978)

**Refs:** escalation 1978


## 2026-10-08 — fear stops the will, #1986; **new**, #1961: the full account of fear, as its own sub-chapter

**Notes:** [Chapter versions, from the narrative index] 10.12 v2: fear stops the will, #1986; **new**, #1961: the full account of fear, as its own sub-chapter

**Refs:** escalation 1986, escalation 1961


## 2026-10-08 — wanting beside choosing, M64 §2a, #1978

**Notes:** [Chapter versions, from the narrative index] 10.6 v8: wanting beside choosing, M64 §2a, #1978; 10.7 v13: Moses and Levite placements confirmed, working-note line removed, #1978; 10.7 v10: **reframed around the account of choosing**, M64 choose §2a, #1978; 11 v16: §4 faces "Desire beside a choice", "Despising", "Knowing that a choice was made", fear beside a choice, M64 §2c, #1978; 13 v2: God bullet points to 13.1 choosing, #1978; 13.1 v2: first content, "Choosing", from the M64 §2a readings, #1978; working note: God's wider choosing verses not yet placed

**Refs:** escalation 1978


## 2026-10-08 — the heart named beside the will, #1986

**Notes:** [Chapter versions, from the narrative index] 04 v12: the heart named beside the will, #1986; 06 v8: hardened and willing spirit, #1986; 10.1 v12: a feeling holds the will, #1986; 10.6 v9: a want met and refused; wanting toward harm, #1986; 10.7 v16: working note, #1986; 10.7 v15: **new section *Willing***, after *Planning*, from the will reading, #1986; 10.9 v15: plotting against God, his word reckoned strange, #1986; 10.10 v13: consent refused, a will pressed, intent pinned, #1986; 10.10 v12: **new section *Plotting against another***, #1986; 10.11 v3: the friendly word as cover, Neh 6:2; Jer 11:19; Psa 140:5, #1986; 10.13 v4: Saul's selective refusal; unwilling to listen, #1986; 10.13 v3: Psa 37:12; Act 5:33, rage that wants to kill at once, #1986; 11 v18: §4 face "Willing", #1986; 13.1 v7: new section *Willing*, God's will, the Son's choosing, the Spirit's willing, Gethsemane, #1986

**Refs:** escalation 1986


## 2026-10-08 — Strand updates — planning (M64): 13.1 *Purposing* (2026-10-08, #1986)

**Strand:** planning

**Sources:** ../../Clusters/M64 - will-resolve/m64-gods-plans-account-v1-20261008.md
m64-plan-scan-v1-20261008.csv

**Original claims changed:** **Original claims changed:** none.

**Not woven:** **Kept out (v25):** Rom 8:27, "the mind of the Spirit" (Holy Spirit, separate study; OT-94); ~~30 of the 31 placed~~ placed in v26 on the researcher's ruling. A person's own planning (the 77 B-routed plan-set verses) is not woven.
**Quote check:** 13.1 v5 *Purposing*, 49 fragments. The only miss is the Eph 1:9–10 quote, which runs across a verse boundary; each part is found in its verse. 0 failures.

**Notes:** **Researcher, verbatim:** *"the 31 God ward verses need to find their way to 13.1 with an analysis of how Gods plans operate."* Source: `../../Clusters/M64 - will-resolve/m64-gods-plans-account-v1-20261008.md`. It covers the 31 verses grouped "God's own purposing" in the plan-set scan (`m64-plan-scan-v1-20261008.csv`), each read in its passage.

**Original claims changed:** none.

| Section | Was (v4) | Now (v5) | Verdict |
|---|---|---|---|
| 13.1 opening | choosing, being chosen, others around a choice | Adds "what the verses on planning and purposing say of his plans" | Widened |
| 13.1 Purposing | — | He forms a plan and makes it known (Jer 49:19-20; 50:44-45; 51:11-12; Act 20:27). His devising answers what people devise (Mic 2:1-3; Jer 18:11-12). He says what he intends so that people may turn, and relents (Jer 18:6, 8, 10; 26:3; 36:3). He also purposes and does not turn back (Jer 4:27-28; Zec 8:14-15; Heb 6:17), with both stated and not reconciled. Carried out and recognised (Lam 2:8, 17; Zec 1:6). Plans for welfare and thought for the needy (Jer 29:10-11; Psa 40:17; 2Sa 14:14). Takes in what people do against him without excusing them (Act 2:23; 4:28-29; Gen 50:20, pointer). Before the ages, not from works (2Ti 1:9; Rom 9:11; Eph 1:9-11; 3:11; Rom 3:25). Turned toward those who love him (Rom 8:28). Refused or served (Luk 7:29-30; Act 13:36). Closing list of where the verses touch a person (Heb 6:19; Jer 29:13; Lam 2:19; Zec 8:17), held for a person's own planning | New |

**Kept out (v25):** Rom 8:27, "the mind of the Spirit" (Holy Spirit, separate study; OT-94); ~~30 of the 31 placed~~ placed in v26 on the researcher's ruling. A person's own planning (the 77 B-routed plan-set verses) is not woven.
**Quote check:** 13.1 v5 *Purposing*, 49 fragments. The only miss is the Eph 1:9–10 quote, which runs across a verse boundary; each part is found in its verse. 0 failures.

[Chapter versions, from the narrative index] 11 v17: §4 faces "Purposing" and "Planning ahead", #1986; 13.1 v5: new section *Purposing*, God's plans, from the plan-set verses, #1986

**Refs:** escalation 1986


## 2026-10-08 — Strand updates — planning (M64): 13.1, the Spirit (2026-10-08, #1986)

**Strand:** planning

**Sources:** ../../Clusters/M64 - will-resolve/m64-gods-plans-account-v2-20261008.md

**Notes:** **Researcher, verbatim:** *"for the purpose of 13.1 (the divine) the Holy Spirit or Spirit is part of it, and should not be left untouched. Add these verses in 13.1 ."*

| Section | Was (v5) | Now (v6) | Verdict |
|---|---|---|---|
| 13.1 Purposing | Rom 8:27 kept out (Holy Spirit) | New paragraph "The Spirit intercedes according to the will of God" (Rom 8:26–27); "mind" left as Paul gives it (OT-94). Rom 8:28 now follows from it. Closing list adds Rom 8:26, the weakness the Spirit helps | Widened |
| 13.1 Choosing (Acts 15:28) | "The Holy Spirit is the subject of a separate study." | Sentence removed; the Spirit is part of the divine for 13.1 | Restated |

**Source:** `../../Clusters/M64 - will-resolve/m64-gods-plans-account-v2-20261008.md` §1.9. All 31 God-ward plan-set verses are now placed.
**Quote check:** the new lines quote Rom 8:26, 8:27 and 8:28 whole; 0 failures.

[Chapter versions, from the narrative index] 13.1 v6: the Spirit intercedes according to the will of God, Rom 8:26-27; the Spirit counted part of the divine for 13.1, #1986

**Refs:** escalation 1986


## 2026-10-08 — Strand updates — planning (M64): the 77 inner-being verses (2026-10-08, #1986)

**Strand:** planning

**Sources:** ../../Clusters/M64 - will-resolve/m64-planning-hib-weave-account-v1-20261008.md

**Original claims changed:** **Original claims changed:** none.

**Notes:** **Researcher, verbatim:** *"now weave the 77 HIB planning verses into the narrative"*. Source: `../../Clusters/M64 - will-resolve/m64-planning-hib-weave-account-v1-20261008.md`. It holds every verse's placement and records that each verse was read in its passage.

**Original claims changed:** none.

| Section | Was | Now | Verdict |
|---|---|---|---|
| 10.7 *Planning* (v14) | — | Looking ahead carried from a choice (Gen 11:6; Pro 16:9); weighing first (Luk 14:28–33; Pro 31:15–16; Judg 19:30); planning without knowing (Act 27:10–14, 39–41; Rom 1:13); a plan carries a person's word (2Co 1:17–18); planning together and parting (Act 15:37–39; Luk 23:51–52); for another's good (Dan 6:3–4; 2Sa 14:13–14); a purpose held (Psa 17:3; Act 11:23; 2Ti 3:10; 1Ch 29:18; Rom 8:6–7; Isa 26:3); devised from one's own heart (1Ki 12:33; Neh 6:8); the plan and its outcome (Isa 8:10; Act 5:38–39; Psa 21:11; Dan 11:24; Gen 50:20); seen and disclosed (1Ch 28:9; 1Co 4:3–5) | New |
| 10.7 *Holding a choice*; working note | — ; "Will, resolve and planning" | Purpose set ahead (Psa 17:3); "Will and resolve" (planning written) | Widened; Restated |
| 10.10 *Plotting against another* (v12) | — | In the heart (Psa 140:2; Zec 7:10; 8:17); together (Psa 31:13; Jer 48:2; Joh 11:53; 12:10–11; Eze 11:2; Dan 11:25, 27; Jer 49:30); at the quiet and weak (Psa 10:2; 35:20; 37:12; Eze 38:10–11); behind a friendly word (Neh 6:2–3; 1Sa 18:25); accusing another of a plan (Neh 6:6, 8–9); the one plotted against (Jer 11:19–20; Psa 140:4, 8; 35:4; 31:14–15; Est 8:3; 9:24; Act 27:42–43); named and checked (Pro 24:8–9; 30:32–33; Deu 19:19–20) | New |
| 10.4 (v7) | devising, reckoning, design | Eze 38:10; 2Ch 2:14; reckoning (Gen 31:15; Lam 4:2; Isa 33:8; 13:17–18); being reckoned (Psa 44:22; 88:3–4; Num 23:9; Neh 13:13); Deu 19:19; connections | Widened |
| 10.9 (v15) | His plans against open to turning | Plotting against him (Hos 7:14–15; Nah 1:9, 11); his word reckoned strange and his name esteemed (Hos 8:12; Mal 3:16); pointer to 13.1 | Widened |
| 10.11 *The hidden trap* (v3) | Psa 64:5–6; 142:3–4 | Neh 6:2; Jer 11:19; Psa 140:5 | Widened |
| 10.13 *What it does next* (v3) | a watching eye, and a plot | Psa 37:12; rage that wants to kill at once (Act 5:33–35) | Widened |
| Ch 11 §4 (v17) | Devising; Planning against | Faces "Purposing" (*zāmam*) and "Planning ahead"; the reading of what changes them is marked "I read" | New |

**Count verses:** the 13 count, regard and esteem verses went into 10.4 *It reckons* (and 10.9), not into *Planning*.
**Already placed (14):** these verses were already quoted for their planning or count word, so they are cross-referenced, not repeated.
**Quote check:** 129 fragments, 0 failures. Five nested-quote matches were confirmed with punctuation ignored.

[Chapter versions, from the narrative index] 10.4 v7: planning, #1986: Eze 38:10, Huram-abi, reckoning and being reckoned, Deu 19:19; 10.7 v14: **new section *Planning***, the 77 inner-being plan verses, #1986

**Refs:** escalation 1986


## 2026-10-08 — Strand updates — willing (M64): 10.7 and 13.1 (2026-10-08, #1986)

**Strand:** willing

**Sources:** ../../Clusters/M64 - will-resolve/m64-will-reading-v1-20261008.md

**Original claims changed:** **Original claims changed:** none.

**Notes:** **Researcher, verbatim:** *"weave the will notes into 10.7 and 13.1"*. Source: `../../Clusters/M64 - will-resolve/m64-will-reading-v1-20261008.md` (the 99 will verses read in their passages, with Part 2 on how they work with the plan reading).

**Original claims changed:** none.

| Section | Was | Now | Verdict |
|---|---|---|---|
| 10.7 *Planning* (v15) | ends "Plans made against another person are in 10.10" | Points to *Willing*; the two often appear in the same passage | Widened |
| 10.7 *Willing* (v15) | — | The will meets what is put before it (Judg 11:17; 19:7–10; 1Sa 22:17; Deu 13:6–8; Pro 1:10; 1Ki 20:8–9; 2Sa 13:12–14; 2:21–23). The "no" keeps faith or does violence (1Sa 22:17–18; 26:23–24; 2Sa 23:15–17; 13:14; Judg 19:25). Selective refusal (1Sa 15:9, 11). Feeling holds the will (1Sa 31:4; 2Sa 6:9–12; Deu 1:26–28; 2Sa 12:17; Pro 6:35). Refusing God refuses something good (Deu 1:25–26; Isa 28:12; Psa 81:10–11; Pro 1:23; Isa 1:18–20). Willing and planning named together (Pro 1:29–31; Psa 81:11–12; Isa 30:1, 15–16; 1Ch 28:19, 21), read as "I read". A plan meets another's will (Gen 24:5–8; 2Sa 13:25–28; 14:29–30; Joh 18:38; Mar 15:15; Act 27:43; 19:30; 18:27). A resolve still weighed (Mat 1:19–20; Act 12:4–5). The will steers (Jam 3:4). Turned toward harm (1Ti 6:6, 9; Jam 4:1, 4). The willing heart (Exo 35:21–22; 2Ch 29:31; Psa 51:10, 12; Phm 13–14). The will made absolute (Dan 5:19–22; 4:27, 34). A will under another (Rom 9:16; Luk 22:42) | New |
| 10.7 *What changes the character* | seven faces | Adds "Willing" | Widened |
| 10.7 Connections; working note | — ; "Will and resolve … still to be read" | Adds 10.10, 10.1, 10.12, 10.6, 13.1 willing. Working note lists what is not yet updated: Ch 4, Ch 6, 10.6, 10.12, 10.1, 10.10 | Widened; Restated |
| 13.1 opening; *Purposing* closing (v7) | "… which is still to be written" | Adds willing; points to 10.7 *Planning* | Restated |
| 13.1 *Willing* (v7) | — | Not willing to destroy: intercession, promise, covenant, grace, love (Deu 10:10; 2Ki 8:19; 2Ch 21:7; 2Ki 13:23; Deu 23:5; Jos 24:10). Not willing to forgive: the self-blessing stubborn heart, innocent blood (Deu 29:19–20; 2Ki 24:4). He does as he wills (Dan 4:17, 25, 32, 34–35, 37; 5:21; Rom 9:18–20, potter noted beside Jer 18 and not joined). His will brings to life and waits (Jam 1:15, 17–18; 2Pe 3:9; Heb 6:17). The Father's will, the Son's choosing, the Spirit's willing (Mat 11:26–27; Luk 10:21–22; 1Co 12:11). Gethsemane (Luk 22:42–44). Nature (Job 39:9) | New |

**Not yet updated (touched by the will reading):** ~~Ch 4 and Ch 6 (hardened, stubborn, lifted-up and willing hearts and spirits); 10.6 (David's water); 10.12 (the armor-bearer, the ark, melted hearts); 10.1 and 10.13 (grief, jealousy); 10.10 (Pro 1:10–11; Absalom pressing; Pilate); Ch 11 §4 (the will faces). The researcher's instruction named 10.7 and 13.1 only.~~ done in v29.
**Slight bearing, kept in the data:** Phi 1:12; Tit 3:8; Jude 5; Act 25:22.
**Quote check:** 10.7 *Willing* 77 fragments, 13.1 *Willing* 26 fragments, 0 failures. Verses were joined in canonical order to check quotes that run across verses.

**Refs:** escalation 1986


## 2026-10-08 — Strand updates — willing (M64): the touched chapters (2026-10-08, #1986)

**Strand:** willing

**Sources:** ../../Clusters/M64 - will-resolve/m64-will-reading-v1-20261008.md

**Original claims changed:** **Original claims changed:** none.

**Notes:** **Researcher, verbatim:** *"update Ch 4, Ch 6 and the other touched chapters"*. Source: `../../Clusters/M64 - will-resolve/m64-will-reading-v1-20261008.md`, Part 2.5.

**Original claims changed:** none.

| Section | Now | Verdict |
|---|---|---|
| Ch 4 *The heart decides and is moved* (v12) | The heart named beside the will: willing (Exo 35:22; 2Ch 29:31), hardened (Exo 10:27; Deu 2:30), stubborn and unwilling to listen (Eze 3:7; Psa 81:12), melted (Deu 1:26, 28), self-blessing (Deu 29:19–20), lifted up and not humbled (Dan 5:19–20, 22) | Widened |
| Ch 6 *The human spirit* (v8) | Hardened: Sihon who would not let them pass (Deu 2:30); Nebuchadnezzar (Dan 5:20). Willing: the spirit moved and the willing heart (Exo 35:21–22); the willing spirit asked with a clean heart, a right spirit and the Holy Spirit (Psa 51:10–12) | Widened |
| 10.1 *Where it turns* (v12) | A feeling holds the will: fear (2Sa 6:10, 12), grief (2Sa 12:17), jealousy (Pro 6:35) | Widened |
| 10.6 (v9) | A want met and refused (2Sa 23:15–17); wanting turned toward harm (1Ti 6:6, 9; Jam 4:4) | Widened |
| 10.10 *Plotting against another* (v13) | Invites others in, and the will's "no" (Pro 1:10–11); it presses another's will (2Sa 13:25–28; 14:29–31; Joh 18:38; Mar 15:15); intent pinned on the other (Act 5:28–29, beside Neh 6:6) | Widened |
| 10.12 *What fear does* (v2) | It stops the will (1Sa 31:4; 2Sa 6:9–10, 12; Deu 1:26, 28) | Widened |
| 10.13 (v4) | Samuel's anger and Saul's selective refusal (1Sa 15:9, 11); God's anger: unwilling to listen (Eze 20:8–9) | Widened |
| Ch 11 §4 (v18) | Face "Willing" (*ʾāḇâ* and *boulomai*); the reading of what changes it is marked "I read" | New face |
| 10.7 working note (v16) | Lists the chapters that now carry their parts | Restated |

**Quote check:** 61 fragments. 1 corrected: Ch 11 had "not willing to forgive", which is now Deu 29:20's own words, "will not be willing to forgive". 0 failures after the correction.

**Refs:** escalation 1986


## 2026-10-08 — Strand updates — the 29 M64 × M47 verses: 13.1 *Choosing* (2026-10-08, #1989)

**Strand:** the 29 M64 × M47 verses

**Sources:** ../../Clusters/M64 - will-resolve/m64-m47-marked-verses-completion-v1-20261008.md

**Original claims changed:** **Original claims changed:** none.

**Notes:** **Researcher, verbatim:** *"2Ch 7:16 and Matt 12:18 must find it way to 13.1, both deal with important characteristics of the divine - Note that Matt 12:18 prophetically is pointing to Jesus, part of the divine. Lev and Eze does not have placements. Lev 17:4 is not about other beings, it has no placement."* Source: `../../Clusters/M64 - will-resolve/m64-m47-marked-verses-completion-v1-20261008.md` §3.3, §3.4.

**Original claims changed:** none.

| Section | Was (v7) | Now (v8) | Verdict |
|---|---|---|---|
| 13.1 *Choosing* | God's choosing spoken of with love and pleasure (Eph 1:4–5; 1Ch 28:4; 2Sa 6:21) | New paragraph: he chooses his servant with delight and puts his Spirit on him (Mat 12:18, quoting Isa 42:1), in Matthew's setting: the plot, the withdrawing, the order to keep quiet, the fulfilment (Mat 12:14–17, 19–20) | Widened |
| 13.1 *Choosing* | the place he chose: blessing and gathering (Deu 16:15; Neh 1:9) | New paragraph: his eyes and his heart are at the place he chose, with his hearing of the prayer made there, and the house cast out of his sight if he is forsaken (2Ch 7:12, 15–16, 20) | Widened |
| 13.1 working note | the wider choosing verses not yet placed | 2Ch 7:16 and Mat 12:18 placed; the rest still held (OT-92) | Restated |

**Not placed (researcher ruling):** Eze 14:7, Lev 7:18, Lev 17:4.
**Quote check:** 10 fragments, 0 failures.

[Chapter versions, from the narrative index] 13.1 v8: *Choosing* gains his eyes and heart at the place he chose, 2Ch 7:12-20, and his servant chosen with delight and the Spirit, Mat 12:18 quoting Isa 42:1, #1989

**Refs:** escalation 1989


## 2026-10-08 — Strand updates — citations needing attention (2026-10-08, #1990)

**Strand:** citations needing attention

**Sources:** ../../Clusters/M64 - will-resolve/m64-reopened-cited-verses-reading-v2-20261008.md

**Original claims changed:** **Original claims changed:** none.

**Notes:** **Researcher, verbatim:** *"continue with the 1987 citations that need attention"*. Source: `../../Clusters/M64 - will-resolve/m64-reopened-cited-verses-reading-v2-20261008.md` (Needs attention; per-verse sections).

**Original claims changed:** none.

| Section | Was | Now | Verdict |
|---|---|---|---|
| Ch 2 *What death is* (v12) | "A wise woman put it to David in a picture" (2Sa 14:14) | Joab sent her with a staged plea, "Joab put the words in her mouth" (14:3); then v14 | Restated |
| 10.4 (v8) | "He even thinks for those who have put themselves outside" (2Sa 14:14) | Set in the plea Joab put in a woman's mouth (14:3); "put themselves outside" removed (not in the verse: "the banished one") | Restated |
| 13.1 *Purposing* (v9) | "the wise woman of Tekoa says" | "In the plea Joab put in her mouth (2 Samuel 14:3)" added. Not flagged in #1987, which predates this 13.1 line; same issue | Restated |
| Ch 6 (v9) | "The righteous man is the one 'in whose spirit there is no deceit'" (Psa 32:2) | The blessed man is the one whose transgression is forgiven (32:1), against whom the Lord counts no iniquity (32:2); the no-deceit stands beside his confession (32:5) | Restated |
| 10.7 working note (v17) | Job 7:15; 9:14; 29:25 "go with *Choices weighed by another*" | Job's own voice set beside the friends' verdicts (the batch 4 intent); 7:15 also with *Life and death set before a person* | Restated |

**Correction to the #1987 verdict on Job 7:15:** the note did not say that anyone weighs Job's choice. It came from choose batch 4, which says these verses "will matter when the account sets the weighing of others beside the chooser's own voice". The wording was loose, not misplaced.
**Quote check:** 5 fragments, 0 failures.

[Chapter versions, from the narrative index] 02 v12: 2Sa 14:14 set in Joab's staged plea, 14:3, #1990; 06 v9: Psa 32:2 restated, the forgiven man who confessed, 32:1, 5, #1990; 10.4 v8: 2Sa 14:14 set in Joab's plea; "those who have put themselves outside" removed, #1990; 10.7 v17: working note, Job's own voice beside the friends' verdicts; Job 7:15 also with life and death, #1990; 13.1 v9: 2Sa 14:14 set in Joab's plea, #1990

**Refs:** escalation 1990


## 2026-10-08 — Strand updates — citations to check (2026-10-08, #1991)

**Strand:** citations to check

**Sources:** ../../Clusters/M64 - will-resolve/m64-reopened-cited-verses-reading-v2-20261008.md

**Original claims changed:** **Original claims changed:** none.

**Notes:** **Researcher, verbatim:** *"continue with the seven check items"*. Source: `../../Clusters/M64 - will-resolve/m64-reopened-cited-verses-reading-v2-20261008.md` (Check; per-verse sections).

**Original claims changed:** none.

| Section | Was | Now | Verdict |
|---|---|---|---|
| Ch 2 *Wanting to die* (v13) | "Under judgment, death is wished for and withheld" (Jer 8:3; Rev 9:6) | "death is chosen over life"; "Preferred" is the choosing word; Rev 9:6 given separately as sought and not found | Restated |
| 10.1 *What anxiety does* (v13) | "It divides" (Luk 10:41–42 under Paul's word) | "Many things against one", with 10:40 "distracted with much serving"; Paul's "divided" kept as his own | Restated |
| 10.1 summary (v13) | "Whether it divides me" | "Whether it pulls me to many things or to one" | Restated |
| Ch 11 §1 (v19) | "Even the leaning is formed": the *yēṣer* of Gen 6:5 linked to the potter (Isa 29:16) and "frame" (Psa 103:14); Exo 35:35 under it | Heading "Skill and laws are put in, and minds are blinded"; the word link is removed, because no verse says God formed the evil intention; Exo 35:35, Heb 8:10 and 2Co 4:4 kept | Withdrawn (word link); Restated |
| Ch 11 §4 (v19) | "Whether it divides the person" | "Whether it pulls the person to many things or to one" | Restated |
| Ch 11 §8 (v19) | "the same evil intention had grieved him 'to his heart' (6:5–6)" | 6:5 and 6:6 quoted as written; the verse does not name the intention as what grieved him | Restated |
| Ch 14 (v13) | 1Ch 29:18 "such purposes" without referent | Preceded by 29:17, "offering freely and joyously to you"; "The purposes are that free and joyful giving" | Restated |
| 10.12 (v3) | "heard the same whisper and answered the same way" (Psa 31:13–14) | Heard "the whispering of many" and "terror on every side", answered in his own words, 31:14 in full | Restated |
| Ch 6 *It is willing* (v10) | "The willing spirit is something God upholds" | The verse does not say whose spirit it is (v10 "within me", v11 "your Holy Spirit", v12 neither); it is asked of God and God upholds it | Restated |

**Quote check:** 10 fragments, 0 failures.

[Chapter versions, from the narrative index] 02 v13: Jer 8:3 "preferred" is the choosing word; Rev 9:6 kept apart, #1991; 06 v10: Psa 51:12, the willing spirit has no possessive, #1991; 10.1 v13: "It divides" restated as "Many things against one", Luk 10:40-42, #1991; 10.12 v3: Psa 31:13-14, the psalmist answers in his own words, #1991; 11 v19: §1 "Even the leaning is formed" restated, the Gen 6:5 word link removed; §4 "many things or one"; §8 Gen 6:5-6 quoted as written, #1991; 14 v13: 1Ch 29:18 given its referent, 29:17, #1991

**Refs:** escalation 1991


## 2026-10-08 — Strand updates — the 18 include verses (2026-10-08, #1992)

**Strand:** the 18 include verses

**Sources:** ../../Clusters/M64 - will-resolve/m64-include-verses-placement-proposal-v1-20261008.md

**Original claims changed:** **Original claims changed:** none.

**Notes:** **Researcher, verbatim:** *"approve all as proposed, no 10.7 for Isa 42:1"*. Source: `../../Clusters/M64 - will-resolve/m64-include-verses-placement-proposal-v1-20261008.md`.

**Original claims changed:** none.

| Section | Added | Verdict |
|---|---|---|
| 10.7 *Life and death set before a person* (v18) | Deu 30:20, 30:17, 30:14: what choosing life is, the other way from inside, and that it can be done; Phili 1:22–25, a choice between two goods that stays open | Widened |
| 10.7 *Holding a choice* (v18) | Luk 10:39–42: guarded by another | Widened |
| 10.7 *Willing* (v18) | Exo 36:2; Psa 51:13 | Widened |
| 10.7 *Planning* (v18) | 2Sa 14:1, 3, 13, 14, 19: the plea set in Joab's scheme; three at work in one passage | Restated |
| Ch 2 *Wanting to die* (v14) | Job 7:13–14, 16; Jer 8:2 | Widened |
| 10.13 *Those who carry it out* (v5) | Isa 10:12–13, 15 | Widened |
| Ch 12 *Flesh as an orientation* (v13) | Rom 8:7 in full, "indeed, it cannot" | Widened |
| 10.12 (v4) | Pro 1:29 beside 1:26–27; Isa 66:2 beside 66:4; both marked "I read" | Widened |
| 10.10 (v14) | 2Sa 19:23 | Widened |

**Already carried, no change:** Isa 42:1 (13.1 through Mat 12:18; no 10.7 placement by ruling), Deu 2:30, 1Ch 28:9, 1Ch 29:18, Psa 32:2.
**Quote check:** 26 fragments, 0 failures.

[Chapter versions, from the narrative index] 02 v14: Job 7:13-16; Jer 8:2, #1992; 10.7 v18: Deu 30:14, 17, 20; Phili 1:22-25; Luk 10:39-42; Exo 36:2; Psa 51:13; 2Sa 14 Joab, #1992; 10.10 v14: 2Sa 19:23, #1992; 10.12 v4: Pro 1:29 and Isa 66:2, both "I read", #1992; 10.13 v5: Isa 10:12-15, #1992; 12 v13: Rom 8:7 "indeed, it cannot", #1992

**Refs:** escalation 1992


## 2026-10-08 — Strand updates — choosing (M64), §2c: Ch 11 §4 and 13.1 (2026-10-08, #1978)

**Strand:** choosing

**Not woven:** **Kept out:** no statement about God's character as a key to the human inner being (image question parked, #1984). The 166 routed verses stay in the 13.1 working note.
**Quote check:** 13.1 v4 new lines, 22 quotes, 0 failures; Ch 11 v16 new lines, all quotes found (the checker's only misses are older lines with bracketed glosses and word definitions).

**Notes:** **Researcher, verbatim:** *"update Ch 11 §4 and 13.1"*.

| Section | Was | Now | Verdict |
|---|---|---|---|
| Ch 11 §4 faces | Fear: *yārēʾ*, both ways; Nehemiah 1:5 | Adds the faces beside a choice: learned at a feast in the chosen place (Deu 14:23); on those who hear (17:13); terror at God's choice made plain (Num 17:13) | Widened |
| Ch 11 §4 faces | — | "Desire beside a choice" (Deu 12:21; 18:6; Isa 66:3) | New |
| Ch 11 §4 faces | — | "Despising" (2Sa 6:16; Isa 49:7; Jer 33:24; Psa 106:24) | New |
| Ch 11 §4 faces | — | "Knowing that a choice was made" (Act 15:7, 12; 1Th 1:4-5; Isa 45:4; Joh 15:21) | New |
| Ch 11 §4 What changes the character | Whose eyes, and whose delight | Adds the other measure held by those around God's choosing (Deu 12:8; 2Sa 6:20; Jer 33:24; 1Pe 2:4) | Widened |
| Ch 11 §4 What changes the character | What it is turned toward | Adds desire (Deu 12:21; 18:6; Isa 66:3) | Widened |
| 13.1 He searches hearts, and acts on them | 2Th 2:10-11; Rev 17:17 | Adds Rom 11:8 with 11:11 and 11:5; 1Pe 2:8 (cause given, the rest not explained); 1Ki 8:39, 58 | Widened |
| 13.1 | — | New paragraphs: he answers those who set themselves against his choosing (Num 16:11; 17:5, 10; Isa 49:7; Jer 33:24-26; Joh 15:18-19); he calls those who do not know him, for the sake of his chosen (Isa 45:4-6); he blesses at the place he chose, so that his people rejoice, and gathers those who return (Deu 16:15; Neh 1:9); what he chooses is turned toward others (Isa 58:3-6); his wrath turned away when his chosen one stands before him (Psa 106:23; pointer to 10.13) | New |

**Kept out:** no statement about God's character as a key to the human inner being (image question parked, #1984). The 166 routed verses stay in the 13.1 working note.
**Quote check:** 13.1 v4 new lines, 22 quotes, 0 failures; Ch 11 v16 new lines, all quotes found (the checker's only misses are older lines with bracketed glosses and word definitions).

**Refs:** escalation 1978

**Quote check:** 22 parts, 0 failures. **Kept out:** no statement about God's character as a key to the human inner being (image question parked, #1984). The 166 routed verses stay in the 13.1 working note.
**Quote check:** 13.1 v4 new lines, 22 quotes, 0 failures; Ch 11 v16 new lines, all quotes found (the checker's only misses are older lines with bracketed glosses and word definitions).


## 2026-10-08 — Strand updates — choosing (M64), §2c: 10.7 *Others around a choice* (2026-10-08, #1978)

**Strand:** choosing

**Sources:** ../../Clusters/M64 - will-resolve/m64-others-around-choosing-account-v1-20261008.md

**Original claims changed:** **Original claims changed:** none.

**Not woven:** **Corrected on the way (HIB/qualifier file, recorded in the readings):** Deu 12:21 is away from the chosen place, not "setting"; Isa 66:3, the soul is the chooser's own, not "other".
**Placements confirmed (researcher, verbatim, 2026-10-08: *confirm Moses and Levite placements as recommended*):** Moses in the breach in *Being chosen* (*Standing for others*); the Levite of Deu 18:6 in *Others around a choice* (*Desire, near and far*). 10.7 v13 removes the working-note line that held them open; the text is unchanged.
**Kept out:** Judg 20:34 and Pro 10:20 (not about choosing; notes for knowing and fear, and for speaking). God's replies (Num 17:5, 10; Isa 45:4-5; 49:7; Jer 33:25-26) and God acting on others (Rom 11:8; 1Pe 2:8) are for 13.1, not placed.
**Quote check:** 10.7 v12, 286 quote fragments, 0 failures; account, 105 fragments, 0 failures in the ESV (the researcher's instruction is the only other quote).
**Quoted share:** 39% (v11) -> 38% (v12), by the same measure.
**Not yet updated:** ~~Ch 11 §4 (candidate faces: desire, despising, fear, knowing); 13.1 (God's replies above)~~ done in v23.

**Notes:** **Researcher, verbatim:** *"write the 2c account and weave into 10.7"*. Source: `../../Clusters/M64 - will-resolve/m64-others-around-choosing-account-v1-20261008.md` (31 verses read in their passages, §2c batches 1-3: the 29 §2c verses, plus Michal, 2Sa 6:16, and Moses in the breach, Psa 106:23, kept back from §2b).

**Original claims changed:** none.

| Section (10.7 v12) | Was (v11) | Now | Verdict |
|---|---|---|---|
| Others around a choice | — (working-note slot) | At the place God chose: rejoicing before the Lord, shared, grounded in the blessing (Deu 12:7, 18; 16:11-12, 15); fear learned at a meal with appetite and joy (14:23, 26); carefulness when a case is too hard, against presumption (17:8, 10, 13). Desire near and far (Deu 12:21; 18:6). Turned toward it from far off (1Ki 8:46-48, 39, 58; Neh 1:9). Set against the chosen: grumbling and seeking more (Num 16:10-11; 17:5, 13; Psa 106:16), Saul's anger and Jonathan's grief (1Sa 20:17, 30-34, 42), Michal's contempt (2Sa 6:16, 20), despised and abhorred (Isa 49:7), a verdict from ruin (Jer 33:24), hatred (Joh 15:18-19, 21), rejection (1Pe 2:4). With the chosen and for them (Psa 106:4-6; 2Ti 2:10; 2Jo 1-2; 1Pe 2:6, 8). Knowing that a choice was made, and not knowing (Act 15:7, 9, 12; 1Th 1:4-5; Isa 45:3-4; Rom 11:7, 11). An inner act weighed by what God chooses (Isa 58:2-7) | New |
| Being chosen | — | *Standing for others*: Moses in the breach (Psa 106:23, 21), with the people's jealousy and embittering (106:16, 33); pointer to 10.13 | Widened |
| The words | *bāḥar*, *māʾas*, *eklegomai*, *authairetos* | Adds *bāḥîr*, "chosen one" (Psa 106:23; Isa 45:4) | Widened |
| Whose measure | the chooser's eyes; the Lord's eyes and delight | Adds "Other people's eyes, set against his choosing" (Deu 12:8, 11; 2Sa 6:20-21; Jer 33:24; 1Pe 2:4) | Widened |
| What changes the character | seven faces | Adds "Desire beside a choice" (Deu 12:21; 18:6; Isa 66:3) and "Despising" (2Sa 6:16, 20; Isa 49:7; Jer 33:24; Psa 106:24) | Widened |
| Connections | | Fear and feeling widened; 10.10 widened; 10.13 added | Widened |
| Working note | others around a choice; held Deu 23:16 / 12:5, 14 phrase | Others line removed (now written); held phrase kept, with the differing forms noted; two placements for the researcher to confirm | Restated |

**Corrected on the way (HIB/qualifier file, recorded in the readings):** Deu 12:21 is away from the chosen place, not "setting"; Isa 66:3, the soul is the chooser's own, not "other".
**Placements confirmed (researcher, verbatim, 2026-10-08: *confirm Moses and Levite placements as recommended*):** Moses in the breach in *Being chosen* (*Standing for others*); the Levite of Deu 18:6 in *Others around a choice* (*Desire, near and far*). 10.7 v13 removes the working-note line that held them open; the text is unchanged.
**Kept out:** Judg 20:34 and Pro 10:20 (not about choosing; notes for knowing and fear, and for speaking). God's replies (Num 17:5, 10; Isa 45:4-5; 49:7; Jer 33:25-26) and God acting on others (Rom 11:8; 1Pe 2:8) are for 13.1, not placed.
**Quote check:** 10.7 v12, 286 quote fragments, 0 failures; account, 105 fragments, 0 failures in the ESV (the researcher's instruction is the only other quote).
**Quoted share:** 39% (v11) -> 38% (v12), by the same measure.
**Not yet updated:** ~~Ch 11 §4 (candidate faces: desire, despising, fear, knowing); 13.1 (God's replies above)~~ done in v23.

[Chapter versions, from the narrative index] 10.7 v12: **new section *Others around a choice***, M64 choose §2c account, #1978; 13.1 v4: from the §2c readings: he answers those set against his choosing; calls those who do not know him; blesses at the place he chose; what he chooses is turned to others; acting on others widened (Rom 11:8; 1Pe 2:8), #1978

**Refs:** escalation 1978

**Quote check:** 286 parts, 0 failures. **Corrected on the way (HIB/qualifier file, recorded in the readings):** Deu 12:21 is away from the chosen place, not "setting"; Isa 66:3, the soul is the chooser's own, not "other".
**Placements confirmed (researcher, verbatim, 2026-10-08: *confirm Moses and Levite placements as recommended*):** Moses in the breach in *Being chosen* (*Standing for others*); the Levite of Deu 18:6 in *Others around a choice* (*Desire, near and far*). 10.7 v13 removes the working-note line that held them open; the text is unchanged.
**Kept out:** Judg 20:34 and Pro 10:20 (not about choosing; notes for knowing and fear, and for speaking). God's replies (Num 17:5, 10; Isa 45:4-5; 49:7; Jer 33:25-26) and God acting on others (Rom 11:8; 1Pe 2:8) are for 13.1, not placed.
**Quote check:** 10.7 v12, 286 quote fragments, 0 failures; account, 105 fragments, 0 failures in the ESV (the researcher's instruction is the only other quote).
**Quoted share:** 39% (v11) -> 38% (v12), by the same measure.
**Not yet updated:** ~~Ch 11 §4 (candidate faces: desire, despising, fear, knowing); 13.1 (God's replies above)~~ done in v23.


## 2026-10-08 — Strand updates — choosing (M64), §2b: Ch 11 §4 and 13.1 (2026-10-08, #1978)

**Strand:** choosing

**Not woven:** **Kept out:** no statement about God's character as a key to the human inner being (image question parked, #1984). The 166 routed verses stay in the 13.1 working note.
**Quote check:** 13.1 v3, 36 quotes, all found; Ch 11 new lines, 6 quotes checked directly against their verses, 0 failures.

**Notes:** **Researcher, verbatim:** *"update Ch 11 §4 and 13.1"*.

| Section | Was | Now | Verdict |
|---|---|---|---|
| Ch 11 §4 faces | — | "Choosing a person" (Eph 1:4; Isa 43:8, 10; Jam 2:5; Act 6:3) | New |
| Ch 11 §4 faces | — | "Holiness" (Eph 1:4; Col 3:12; "the verses do not say how the two fit") | New |
| Ch 11 §4 What changes the character | — | Factor "Who chooses" (Isa 43:10; Act 6:3, 5) | New |
| 13.1 Choosing | v2: he chooses; eyes and delight; acts first; good, upright, holy; knows the heart and gives; reasons, answers, judges | Adds: he chooses before anything is in the one chosen, with his love and pleasure (Eph 1:4-5; 1Ch 28:4; 2Sa 6:21; Jam 2:5; Isa 43:8, 10); he searches hearts and acts on them (1Ch 28:9; 2Th 2:10-11; Rev 17:17); he remembers and does not remember (Psa 105:8, 42; 106:45; Isa 43:25; 44:21) | Widened |

**Kept out:** no statement about God's character as a key to the human inner being (image question parked, #1984). The 166 routed verses stay in the 13.1 working note.
**Quote check:** 13.1 v3, 36 quotes, all found; Ch 11 new lines, 6 quotes checked directly against their verses, 0 failures.

**Refs:** escalation 1978

**Quote check:** 6 parts, 0 failures. **Kept out:** no statement about God's character as a key to the human inner being (image question parked, #1984). The 166 routed verses stay in the 13.1 working note.
**Quote check:** 13.1 v3, 36 quotes, all found; Ch 11 new lines, 6 quotes checked directly against their verses, 0 failures.


## 2026-10-08 — Strand updates — choosing (M64), §2b: 10.7 *Being chosen* (2026-10-08, #1978)

**Strand:** choosing

**Sources:** ../../Clusters/M64 - will-resolve/m64-being-chosen-account-v1-20261008.md

**Original claims changed:** **Original claims changed:** none.

**Not woven:** **Corrected on the way:** Eph 1:4 "In love" belongs with v5 in the ESV sentence; the love is God's, not a purpose of the chosen (batch 2).
**Kept out:** Michal's contempt and Moses in the breach (for §2c); 2Th 2:11 and Rev 17:17, God acting on others' hearts (for 13.1, not yet placed).
**Quote check:** 10.7 v11, 199 quotes, 0 failures; account, 78 quotes, 0 failures.
**Quoted share:** 39% -> 41% (list-drift warning: a small rise).
**Not yet updated:** ~~Ch 11 §4 (the two new faces); 13.1 (2Th 2:11; Rev 17:17; God remembering his covenant)~~ done in v21.

**Notes:** **Researcher, verbatim:** *"write the 2b account and weave into 10.7"*. Source: `../../Clusters/M64 - will-resolve/m64-being-chosen-account-v1-20261008.md` (15 verses read in their passages, §2b batches 1-2).

**Original claims changed:** none.

| Section (10.7 v11) | Was (v10) | Now | Verdict |
|---|---|---|---|
| Being chosen | — (working-note slot) | The choosing comes first, the inner life its purpose (Isa 43:8, 10; Eph 1:4; Jam 2:5; Psa 65:3-4); belief and choosing named together, not fitted (2Th 2:13); the other order when people choose (Act 6:3, 5; 7:55, 60); moved to: celebrating, not fearing, satisfaction, joy, gladness shared (2Sa 6:8-10, 20-21; Isa 44:2; Psa 65:4; 105:43; 106:5-6); called to: be strong, put on, stand firm, confirm, remember (1Ch 28:9-10; Col 3:12-14; 2Th 2:15; 2Pe 1:3, 5-7, 10; Psa 105:5-6; Isa 44:21); faith and the truth (Tit 1:1; Jam 2:5, 17; 2Th 2:13; Eph 1:18); not a guarantee (1Ch 28:9; Psa 106:13, 24; Isa 43:22; 2Pe 1:9) and the way back (Psa 106:45; Isa 43:25); set against others (Isa 44:18; 2Th 2:10, 12; Tit 1:16; Jam 2:4, 6; Rev 17:13-14) | New |
| The words | God's choosing "not this section's subject" (Ch 13) | Points to *Being chosen* for the person, and to 13.1 for God's own choosing | Restated |
| What a choice rests on: Knowing how | Isa 7:15; 1:3 | Adds: for the person God chooses, the order runs the other way | Widened |
| Holding a choice | — | 2Pe 1:10 pointer | Widened |
| What changes the character | five faces | Adds "Choosing a person" (who chooses) and "Holiness" (purpose in Eph 1:4, name in Col 3:12; why not stated) | Widened |
| Connections | | 10.10 widened; God's choosing -> 13.1 | Widened |

**Corrected on the way:** Eph 1:4 "In love" belongs with v5 in the ESV sentence; the love is God's, not a purpose of the chosen (batch 2).
**Kept out:** Michal's contempt and Moses in the breach (for §2c); 2Th 2:11 and Rev 17:17, God acting on others' hearts (for 13.1, not yet placed).
**Quote check:** 10.7 v11, 199 quotes, 0 failures; account, 78 quotes, 0 failures.
**Quoted share:** 39% -> 41% (list-drift warning: a small rise).
**Not yet updated:** ~~Ch 11 §4 (the two new faces); 13.1 (2Th 2:11; Rev 17:17; God remembering his covenant)~~ done in v21.

[Chapter versions, from the narrative index] 10.7 v11: **new section *Being chosen***, M64 choose §2b account, #1978; 13.1 v3: from the §2b readings: he chooses before anything is in the one chosen; he searches hearts and acts on them, including giving over (2Th 2:11; Rev 17:17); he remembers, and does not remember sins, #1978

**Refs:** escalation 1978

**Quote check:** 199 parts, 0 failures. **Corrected on the way:** Eph 1:4 "In love" belongs with v5 in the ESV sentence; the love is God's, not a purpose of the chosen (batch 2).
**Kept out:** Michal's contempt and Moses in the breach (for §2c); 2Th 2:11 and Rev 17:17, God acting on others' hearts (for 13.1, not yet placed).
**Quote check:** 10.7 v11, 199 quotes, 0 failures; account, 78 quotes, 0 failures.
**Quoted share:** 39% -> 41% (list-drift warning: a small rise).
**Not yet updated:** ~~Ch 11 §4 (the two new faces); 13.1 (2Th 2:11; Rev 17:17; God remembering his covenant)~~ done in v21.


## 2026-10-08 — Strand updates — choosing (M64): 10.6 and 13.1 (2026-10-08, #1978)

**Strand:** choosing

**Method:** **Kept out:** no statement about God's character as a key to the human inner being (the image question is parked, #1984). "Once the words cross" in 10.6 restated as "the words can cross" (uncounted).
**Held:** God's wider choosing verses (rule 72 routing, 166 verses) are not placed in 13.1 until read in their passages (13.1 working note).
**Quote check:** all new quotes found in the ESV text; 10.6's two cross-verse quotes (Jam 4:1–2; Psa 78:30–31) checked by verse range.

**Not woven:** **Kept out:** no statement about God's character as a key to the human inner being (the image question is parked, #1984). "Once the words cross" in 10.6 restated as "the words can cross" (uncounted).
**Held:** God's wider choosing verses (rule 72 routing, 166 verses) are not placed in 13.1 until read in their passages (13.1 working note).
**Quote check:** all new quotes found in the ESV text; 10.6's two cross-verse quotes (Jam 4:1–2; Psa 78:30–31) checked by verse range.

**Notes:** **Researcher, verbatim:** *"update 10.6 and 13.1"*.

| Section | Was | Now | Verdict |
|---|---|---|---|
| 10.6 Wanting | — | Wanting beside choosing: 2Sa 19:38 ("desire" renders the choosing verb); desire (Isa 1:29), the soul's delight (Isa 66:3), envy (Pro 3:31), wanting weighed (Pro 3:15); desire carried through (2Cor 8:11); pointer to 10.7 | New |
| 13.0 | God bullet: anger (10.13), Spirit (Ch 6) | Adds pointer to 13.1 choosing | Widened |
| 13.1 Divine | Empty | "Choosing": he chooses (Deu 12:5; Act 15:7; Isa 66:4); eyes and delight as the measure (Isa 66:4; 56:4); acts first (Jos 24:3, 13; Isa 65:1–2); good, upright, holy (Psa 25:8, 14; Jos 24:19); knows the heart and gives (Act 15:8, 28; 2Cor 8:16); reasons, answers, judges (Isa 1:18; 56:3, 5; Job 42:7) | New |

**Kept out:** no statement about God's character as a key to the human inner being (the image question is parked, #1984). "Once the words cross" in 10.6 restated as "the words can cross" (uncounted).
**Held:** God's wider choosing verses (rule 72 routing, 166 verses) are not placed in 13.1 until read in their passages (13.1 working note).
**Quote check:** all new quotes found in the ESV text; 10.6's two cross-verse quotes (Jam 4:1–2; Psa 78:30–31) checked by verse range.

**Refs:** escalation 1978


## 2026-10-08 — Strand updates — choosing (M64): Ch 11 §4 five faces (2026-10-08, #1978)

**Strand:** choosing

**Notes:** **Researcher, verbatim:** *"update Ch 11 §4 with the five faces of choosing"*.

| Section | Was (v13) | Now (v14) | Verdict |
|---|---|---|---|
| §4 faces | — | "Good" or "evil" in your eyes (Jos 24:15; 2Sa 19:38; Isa 65:12) | New |
| §4 faces | — | Knowing good and evil (Isa 7:15; 2Sa 19:35, same verb and "good"; Job 34:4) | New |
| §4 faces | — | Refusing, *māʾas* (Isa 7:15; 8:6; Job 34:33; 42:6) | New |
| §4 faces | — | Choosing, *bāḥar* (Jos 24:15; Deu 23:16; Psa 119:30; Isa 66:3; Pro 16:16; Job 34:4) | New |
| §4 faces | — | Delight, *ḥāpēṣ* (Isa 66:3; 65:12; 56:4) | New |
| What changes the character | "What it is turned toward" (fear only) | Widened: refusing, knowing and choosing, each turned by what it is aimed at | Widened |
| What changes the character | — | New factor "Whose eyes, and whose delight" | New |

**Quote check:** 12 new quotes, 0 failures.

[Chapter versions, from the narrative index] 11 v15: §4 faces "Choosing a person" and "Holiness", factor "Who chooses", M64 §2b, #1978; 11 v14: choosing, M64 §2a, #1978, §4 five faces (good or evil in your eyes; knowing good and evil; refusing; choosing; delight), factor "Whose eyes, and whose delight", "What it is turned toward" widened

**Refs:** escalation 1978


## 2026-10-08 — Strand updates — choosing (M64), §2a: 10.7 reframed (2026-10-08, #1978)

**Strand:** choosing

**Sources:** ../../Clusters/M64 - will-resolve/m64-choosing-account-v1-20261007.md

**Original claims changed:** **Original claims changed:** none. The original essay's claims on choosing were already restated or withdrawn earlier (10.7 "if the soul wants, the heart sets direction … the spirit supplies energy", withdrawn 2026-10-01, #1921).

**Notes:** **Researcher, verbatim:** *"first build the 2a into the narrative 10.7.  you will need to reframe 10.7 to ensure 2a is part of a larger context of choosing and setting direction and not a disconnected list of paragraphs. you need to take into account what is already there, and also allow for other further research results that forms part of this chapter to fit in later."* Source: `../../Clusters/M64 - will-resolve/m64-choosing-account-v1-20261007.md` (21 verses read in their passages: test, batches 1–4).

**Original claims changed:** none. The original essay's claims on choosing were already restated or withdrawn earlier (10.7 "if the soul wants, the heart sets direction … the spirit supplies energy", withdrawn 2026-10-01, #1921).

| Section (10.7 v10) | Was (v9) | Now | Verdict |
|---|---|---|---|
| Opening | "Scripture speaks of setting, inclining, turning and directing the heart" + list | Opens from Joshua 24: the choice (24:15) and the inclined heart (24:23) in one speech; Isa 7:15 and Job 1:1 on refusing and choosing | Restated |
| The words | — | *bāḥar* (choose, desire, preferred), *māʾas* (refuse, reject, despise), *eklegomai*, *authairetos*; the direction verbs (incline, direct, set before) | New |
| Two sides | — | Refusing is choosing (Isa 7:12, 15; 8:6); not answering (Isa 65:12); in the negative (Pro 3:31); both sides and ends (Isa 1:16–20) | New |
| What a choice rests on | — | Knowing how (Isa 7:15; 1:3); being taught (Psa 25:4, 8, 12; 86:11; 119:29); the fear of the Lord (Psa 25:12; Jos 24:14); seen and remembered (Jos 24:17; Job 42:5; Psa 25:15); the chooser's own good (Deu 23:16; 2Sa 19:38) | New |
| What draws it | — | Desire, the soul's delight, envy, being pleased, earnestness, preferring (Isa 1:29; 66:3; Pro 3:31; Act 6:5; 2Cor 8:17; Pro 16:16; 3:15); pointer to 10.6 | New |
| Whose measure | — | The chooser's eyes, the Lord's eyes, the Lord's delight not met and met (one word), the soul's delight against his (Jos 24:15; Isa 65:12; 66:3–4; 56:4); "good in your eyes" honoured (2Sa 19:38) | New |
| Choosing before God | — | Choice after God has acted (Jos 24:3; Isa 65:1–2; Act 15:7); God at work and own accord, not set against each other (2Cor 8:3–5, 16–17; Act 15:28; Psa 119:32). "I read" limited to 2Cor 8 | New |
| Choosing together | — | Jos 24:21–22; Act 6:5; 15:25; Job 34:4 | New |
| A choice that is honoured | — | Deu 23:16; 2Sa 19:35, 38. The Deu 12 phrase echo is **held** (working note), not in the text | New |
| Choosing from weakness | — | Psa 119:28; 25:11, 16; Isa 56:3, 5; 2Sa 19:35; Job 36:21 | New |
| Fear and choosing | v9 paragraphs on fear stopping a choice, setting a direction, "fear not", the judges | Kept unchanged in substance, regrouped under one heading with prose leads | Stands |
| Setting the heart | v9 heart list (Jos 24:23; Psa 119:36; 1Sa 7:3; Psa 86:11; 12:2; 1Ki 11:4; Jer 7:24; Exo 35:21) | Kept; Jos 24:23 and 1Sa 7:3 set side by side (same words: put away the foreign gods, turn the heart); Psa 119:36 after the choice at 119:30 | Widened |
| Holding a choice | — | Jos 24:19, 21–22, 31; Psa 119:25, 30–31; Isa 56:4; Psa 25:21; 2Cor 8:11. Jos 24:31: "gives the timing; it does not give the cause" | New |
| Life and death set before a person | v9 paragraphs (Deu 30:19; Eze 18:28; Jer 21:8; Pro 14:12; Gen 25:32; 2Cor 5:15; Jam 4:14–15; Joh 6:27; Mat 7:14) | Kept, with prose leads and bullets; Ch 2 pointers kept | Stands |
| What follows a choice | — | Right: Psa 25:13–14; Pro 3:32; Isa 56:5, 7; Act 15:31, 33; 2Sa 19:39; Isa 7:15, 22. Wrong: Isa 1:29; 65:13–14; 66:4–5. The outcome answers the choice (Isa 65:11–12; 1:30; 66:4); the way back (Isa 1:18, 27) | New |
| Choices weighed by another | — | Job 15:5–6, 12; 34:3–4, 33; 36:21; the book's verdicts 1:8; 42:7; Job's turning 42:5–6 | New |
| What changes the character | — | Five faces: good/evil in your eyes; knowing good and evil; refusing; choosing; delight, each with its *why* | New |

**Cut from the account in the chapter text (let-Scripture-speak):**
- "I read this as the good that is chosen becoming the place the soul lives" (Psa 25:13 / Isa 7:15): the shared word is stated; the reading is not.
- "I read these as the same thing said in different figures" (Isa 65:11–12; 1:30; 66:4): each verse is given in its own figure.
- "I read this as the law giving the slave a small share of the kind of choosing the Lord keeps" (Deu 23:16 / 12:5): held in the working note.
- The Psa 119:25/31 "cling" sentence was restated so it does not say "the soul" of 119:31, where the verse does not.

**Quote check:** 10.7 v10, 145 quotes, 0 failures (3 matched by direct lookup where the checker misread the cited book: Isa 65:1, 65:2, Pro 3:31).
**Quoted share:** v9 54% → v10 39%.
**Not yet updated (touched by this material):** ~~Ch 11 §4 (five faces of choosing)~~ done in v18; ~~10.6~~ and ~~13.1~~ done in v19; 10.6 (desire and delight beside the choice); 13.1 (God's choosing, when the routed verses are placed).

**Refs:** escalation 1978

**Quote check:** 145 parts, 0 failures. **Quote check:** 10.7 v10, 145 quotes, 0 failures (3 matched by direct lookup where the checker misread the cited book: Isa 65:1, 65:2, Pro 3:31).
**Quoted share:** v9 54% → v10 39%.
**Not yet updated (touched by this material):** ~~Ch 11 §4 (five faces of choosing)~~ done in v18; ~~10.6~~ and ~~13.1~~ done in v19; 10.6 (desire and delight beside the choice); 13.1 (God's choosing, when the routed verses are placed).


## 2026-10-07 — Structure: Ch 13 becomes "Other beings", with 13.1 Divine, 13.2 Angels, 13.3 Other spirits and 13.4 Nature. 13.

**Strand:** choosing (M64)


## 2026-10-07 — **new**, empty

**Notes:** [Chapter versions, from the narrative index] 13.1 v1: **new**, empty


## 2026-10-07 — **new, replaces the pointer to 10.13**, #1982: why the chapter is included, and what has been found so far; old v10 poin

**Notes:** [Chapter versions, from the narrative index] 13 v1: **new, replaces the pointer to 10.13**, #1982: why the chapter is included, and what has been found so far; old v10 pointer and earlier versions in `archive/`

**Refs:** escalation 1982


## 2026-10-05 — Structure: Ch 13 "Under God's anger" folded into 10.13 as its section *Living under God's anger*. Ch 13's secti

**Strand:** Ch 13 into 10.13 (#1977, OT-13)

**Refs:** escalation 1977, thread OT-13


## 2026-10-05 — Structure: The anger material on the heart, soul, spirit, flesh and conscience woven into Chapters 4–8. New Ch 

**Strand:** anger (M02) and the inner seat (M47): the M47 step (#1974, OT-18)

**Refs:** escalation 1974, thread OT-18


## 2026-10-05 — Structure: New 10.13 "Anger", after 10.12, with no renumbering, following the #1961 precedent for key character

**Strand:** anger (M02), units 1–5, overview v2 (#1963, #1966–#1969, #1973, #1974)

**Refs:** escalation 1963, escalation 1966, escalation 1969, escalation 1973, escalation 1974, escalation 1961, escalation 1947, thread OT-13


## 2026-10-05 — anger and the soul, M47 step, #1974; was Ch 4, renumbered 2026-10-02, #1936

**Notes:** [Chapter versions, from the narrative index] 05 v3: anger and the soul, M47 step, #1974; was Ch 4, renumbered 2026-10-02, #1936; 07 v6: Ecc 11:10, M47 step, #1974; was Ch 6, renumbered 2026-10-02, #1936; anger, fear strands; 08 v5: conscience beside the wrath, Rom 13:5, M47 step, #1974; was Ch 7, renumbered 2026-10-02, #1936; anger strand

**Refs:** escalation 1974, escalation 1936


## 2026-10-05 — anger and the heart, M47 step, #1974 ("The heart and anger")

**Notes:** [Chapter versions, from the narrative index] 04 v11: anger and the heart, M47 step, #1974 ("The heart and anger"); 06 v7: anger and the spirit, M47 step, #1974 (held back, heated, pressed, embittered; the Spirit with anger; grieved)

**Refs:** escalation 1974


## 2026-10-05 — Ch 13 folded into 10.13 (2026-10-05, #1977, OT-13)

**Sources:** wa-essay-narrative-ch13-into-10-13-crosscheck-v1-20261005.md

**Original claims changed:** **Original claims changed:** none. Ch 13's statements move unchanged into 10.13 v2, under *Living under God's anger*, with these exceptions:
- **Cut as uncounted superlatives** (let-Scripture-speak):
  - "Scripture speaks of God's anger far more often than of human anger" (10.13 already says "more often", by count)
  - "in the middle of the hardest book" → "in the middle of Lamentations"
- **Merged, not repeated:**
  - "Why it is held back" and "For a moment" were already in 10.13; Isa 48:9 is added to 10.13's list.
  - 10.13 v1's "The ones who bear it for others" goes into *Pleading, and standing in the breach* (Moses "because of you", Aaron, David).
  - Daniel 8:18 and 11:35 go into *Bearing it*.
- **Pointers:** Ch 2 section names now in italics. Two bare references given their books (Psa 88:16; Lam 5:22).

**Notes:** **Researcher, verbatim:** *"1977 - correct, ch13 becomes part of ch10.13"*. Proposal: `wa-essay-narrative-ch13-into-10-13-crosscheck-v1-20261005.md`.

**Original claims changed:** none. Ch 13's statements move unchanged into 10.13 v2, under *Living under God's anger*, with these exceptions:
- **Cut as uncounted superlatives** (let-Scripture-speak):
  - "Scripture speaks of God's anger far more often than of human anger" (10.13 already says "more often", by count)
  - "in the middle of the hardest book" → "in the middle of Lamentations"
- **Merged, not repeated:**
  - "Why it is held back" and "For a moment" were already in 10.13; Isa 48:9 is added to 10.13's list.
  - 10.13 v1's "The ones who bear it for others" goes into *Pleading, and standing in the breach* (Moses "because of you", Aaron, David).
  - Daniel 8:18 and 11:35 go into *Bearing it*.
- **Pointers:** Ch 2 section names now in italics. Two bare references given their books (Psa 88:16; Lam 5:22).

**Quote check:** 10.13 v2, 397 quotes, 0 failures.
**Structure:** Ch 13 v10 is a pointer. Twelve chapters still say "Chapter 13" (index Structure log); they resolve through the pointer until each is next touched.

[Chapter versions, from the narrative index] 10.13 v2: **Ch 13 folded in** as the section *Living under God's anger*, #1977

**Refs:** escalation 1977, thread OT-13

**Quote check:** 397 parts, 0 failures. **Quote check:** 10.13 v2, 397 quotes, 0 failures.
**Structure:** Ch 13 v10 is a pointer. Twelve chapters still say "Chapter 13" (index Structure log); they resolve through the pointer until each is next touched.


## 2026-10-05 — Strand updates — anger and the inner seat (M02 × M47): Chapters 4–8 (2026-10-05, #1974, OT-18)

**Strand:** anger and the inner seat

**Sources:** _analytics/Clusters/M02 - anger-wrath/anger-m47-seat-ledger-v1-20261005.md

**Original claims changed:** **Original claims changed:** none. The "spirit/heart division of labour" for anger (U1 §38 point 2) stays **withdrawn**. It is not used.

**Notes:** **Sources:** `_analytics/Clusters/M02 - anger-wrath/anger-m47-seat-ledger-v1-20261005.md` (MS-01 to MS-31), from U1 §38, U2 §66, the U1/U2 seat lines and overview v2 part M.
**Researcher, verbatim (2026-10-05):** *"M47 has already been documented in the narration and the narration must be updated with the what does this multi cluster connection actually do or mean."*

**Original claims changed:** none. The "spirit/heart division of labour" for anger (U1 §38 point 2) stays **withdrawn**. It is not used.

**Statements of the narrative that are new:**
- **Ch 4 "The heart and anger" (new section).** The heart is named in an anger:
  - before it (Est 5:9; 2Ch 26:16, where the Hebrew has the heart lifted up)
  - where it is kept and planned (Job 36:13; Pro 6:14; Gen 27:41)
  - where it is taken to counsel (Neh 5:7, where the Hebrew is "my heart took counsel")
  - raging at God (Pro 19:3)
  - carrying vexation and cleared of it (Ecc 2:23; 7:3; 11:10)
  - what must not faint before another's anger (Isa 7:2, 4)
  - misreading another's heart (1Sa 17:28)

  Under God's anger it provokes, turns, is to be torn or circumcised, does not take it in, and rejoices. The other party's heart is named in Mar 3:5 and Act 7:54. **The count stated** (narratives rarely name the angry person's own heart; the wisdom books often do) is U1 §38's count, given without its "so that" clause.
- **Ch 5:** the soul in anger: worn by vexation (Psa 31:9; 1Sa 1:6, 10), torn by its own anger (Job 18:4), kept from the company of the angry (Gen 49:6), snared (Pro 22:24–25).
- **Ch 6:** the spirit held back or cool (Ecc 7:8; Pro 17:27), provoked and followed by reasoning (Act 17:16–17), pressed until it speaks (Job 32:18–20), embittered with rash lips, whose spirit left open (Psa 106:33), receiving God's anger (Job 6:4), and what would faint (Isa 57:16; Num 16:22). Under God's Spirit: the Spirit comes and anger follows (1Sa 11:6; Judg 14:19), ending in mercy (1Sa 11:13); the Spirit grieved before the anger list (Eph 4:30–31).
- **Ch 7:** heart and body in one command (Ecc 11:10).
- **Ch 8:** conscience beside the fear of wrath (Rom 13:5). This is new as a reading (U2 §66).

**Correction made in 10.13 during this step:** Judg 14:19 is at Ashkelon, not Lehi (Lehi is Judg 15). The 10.13 text is corrected.

**Quote check:** every new passage, 0 failures. **Flags found in text this step did not write** (left as they were, for a later pass):
- Ch 4: line 24, a quote attributed to Isa 14:13 and Psa 10:6 that is not in either verse; two section titles in quotation marks
- Ch 5: "seek my life", "save his life", "life for life", with no verse in the row
- Ch 7: the John 6 quotes read as 2Cor 6 (the book carried from the line before)
- Ch 8: "God is greater than our heart" cited to 1Jo 3:19; it is 3:20

**OT-18:** resolved by this step (register updated).

**Refs:** escalation 1974, thread OT-18


## 2026-10-05 — Strand updates — anger (M02): new 10.13 "Anger" (2026-10-05, #1963 step 4, #1974)

**Strand:** anger

**Sources:** _analytics/Clusters/M02 - anger-wrath/anger-cross-ledger-overview-v2-20261005.md

**Original claims changed:** **Original claims changed:** none in this step.

**Notes:** **Sources:** anger units 1–5 (#1966–#1969, #1973); `_analytics/Clusters/M02 - anger-wrath/anger-cross-ledger-overview-v2-20261005.md` (parts A–D, F, G, H); U1 and U2 (approved #1888, #1898); the 2026-10-01 strand ledger.
**Researcher, verbatim (2026-10-05):** *"M47 after the overview revision; archive them, proceed through to the generation of the ch 13 narrative and the updated M47 related chapters."* The #1961 precedent (a key characteristic gets its own Ch 10 sub-chapter) is followed.

**Original claims changed:** none in this step.

**Statements of the narrative that are new, or stated differently from earlier chapters:**
- **The words are set out by party.** God and people share most of the anger words. A few are kept almost wholly for God: *ḥārôn*, "burning", is God's every time it is anger, *qeṣep̄* and *zaʿam* nearly always are, and *orgē* is in most of its uses. *Orgizō* is never God's own anger. (No earlier chapter says this.)
- **God's heart named with his anger, three times** (Hos 11:8–9; Jer 23:20; Isa 63:4–5). Ch 13 quoted Jer 23:20 and Hos 11:9, but not Hos 11:8's heart line or Isa 63:4.
- **The responses to God's anger as one set** (22 items, each with its verse). Ch 13 gives them as sections. 10.13 lists the set, and Ch 13 keeps the detail.
- **Those who bear it for others:** Moses "because of you", Aaron between the dead and the living, David asking to bear it alone, Job praying for his friends, no one found for the breach.
- **Those who carry it out:** Assyria with a heart of its own; Babylon and Israel's army exceeding the commission; Saul judged for not carrying it out; the authority, "for the sake of conscience" (Rom 13:5).
- **Restraint by stated reasons, now seven,** adding "I have no wrath" (Isa 27:4) and "for I am merciful" (Jer 3:12).
- **Jesus' indignation:** one Greek word is aimed three ways (Jesus, the disciples, the ruler of the synagogue). 10.1 holds the three beside each other under *Feeling* (OT-12).
- **A person's anger followed into what it does next, 14 ways,** including counsel, prayer, fear and mercy. It is not only harm.
- **"Be angry and do not sin" and "put away … anger"** are set side by side, five verses apart, and not reconciled.

**Statements elsewhere that 10.13 does not repeat** (for the Ch 13 cross-check, OT-13, and the Ch 10 retune, OT-14):
- **10.10:** "the answer to anger is most often a question or a reframing". The word "most" was never counted. 10.13 says "In several passages". **RS** proposed for 10.10.

**Let-Scripture-speak cuts made while writing:**
- "The difference between the two angers is carried by what the verses say about them, not by the words alone" → cut (a conclusion no verse states)
- "the anger that the verses most often speak of as turning" → "Many of its verses speak of it turning" (the superlative was not counted across words)
- "very often a question or a reframing" → "In several passages"
- "Inside the hardest of the laments" → "In Lamentations"
- "done to his face" → the verse added: "a people who provoke me to my face continually" (Isa 65:3)

**Quote check:** 265 quotes, 0 failures. One misquote was corrected first: Jer 6:11 begins "Therefore I am full of the wrath of the Lord", not "But".

**Structure:** 10.13 is added after 10.12, with no renumbering. **Ch 13 is not changed.** It is to be consolidated into 10.13 later (OT-13, ruling 6.3). The heart and spirit material in the anger verses follows in the M47 step.

[Chapter versions, from the narrative index] 10.13 v1: **new**, #1963 step 4: the full account of anger, as its own sub-chapter

**Refs:** escalation 1963, escalation 1974

**Quote check:** 265 parts, 0 failures. **Statements of the narrative that are new, or stated differently from earlier chapters:**
- **The words are set out by party.** God and people share most of the anger words. A few are kept almost wholly for God: *ḥārôn*, "burning", is God's every time it is anger, *qeṣep̄* and *zaʿam* nearly always are, and *orgē* is in most of its uses. *Orgizō* is never God's own anger. (No earlier chapter says this.)
- **God's heart named with his anger, three times** (Hos 11:8–9; Jer 23:20; Isa 63:4–5). Ch 13 quoted Jer 23:20 and Hos 11:9, but not Hos 11:8's heart line or Isa 63:4.
- **The responses to God's anger as one set** (22 items, each with its verse). Ch 13 gives them as sections. 10.13 lists the set, and Ch 13 keeps the detail.
- **Those who bear it for others:** Moses "because of you", Aaron between the dead and the living, David asking to bear it alone, Job praying for his friends, no one found for the breach.
- **Those who carry it out:** Assyria with a heart of its own; Babylon and Israel's army exceeding the commission; Saul judged for not carrying it out; the authority, "for the sake of conscience" (Rom 13:5).
- **Restraint by stated reasons, now seven,** adding "I have no wrath" (Isa 27:4) and "for I am merciful" (Jer 3:12).
- **Jesus' indignation:** one Greek word is aimed three ways (Jesus, the disciples, the ruler of the synagogue). 10.1 holds the three beside each other under *Feeling* (OT-12).
- **A person's anger followed into what it does next, 14 ways,** including counsel, prayer, fear and mercy. It is not only harm.
- **"Be angry and do not sin" and "put away … anger"** are set side by side, five verses apart, and not reconciled.

**Quote check:** 265 quotes, 0 failures. One misquote was corrected first: Jer 6:11 begins "Therefore I am full of the wrath of the Lord", not "But".


## 2026-10-04 — Structure: New 10.12 "Fear", after 10.11, with no renumbering. Researcher, verbatim: *"I think you must encapsu

**Strand:** fear (M01), units 3–4, overview (#1957, #1958, #1960, #1961)

**Refs:** escalation 1957, escalation 1958, escalation 1960, escalation 1961, escalation 1920, thread OT-12


## 2026-10-04 — Structure: Ch 2 "The inner person dying" reworked as "Soul, spirit and heart at death": the soul's several face

**Strand:** life and death (M25), Q2 and Q3 (#1950)

**Refs:** escalation 1950


## 2026-10-04 — Structure: New Ch 2 section "Sleep and waking", before "Life weighed": the verses' own picture of death as slee

**Strand:** life and death (M25), unit 4 (#1949)

**Refs:** escalation 1949, escalation 1942


## 2026-10-04 — Structure: Two new Ch 2 sections: "Living before God" after "Life set before a person" (the oath by the Lord's 

**Strand:** life and death (M25), unit 3 (#1940)

**Refs:** escalation 1940


## 2026-10-04 — Strand updates — fear (M01): new 10.12 "Fear" (2026-10-04, #1961)

**Strand:** fear

**Sources:** _analytics/Clusters/M01 - fear-awe/fear-cross-ledger-overview-v1-20261004.md

**Original claims changed:** **Original claims changed:** none. 9-4 stays restated (10.12 quotes 2Ti 1:7–8 with its setting). 8-2 stays **Held**.

**Notes:** **Sources:** fear units 1–4, the unit 3 addendum (H4172A), and `_analytics/Clusters/M01 - fear-awe/fear-cross-ledger-overview-v1-20261004.md` (§A–§F).
**Researcher, verbatim:** *"I think you must encapsulate the full finding of fear, as it emerged from the ledgers, the cross ledger review and the co-existence review into a separate Ch10 sub chapter."*

**Original claims changed:** none. 9-4 stays restated (10.12 quotes 2Ti 1:7–8 with its setting). 8-2 stays **Held**.

**Statements of the narrative that are new, or stated differently from 10.1:**
- **1Jo 4:18 is limited to its setting.** 10.1 says it is the verse "closest to saying what fear itself is". 10.12 says it is said of fear before judgment (4:17), and not of every fear.
- **"The fear of a threat makes a person run" (10.1) is not repeated.** The verses also show fear of a threat turning to trust, coming forward, telling the truth, and glorifying God.
- **"Fear and trembling" is counted.** The phrase is in five New Testament verses, each with coming near. Mark 16:8 is shown as trembling with flight.
- **The two fears before God as Father** (1Pe 1:17; Rom 8:15) are set side by side. Mal 1:6 states father and fear in one verse.
- **Respect and fear** are one Greek word (Rom 13:3, 7; 1Pe 3:14–15). The verse does not say toward whom the respect in 1Pe 3:15 is directed.

**Let-Scripture-speak cuts made while writing:**
- "Jesus himself was afraid" → "Jesus himself was distressed" (Mar 14:33)
- "It brings what terror does not bring" → "The verses join it to"
- "nearly always with a reason" → "a reason is given"
- "runs through every part of life" and "nearly every activity" → plain wording

**Structure:** 10.12 is added after 10.11, with no renumbering. 10.1's "Fear" section overlaps it. That is held with the 10.1 frame question (OT-12).

**Refs:** escalation 1961


## 2026-10-04 — Strand updates — fear (M01), unit 4: the Greek words (2026-10-04, #1958)

**Strand:** fear

**Researcher:** approve 1958, hold the weave.

**Sources:** _analytics/Clusters/M01 - fear-awe/fear-observation-ledger-unit4-v1-20261004.md

**Original claims changed:** **Original claims changed:** none.
- **9-4** ("spirit of fear", 2Ti 1:7): the Greek reading is done (FE-137). **The restatement stands.** The setting adds to it: the "spirit not of fear" is what lets Timothy "not be ashamed of the testimony about our Lord" and "share in suffering for the gospel" (2Ti 1:6–8). In Rom 8:15, fear goes with "the spirit of slavery", set against "the Spirit of adoption". No verse names a spirit-being of fear.
- 8-2 stays **Held**.

**Notes:** **Ledger:** `_analytics/Clusters/M01 - fear-awe/fear-observation-ledger-unit4-v1-20261004.md` (FE-121 to FE-162).
- Unit 4 covers the 22 Greek M01 Strong's: 183 hits in 162 verses. With unit 3 (Hebrew and Aramaic, #1957) and the unit 3 addendum (H4172A, 10 hits that had fallen between units 2 and 3; corrected 2026-10-04), every M01 word has now been read.
- Approved by the researcher: *"approve 1958, hold the weave."* No chapter text is written from it.

**Original claims changed:** none.
- **9-4** ("spirit of fear", 2Ti 1:7): the Greek reading is done (FE-137). **The restatement stands.** The setting adds to it: the "spirit not of fear" is what lets Timothy "not be ashamed of the testimony about our Lord" and "share in suffering for the gospel" (2Ti 1:6–8). In Rom 8:15, fear goes with "the spirit of slavery", set against "the Spirit of adoption". No verse names a spirit-being of fear.
- 8-2 stays **Held**.

**No structure change.** The weave is held with unit 3 (OT-10).

**Refs:** escalation 1958


## 2026-10-04 — Strand updates — life and death (M25), Q2 and Q3: soul, spirit and heart at death (2026-10-04, #1950)

**Strand:** life and death

**Researcher:** prepare 1950 for approval and then adding it to the narrative

**Sources:** _analytics/Clusters/M25 - life-death/life-death-q2-q3-soul-spirit-heart-ledger-v1-20261004.md

**Original claims changed:** **Original claims touched:**

**Notes:** **Ledger:** `_analytics/Clusters/M25 - life-death/life-death-q2-q3-soul-spirit-heart-ledger-v1-20261004.md` (Q2-01 to Q2-12, Q3-01 to Q3-04). Co-occurrence pulls: Q2, soul, spirit and breath with death words, 123 hits / 111 verses; Q3, heart with death words, 23 hits / 21 verses. Supplement §H: Luk 23:42–43; Phili 1:21–24; 2Cor 5:6–9.
- **Instruction:** the researcher, verbatim: *"prepare 1950 for approval and then adding it to the narrative"* (#1950 set ready for approval; woven with all four §F decisions as recommended).

**Original claims touched:**

| # | Before (verdict) | Evidence now read | Now |
|---|---|---|---|
| 3-9 | Soul to Sheol, so different destinations: **Restated** | Count of soul-delivered verses: 12 of 15 rescue from dying; Psa 49:15 and 16:10 look beyond death; Psa 89:48 none can | **Restated** (verdict unchanged); the restatement's wording corrected in place |
| 6-2 | Survival after death: **Restated** | Psa 49:15 ("he will receive me") and 49:19 ("his soul will go to the generation of his fathers"); Luk 23:43; Phili 1:23; 2Cor 5:8; 1Pe 4:6 | No change of verdict; more witnesses, set side by side |

**The narrative's own statements this change made:**

| Where | Before | After | Kind |
|---|---|---|---|
| Ch 2 "The inner person dying" → **"Soul, spirit and heart at death"** | "At death, Scripture gives each inner word its own verb", with one verb per word (the soul departs) | The soul departs, **dies** (Num 23:10; Judg 16:30, literally *let my soul die*; Eze 18:4), is **poured out** (Isa 53:12; Mat 26:38), is named to the end (Num 19:11), has **two ends beyond death** in Psalm 49 (49:10, 15, 19), and is not abandoned (Psa 16:10 with Act 2:31). The spirit is committed and returns; the body without it is dead; "who knows" (Ecc 3:21, moved here). "No verse sends the soul one way and the spirit another." The heart is named "while they live" (Ecc 9:3), and "I have found no verse that speaks of the heart after death." One reading marked "I read" | **Restated** (one verb per word was too narrow); NS |
| Ch 2 "Delivered from death" | "almost always about a living person rescued from dying" (uncounted); Psa 16:10 in the list | "most of them": 12 of 15, with 2 beyond death and 1 none can; Psa 16:10 moved | **Restated** (uncounted superlative) |
| Ch 2 "After death" | With God: five bullets | Adds Psa 49:15; Luk 23:43; Phili 1:23–24; 2Cor 5:8 (with 5:4 side by side); 1Pe 4:6. From this side: adds Psa 49:19 | Widened (side by side, unreconciled) |
| Ch 4 | — | Pro 10:21 ("lack of sense", literally *heart*); Eze 18:31; Rom 10:9 ("from the dead"); nothing on the heart after death | Widened |

**Quote check:** Ch 2 v11: 479 checked; new flags are section titles and the label "delivered from" only. Ch 4 v10: one section title. Ledger: 87 fragments, 0 verse-text failures.

[Chapter versions, from the narrative index] 02 v11: **life-death Q2 and Q3**: "The inner person dying" reworked into "Soul, spirit and heart at death"; "Delivered from death" restated by count; "After death" widened, #1950; 04 v10: life-death Q3, the heart and death, #1950

**Refs:** escalation 1950

- **3-9** claim restated (recorded, 2026-10-04)
  - claim before: These verses speak of the soul delivered or brought up from Sheol: a living person rescued from death. Sheol here is death and the grave, not a destination distinct from the spirit's. Ecc 3:21 leaves the spirit's destination open ("Who knows?"). The "different destinations" argument, which the original called "the most compelling evidence", does not hold (G §16.4; dep §3.9)
  - claim after: Most of these verses speak of the soul delivered or brought up from Sheol: a living person rescued from death. Corrected 2026-10-04 (#1950): of 15 soul-delivered verses, 12 are rescue from dying; Psa 49:15 (set against the death of all, 49:10) and Psa 16:10 (as Act 2:27, 31 read it) look beyond death; Psa 89:48 says no one can. The verdict holds: no verse gives soul and spirit different destinations. Sheol here is death and the grave, not a destination distinct from the spirit's. Ecc 3:21 leaves the spirit's destination open ("Who knows?"). The "different destinations" argument, which the original called "the most compelling evidence", does not hold (G §16.4; dep §3.9)
  - note: evidence and restatement cell changed \| version note: life and death Q2 and Q3, soul, spirit and heart at death, #1950

## 2026-10-04 — Strand updates — life and death (M25), unit 4: roused and stirred (2026-10-04, #1949)

**Strand:** life and death

**Researcher:** approved, proceed with H6974 and the weave

**Sources:** _analytics/Clusters/M25 - life-death/life-death-observation-ledger-unit4-v1-20261004.md

**Original claims changed:** **Original claims touched:**

**Not woven:** **Ledger:** `_analytics/Clusters/M25 - life-death/life-death-observation-ledger-unit4-v1-20261004.md` (LD-143 to LD-155). H5782: 78 hits / 64 verses, faces W01–W17; supplement §H, H6974 (tagged T3): 22 hits / 21 verses. The inner-being faces of H5782 (49 hits) are handed to #1942, not woven. Written with meaning in setting and implication (#1943).
- **Approval:** the researcher, verbatim: *"approved, proceed with H6974 and the weave"* (#1949), with all four §F decisions as recommended.

**Notes:** **Ledger:** `_analytics/Clusters/M25 - life-death/life-death-observation-ledger-unit4-v1-20261004.md` (LD-143 to LD-155). H5782: 78 hits / 64 verses, faces W01–W17; supplement §H, H6974 (tagged T3): 22 hits / 21 verses. The inner-being faces of H5782 (49 hits) are handed to #1942, not woven. Written with meaning in setting and implication (#1943).
- **Approval:** the researcher, verbatim: *"approved, proceed with H6974 and the weave"* (#1949), with all four §F decisions as recommended.

**Original claims touched:**

| # | Before (verdict) | Evidence now read | Now |
|---|---|---|---|
| 3-10 | Conscious existence after death: **Stands** (side by side) | Isa 14:9–10, the shades greet the dead king, is a **taunt** (14:4). It is not read as teaching, and is held in OT-03 | No change |

**The narrative's own statements this change made:**

| Where | Before | After | Kind |
|---|---|---|---|
| Ch 2, new "Sleep and waking" (before "Life weighed") | Death as sleep was one paragraph in "What death is" | One account in the verses' own picture: Job 14:7, 12–15 (no waking "till the heavens are no more", and the plea "remember me!"); Jer 51:39 (a perpetual sleep in judgment); 2Ki 4:31–35 ("The child has not awakened"); Mat 9:24; Joh 11:13; 1Th 4:14 (moved here); Psa 3:2, 5–6; 139:18 (waking kept by God); the call to God to wake where life is at stake (Psa 7:5–6; 35:17, 23; 44:22–23; 59:3–4; 80:2, 18), with Psa 121:4 **side by side, unreconciled**, and Rom 8:36–37; the dead waking (Dan 12:2; Isa 26:14, 19; Psa 17:15) beside Job's "he will not awake", unreconciled. Two readings marked "I read" | New (NS) |
| Ch 2 "Breath lent" | Psa 78:39 | Psa 78:38–39 together: "did not destroy them … did not stir up all his wrath". "The people lived because his wrath was not stirred" | Widened |
| Ch 2 "Living before God" | The living God against idols | Adds Hab 2:18–20 (no breath to wake; "the Lord is in his holy temple") | Widened |
| Ch 2 "Made alive" | The making alive rests on a death | Adds Zec 13:7 with Mat 26:31 | Widened |
| 10.9, new "Calling on God to wake"; Ch 11 §4 "Who rouses, and toward what"; Ch 12 (Isa 14:4, 10–11, under pride); Ch 13 (Psa 78:38 elision restored) | — | Short passages pointing back to Ch 2 | Widened |

**Quote check:** Ch 2 v10, 459 checked: the 14 older flags, plus two section titles and the phrase "he will not awake" (Job 14:12, named just above). 10.9: one section title. Ch 11, 12 and 13: no new flags. Ledger: 84 fragments, 0 verse-text failures.

[Chapter versions, from the narrative index] 02 v10: **life-death unit 4, roused and stirred**: new section "Sleep and waking" before "Life weighed" (death as sleep moved into it), #1949; 10.9 v14: life-death unit 4, roused and stirred, #1949 ("Calling on God to wake"); 11 v13: life-death unit 4, roused and stirred, #1949, §4 "Who rouses, and toward what"; 12 v12: life-death unit 4, roused and stirred, #1949

**Refs:** escalation 1949


## 2026-10-04 — Strand updates — life and death (M25), unit 3: living before God (2026-10-04, #1940)

**Strand:** life and death

**Researcher:** approve 1940 as recommended

**Sources:** _analytics/Clusters/M25 - life-death/life-death-observation-ledger-unit3-v1-20261003.md

**Original claims changed:** **Original claims touched:**

**Notes:** **Ledger:** `_analytics/Clusters/M25 - life-death/life-death-observation-ledger-unit3-v1-20261003.md` (LD-92 to LD-142). It covers 690 hits in 629 verses (H2416A, H2416E, G2198, G2222, H0748), with faces L01–L32. The supplement §B.19 adds H2416C / H2416D (109 hits, LD-139 to LD-142, faces L33–L36).
- **Approval:** the researcher, verbatim: *"approve 1940 as recommended"* (chat, 2026-10-04). The four decisions: (1) a new Ch 2 section "Living before God"; (2) a new Ch 2 section "Life weighed", before "Facing death"; (3) LD-101 and LD-102 side by side, unreconciled; (4) the H2416C supplement read first. LD-106 is held in OT-01.

**Original claims touched:**

| # | Before (verdict) | Evidence now read | Now |
|---|---|---|---|
| 3-10 | Conscious existence after death: **Stands** (set side by side, v10) | "for all live to him" (Luk 20:38); "whether we are awake or asleep we might live with him" (1Th 5:10), added to the "with God" list (LD-126) | No change of verdict. More witnesses on the "with God" side; still unreconciled |
| 10-1, 10-2 | The Spirit and new life | "the Spirit is life because of righteousness" (Rom 8:10); "the law of the Spirit of life" (Rom 8:2); "If we live by the Spirit" (Gal 5:25) (LD-127) | No change. Woven into Ch 14 as text |

**The narrative's own statements this change made:**

| Where | Before | After | Kind |
|---|---|---|---|
| Ch 2, new "Living before God" | The opening says life is "lived before him"; no section said it | The oath by the Lord's life and by the life of the one spoken to (1Sa 20:3; 2Ki 2:2; 2Sa 15:21; 1Ki 1:29; 17:1; Job 27:2); the same oath in anger, rashness and greed (2Sa 12:5; 1Sa 14:45; 2Ki 5:20), judged (Jer 5:2; 4:2); God's own oath (Eze 33:11; 20:3; Rom 14:11); the living God (Jer 10:10; 1Th 1:9; Psa 42:2; 84:2; Heb 3:12; 10:31; 2Sa 22:47); the days of a life (Deu 4:10; 17:19; 16:3; Psa 146:2; 27:4; Gen 47:9); the land of the living (Psa 27:13; 142:5; Isa 38:11; 1Sa 25:29). One reading marked "I read" (the oath binds the speaker by life) | New |
| Ch 2, new "Life weighed" | — | Life loathed (Job 10:1; Gen 27:46; Ecc 2:17; Job 3:20), worn down (Psa 31:10; 88:3; Deu 28:66; 2Cor 1:8), the living weighed (Ecc 9:4, 3; Psa 143:2), enjoyed (Ecc 9:9; 5:20), and what life does not consist in (Luk 12:15; 1Ti 6:19; 1Cor 15:19; Joh 12:25). One reading marked "I read" (the difference lies in what each verse sets life beside) | New |
| Ch 2 "Life set before a person" | Deu 30:19; doing, seeking, holding on; the death side | Adds Deu 30:6 (God circumcises the heart, "that you may live"); long days (Exo 20:12; Deu 6:2; 1Pe 3:10) **beside** the wicked who prolongs his life (Ecc 7:15; 8:12). "Scripture states both. I leave them side by side." | Widened (contradiction shown, not resolved) |
| Ch 2 "Where life flows from" | Pro 4:23; 14:30; Ecc 3:11; Psa 90:12; Deu 8:3; Psa 36:9; Deu 30:20; Col 3:4; Joh 11:25; 17:3 | Adds Pro 13:12; 15:4; Jer 2:13; Joh 4:14; 5:26; 14:19 | Widened |
| Ch 2 "Life breathed in" | Gen 2:7 | Adds the tree of life (Gen 2:9; 3:24; Rev 2:7) | Widened |
| Ch 2 "Breath lent, and held by God" | Breath given and taken | Adds Job 7:7; Jam 4:14–15 | Widened |
| Ch 2 "Life asked for" | For oneself, others, a people | Adds Psa 74:19 (the poor) | Widened |
| Ch 2 › *Death in the living* | Six bullets | Adds "called alive and be dead" (Rev 3:1; 1Ti 5:6; Eph 4:18) | Widened |
| Ch 2 "Delivered from death" | Job 33:24, 28 (two lines) | Elihu's account read whole (Job 33:20, 22, 24, 26–30): pain, the soul near the pit, the ransom, prayer, joy, confession, "the light of life" | Widened |
| Ch 2 "Made alive" | — | Eternal life had now and to come (Joh 6:47; 1Jo 5:13; Mar 10:30), both stated; Gal 2:19–20; Rom 12:1; 1Pe 2:24 | Widened |
| Ch 2 "Life, and judgment" | Second death | Adds the books (Rev 20:12, 15) and 2Ti 4:1 | Widened |
| Ch 2 "After death" | Dead with God (three bullets) | Adds Luk 20:38; 1Th 5:10 | Widened |
| Ch 4, 6; 10.1–10.7, 10.9, 10.10; Ch 11 §4; Ch 12; Ch 13; Ch 14 | — | Short passages, each pointing back to Ch 2 (ledger "Woven — where"). 10.4 gains "Thinking and life"; 10.5 "The oath"; 10.9 "The living God"; 10.10 "Loyalty and honour". Ch 11 §4 gains "Who swears it, and what for" and "What it is joined to" | Widened |

**Correction to the ledger:** LD-119 marked Psa 27:13 "(in Ch 2)". A text search found it in no chapter. It is now in Ch 2 "Living before God".

**Quote check:** every quote was checked against iba.db `verse` (ESV, `--prose`).
- **Ch 2 v9:** 428 checked (339 before). The 14 flags are the same as in v8 (gloss labels, the carried-book noise on older lines, and Psa 116:9, which is missing from iba.db, #1891). **No new flag.**
- **Other chapters:** every new verse quote passes. The only new flags are section titles in quotation marks ("Living before God", "Life weighed", "Delivered from death", "Death in the living", "Life set before a person", "Breath lent", "Made alive") and the label "fear not" in 10.1. None of them is a verse quote.

[Chapter versions, from the narrative index] 02 v9: **life-death unit 3, living before God**: new sections "Living before God" (after "Life set before a person") and "Life weighed" (before "Facing death"); long days and the wicked who prolongs his life set side by side; Elihu's account (Job 33) read whole, #1940; 04 v9: life-death unit 3, living before God, #1940; 06 v6: life-death unit 3, living before God, #1940; 10.1 v11: life-death unit 3, living before God, #1940; 10.2 v9: life-death unit 3, living before God, #1940; 10.3 v5: life-death unit 3, living before God, #1940; 10.4 v6: life-death unit 3, living before God, #1940 ("Thinking and life"); 10.5 v12: life-death unit 3, living before God, #1940 ("The oath"); 10.6 v7: life-death unit 3, living before God, #1940; 10.7 v9: life-death unit 3, living before God, #1940; 10.9 v13: life-death unit 3, living before God, #1940 ("The living God"); 10.10 v11: life-death unit 3, living before God, #1940 ("Loyalty and honour"); 11 v12: life-death unit 3, living before God, #1940, §4 "Who swears it, and what for", "What it is joined to"; 12 v11: life-death unit 3, living before God, #1940; 14 v12: life-death unit 3, living before God, #1940

**Refs:** escalation 1940


## 2026-10-03 — Structure: Ch 2 widened: "What death is" gains two sub-sections (*Death and sin*, *Death in the living*); new s

**Strand:** life and death (M25), unit 2 (#1939)

**Refs:** escalation 1939


## 2026-10-03 — Strand updates — life and death (M25), unit 2: dying and death (2026-10-03, #1939)

**Strand:** life and death

**Researcher:** proceed to weave in

**Sources:** _analytics/Clusters/M25 - life-death/life-death-observation-ledger-unit2-v1-20261002.md

**Original claims changed:** **Original claims touched:**

**Notes:** **Ledger:** `_analytics/Clusters/M25 - life-death/life-death-observation-ledger-unit2-v1-20261002.md` (LD-43 to LD-91). It covers 1,237 hits in 1,045 verses (H4191, H4194, G0599, G2288, G3499, G1312, G4881, G2253), with 28 faces.
- **Approval:** the researcher, verbatim: *"proceed to weave in"* (#1939). This approved the weave as proposed, including setting LD-46 and LD-47 side by side.

**Original claims touched:**

| # | Before (verdict) | Evidence now read | Now |
|---|---|---|---|
| 3-10 | Conscious existence after death (Rev 6:9; Heb 12:23): **Stands** | Set beside the dead seen from this side: "the dead know nothing" (Ecc 9:5); "The dead do not praise the Lord" (Psa 115:17); "where is he?" (Job 14:10). The dead with God: Luk 16:22; Rev 14:13; 2Sa 12:23 (LD-46, LD-47) | **Stands**, and is now **set side by side, unreconciled**, with the verses that speak of the dead from this side |
| 2-3 | Souls saved from death (Jam 5:20): **Stands** | Jam 5:20 now woven (Ch 2 "Delivered from death"; 10.10) | No change |
| 6-2, 3-9 | Survival after death; the soul delivered from Sheol | No new verse changes them | No change |

**The narrative's own statements this change made:**

| Where | Before | After | Kind |
|---|---|---|---|
| Ch 2 "Wanting to die" | "the wish belongs almost always to the soul" | Of the 24 wish verses in the pull, **7 carry *nephesh*** (1Ki 19:4; 2Sa 1:9; Job 7:15; Jon 4:3, 8; Judg 16:30; Num 21:5). Restated: *nephesh* stands behind "my life" or "I" in the words of Elijah, Jonah, Job and Saul; most other such wishes name no inner word | **Restated** (the uncounted "almost always" was wrong) |
| Ch 2 "Wanting to die" | "Only twice is the wish granted" (Samson, Saul) | **Abimelech** asks to be killed and is (Judg 9:54). Restated: where the wish is granted, it comes at the end of a life already lost (Samson, Abimelech, Saul) | **Restated** (the count was wrong) |
| Ch 2 "Wanting to die" | Elijah, Jonah, Job, Saul; the answers | Adds Job 3:11, 21; Gen 30:1; Ecc 4:2; Jer 8:3; Rev 9:6; Job 2:9 | Widened |
| Ch 2 "What death is" | Breath gone; the end of a life's way; it comes to all; death in the living (two bullets) | Adds the common lot (2Sa 14:14; Ecc 2:16; 3:2; Heb 9:27; Job 21:23, 25; Psa 49:17; Pro 11:7; Gen 27:2; Ecc 7:1), death as sleep (Mat 9:24; Joh 11:13; 1Th 4:14), and two sub-sections: **Death and sin** (Gen 2:17; 3:4; Rom 5:12, 14; 6:23; 1Cor 15:56; Jam 1:15; Rom 7:5, 9–10; Eze 18:4; 2Ki 14:6; Joh 8:24; 1Jo 5:16–17 quoted and stopped; 2Sa 12:13–14) and **Death in the living** (Rom 8:6; 1Jo 3:14; 2Cor 7:10; Rom 7:24; Rev 3:2; Psa 88:5; 143:3; Isa 59:10; Mat 4:16) | Widened (NS within the section) |
| Ch 2, new "Facing death" | — | Psa 55:4; 1Sa 20:3; Psa 13:3; Mat 26:38; Gen 26:9; Isa 51:12; Heb 2:14–15; 2Cor 1:9; Heb 5:7 | New |
| Ch 2, new "Dying to the Lord" | — | Rom 14:7–8; Phili 1:20–21; 1Cor 15:31; 2Cor 4:11; 6:9; Psa 116:15; Num 23:10; Pro 14:32; Heb 11:13, 4; Joh 12:24; last words (Gen 27:4; 46:30; 50:24; Pro 30:7; Heb 11:21); Rut 1:17 | New |
| Ch 2 "Life set before a person" | The life side | Adds the death side: Deu 30:15; Jer 21:8; Pro 14:12; 12:28; 18:21; Job 5:2; Pro 21:25 | Widened |
| Ch 2 "Delivered from death" | Psa 116; 56; 30; 71; 16; 118:17; Job 33; Proverbs | Adds 2Sa 22:5–6; Psa 9:13; 68:20; 118:18; 2Cor 1:10; Pro 24:11; Jam 5:20 | Widened |
| Ch 2 "Made alive" | Joh 5:21; Rom 4:17; Joh 6:63; 2Cor 3:6; Col 2:13; Eph 2:5; Joh 5:24; Rom 6:4; Col 3:3; 1Pe 3:18 | Adds Joh 8:51; 11:26; 1Jo 3:14; Christ's death (1Cor 15:3; Rom 5:8; Heb 2:9; Isa 53:12; 2Cor 5:15); Rom 6:2; Col 3:5 | Widened |
| Ch 2 "The body raised" | — | "Christ first" adds Act 2:24, 27; 13:36–37; "Changed" adds Hos 13:14; 1Cor 15:26; Rev 1:18; 2Ti 1:10; "Life, and judgment" adds the second death (Rev 2:11; 21:8; 20:14) | Widened |
| Ch 2 "After death" | Souls and spirits alive before God (Rev 6:9–10; Heb 12:23; 1Pe 3:19; Mat 10:28) | Adds the dead seen from this side (Job 14:10; Ecc 9:5; Psa 6:5; 115:17) **beside** the dead with God (Luk 16:22; Rev 14:13; 2Sa 12:23). "Scripture states both. I leave them side by side." | Widened (contradiction shown, not resolved) |
| 10.1, 10.3, 10.4, 10.5, 10.6, 10.7, 10.9, 10.10, 10.11; Ch 11 §4; Ch 12; Ch 13; Ch 14 | — | Short passages, each pointing back to Ch 2 (ledger "Woven — where"). Ch 11 §4 gains "What brings it about, and who acts" | Widened |

**Quote check:** every quote was checked against iba.db `verse` (ESV, `--prose`).
- **Ch 2 v8:** 339 checked. The 14 flags are the same as in v7: gloss labels, the carried-book noise on older lines, and Psa 116:9, which is missing from iba.db (#1891).
- **Other chapters:** every new verse quote passes. The only new flags are section titles in quotation marks ("Facing death", "Death and sin", "Made alive", "The body raised"), which are not verse quotes.

[Chapter versions, from the narrative index] 02 v8: **life-death unit 2, dying and death**: "What death is" widened (Death and sin; Death in the living), new "Facing death" and "Dying to the Lord", two "Wanting to die" claims restated, "After death" sets the dead seen from this side beside the dead with God, #1939; 10.1 v10: life-death unit 2, dying and death, #1939 (fear of death, grief at a death, vexation that kills); 10.3 v4: life-death unit 2, dying and death, #1939; 10.4 v5: life-death unit 2, dying and death, #1939; 10.5 v11: life-death unit 2, dying and death, #1939; 10.6 v6: life-death unit 2, dying and death, #1939; 10.7 v8: life-death unit 2, dying and death, #1939; 10.9 v12: life-death unit 2, dying and death, #1939; 10.10 v10: life-death unit 2, dying and death, #1939 (loyalty to death, answerable for another's death); 10.11 v2: life-death unit 2, dying and death, #1939; **new**, NS-D1, M20; 11 v11: life-death unit 2, dying and death, #1939, §4 "What brings it about, and who acts"; 12 v10: life-death unit 2, dying and death, #1939; 14 v11: life-death unit 2, dying and death, #1939

**Refs:** escalation 1939


## 2026-10-02 — Structure: Ch 2 rewritten as the scene-setting chapter (researcher: *"the context of Ch 2 is that it sets the s

**Strand:** life and death (M25), unit 1 (#1934, #1937)

**Refs:** escalation 1934, escalation 1937


## 2026-10-02 — Structure: Ch 9 "Life, breath and death" moved to Ch 2 (researcher, verbatim: *"Move Ch 9 to Ch 2"*). Old Ch 2–

**Strand:** life and death (M25; #1936)

**Refs:** escalation 1936, escalation 1920, thread OT-08


## 2026-10-02 — Structure: New 10.11 "Hiding and disclosing" (NS-D1 option A; researcher: "ns-d1: select A; I reviewed the edit

**Strand:** doubt and discouragement (M20), NS-D1 + second pass (#1931)

**Refs:** escalation 1931


## 2026-10-02 — Structure: Accounts written for meaning, from the M20 reading already done (not re-read). 10.1 gains "Anxiety" 

**Strand:** doubt and discouragement (M20; #1931)

**Refs:** escalation 1931


## 2026-10-02 — M20; "seat" removed) (was 14

**Notes:** [Chapter versions, from the narrative index] 15 v6: M20; "seat" removed) (was 14


## 2026-10-02 — M20) (was 13

**Notes:** [Chapter versions, from the narrative index] 14 v8: M20) (was 13


## 2026-10-02 — M20 hidden trap

**Notes:** [Chapter versions, from the narrative index] 12 v8: M20 hidden trap


## 2026-10-02 — M20 faces and factors

**Notes:** [Chapter versions, from the narrative index] 11 v8: M20 faces and factors


## 2026-10-02 — life-death unit 1, §4 "What it is set against"

**Notes:** [Chapter versions, from the narrative index] 11 v10: life-death unit 1, §4 "What it is set against"


## 2026-10-02 — M20 — care, discouragement and hiding between people) (was 10.9

**Notes:** [Chapter versions, from the narrative index] 10.10 v8: M20 — care, discouragement and hiding between people) (was 10.9


## 2026-10-02 — life-death unit 1; anger, fear strands

**Notes:** [Chapter versions, from the narrative index] 10.10 v9: life-death unit 1; anger, fear strands; 14 v9: life-death unit 1; anger, fear strands


## 2026-10-02 — pointers to 10.11) (was 10.8

**Notes:** [Chapter versions, from the narrative index] 10.9 v9: pointers to 10.11) (was 10.8


## 2026-10-02 — M20 — When God hides his face

**Notes:** [Chapter versions, from the narrative index] 10.9 v8: M20 — When God hides his face


## 2026-10-02 — life-death unit 1; anger, fear strands) (was 10.6

**Notes:** [Chapter versions, from the narrative index] 10.7 v7: life-death unit 1; anger, fear strands) (was 10.6


## 2026-10-02 — pointer to 10.11) (was 10.4

**Notes:** [Chapter versions, from the narrative index] 10.5 v8: pointer to 10.11) (was 10.4


## 2026-10-02 — M20 — Grumbling, Whispering

**Notes:** [Chapter versions, from the narrative index] 10.5 v7: M20 — Grumbling, Whispering


## 2026-10-02 — M20 — Perplexity, Understanding that is hidden, Doubt

**Notes:** [Chapter versions, from the narrative index] 10.2 v6: M20 — Perplexity, Understanding that is hidden, Doubt


## 2026-10-02 — life-death unit 1

**Notes:** [Chapter versions, from the narrative index] 10.2 v8: life-death unit 1; 10.3 v3: life-death unit 1; 10.5 v10: life-death unit 1; 10.9 v11: life-death unit 1


## 2026-10-02 — M20 pointer to 10.11

**Notes:** [Chapter versions, from the narrative index] 04 v6: M20 pointer to 10.11


## 2026-10-02 — roadmap for the new order, #1936

**Notes:** [Chapter versions, from the narrative index] 01 v4: roadmap for the new order, #1936; 04 v8: life-death unit 1; was Ch 3, renumbered 2026-10-02, #1936; v4, v5: fear strand; 06 v5: life-death unit 1; was Ch 5, renumbered 2026-10-02, #1936; anger, fear strands; 10.1 v8: chapter pointers, #1936; 10.2 v7: chapter pointer, #1936; anger, fear strands; 10.3 v2: chapter pointer, #1936; **new**, NS-M3; 10.4 v4: chapter pointer, #1936; anger strand) (was 10.3; 10.5 v9: chapter pointer, #1936; anger, fear strands; 10.6 v4: chapter pointers, #1936; anger strand) (was 10.5; 10.8 v5: chapter pointers, #1936; anger, fear strands) (was 10.7; 10.9 v10: chapter pointer, #1936; anger, fear strands; 11 v9: chapter pointers, #1936; anger, fear strands; 12 v9: chapter pointers, #1936; anger, fear strands; 15 v7: chapter pointer, #1936; anger, fear strands

**Refs:** escalation 1936


## 2026-10-02 — Strand updates — life and death (M25), Q4: the body and the resurrection (2026-10-02, #1938)

**Strand:** life and death

**Sources:** _analytics/Clusters/M25 - life-death/life-death-q4-body-resurrection-ledger-v1-20261002.md

**Original claims changed:** **Original claims touched:**

**Notes:** **Ledger:** `_analytics/Clusters/M25 - life-death/life-death-q4-body-resurrection-ledger-v1-20261002.md` (Q4-01 to Q4-17). It is the focused pull for open thread OT-05.
- **Trigger:** the researcher noted that Ch 2 was missing the resurrected body, and supplied an outside summary to check.
- **Approval:** the researcher approved the ledger and the weave (#1938).
- **Not taken in:** the church-history material in that summary (Origen, Augustine). It is not the voice of the Bible.
- **Not adopted:** its gloss of "spiritual" as "not opposed to materiality". No verse states it.

**Original claims touched:**

| # | Before (verdict) | Evidence now read | Now |
|---|---|---|---|
| 10-4 | **Restated**. The body's redemption "not in the reading" (**held**) | Rom 8:23; 1Cor 15:35–55; Phili 3:20–21; 2Cor 5:1–4; 1Jo 3:2 (Q4-03, Q4-06, Q4-09, Q4-10) | **Restated** (unchanged). The body's part is **now read, no longer held**. Scripture puts the body's redemption at the end ("the redemption of our bodies", Rom 8:23; "we shall all be changed", 1Cor 15:51), and has the inner being renewed now (2Co 4:16; Rom 12:2). It does **not** assign the three phases to three parts. That half of the claim stays restated |
| 10-7, 3-x (conscious existence after death) | Stands | 2Cor 5:8 belongs to Q2 / OT-03 | No change. Signposted only |

The narrative's own statements this change made:

| Where | Before | After | Kind |
|---|---|---|---|
| Ch 2 "The body raised" | Isa 26:19, 14; Hos 6:2; Rom 8:11; 1Cor 15:22, 36, 45 | Adds Job 19:25–27; Psa 17:15; 1Pe 1:3; five sub-sections: **Sown and raised** (1Cor 15:35–46, 49; the *psychikos* face, with 1Cor 2:14), **Christ first** (15:20–23; Col 1:18; 1Cor 6:14; the risen body in Luk 24, Joh 20–21, Act 10:41; 1Cor 15:50 set beside Luk 24:39 and **not reconciled**), **Changed** (15:51–55; Isa 25:8; Phili 3:20–21; 1Jo 3:2), **Waited for** (Rom 8:23; 2Cor 5:1–4), **Life, and judgment** (Mat 22:30; Luk 20:36; Rev 21:4; Joh 5:28–29; Dan 12:2; Act 24:15; 1Th 4:16–17) | Widened (NS within the section) |
| Ch 2 "Where life flows from" | Life named as a person (Deu 30:20; Col 3:4; Joh 17:3) | Adds Joh 11:25, "I am the resurrection and the life" | Widened |
| 10.1 "Where it turns"; 10.6; Ch 13 "Delivered from the wrath to come"; Ch 14 "Revived, restored, renewed" | — | Short passages pointing back to Ch 2: the groan that waits (Rom 8:23; 2Cor 5:2), the longing (2Cor 5:2, 4; Phili 3:20), the resurrection of judgment (Joh 5:29; Dan 12:2), born again to a living hope (1Pe 1:3; Phili 3:10) and the mind transformed (Rom 12:2) | Widened |

**Quote check:** all quotes were checked against iba.db `verse` (ESV): 50 in Ch 2 "The body raised", and every quote added elsewhere. 1Cor 15:47 is missing from iba.db (#1891) and is not quoted.

[Chapter versions, from the narrative index] 02 v7: **"The body raised" expanded**, Q4 body and resurrection, #1938; 10.1 v9: Q4 pointer, the groan that waits, #1938; 10.6 v5: Q4 pointer, longing, #1938; 14 v10: Q4 pointers, #1938

**Refs:** escalation 1938


## 2026-10-02 — Strand updates — life and death (M25), unit 1 and the Ch 2 rewrite (2026-10-02, #1934, #1937)

**Strand:** life and death

**Researcher:** proceed with writing ch2 and weaving it in.

**Sources:** _analytics/Clusters/M25 - life-death/life-death-observation-ledger-unit1-v1-20261002.md
_analytics/Clusters/M25 - life-death/life-death-linkage-map.md

**Original claims changed:** **Original claims touched:**

**Notes:** **Ledger:** `_analytics/Clusters/M25 - life-death/life-death-observation-ledger-unit1-v1-20261002.md`
- Unit 1 covers life given, revived and prayed for, and the breath words: 356 hits in 326 verses, read by surface.
- The researcher approved it: *"proceed with writing ch2 and weaving it in."*

**Linkage map:** `_analytics/Clusters/M25 - life-death/life-death-linkage-map.md`.

**Structure change:** Ch 9 was moved to Ch 2 (#1936). Ch 2 was then rewritten in the approved four-movement shape (#1937), with eight new sections. Every existing section was kept.

**Original claims touched:**

| # | Before (verdict) | Evidence now read | Proposed |
|---|---|---|---|
| 4-8 | *Neshamah* outside the reading: **Held** (word); the model **Withdrawn** | *nəšāmâ* ("breath") is read in unit 1 (24 hits). "It is the spirit in man, the breath of the Almighty, that makes him understand" (Job 32:8); "The spirit of man is the lamp of the Lord" (Pro 20:27, *nəšāmâ*) (LD-15) | **Word: read.** The breath gives understanding and searches. The model "spirit becomes breath becomes soul" stays **Withdrawn**: no verse states it. For the researcher to confirm |
| 8-4 | "The spirit was dead through sin" (Eph 2:1–5): **Held** | "even when we were dead in our trespasses, made us alive together with Christ" (Eph 2:5); "you, who were dead in your trespasses" (Col 2:13) (LD-26) | **Restated** (proposed): the verses say *you* were dead, the person, not "the spirit". For the researcher to confirm |
| 3-9, 3-14, 2-15 | Restated / Restated / Restated | Psa 30:3, 71:20 (LD-07); 1Ki 17:22, 2Ki 13:21 (LD-18); Pro 20:27 (LD-15) | No change. More witnesses for the existing verdicts |
| 10-4 | **Restated** (the body's redemption not in the reading) | Rom 8:11; Isa 26:19; 1Cor 15:22, 36, 45 (LD-20–LD-24) | No change yet. The glorified body (1Cor 15:42–44; Phili 3:21) waits for the Q4 pull (OT-05). **Done in v9 — see the Q4 section below** |

The narrative's own statements this unit changed:

| Where | Before | After | Kind |
|---|---|---|---|
| Ch 2 opening | "This is where Scripture's inner words come closest to being separated" (written for the end of the book) | Sets the scene: life given, lived before God, ended; Pro 4:23, "from it flow the springs of life", read as the life lived flowing from within ("I read"). The old sentence is kept, re-placed | Restated (place and scope) |
| Ch 2 "Breath lent" | Breath given and taken | Adds: God kills and makes alive (Deu 32:39; 1Sa 2:6; 2Ki 5:7); keeps alive (Psa 33:19; Job 36:6; Gen 50:20; Deu 6:24); breath that understands (Job 32:8; Pro 20:27); breath failing in the living (Dan 10:17); every breath to praise (Psa 150:6) | Widened |
| Ch 2, new sections | — | "Where life flows from", "Life set before a person", "Life asked for", "What death is", "Made alive", "The body raised", "What follows" | New |
| Ch 2 "Life that returns", "Delivered from death" | Spirit, life and breath return; soul delivered | Adds 2Ki 13:21; 2Ki 8:5; Eze 37:3, 6; the inner person revived (Isa 57:15; Psa 69:32; Isa 55:3; Isa 38:16); Psa 30:3; 71:20; 118:17 | Widened |
| Ch 4, 6; 10.2, 10.3, 10.5, 10.7, 10.9, 10.10; Ch 11 §4; Ch 13; Ch 14 | — | Short passages, each pointing back to Ch 2 (ledger "Woven — where") | Widened |

[Chapter versions, from the narrative index] 02 v6: **rewritten as the scene-setting chapter**, life-death unit 1, #1937; **was Ch 9**; moved to Ch 2, #1936; anger, fear strands

**Refs:** escalation 1934, escalation 1937


## 2026-10-02 — Strand updates — doubt and discouragement (M20) (2026-10-02, #1931)

**Strand:** doubt and discouragement

**Sources:** ../../Clusters/M20 - doubt-discouragement/wa-cluster-M20-narrative-digest-v1-20261002.md

**Original claims changed:** **Checks:** 454 quotes checked in the four chapters, with one flag. That flag is Psa 106:24–25 across two verses, which the checker does not join; it was checked by hand. Let-Scripture-speak cuts made while writing are listed in the digest §1. No original claim's verdict changes in this pass.

**Notes:** **Researcher, verbatim:** *"proceed with M20 - similar to the previous session. read the m20 folder for the previous analysis"*. Source: the M20 reading already approved (#1885), not re-read. Digest and placements: `../../Clusters/M20 - doubt-discouragement/wa-cluster-M20-narrative-digest-v1-20261002.md`.

| Where | Before | After | Kind |
|---|---|---|---|
| 10.1 (v7) | "anxiety" named only in the heart's range; Psa 94:19 in "Feeling and thinking" | New section **"Anxiety"**: what it is (Pro 12:25; Mat 6:25; Luk 12:23); the words (*merimnaō* is anxiety about food and also care for the churches and for one another; *dāʾag* is dread of a coming harm and also sorrow for sin, Psa 38:18); what it does (adds nothing, runs ahead, weighs the heart, chokes the word, divides, what it fears follows); care that is good (2Cor 11:28–29; Phili 2:20–21; 1Sa 10:2; 1Cor 7:32–35); meeting it (handed to God, Phili 4:6–7; a word; looking; the Spirit, Mat 10:19–20; searched, Psa 139:23; Jer 17:7–8) | New |
| 10.1 (v7) | — | New section **"Losing heart"**: in all five uses, another party does it (Col 3:21; Eze 13:22; Psa 10:10; 109:16; Dan 11:30, with 11:28) | New |
| 10.1 (v7) | Change-of-character list without anxiety | Bullet added: anxiety rebuked or praised by its object; *dāʾag* is also sorrow for sin | Widened |
| 10.2 (v6) | — | New sections **"Perplexity"** (what it is; its occasions; it asks, looks, stays inside, hands on; it sits with fear and gladness, Mar 6:20; in love, Gal 4:19–20; bounded, 2Cor 4:8; ends when someone comes in 5 of 11 verses), **"Understanding that is hidden"** (for a time; as judgement; by God in thanks; from myself; Deu 29:29), **"Doubt"** (read as different from perplexity, marked "I read"; Peter; worship and doubt together; *dipsuchos*, "two-souled"; the heart named as the place to be made clean, Jam 4:8) | New |
| 10.5 (v7) | — | New sections **"Grumbling"** (*lûn*, *rāgan*; re-aimed at God, Exo 16:7–8; its occasions; the past retold as a plan to kill; its companions; answered by provision, judgement, a sign, a promise; Caleb's different spirit) and **"Whispering"** (the same *rāgan*; separates; feeds a quarrel; is wanted; the glazed lips over an evil heart; the fool's own soul snared, Pro 18:7) | New |
| 10.9 (v8) | Psa 10:11 only (Ch 3, Ch 12) | New section **"When God hides his face"**: *sātar* in three directions (Psa 27:5, 9; 51:9); reasons given or not; what it does (dismay, the spirit fails, the soul cast away, sorrow, the body bowed, no comforter, fear of people, complaint); how different hearts meet it (seeking, penitent, taking it as permission, not noticing, waiting); Psa 30:6–8; its end (Psa 22:24, 26; Isa 54:8; Eze 39:29) | New |

**Researcher, verbatim (2026-10-02):** *"ns-d1: select A; I reviewed the edited files, looks good."* NS-D1 option A was made, and then the second pass:

| Where | Before | After | Kind |
|---|---|---|---|
| 10.11 (v1, new) | Hiding scattered (Gen 3:10 in 10.1; Isa 26:20 and Rev 6:16 in 13; Job 14:13 in 10.3) | One account, **"Hiding and disclosing"**: the words (*ḥāvāʾ* hiding oneself; *ṭāman* putting into or under; *kāḥad* keeping back, also "cut off"; *sātar*, the widest); hiding from God (a perception of God first; Job 13:20–21; nothing hidden from him, which is comfort, wonder or judgement); hiding from people (the weaker side; counsel to hide; fear named; prudence; refused or impossible); hiding another (Rahab's confession; parents "not afraid"; God hides those who ask; Col 3:3; false shelter); hiding what I hold (Achan; failure and fear; conscience; enjoyment; shamelessness; God's works not hidden; treasure in joy, talent in fear); the hidden trap; longing to be hidden; what changes it | New |
| 10.0 (v5) | Map of 10.1–10.10 | 10.11 added; "Fear drives hiding"; "What is hidden is drawn out by speech" | Widened |
| 10.10 (v8) | — | "Care, discouragement and hiding between people" | New |
| Ch 11 §4 (v8) | No care, hiding or murmuring entries | Faces: care (*merimnaō*, *dāʾag*), hiding (*sātar* both ways; treasure and talent), murmuring (*rāgan*). Factors: whether it divides the person; who acts on whom | Widened |
| Ch 12 (v8) | Evil hidden behind the mouth | The heart hides a purpose to catch another (Psa 64:5–6; 140:2, 5) | Widened |
| Ch 3 (v6) | God sees the hidden heart | People try to hide the heart's counsel (Isa 29:15–16) | Widened |
| Ch 14 (v8) | — | Eze 39:29 (the hidden face ends with the Spirit poured out); Isa 29:24; Col 3:3 | Widened |
| Ch 15 (v6) | "named with no seat at all"; strand paragraph to fear | "named with no inner word at all" (project word removed); M20 added to the strand paragraph | Restated |

**Checks:** new and changed text: 0 quote failures. The remaining flags in 03, 11, 12, 14 and 15 are on older lines (carried-forward book noise, Held labels). Let-Scripture-speak cuts made in the 10.11 draft before review: "Most hiding in Scripture", "the most dangerous hiding", "the one who hides himself is usually afraid", "the reason changes everything", "does not stay quiet inside", "shame".

**Checks:** 454 quotes checked in the four chapters, with one flag. That flag is Psa 106:24–25 across two verses, which the checker does not join; it was checked by hand. Let-Scripture-speak cuts made while writing are listed in the digest §1. No original claim's verdict changes in this pass.

[Chapter versions, from the narrative index] 10.1 v7: M20 — Anxiety, Losing heart, #1931

**Refs:** escalation 1931


## 2026-10-01 — Narrative audit — imputed readings removed (#1921)

**Researcher:** you are bordering on imputing meaning that is not supported by the verses. don't drive synergy and phantom observations into the findings. Rather allow scripture to speak for itself.

**Method:** Workflow/Instructions/wa-inner-being-narrative-style-guide-v1-20261001.md §1, §2, §8.2

**Sources:** _analytics/essay/spirit_soul_body/wa-essay-narrative-imputed-readings-audit-v1-20261001.md

**Notes:** # Narrative audit — imputed readings removed (v1)

**Date:** 2026-10-01 · **Author:** Claude Code · **Escalation:** #1921 · **Status:** applied in place (in-review edits), for the researcher to review.
**Researcher, verbatim (2026-10-01):** *"you are bordering on imputing meaning that is not supported by the verses. don't drive synergy and phantom observations into the findings. Rather allow scripture to speak for itself."* Then: *"proceed with the #1921 audit of earlier readings."*
**Standard applied:** `Workflow/Instructions/wa-inner-being-narrative-style-guide-v1-20261001.md` §1, §2 and §8.2.
**Scope:**
- every chapter file, 01–15, read in full and checked for narrator readings and joining sentences
- every "I read / I take / I find", every "so" or "this shows", every superlative and frequency word
- this covers readings from the earlier passes (#1912–#1918); the 34 removals from today's weaves are listed separately in claim register v4
**Method:** a sentence was kept if a cited verse says it. It was cut back to the verses if it joined them into something no verse states, or if it used a count that was never made. Counted claims were kept, after the counts were checked:
- "the one word Scripture leans on most" (heart, about 930 verse rows against about 770 for soul; M47 stocktake §2)
- "about one verse in ten" (seat coverage)
- "life and myself … more often than soul" (Ch 4)

**Totals:** 88 edits.

| Kind | Count |
|---|---:|
| synthesis / pattern not stated | 58 |
| uncounted superlative or frequency | 15 |
| mechanism or metaphor imputed | 10 |
| division of labour between inner words | 5 |

| File | Edits |
|---|---:|
| 01-the-question | 1 |
| 02-one-inner-person | 3 |
| 03-the-heart | 9 |
| 04-the-soul | 8 |
| 05-the-spirit | 3 |
| 06-flesh | 5 |
| 07-conscience-and-bosom | 4 |
| 09-life-breath-and-death | 6 |
| 10-00-the-inner-being-at-work | 1 |
| 10-01-feeling | 1 |
| 10-04-thinking | 9 |
| 10-05-speaking | 4 |
| 10-06-wanting | 1 |
| 10-07-choosing-and-setting-direction | 2 |
| 10-08-right-and-wrong | 2 |
| 10-09-relating-to-god | 1 |
| 10-10-relating-to-others | 2 |
| 11-patterns-of-the-inner-life | 15 |
| 12-when-the-inner-being-goes-wrong | 7 |
| 14-made-new | 3 |
| 15-beyond-the-named-words | 1 |

**Refs:** escalation 1921


## 2026-10-01 — Structure: Fear rewritten for meaning across the book. 10.1's "Fear" section approved as the model (researcher:

**Strand:** fear (M01), rework (#1930)

**Refs:** escalation 1930


## 2026-10-01 — Structure: 10.1 gains a section "Fear" (what fear is; the words *yārēʾ*, *paḥad*, *ḥārad*, *rāgaz*; what fear d

**Strand:** fear (M01), review (#1930)

**Refs:** escalation 1930


## 2026-10-01 — Structure: No structure change. New sections: 13 "Dread and trembling"; 14 "No one to make them afraid". Ch 11 

**Strand:** fear (M01), unit 2 (#1929)

**Refs:** escalation 1929


## 2026-10-01 — Structure: No structure change. Fear is woven by activity, as anger was. New sections: 10.5 "Fear and the mouth

**Strand:** fear (M01), unit 1 (#1927, #1928)

**Refs:** escalation 1927, escalation 1928


## 2026-10-01 — Structure: Chapter titles reduced to their subject. Ch 3 "The heart", Ch 4 "The soul", Ch 5 "The spirit", Ch 6 

**Strand:** (researcher ruling, #1924)

**Refs:** escalation 1924


## 2026-10-01 — Structure: Three structure changes (researcher: "approve 1920 as recommended, remembering after 10.2"). (1) Hum

**Strand:** anger (M02; #1920)

**Refs:** escalation 1920


## 2026-10-01 — Structure: No new files; Ch 11 §4 grows into an account. §4 "One word, opposite values" gains the sub-section "

**Strand:** origin of thought — change of character (#1919)

**Refs:** escalation 1919, thread OT-41, thread OT-53


## 2026-10-01 — Structure: Woven (step 4). New: 10.3 Thinking, 10.4 Speaking. Rewritten: 10.0 (the path from a thought to a dee

**Strand:** origin of thought


## 2026-10-01 — anger strand — **rewritten**; v4, v5: fear strand

**Notes:** [Chapter versions, from the narrative index] 10.1 v3: anger strand — **rewritten**; v4, v5: fear strand


## 2026-10-01 — anger strand — roadmap

**Notes:** [Chapter versions, from the narrative index] 01 v3: anger strand — roadmap


## 2026-10-01 — Correction — imputed readings removed (2026-10-01)

**Researcher:** AI assumptions and wrong
the title is appropriate

**Sources:** wa-essay-narrative-imputed-readings-audit-v1-20261001.md

**Notes:** **Researcher, verbatim:** *"you are bordering on imputing meaning that is not supported by the verses. don't drive synergy and phantom observations into the findings. Rather allow scripture to speak for itself."*

**Withdrawn:** the spirit/heart "division of labour" for anger (anger ledger AN-H1; M02 U1 §38 point 2; Batch A §2.1 "two stages, two seats").

**Removed in place from the chapters (34 edits, all from the #1919/#1920 weaves).** Narrator readings that joined verses into a pattern or claim no verse states, or that used an uncounted superlative:
- **Ch 9:** *ʾaph* "anger is not a separate part … what happens in the place of breath"
- **10.0:** "closer to a circle than a line"; Nehemiah's "just charge, not a weapon"
- **10.4:** "one gift with three directions"; "the clearest single picture …", restated as what Jer 18:11–12 says; "what comes back shows what the thought was"; "inside becomes a quarrel once shared"; "not proved true by arriving in the dark"
- **11 §2/§4:** "lifted heart, checked, turns to anger"; "one of the most important things"; "the place reveals more than decides"; "what comes back shows what the act was"; "the hand is the same; where the person stands has changed" (and that factor)
- **10.3:** "memory governs much of what happens inside"; "a remembering that does not lead back into sin"; "what decides seems to be …"
- **10.1:** "the feeling Scripture traces most fully"; "one family shows both courses"
- **13:** "not hardness … the end of a long refusal"; "every inner activity is in play"; "the hand does not change", restated as "the same words for the hand are used in both directions"
- **15:** the genre reading, "two ways of seeing the same thing"
- **10.5:** "the voice of one who protects his own"
- **Ch 7:** "kept on purpose"; "cherished anger shuts out the cry"
- **10.10:** "most often"; "so that the rise … no longer counts"; "the father gives the brother back"
- **10.9:** "the very thing that is the opposite of anger"; "its character changes with the one who uses it"; "the same words delight … and fill"

**Earlier passes audited (#1921, 2026-10-01):** 88 more in-place edits across Ch 1–15, each listed before and after in `wa-essay-narrative-imputed-readings-audit-v1-20261001.md`. They include two further divisions of labour that are withdrawn: 10.7 "if the soul wants, the heart sets direction … the spirit supplies energy", and Ch 5 "much more about energy and disposition than about deciding". The researcher then ruled (#1924) that the four chapter subtitles are *"AI assumptions and wrong"*, and they are removed: Ch 4 "the living, needing self", Ch 5 "breath, wind and the moving force", Ch 6 "the visible, mortal, related self", Ch 7 "the self that judges, the place that holds". By the same rule Ch 3 "the centre" is removed too. Ch 2's title was flagged. The researcher ruled it stays (2026-10-01, verbatim): *"the title is appropriate"*.

---


## 2026-10-01 — Fear account integrated for review (2026-10-01, #1930)

**Sources:** wa-essay-trial-fear-account-v1-20261001.md

**Notes:** **Researcher, verbatim:** *"i think it is starting to unravel. We lost meaning and interpretation, it is starting to just become a list of quotes"*; *"many quoted verses say nothing about what it means for the inner being. it also says nothing about the word. a simple question of : what does the bible say fear is? what is its different forms? why is it different?"*; *"weaving means applying into other sections appropriate parts - it does not say you must ignore all the work that was done and listed in the ledger. you are not writing with intelligence and interpretation, you just doing a machanical mix and match excercise and it has lost its meaning and coherance."*; *"integrate it into the narrative so I can review it in context."*

| Where | Before | After | Kind |
|---|---|---|---|
| 10.1 Feeling (v6) | Fear followed through each stage as lists of verses (v4, v5) | A section **"Fear"**: what fear is (whole person; it comes upon; a cause outside, often a reason inside); the four Hebrew words and their renderings, read as one inner stirring whose character the situation decides (marked "I read"); what fear does; the fear of God (Exo 20:18–21 read as one fear taken away and another set in its place, marked "I read"); what changes it; meeting fear; 1Jo 4:18 quoted ahead of the Greek unit. The stage sections now follow anger; the change-of-character bullet for fear points to the section | Restated |

**Researcher (2026-10-01, verbatim):** *"proceed, I read in there is an improvement."* The same rewrite was then made in every chapter carrying fear:

| Where | Before | After | Kind |
|---|---|---|---|
| 10.5 (v6) | "Fear and the mouth" as lists | Prose: fear shuts the mouth when the truth would hurt (fear *for* the hearer, 2Sa 12:18), or makes it lie when the truth looks dangerous to the speaker (Gen 26:7); words used to frighten; the words of comfort used to deceive. **Correction:** Job 31:33–34 is now given as Job's oath of innocence (a silence he swears he did not keep), not as his own experience | Restated |
| 10.7 (v6) | Lists of fear stopping and setting choices; commands with "do not fear" | Prose: fear stops a choice given by another; Exo 9:20–21 (the fear of God's word made the difference in what people did); the commands with "fear not" send a person forward | Restated |
| 10.9 (v7) | About 2,000 words of fear lists | About 1,100 words in four parts: afraid in his presence (the reason each time: they cannot stand before him; Jacob's fear as recognition; the brothers' fear after naming their guilt, Gen 42:21, 28); fearing God as a way of life (with love, Deu 10:12; learned; in the heart or missing; given; tested); what it rests on (forgiveness, goodness, his acts, Psa 130:4; Hos 3:5; Jer 33:8–9); how God meets those who fear him. "Fear not": God gives himself as the reason; the person says it back (Isa 41:10 / Psa 23:4) | Restated |
| 10.10 (v7) | Lists | Prose: the fear of God and the weak (Lev 19:14; 25:43, read as God seeing what the victim cannot, marked "I read"); reverence for people for God's work in them (Jos 4:14; 1Ki 3:28); speaking to another's fear; fear that arrives with a person; making others afraid; trembling for another | Restated |
| Ch 11 §4 (v7) | Six fear entries | Four: fear; "do not fear"; trembling and dread (one stirring, marked "I read"); "none shall make you afraid" | Restated |
| Ch 12 (v7) | Bullet list | Prose: fear given to the wrong one; fear planted for sin; the fear of God going wrong in the heart; terror "where there is no terror" (Psa 53:5, marked "I read") | Restated |
| Ch 13 (v4) | "Dread and trembling" as a list | Prose: the chain with no way out (Isa 24:17–18); dread given into the heart; understanding as terror; Ezekiel's sign; fear for oneself at another's fall; Wisdom's storm; the earth and heavens | Restated |
| Ch 14 (v7) | List of promises | Prose: what comes with "no one will make them afraid"; what they fear has changed | Restated |
| Ch 15 (v5) | Five bullets | Four, each with what the verses show | Restated |

**Checks:** every added quote matches the ESV in iba.db. The only flags remaining are older ones (checker noise or labels). Let-Scripture-speak cuts made in this rework: "most careful", "Haman wanted to be feared", "the whole of creation", "end with", "as they are", and "because of what they already knew". Interpretation beyond what a verse states is marked "I read".

**Status:** reworked. Trial source: `wa-essay-trial-fear-account-v1-20261001.md`. Quotes ESV-checked: 133 in 10.1 v6, 0 failures. Two uncounted words in the trial ("rarely", "more often") were cut while integrating.

[Chapter versions, from the narrative index] 10.1 v6: fear account integrated for review, #1930

**Refs:** escalation 1930


## 2026-10-01 — Strand updates — fear (M01), unit 2 (2026-10-01, #1929)

**Strand:** fear

**Researcher:** proceed with the weaving

**Sources:** _analytics/Clusters/M01 - fear-awe/fear-observation-ledger-unit2-v1-20261001.md

**Original claims changed:** **Original claims changed:** none. 8-2 stays **Held**; 9-4 (2Ti 1:7) is Greek and comes in unit 4.

**Notes:** **Ledger:** `_analytics/Clusters/M01 - fear-awe/fear-observation-ledger-unit2-v1-20261001.md`
- Unit 2 covers *paḥad*, "dread", and the Hebrew trembling and shuddering words: 227 hits in 196 verses, read by surface.
- The ledger was approved by the researcher: *"proceed with the weaving"*.

**Original claims changed:** none. 8-2 stays **Held**; 9-4 (2Ti 1:7) is Greek and comes in unit 4.

**No structure change.** Two new sections inside existing chapters (13, 14).

The narrative's own statements this unit changed:

| Where | Before | After | Kind |
|---|---|---|---|
| 10.1 Feeling | Fear rises from what is seen and heard; fear in the heart and body | Dread and trembling rise at an arrival (1Sa 16:4; 1Ki 1:49), a discovery (Gen 27:33), in the night before a spirit (Job 4:13–15), from two causes (Ezr 10:9); felt in the heart (Psa 55:4; Job 37:1; Isa 21:4); fills night and day (Deu 28:66–67); the dreaded thing arrives (Job 3:25); hiding from the terror of the Lord (Isa 2:10); silence from fear of the many (Job 31:34); the trembling and dread words change character (Psa 4:4; 2Ki 19:27; 2Sa 18:33; Isa 60:5) | Widened |
| 10.2 Knowing and hearing | — | Wisdom refused, terror and security (Pro 1:26, 33); one scroll, fear and no fear (Jer 36:16, 23–24); "sheer terror to understand" (Isa 28:19); awe of his words (Psa 119:161) | Widened |
| 10.5 Speaking | Fear stops speech (three cases) | Adds Job 31:34 | Widened |
| 10.7 Choosing | Commands that come with "do not fear" | Adds Jos 1:9; Deu 20:3; the fear of the Lord set before the judges (2Ch 19:7); the dread of the Lord and "as one man" (1Sa 11:7) | Widened |
| 10.9 Relating to God | Fear before God; the fear of God; "Fear not" | Adds: afraid in his presence (Exo 19:16; Job 23:15; 37:1–2; Dan 10:10–11; Gen 42:28; Isa 33:14; Job 31:23); trembled at his word (Isa 66:2, 5; Ezr 9:4); kept always (Pro 28:14); trembling at good (Jer 33:8–9); coming to him trembling (Hos 11:10–11; 3:5; Mic 7:17); trembling called for (Psa 96:9; 99:1; 114:7; Joe 2:1; Isa 32:11; Dan 6:26; Jer 5:22); God called "the Fear of Isaac" (Gen 31:42, 53; Psa 89:7); "do not be in dread" (Deu 7:21; Isa 44:8); self-spoken (Isa 12:2); terror spoken to (Psa 91:5; Pro 3:24–25); Isa 51:13; **Isa 8:12–13** (held from unit 1); Psa 64:1 | Widened |
| 10.10 Relating to others | Fear between people | Adds: trembling at an arrival (1Sa 16:4; 21:1); fear made (2Sa 17:2; Judg 8:12; Isa 47:12; Psa 10:18); an object of dread (Psa 31:11); the fear of one falling on many (Est 8:17; 9:3; Dan 5:19; Hos 13:1); Mordecai would not tremble (Est 5:9); trembling for another (1Sa 4:13; 2Ki 4:13; Est 4:4); *rāgaz* as quarrel and rage (Gen 45:24; Pro 29:9) | Widened |
| Ch 11 §1 | God turns, stirs, hardens hearts | Adds "Dread is laid on, given, and comes upon" (Deu 11:25; 28:65; Job 4:14; Isa 33:14; Psa 48:6; Dan 10:7) | Widened |
| Ch 11 §4 | Faces: fear; the one who is feared; "do not fear" | Faces: **dread** (Isa 8:12–13; Isa 60:5; Jer 33:9); **trembling**, *rāgaz* rendered tremble, "Be angry", "raging", "quarrel", "deeply moved", "disturbed" (and *ḥārad* trembling *for*, 1Sa 4:13); **"none shall make you afraid"**, used of peace and of desolation (Lev 26:6; Isa 17:2; Deu 28:26). Factor: **who hears it** (Jer 36:16, 24) | Widened |
| Ch 3 | — | The heart trembles for something (1Sa 4:13); a trembling heart given in the curse (Deu 28:65); "your heart shall thrill" (Isa 60:5) | Widened |
| Ch 5 | — | Isa 66:2 beside Isa 57:15 | Widened |
| Ch 6 | — | Bones (Job 4:14), shuddering at what is remembered (Job 21:6), hair and face (Eze 27:35), trembling in age (Ecc 12:3) | Widened |
| Ch 12 | Fear that goes wrong | Adds: lays a snare (Pro 29:25); "not in you" (Jer 2:19); set against a hardened heart (Pro 28:14); terror "where there is no terror" (Psa 53:1, 5). **Correction:** "One of the most dangerous things the heart says" (an uncounted superlative missed by the #1921 audit) → "The heart can say that all is well" | Widened; Restated |
| Ch 13 | — | "How it is provoked" gains Eze 16:43. New section **"Dread and trembling"**: terror, pit and snare (Isa 24:17–18; Jer 48:43–44); the curse (Deu 28:65–67, pointer); Isa 28:19; Ezekiel's sign (Eze 12:18–19); Wisdom's warning (Pro 1:27); trembling at another's fall (Eze 32:10; 26:16); the earth and heavens at his anger (Psa 18:7; Isa 13:13; 5:25). "Shelter" gains Isa 2:10, 19 | Widened |
| Ch 14 | — | New section **"No one to make them afraid"** (Mic 4:4; Eze 39:26; Zep 3:13; Jer 30:10); returning trembling (Hos 11:10–11); Jer 33:9 | Widened |
| Ch 15 | Fear spoken to the land and beasts; laid on nations | Adds: dread on whole peoples (1Ch 14:17; 2Ch 17:10; Exo 15:16; Psa 105:38); a spirit passes by (Job 4:15–16); the earth, waters and dead tremble (Exo 19:16, 18; Psa 77:16; 104:32; Job 26:11, 5; Isa 14:9; Jer 2:12; Pro 30:21–22); creatures without fear (Job 39:22, 16); last paragraph names life under God's anger | Widened |

**Checks done:**
- **Quotes.** Every chapter touched was run through `fear-quote-check-v1-20261001.py --prose` (rebuilt this unit; it now maps full book names). Every quote on an added line matches the ESV in iba.db. One label was corrected to match its cited verse (Ch 11, "None shall make you afraid"). The remaining flags are on older lines and are checker noise: a bare reference such as "(143:3)" is read against the wrong carried-forward book, or a quoted label has no reference of its own.
- **Let Scripture speak.** Ten phrases were cut back to what the verses say: "often" (uncounted), "on purpose", "closes in", "by their own", "even", "those who must choose", "in judgment", "the promises of return", "the terror of the night" (Pro 3:25 is not of the night), and "can bring fear to some" (one case, stated as one). Wisdom's warning (Pro 1:27) was moved out of the list headed "comes with God's anger", since the speaker is Wisdom.
- **Reverse audit.** Every observation FE-47 to FE-84 has at least one of its verses in the chapters. FE-85 (Lam 4:6) is held, as approved. Verses not quoted stay accounted for in the ledger's face column.
- **External parties (§7a).** A spirit (Job 4:15–16), Wisdom (Pro 1:26–27, 33), Samuel brought up (1Sa 28:15), Sheol (Isa 14:9), the heavens, waters, earth and the dead, creatures, and the heavy rain (Ezr 10:9) are each named in their own terms beside the phenomenon.

**Refs:** escalation 1929


## 2026-10-01 — Strand updates — fear (M01), unit 1 (2026-10-01, #1927, #1928)

**Strand:** fear

**Researcher:** the ledger is approved to continue

**Sources:** _analytics/Clusters/M01 - fear-awe/fear-observation-ledger-v1-20261001.md

**Original claims changed:** **Original claims changed:** none.
- 8-2 ("natural fear" not produced by the Spirit) stays **Held**. The fruit lists are not yet read.
- 9-4 ("spirit of fear", 2Ti 1:7) is Greek and comes in a later fear unit.

**Notes:** **Ledger:** `_analytics/Clusters/M01 - fear-awe/fear-observation-ledger-v1-20261001.md`
- Unit 1 covers the *yārēʾ* family, "to fear, revere": 424 hits in 408 verses, read by surface.
- The ledger was approved by the researcher: *"the ledger is approved to continue"*.

**Original claims changed:** none.
- 8-2 ("natural fear" not produced by the Spirit) stays **Held**. The fruit lists are not yet read.
- 9-4 ("spirit of fear", 2Ti 1:7) is Greek and comes in a later fear unit.

**No structure change.** Fear is woven by activity, as anger was (#1920).

The narrative's own statements this unit changed:

| Where | Before | After | Kind |
|---|---|---|---|
| 10.1 Feeling | Anger is the one feeling followed through its course | **Anger and fear** are followed:<br>- fear rising from what is seen and heard, from being found out, and at a sound (Gen 3:10)<br>- fear in the heart and body (1Sa 28:5, 20; Psa 119:120; 55:5; Neh 2:2)<br>- fear followed by the feared thing (Jer 42:16)<br>- what fear does: hides, runs, holds back hand and mouth, does wrong, hardens into enmity, turns to trust<br>- fear spreads (Judg 7:3)<br>- fear is spoken to<br>- the change-of-character bullet for fear (Exo 20:20; Exo 14:10, 31; Jon 1:5, 16; Psa 2:11; Neh 6:13)<br>- the factor "what, or whom, it faces" | Widened |
| 10.2 Knowing and hearing | — | The fear of the Lord as the beginning of knowledge and wisdom (Pro 1:7; 9:10; Job 28:28), understood by seeking wisdom (Pro 2:5), refused (Pro 1:29) | Widened |
| 10.5 Speaking | — | "Fear and the mouth": fear stops speech (1Sa 3:15; 2Sa 12:18; Job 32:6) and bends it into a lie (Gen 18:15; 26:7; Isa 57:11); words used to frighten (2Ch 32:18; Neh 6:9); "do not fear" spoken in bad faith (Judg 4:18, 21; 2Sa 13:28) | Widened |
| 10.7 Choosing | — | Fear stops a choice (Judg 8:20; 1Sa 31:4; 14:26) and sets a direction (Jer 26:21; Exo 9:20; Pro 14:16); the commands that come with "do not fear" (Deu 31:6; Exo 14:13; Isa 7:4) | Widened |
| 10.8 Right and wrong | — | Fear leading into wrong (1Sa 15:24; Neh 6:13); the fear of the Lord joined with turning from evil (Job 1:1; Pro 3:7; 16:6; 8:13; 13:13); hearing of judgment (Deu 19:20); the absence of fear named with the wrong (Exo 9:30; Jer 5:24; 2Sa 1:14; Num 12:8; Psa 64:4) | Widened |
| 10.9 Relating to God | Anger toward and before God | New "Fear before God, and the fear of God":<br>- afraid in his presence<br>- required, learned, taught without the heart, longed for, given, prayed for<br>- following his acts and his forgiveness<br>- with joy, confidence and life<br>- tested; divided (2Ki 17:33–34)<br>- what God does toward those who fear him<br>- the word turned onto God (awesome)<br>New "'Fear not'": God's word with its reasons; the self-spoken "I will not fear"; fear of man set against him (Isa 51:12–13) | Widened |
| 10.10 Relating to others | Anger between people | New "Fear between people":<br>- the fear of God named in the treatment of others (Lev 19:14, 32; 25:17, 43; Exo 1:17; Neh 5:15; Gen 42:18; Exo 18:21)<br>- its absence where people are harmed (Gen 20:11; Deu 25:18; Job 6:14)<br>- reverence for people (Lev 19:3; Jos 4:14; 1Ki 3:28; Pro 24:21)<br>- "do not fear" spoken by people, with reasons<br>- fear as weapon and as enmity<br>- those who fear God named together | Widened |
| Ch 11 §4 | Thought and anger faces and factors | Faces: **fear**; **the one who is feared**; **"Do not fear."** Factors: **what it is turned toward**; **whether the heart is in it**; **who speaks it, and to what end**; "brought before God" gains Psa 56:3. §6 gains Judg 7:3 | Widened |
| Ch 3 | — | The heart trembles, and stands firm against fear (1Sa 28:5; Psa 27:3); fear of God taught without the heart (Isa 29:13), and put into the heart by God (Jer 32:40; Psa 86:11) | Widened |
| Ch 6 | — | Flesh gives way under fear and hunger together (1Sa 28:20, quoted whole so that the stated physical cause stands) | Widened |
| Ch 9 | — | The fear of the Lord joined with life (Pro 10:27; 14:27; 19:23) | Widened |
| Ch 12 | — | "Fear that goes wrong": obeys the wrong voice, lies, is planted, hardens into enmity, is followed by what it flees; the fear of God taught without the heart, divided, absent. Isa 63:17 is added under hardening | Widened |
| Ch 13 | — | Psa 90:11 (God's wrath "according to the fear of you"); God's awesome deeds and his enemies (Psa 66:3; Zep 2:11) | Widened |
| Ch 14 | — | The fear of God given (Jer 32:39–40), and forgiveness "that you may be feared" (Psa 130:4) | Widened |
| Ch 15 | Roadmap: "in time fear" | Fear is woven, with the chapters named. New bullet: fear spoken to the land and beasts (Joe 2:21–22) and laid on nations (Eze 30:13; Deu 28:10) | Restated |

**Ledger correction made while weaving:** FE-16 had grouped Gedaliah (Jer 40:9) with Jael and Absalom, as "do not fear" in the mouth of one who means harm. Gedaliah's assurance was in good faith, and he was himself the one murdered (Jer 41:2). The grouping was wrong. Only Jael and Absalom are woven under that heading, and the ledger row is corrected.

**Checks done:**
- **Quotes.** Every quotation on an added line was matched mechanically against the ESV text in iba.db: 225 segments.
  - Two wordings were corrected: Isa 41:10 is "fear not", not "Do not fear"; and "You shall fear the Lord your God" is cited as Deu 10:20, not 6:13.
  - The remaining flags are checker noise: New Testament books not in its map, and multi-verse citations.
- **Let Scripture speak.** Nine sentences were cut back to what the verses say. Among them: "the first fear in Scripture is of this kind", "almost always a reason follows", "governs", "seek one another out", "the same deeds face two ways", "not set against them".
- **2Sa 14:15** is left out of the narrative. The woman of Tekoa's "the people have made me afraid" is part of a staged story.

**Refs:** escalation 1927, escalation 1928


## 2026-10-01 — Strand updates — anger (M02) (2026-10-01, #1920)

**Strand:** anger

**Researcher:** approve 1920 as recommended, remembering after 10.2

**Sources:** _analytics/Clusters/M02 - anger-wrath/anger-strand-observation-ledger-v1-20261001.md

**Original claims changed:** Ledger: `_analytics/Clusters/M02 - anger-wrath/anger-strand-observation-ledger-v1-20261001.md`. Structure ruled by the researcher (*"approve 1920 as recommended, remembering after 10.2"*). **Original claim changed:** 9-5 (above). The narrative's own statements this strand changed:

**Not woven:** **Held, not woven:** the spirit/heart division of labour for anger (U1 §38 point 2). The researcher said "not in the way you portrayed it", and the clarification is still pending. The verses are woven without the claim. The other unruled M02 points (U1 §X, U2 §X) are woven only as verses.

**Notes:** Ledger: `_analytics/Clusters/M02 - anger-wrath/anger-strand-observation-ledger-v1-20261001.md`. Structure ruled by the researcher (*"approve 1920 as recommended, remembering after 10.2"*). **Original claim changed:** 9-5 (above). The narrative's own statements this strand changed:

| Where | Before | After | Kind |
|---|---|---|---|
| Structure | 10.1–10.9; Ch 13 Made new; Ch 14 Beyond | New **10.3 Remembering and forgetting**; 10.3–10.9 → 10.4–10.10. New **Ch 13 Under God's anger**; 13 → 14, 14 → 15 | New |
| 10.1 Feeling | A list of what each inner word feels, plus feeling ↔ thinking | **Rewritten:** how a feeling rises (perceived, even falsely; a will blocked; a lifted heart checked; for another), settles in the body, stays or passes (time as its course), turns (on oneself, into heat, into fear, joined with grief), and when it changes character | Restated + Widened |
| 10.0 | The path begins with a thought | **The path can begin with a feeling** (1Sa 18:7–25; Gen 27:41–42), and where it can be broken (Gen 4:7; Neh 5:7; Gen 33:4). Anger poured out comes back (Hab 2:15–16) | Widened |
| 10.4 Thinking | — | "When anger thinks": it misreads, calculates, soothes itself with a plan; zeal reckoned rightly (Psa 106:31) | Widened |
| 10.5 Speaking | — | "Anger in words": the held grievance as a ledger; the soft answer; venom; the curse that cannot land; words given to return | Widened |
| 10.9 Relating to God | — | Anger at God (at his striking, at his mercy, misdirected); God answers with a question; anger brought to him; four relations of human anger to God's; the prophet as vessel; the creed used many ways | Widened |
| 10.10 Relating to others | — | "Anger between people": kinship, brothers, power, company, the house, love not irritable, vengeance left to God; **the answer to anger is most often a question or a reframing** | Widened |
| Ch 9 | Gen 2:7 read as God's closeness in making | Adds: the nostrils of life are the word for anger (*ʾaph*); anger is what happens in the place of breath when it is heated (reading) | Widened |
| Ch 11 §4 | Thought-strand faces and factors | Anger-strand faces (nose, anger, vexation, provoking, overflow, storm, denouncing, a creed, mourning, God's hand, remembering) and factors (distress both ways, joined with, how long, seen truly, the answer it meets, where the person stands) | Widened |
| Ch 12 | — | "Anger that goes wrong"; "False peace"; "The hardened heart remembered" (Meribah) | Widened |
| Ch 13 (new) | — | The human inner being under God's anger | New |
| Ch 15 (was 14) | "The chapters that follow in time will take up strands … one at a time" | Strands are **woven**, not given chapters; anger has been. Adds the genre reading and the seat named in the other party | Restated |

**Held, not woven:** the spirit/heart division of labour for anger (U1 §38 point 2). The researcher said "not in the way you portrayed it", and the clarification is still pending. The verses are woven without the claim. The other unruled M02 points (U1 §X, U2 §X) are woven only as verses.

**Pass 2, no change:** Ch 3 (references renumbered only). Ch 2, 4 and 8 were **scanned** (not re-read in full) for anger, vexation and memory passages. Their Hannah passages (Ch 2 §"one inner person"; Ch 4 "where bitterness lives") stand; her vexation (1Sa 1:6, 16) is carried in 10.1. Ch 8's "the spirit is … provoked" stands.

**Refs:** escalation 1920


## 2026-10-01 — Strand updates — change of character in the thought strand (2026-10-01, #1919)

**Strand:** change of character in the thought strand

**Sources:** _analytics/cross-cluster-web/origin-of-thought/origin-of-thought-observation-ledger-v2-20261001.md

**Original claims changed:** Built from ledger v2 (`_analytics/cross-cluster-web/origin-of-thought/origin-of-thought-observation-ledger-v2-20261001.md`, §I–§J). **No original claim changes verdict.** The narrative's own statements that this pass changed:

**Notes:** Built from ledger v2 (`_analytics/cross-cluster-web/origin-of-thought/origin-of-thought-observation-ledger-v2-20261001.md`, §I–§J). **No original claim changes verdict.** The narrative's own statements that this pass changed:

| Where | Before | After | Kind |
|---|---|---|---|
| 11 §4 "One word, opposite values" | A list of examples, closing with "which way my heart is set" | The list is widened (planning against, reckoning, likening, reasoning). A new sub-section, **"What changes the character"**, sets out what the verses put beside the change: which way it faces and what it is for, company, the heart state (Eph 4:18 as stated cause), ease or distress, haste or pause, place (it reveals more than it decides; the sanctuary changes sight), being brought before God, what comes back, the story around it. Left open for later strands | Widened + Restated (from examples to an account) |
| 10.3 Thinking | Design, reckoning, likening, murmuring and reasoning, each with one or two faces | Each activity is given its several faces and the *why*. New sections: "When thinking changes character", "Thoughts that turn on the thinker" (flow 3), "What is devised comes back" (flow 5). Night thoughts are distinguished: revelation, alarm, or a claimed vision that was wrong (Job 4:13 with 42:7) | Widened |
| 10.3 "It designs" | One faculty, good or evil by its aim | The given skill has three directions: God's house, the king's strength (2Ch 26:15–16), one's own ease (Amo 6:1, 5) | Widened |
| 10.3 "It reckons" | People misreckon; God reckons truly | Reckoning also serves **release** (Lev 25:50) and is set aside where there is **trust** (2Ki 12:15). Jesus took the wrong reckoning on himself (Luk 22:37). Credit is not mine to claim (2Co 3:5) | Widened |
| 10.0 The path | A line from arising to the deed | **What lodges can be kept rather than plotted** (Dan 7:28). **The path runs back:** what is devised returns on the deviser (Est 9:25; Psa 7:15–16; Mic 2:1–3), and for good (Pro 21:5; 16:3). "Closer to a circle than a line" | Restated |
| 10.0 How the activities connect | Seven connections | Two more (thinking acts back on itself; what goes out comes back), plus a paragraph on change of character pointing to 11 §4 | Widened |
| 11 §8 God thinks and plans | Gen 50:20 | Adds Joh 11:50–51: a cold calculation taken up into God's purpose | Widened |
| 10.8 | — | God's plans against are open to turning (Jer 26:3). Thinking in his presence sees differently (Psa 73:16–17). Love with all the mind (Mat 22:37). His thoughts are precious (Psa 139:17) | Widened |
| 10.9 | — | Reasoning becomes a quarrel (Luk 9:46; Rom 14:1; Phili 2:14). Partiality (Jam 2:4). Asking not to be reckoned (2Sa 19:19). Trust sets the count aside (2Ki 12:15) | Widened |
| 10.4 | — | *hāgāh* as mourning over the enemy (Jer 48:31) and as God's protective growl (Isa 31:4); idols without a voice (Psa 115:7) | Widened |
| 12 Idols; Pride; Hardening | — | Imagination makes gods (Act 17:29); the maker trusts his creation (Hab 2:18). The proud scattered "in the thoughts of their hearts" (Luk 1:51). Minds hardened (2Co 3:14) | Widened |
| 13 Thoughts taken captive | — | The hostile mind reconciled (Col 1:21–22); the mind prepared (1Pe 1:13) | Widened |

**Re-read, no change needed (pass 2, adjust):** 10.1, 10.2, 10.5, 10.6, 10.7. Their thought-related lines (Psa 94:19; 1Ki 18:21; Isa 10:7; Rom 2:15) stand as written and are now set in context by 10.3.

**Refs:** escalation 1919


## 2026-10-01 — Strand updates — origin of thought (2026-10-01, #1918)

**Strand:** origin of thought

**Method:** Woven by the approved method (weave, don't fit). Ledger: `_analytics/cross-cluster-web/origin-of-thought/origin-of-thought-observation-ledger-v1-20260930.md`. The original claims touched are 4-1, 4-4 and 9-1 above; none of their verdicts changes. The **narrative's own statements** that this strand changed:

**Sources:** _analytics/cross-cluster-web/origin-of-thought/origin-of-thought-observation-ledger-v1-20260930.md

**Original claims changed:** Woven by the approved method (weave, don't fit). Ledger: `_analytics/cross-cluster-web/origin-of-thought/origin-of-thought-observation-ledger-v1-20260930.md`. The original claims touched are 4-1, 4-4 and 9-1 above; none of their verdicts changes. The **narrative's own statements** that this strand changed:

**Notes:** Woven by the approved method (weave, don't fit). Ledger: `_analytics/cross-cluster-web/origin-of-thought/origin-of-thought-observation-ledger-v1-20260930.md`. The original claims touched are 4-1, 4-4 and 9-1 above; none of their verdicts changes. The **narrative's own statements** that this strand changed:

| Where | Before | After | Kind |
|---|---|---|---|
| Ch 3 "The heart speaks to itself" | "very often a verdict on itself, and very often a false one" | The verdicts are shown by kind: about God, about self, taking the credit, fear, enquiry. Absent speech (Jer 5:24) is added. Scripture forbids and answers inner speech | Widened |
| Ch 3 "The heart thinks…" | The heart as the place where thinking happens, with no account of the activity | The heart stays the *place*. The activity moves to 10.3 | Restated (scope) |
| 10.2 Knowing and hearing | "Hearing is the main way in" | Hearing goes **both ways**: God hears plots and the God-fearing (Lam 3:61; Mal 3:16), and refusing to hear goes with devising | Widened |
| Ch 12 "The heart as the source" | Gen 6:5 quoted as evidence of evil only | Gen 6:5 read with Gen 8:21: the same inclination grounds God's forbearance | Restated |
| Ch 12 Pride | Pride as the lifted heart and spirit | Pride is also **false likeness** (Isa 14:14; Eze 28:2; Psa 50:21) | Widened |
| 10.0 opening | Activities listed, no account of how they connect | The path from a thought to a deed, where I am answerable, and how the activities connect | New |
| 10.3 Thinking, 10.4 Speaking | — | New sections | New |
| Ch 7, 9, 11, 13; 10.1, 10.5–10.9 | — | Instances and connections added (see the index's Structure log) | Widened |

**Refs:** escalation 1918

- **4-1** edited (recorded, 2026-10-01)
  - note: New ch: 03 -> 03, 10.0, 10.3
- **4-4** edited (recorded, 2026-10-01)
  - note: New ch: 03 -> 03, 10.3
- **9-1** claim restated (recorded, 2026-10-01)
  - claim before: Scripture locates the source of evil chiefly in the heart: "out of the heart come evil thoughts" (Mat 15:19; Mar 7:21); "the heart is deceitful above all things" (Jer 17:9); sin "engraved on the tablet of their heart" (Jer 17:1). The vice-list catalogue is not yet read (D §11.1, §11.7)
  - claim after: Scripture locates the source of evil chiefly in the heart: "out of the heart come evil thoughts" (Mat 15:19; Mar 7:21); "the heart is deceitful above all things" (Jer 17:9); sin "engraved on the tablet of their heart" (Jer 17:1). The vice-list catalogue is not yet read (D §11.1, §11.7). Added 2026-10-01: Gen 6:5's "intention" is *yēṣer*, the formed inclination of the heart. It must be read with Gen 8:21, where the same evil inclination is the ground of God's forbearance
  - note: evidence and restatement cell changed
- **9-1** edited (recorded, 2026-10-01)
  - note: New ch: 12 -> 12, 10.3, 11

## 2026-09-30 — Reset: what the latest findings add that the original never had (digest §4)

**Strand:** inner seat (M47)

**Sources:** _analytics/essay/spirit_soul_body/wa-essay-spirit-soul-body-digest-v1-20260930.md

**Notes:** ## 4. What the latest findings add that the original never had

These areas are absent from the original, or are listed there only as gaps. [Claude reading]

1. **Flesh as a full component** (original gap 1–2): kin, "all flesh", frailty, response to the inner seat, the "heart of flesh", and Paul's flesh as an orientation. Depiction §2.4; C §11.5; D §11.8; G §7.
2. **The heart as the centre**: inner speech ("said in his heart"), attention as "setting the heart", the heart as store, surface and soil, its opacity to all but God. Depiction §2.1; B §9.1; C §11.2.
3. **Conscience and bosom** (original gap 4): conscience as the NT's name for what the OT does with the heart ("David's heart struck him"); the bosom as the holding place. Depiction §2.5–2.6; D §11.6.
4. **The inner seat between persons**: souls knit, hearts stolen, spirit passed on, states spreading from one person to another. Depiction §3.8; F §14.
5. **The seat acted upon**: God turns, stirs, hardens and fills; the king's heart. H §7.1; G §11.
6. **The seat in motion** (the twelve threads, framework overview §5): thresholds of eating and drinking, components giving way in sequence, one word with opposite values, voices to the soul, the governed seat, hearing as the way in, spirits that arrive, wind and breath as emptiness, God's own heart and soul.
7. **Beyond the seat**: only about 10% of inner-being verses name a seat at all; twelve other ways the text carries an inner operation. Framework overview §6.

---


## 2026-09-30 — Structure: The thought-to-deed path goes in 10.0 (researcher: "path in 10.0").

**Strand:** origin of thought


## 2026-09-30 — Structure: Remembering not given a file. Watched (NS-2: "watch NS-2").

**Strand:** origin of thought


## 2026-09-30 — Structure: 10.3 Thinking reserved (option B). 10.4 Speaking reserved (NS-1, approved: "approve NS-1 speaking").

**Strand:** origin of thought


## 2026-09-30 — Structure: Ch 10 → Part 10. One file per operation (10.0 opening/map + 10.1–10.9). Text moved unchanged (verifi

**Strand:** origin of thought


## Direct edits (no update)

- **I-3** renumbered (recorded, 2026-10-02)
  - note: New ch: 08 -> 09 \| version note: chapter renumbering, #1936
- **I-6** renumbered (recorded, 2026-10-02)
  - note: New ch: 05, 13 -> 06, 14 \| version note: chapter renumbering, #1936
- **1-1** renumbered (recorded, 2026-10-02)
  - note: New ch: 02 -> 03 \| version note: chapter renumbering, #1936
- **1-2** renumbered (recorded, 2026-10-02)
  - note: New ch: 02, 10.8 -> 03, 10.9 \| version note: chapter renumbering, #1936
- **1-3** renumbered (recorded, 2026-10-02)
  - note: New ch: 02, 04, 05 -> 03, 05, 06 \| version note: chapter renumbering, #1936
- **1-5** renumbered (recorded, 2026-10-02)
  - note: New ch: 10.8 -> 10.9 \| version note: chapter renumbering, #1936
- **1-6** renumbered (recorded, 2026-10-02)
  - note: New ch: 02 -> 03 \| version note: chapter renumbering, #1936
- **2-1** renumbered (recorded, 2026-10-02)
  - note: New ch: 04, 12 -> 05, 12 \| version note: chapter renumbering, #1936
- **2-2** renumbered (recorded, 2026-10-02)
  - note: New ch: 05, 08, 12 -> 06, 09, 12 \| version note: chapter renumbering, #1936
- **2-3** renumbered (recorded, 2026-10-02)
  - note: New ch: 04 -> 05 \| version note: chapter renumbering, #1936
- **2-4** renumbered (recorded, 2026-10-02)
  - note: New ch: 09 -> 02 \| version note: chapter renumbering, #1936
- **2-5** renumbered (recorded, 2026-10-02)
  - note: New ch: 09 -> 02 \| version note: chapter renumbering, #1936
- **2-8** renumbered (recorded, 2026-10-02)
  - note: New ch: 04, 09 -> 05, 02 \| version note: chapter renumbering, #1936
- **2-9** renumbered (recorded, 2026-10-02)
  - note: New ch: 05 -> 06 \| version note: chapter renumbering, #1936
- **2-10** renumbered (recorded, 2026-10-02)
  - note: New ch: 04 -> 05 \| version note: chapter renumbering, #1936
- **2-11** renumbered (recorded, 2026-10-02)
  - note: New ch: 06 -> 07 \| version note: chapter renumbering, #1936
- **2-13** renumbered (recorded, 2026-10-02)
  - note: New ch: 02 -> 03 \| version note: chapter renumbering, #1936
- **2-14** renumbered (recorded, 2026-10-02)
  - note: New ch: 04 -> 05 \| version note: chapter renumbering, #1936
- **2-15** renumbered (recorded, 2026-10-02)
  - note: New ch: 05 -> 06 \| version note: chapter renumbering, #1936
- **2-16** renumbered (recorded, 2026-10-02)
  - note: New ch: 08 -> 09 \| version note: chapter renumbering, #1936
- **3-1** renumbered (recorded, 2026-10-02)
  - note: New ch: 09 -> 02 \| version note: chapter renumbering, #1936
- **3-2** renumbered (recorded, 2026-10-02)
  - note: New ch: 09 -> 02 \| version note: chapter renumbering, #1936
- **3-3** renumbered (recorded, 2026-10-02)
  - note: New ch: 09 -> 02 \| version note: chapter renumbering, #1936
- **3-4** renumbered (recorded, 2026-10-02)
  - note: New ch: 09 -> 02 \| version note: chapter renumbering, #1936
- **3-5** renumbered (recorded, 2026-10-02)
  - note: New ch: 09 -> 02 \| version note: chapter renumbering, #1936
- **3-6** renumbered (recorded, 2026-10-02)
  - note: New ch: 09 held -> 02 held \| version note: chapter renumbering, #1936
- **3-7** renumbered (recorded, 2026-10-02)
  - note: New ch: 09 -> 02 \| version note: chapter renumbering, #1936
- **3-8** renumbered (recorded, 2026-10-02)
  - note: New ch: 09 -> 02 \| version note: chapter renumbering, #1936
- **3-9** renumbered (recorded, 2026-10-02)
  - note: New ch: 09 -> 02 \| version note: chapter renumbering, #1936
- **3-10** renumbered (recorded, 2026-10-02)
  - note: New ch: 09 -> 02 \| version note: chapter renumbering, #1936
- **3-11** renumbered (recorded, 2026-10-02)
  - note: New ch: 09 -> 02 \| version note: chapter renumbering, #1936
- **3-13** renumbered (recorded, 2026-10-02)
  - note: New ch: 09 -> 02 \| version note: chapter renumbering, #1936
- **3-14** renumbered (recorded, 2026-10-02)
  - note: New ch: 09 -> 02 \| version note: chapter renumbering, #1936
- **4-1** renumbered (recorded, 2026-10-02)
  - note: New ch: 03, 10.0, 10.3 -> 04, 10.0, 10.4 \| version note: chapter renumbering, #1936
- **4-2** renumbered (recorded, 2026-10-02)
  - note: New ch: 02, 13 -> 03, 14 \| version note: chapter renumbering, #1936
- **4-3** renumbered (recorded, 2026-10-02)
  - note: New ch: 03 -> 04 \| version note: chapter renumbering, #1936
- **4-4** renumbered (recorded, 2026-10-02)
  - note: New ch: 03, 10.3 -> 04, 10.4 \| version note: chapter renumbering, #1936
- **4-5** renumbered (recorded, 2026-10-02)
  - note: New ch: 02 -> 03 \| version note: chapter renumbering, #1936
- **4-7** renumbered (recorded, 2026-10-02)
  - note: New ch: 08 -> 09 \| version note: chapter renumbering, #1936
- **4-8** renumbered (recorded, 2026-10-02)
  - note: New ch: 09 held -> 02 held \| version note: chapter renumbering, #1936
- **4-9** renumbered (recorded, 2026-10-02)
  - note: New ch: 02 -> 03 \| version note: chapter renumbering, #1936
- **4-10** renumbered (recorded, 2026-10-02)
  - note: New ch: 13 -> 14 \| version note: chapter renumbering, #1936
- **5-1** renumbered (recorded, 2026-10-02)
  - note: New ch: 05 -> 06 \| version note: chapter renumbering, #1936
- **5-2** renumbered (recorded, 2026-10-02)
  - note: New ch: 05 -> 06 \| version note: chapter renumbering, #1936
- **5-3** renumbered (recorded, 2026-10-02)
  - note: New ch: 05, 12 -> 06, 12 \| version note: chapter renumbering, #1936
- **6-1** renumbered (recorded, 2026-10-02)
  - note: New ch: 04 -> 05 \| version note: chapter renumbering, #1936
- **6-2** renumbered (recorded, 2026-10-02)
  - note: New ch: 04, 09 -> 05, 02 \| version note: chapter renumbering, #1936
- **6-3** renumbered (recorded, 2026-10-02)
  - note: New ch: 04 -> 05 \| version note: chapter renumbering, #1936
- **8-1** renumbered (recorded, 2026-10-02)
  - note: New ch: 10.1, 13 -> 10.1, 14 \| version note: chapter renumbering, #1936
- **8-2** renumbered (recorded, 2026-10-02)
  - note: New ch: 13 held -> 14 held \| version note: chapter renumbering, #1936
- **8-4** renumbered (recorded, 2026-10-02)
  - note: New ch: 13 held -> 14 held \| version note: chapter renumbering, #1936
- **9-1** renumbered (recorded, 2026-10-02)
  - note: New ch: 12, 10.3, 11 -> 12, 10.4, 11 \| version note: chapter renumbering, #1936
- **9-4** renumbered (recorded, 2026-10-02)
  - note: New ch: 05, 12 -> 06, 12 \| version note: chapter renumbering, #1936
- **10-1** renumbered (recorded, 2026-10-02)
  - note: New ch: 13 -> 14 \| version note: chapter renumbering, #1936
- **10-2** renumbered (recorded, 2026-10-02)
  - note: New ch: 13 -> 14 \| version note: chapter renumbering, #1936
- **10-3** renumbered (recorded, 2026-10-02)
  - note: New ch: 13 -> 14 \| version note: chapter renumbering, #1936
- **10-4** renumbered (recorded, 2026-10-02)
  - note: New ch: 13 -> 14 \| version note: chapter renumbering, #1936
- **10-5** renumbered (recorded, 2026-10-02)
  - note: New ch: 13 held -> 14 held \| version note: chapter renumbering, #1936
- **10-6** renumbered (recorded, 2026-10-02)
  - note: New ch: 13 held -> 14 held \| version note: chapter renumbering, #1936
- **10-7** renumbered (recorded, 2026-10-02)
  - note: New ch: 13 -> 14 \| version note: chapter renumbering, #1936
- **9-5** verdict changed (recorded, 2026-10-01)
  - verdict before: Held
  - verdict after: Restated
  - note: verdict cell: 'Held' -> 'Restated (verse) / Held (model)' \| version note: anger strand, #1920
- **9-5** claim restated (recorded, 2026-10-01)
  - claim before: The foothold principle (Eph 4:26–27)
  - claim after: Updated 2026-10-01 (anger strand): Eph 4:26–27 is now read. The verse ties the "opportunity to the devil" to anger kept past sunset: "do not let the sun go down on your anger, and give no opportunity to the devil". That is woven. A general model of how the devil gains ground is not stated and stays held
  - note: evidence and restatement cell changed \| version note: anger strand, #1920
- **9-5** edited (recorded, 2026-10-01)
  - note: New ch: 12 held -> 12 \| version note: anger strand, #1920
- **I-1** claim created (recorded, 2026-09-30)
  - claim before: —
  - claim after: The study spans "five centuries of personal inquiry"
  - verdict before: —
  - verdict after: Withdrawn
  - note: as first recorded in claim register v1: verdict cell 'Withdrawn'; evidence 'Error in the original. The May retelling already dropped it'; new ch '—'
- **I-1** claim withdrawn (recorded, 2026-09-30)
  - note: status: current -> withdrawn
- **I-2** claim created · 01 (recorded, 2026-09-30)
  - claim before: —
  - claim after: The earlier counts came from extracts and are partly estimates ("~150"). The reading now covers 2,688 verses containing 38 Hebrew and Greek words for heart, soul, spirit, flesh, conscience and bosom, each verse read in context
  - verdict before: —
  - verdict after: Restated
  - note: as first recorded in claim register v1: verdict cell 'Restated'; evidence 'The earlier counts came from extracts and are partly estimates ("~150"). The reading now covers 2,688 verses containing 38 Hebrew and Greek words for heart, soul, spirit, flesh, conscience and bosom, each verse read in context'; new ch '01'
- **I-3** claim created · 09 (recorded, 2026-09-30)
  - claim before: —
  - claim after: Only the overlap is confirmed as stated. The other three are qualified or withdrawn (2-2, 2-5, 2-14/15)
  - verdict before: —
  - verdict after: Restated
  - note: as first recorded in claim register v1: verdict cell 'Restated'; evidence 'Only the overlap is confirmed as stated. The other three are qualified or withdrawn (2-2, 2-5, 2-14/15)'; new ch '08'
- **I-4** claim created · 01 (recorded, 2026-09-30)
  - claim before: —
  - claim after: The original then framed everything as two parts against three. The new narrative does what this sentence says: the central question is how the inner being works, as Scripture describes it
  - verdict before: —
  - verdict after: Restated
  - note: as first recorded in claim register v1: verdict cell 'Restated'; evidence 'The original then framed everything as two parts against three. The new narrative does what this sentence says: the central question is how the inner being works, as Scripture describes it'; new ch '01'
- **I-5** claim created (recorded, 2026-09-30)
  - claim before: —
  - claim after: "Modern neuroscience unexpectedly corroborated" the findings
  - verdict before: —
  - verdict after: Held
  - note: as first recorded in claim register v1: verdict cell 'Held'; evidence 'Science chapters later'; new ch '—'
- **I-5** edited (recorded, 2026-09-30)
  - note: status: current -> held
- **I-6** claim created · 06 (recorded, 2026-09-30)
  - claim before: —
  - claim after: God's Spirit is given into the heart (Gal 4:6; 2Co 1:22), pours love into hearts (Rom 5:5), is put within (Eze 36:27), comes upon people (Judg 14:6; 1Sa 16:13), and makes the body a temple (1Co 6:19). The human spirit is one of several places, not the primary one (dep §2.3d, §3.7)
  - verdict before: —
  - verdict after: Restated
  - note: as first recorded in claim register v1: verdict cell 'Restated'; evidence "God's Spirit is given into the heart (Gal 4:6; 2Co 1:22), pours love into hearts (Rom 5:5), is put within (Eze 36:27), comes upon people (Judg 14:6; 1Sa 16:13), and makes the body a temple (1Co 6:19). The human spirit is one of several places, not the primary one (dep §2.3d, §3.7)"; new ch '05, 13'
- **1-1** claim created · 03 (recorded, 2026-09-30)
  - claim before: —
  - claim after: Soul and spirit in synonymous parallel (Isa 26:9; Job 7:11; Luk 1:46–47)
  - verdict before: —
  - verdict after: Widened
  - note: as first recorded in claim register v1: verdict cell 'Widened'; evidence 'Stands. Heart // spirit (Psa 51:10, 17; 34:18; 143:4; Exo 35:21) and heart // soul (Pro 2:10; Psa 13:2) are just as common. Translators move one Hebrew word between heart, soul, spirit and mind (dep §3.1)'; new ch '02'
- **1-2** claim created · 03 (recorded, 2026-09-30)
  - claim before: —
  - claim after: Hannah uses both words for one experience (1Sa 1:10–15)
  - verdict before: —
  - verdict after: Widened
  - note: as first recorded in claim register v1: verdict cell 'Widened'; evidence 'Stands, and the scene uses four: bitter of soul (1:10), "speaking in her heart" (1:13), "why is your heart sad?" (1:8), "troubled in spirit … pouring out my soul" (1:15) (E §1.1; F §7)'; new ch '02, 10.8'
- **1-3** claim created · 03 (recorded, 2026-09-30)
  - claim before: —
  - claim after: Soul as "myself" is common (about 126 Hebrew verses; e.g. Lev 16:29 "afflict yourselves"). Spirit is not shown as a reflexive. 1Co 5:3 and Col 2:5 say the spirit can be present where the body is absent, which is a different claim. Rom 1:9 is service located in the spirit (dep §2.2a, §3.4; H §3.1)
  - verdict before: —
  - verdict after: Restated
  - note: as first recorded in claim register v1: verdict cell 'Restated'; evidence 'Soul as "myself" is common (about 126 Hebrew verses; e.g. Lev 16:29 "afflict yourselves"). Spirit is not shown as a reflexive. 1Co 5:3 and Col 2:5 say the spirit can be present where the body is absent, which is a different claim. Rom 1:9 is service located in the spirit (dep §2.2a, §3.4; H §3.1)'; new ch '02, 04, 05'
- **1-4** claim created · 10.1 (recorded, 2026-09-30)
  - claim before: —
  - claim after: They overlap, but each word has its own profile. Soul: bitterness, longing, weariness. Spirit: troubled, crushed, faint, and temper. Heart: the widest range of all (A §9.1)
  - verdict before: —
  - verdict after: Restated
  - note: as first recorded in claim register v1: verdict cell 'Restated'; evidence 'They overlap, but each word has its own profile. Soul: bitterness, longing, weariness. Spirit: troubled, crushed, faint, and temper. Heart: the widest range of all (A §9.1)'; new ch '10.1'
- **1-5** claim created · 10.9 (recorded, 2026-09-30)
  - claim before: —
  - claim after: Soul and spirit both worship
  - verdict before: —
  - verdict after: Widened
  - note: as first recorded in claim register v1: verdict cell 'Widened'; evidence 'Stands. The heart is the most prominent: it prays without voice (1Sa 1:13), cries (Lam 2:18), thanks "with my whole heart" (E §1.1, §13.1)'; new ch '10.8'
- **1-6** claim created · 03 (recorded, 2026-09-30)
  - claim before: —
  - claim after: The overlap is real but not total
  - verdict before: —
  - verdict after: Stands
  - note: as first recorded in claim register v1: verdict cell 'Stands'; evidence 'Now read as one inner person spoken of from several angles (dep §1)'; new ch '02'
- **2-1** claim created · 05 (recorded, 2026-09-30)
  - claim before: —
  - claim after: In these verses *nephesh* is the person, the one who answers for sin; it is not a faculty inside the person. The soul is the accountable, answerable self (D §3.1, §11.2)
  - verdict before: —
  - verdict after: Restated
  - note: as first recorded in claim register v1: verdict cell 'Restated'; evidence 'In these verses *nephesh* is the person, the one who answers for sin; it is not a faculty inside the person. The soul is the accountable, answerable self (D §3.1, §11.2)'; new ch '04, 12'
- **2-2** claim created · 06 (recorded, 2026-09-30)
  - claim before: —
  - claim after: No verse read makes the spirit the subject of "to sin". But the spirit is morally judged: haughty before a fall (Pro 16:18), "spirit was not faithful" (Psa 78:8), hardened by God (Deu 2:30), needing to be made "right" (Psa 51:10), with or without deceit (Psa 32:2), defiled with the body (2Co 7:1). The part Scripture judges most is the heart (D §3.4, §9.2, §11.1–3; C §9.2). The original itself listed Pro 16:18 and Deu 2:30, then set them aside
  - verdict before: —
  - verdict after: Restated
  - note: as first recorded in claim register v1: verdict cell 'Restated'; evidence 'No verse read makes the spirit the subject of "to sin". But the spirit is morally judged: haughty before a fall (Pro 16:18), "spirit was not faithful" (Psa 78:8), hardened by God (Deu 2:30), needing to be made "right" (Psa 51:10), with or without deceit (Psa 32:2), defiled with the body (2Co 7:1). The part Scripture judges most is the heart (D §3.4, §9.2, §11.1–3; C §9.2). The original itself listed Pro 16:18 and Deu 2:30, then set them aside'; new ch '05, 08, 12'
- **2-3** claim created · 05 (recorded, 2026-09-30)
  - claim before: —
  - claim after: Souls are saved from death and purified (Jam 5:20; 1Pe 1:22)
  - verdict before: —
  - verdict after: Stands
  - note: as first recorded in claim register v1: verdict cell 'Stands'; evidence 'Both in the reading'; new ch '04'
- **2-4** claim created · 02 (recorded, 2026-09-30)
  - claim before: —
  - claim after: Animals are *nephesh ḥayyâ* just as man is (Gen 1:20–24; 2:7; 9:10)
  - verdict before: —
  - verdict after: Stands
  - note: as first recorded in claim register v1: verdict cell 'Stands'; evidence 'G §1.1'; new ch '09'
- **2-5** claim created · 02 (recorded, 2026-09-30)
  - claim before: —
  - claim after: Animals almost never have *rûaḥ*; Ecc 3:21 is the only exception; Gen 7:22 uses *neshamah*, not *rûaḥ*
  - verdict before: —
  - verdict after: Withdrawn
  - note: as first recorded in claim register v1: verdict cell 'Withdrawn'; evidence 'The flood falls on "all flesh in which is the breath [*rûaḥ*] of life" (Gen 6:17; 7:15); "they all have the same breath" (Ecc 3:19); "the spirit of the beast" (Ecc 3:21); "When you take away their breath, they die" (Psa 104:29). [lexical] Gen 7:22 has both words together. What sets man apart in Gen 2:7 is God\'s own breathing into him, not the possession of breath (G §1.1; dep §3.10)'; new ch '09'
- **2-5** claim withdrawn (recorded, 2026-09-30)
  - note: status: current -> withdrawn
- **2-6** claim created (recorded, 2026-09-30)
  - claim before: —
  - claim after: The image of God may be located in the spirit
  - verdict before: —
  - verdict after: Withdrawn
  - note: as first recorded in claim register v1: verdict cell 'Withdrawn'; evidence 'No verse says so; inference from 2-5, which is withdrawn'; new ch '—'
- **2-6** claim withdrawn (recorded, 2026-09-30)
  - note: status: current -> withdrawn
- **2-7** claim created (recorded, 2026-09-30)
  - claim before: —
  - claim after: Animals cannot sin because they lack the spirit's moral awareness
  - verdict before: —
  - verdict after: Withdrawn
  - note: as first recorded in claim register v1: verdict cell 'Withdrawn'; evidence 'No verse says so; inference from 2-5'; new ch '—'
- **2-7** claim withdrawn (recorded, 2026-09-30)
  - note: status: current -> withdrawn
- **2-8** claim created · 05 (recorded, 2026-09-30)
  - claim before: —
  - claim after: The verse says "the life [*nephesh*] of the flesh is in the blood". Life is located in the blood; the soul is not equated with blood (dep §3.9)
  - verdict before: —
  - verdict after: Restated
  - note: as first recorded in claim register v1: verdict cell 'Restated'; evidence 'The verse says "the life [*nephesh*] of the flesh is in the blood". Life is located in the blood; the soul is not equated with blood (dep §3.9)'; new ch '04, 09'
- **2-9** claim created · 06 (recorded, 2026-09-30)
  - claim before: —
  - claim after: The spirit is "almost never associated with eating, appetite or physical needs"
  - verdict before: —
  - verdict after: Withdrawn
  - note: as first recorded in claim register v1: verdict cell 'Withdrawn'; evidence '"When he had eaten, his spirit revived" (1Sa 30:12); "when he drank, his spirit returned" (Judg 15:19); "a crushed spirit dries up the bones" (Pro 17:22); breath in the nostrils (Job 27:3) (dep §2.3b, §3.6)'; new ch '05'
- **2-9** claim withdrawn (recorded, 2026-09-30)
  - note: status: current -> withdrawn
- **2-10** claim created · 05 (recorded, 2026-09-30)
  - claim before: —
  - claim after: *Nephesh* is connected to throat and appetite
  - verdict before: —
  - verdict after: Widened
  - note: as first recorded in claim register v1: verdict cell 'Widened'; evidence '"The waters have come up to my neck" (Psa 69:1); "a knife to your throat if you are given to appetite" (Pro 23:2); *nephesh* as ordinary "want" (C §1.1; dep §2.2a)'; new ch '04'
- **2-11** claim created · 07 (recorded, 2026-09-30)
  - claim before: —
  - claim after: Stands for the NT. In the OT, flesh is frail, not hostile, and "a heart of flesh" is God's gift (Eze 36:26). The hostility of flesh to Spirit is NT-specific (dep §3.5)
  - verdict before: —
  - verdict after: Restated
  - note: as first recorded in claim register v1: verdict cell 'Restated'; evidence 'Stands for the NT. In the OT, flesh is frail, not hostile, and "a heart of flesh" is God\'s gift (Eze 36:26). The hostility of flesh to Spirit is NT-specific (dep §3.5)'; new ch '06'
- **2-12** claim created · 11 (recorded, 2026-09-30)
  - claim before: —
  - claim after: "God is spirit" (Joh 4:24) stands. But Scripture speaks freely of God's soul ("my soul shall not abhor you", Lev 26:11; "my soul hates", Isa 1:14; "my soul delights", Isa 42:1; he swears by his soul, Amo 6:8) and God's heart (Gen 6:6; Hos 11:8). No ranking of the words follows (dep §3.10)
  - verdict before: —
  - verdict after: Restated
  - note: as first recorded in claim register v1: verdict cell 'Restated'; evidence '"God is spirit" (Joh 4:24) stands. But Scripture speaks freely of God\'s soul ("my soul shall not abhor you", Lev 26:11; "my soul hates", Isa 1:14; "my soul delights", Isa 42:1; he swears by his soul, Amo 6:8) and God\'s heart (Gen 6:6; Hos 11:8). No ranking of the words follows (dep §3.10)'; new ch '11'
- **2-13** claim created · 03 (recorded, 2026-09-30)
  - claim before: —
  - claim after: The soul sits in a middle position, the interface between body and spirit
  - verdict before: —
  - verdict after: Withdrawn
  - note: as first recorded in claim register v1: verdict cell 'Withdrawn'; evidence 'A model, not a text. The verses show cause and effect running between every pair: heart → bones, spirit → bones, food → heart, food → spirit, sight → spirit (dep §3.6)'; new ch '02'
- **2-13** claim withdrawn (recorded, 2026-09-30)
  - note: status: current -> withdrawn
- **2-14** claim created · 05 (recorded, 2026-09-30)
  - claim before: —
  - claim after: The soul is the needing self, and much of its need is for God: "My soul thirsts for you" (Psa 63:1); "To you, O Lord, I lift up my soul" (Psa 25:1); "Bless the Lord, O my soul" (Psa 103:1) (dep §2.2b)
  - verdict before: —
  - verdict after: Restated
  - note: as first recorded in claim register v1: verdict cell 'Restated'; evidence 'The soul is the needing self, and much of its need is for God: "My soul thirsts for you" (Psa 63:1); "To you, O Lord, I lift up my soul" (Psa 25:1); "Bless the Lord, O my soul" (Psa 103:1) (dep §2.2b)'; new ch '04'
- **2-15** claim created · 06 (recorded, 2026-09-30)
  - claim before: —
  - claim after: The spirit is prominent in worship and is what is committed to God at death (E §13.4). Pro 20:27 uses *neshamah* "breath", not *rûaḥ* [lexical], and is outside the reading. The human spirit is equally temper, trouble and provocation (Pro 29:11; Gen 41:8; Act 17:16)
  - verdict before: —
  - verdict after: Restated
  - note: as first recorded in claim register v1: verdict cell 'Restated'; evidence 'The spirit is prominent in worship and is what is committed to God at death (E §13.4). Pro 20:27 uses *neshamah* "breath", not *rûaḥ* [lexical], and is outside the reading. The human spirit is equally temper, trouble and provocation (Pro 29:11; Gen 41:8; Act 17:16)'; new ch '05'
- **2-16** claim created · 09 (recorded, 2026-09-30)
  - claim before: —
  - claim after: The verse puts soul and spirit beside joints and marrow, which are adjacent, and its end point is the heart: "discerning the thoughts and intentions of the heart". It shows closeness that only the word can divide. It is one of several places the words part; others are added (1Co 15:45; 1Co 14:14–15; the *psychikos* / *pneumatikos* contrast in 1Co 2:14; 15:44–46) (dep §3.4; B §8)
  - verdict before: —
  - verdict after: Restated
  - note: as first recorded in claim register v1: verdict cell 'Restated'; evidence 'The verse puts soul and spirit beside joints and marrow, which are adjacent, and its end point is the heart: "discerning the thoughts and intentions of the heart". It shows closeness that only the word can divide. It is one of several places the words part; others are added (1Co 15:45; 1Co 14:14–15; the *psychikos* / *pneumatikos* contrast in 1Co 2:14; 15:44–46) (dep §3.4; B §8)'; new ch '08'
- **2-17** claim created (recorded, 2026-09-30)
  - claim before: —
  - claim after: Summary: spirit = "eternal essence, does not sin, uniquely human"; soul = "can sin, shared with animals"
  - verdict before: —
  - verdict after: Withdrawn
  - note: as first recorded in claim register v1: verdict cell 'Withdrawn'; evidence 'Rests on 2-2, 2-5 and 2-12'; new ch '—'
- **2-17** claim withdrawn (recorded, 2026-09-30)
  - note: status: current -> withdrawn
- **3-1** claim created · 02 (recorded, 2026-09-30)
  - claim before: —
  - claim after: The man becomes a *nephesh* (Gen 2:7)
  - verdict before: —
  - verdict after: Stands
  - note: as first recorded in claim register v1: verdict cell 'Stands'; evidence 'Text'; new ch '09'
- **3-2** claim created · 02 (recorded, 2026-09-30)
  - claim before: —
  - claim after: Gen 2:7's phrase is shared with the animals. The verse is marked by God breathing into one creature. The "formula" is an inference, not something the text states. 1Co 15:45 sets "a living being" against "a life-giving spirit" (G §1.1, §1.5)
  - verdict before: —
  - verdict after: Restated
  - note: as first recorded in claim register v1: verdict cell 'Restated'; evidence 'Gen 2:7\'s phrase is shared with the animals. The verse is marked by God breathing into one creature. The "formula" is an inference, not something the text states. 1Co 15:45 sets "a living being" against "a life-giving spirit" (G §1.1, §1.5)'; new ch '09'
- **3-3** claim created · 02 (recorded, 2026-09-30)
  - claim before: —
  - claim after: The original itself cites "the Lord who made our souls" (Jer 38:16). Also: "The Spirit of God has made me, and the breath of the Almighty gives me life" (Job 33:4). Both are made by God. The distinct-origins argument does not hold
  - verdict before: —
  - verdict after: Restated
  - note: as first recorded in claim register v1: verdict cell 'Restated'; evidence 'The original itself cites "the Lord who made our souls" (Jer 38:16). Also: "The Spirit of God has made me, and the breath of the Almighty gives me life" (Job 33:4). Both are made by God. The distinct-origins argument does not hold'; new ch '09'
- **3-4** claim created · 02 (recorded, 2026-09-30)
  - claim before: —
  - claim after: Whether this is spirit or breath cannot be decided from the verse (SC: U)
  - verdict before: —
  - verdict after: Restated
  - note: as first recorded in claim register v1: verdict cell 'Restated'; evidence 'Whether this is spirit or breath cannot be decided from the verse (SC: U)'; new ch '09'
- **3-5** claim created · 02 (recorded, 2026-09-30)
  - claim before: —
  - claim after: The verses stand (God's Spirit, SC D1). The inference about the human spirit is not stated by them and is dropped
  - verdict before: —
  - verdict after: Restated
  - note: as first recorded in claim register v1: verdict cell 'Restated'; evidence "The verses stand (God's Spirit, SC D1). The inference about the human spirit is not stated by them and is dropped"; new ch '09'
- **3-6** claim created (recorded, 2026-09-30)
  - claim before: —
  - claim after: Isa 49:1; Psa 71:6: identity and calling before birth
  - verdict before: —
  - verdict after: Held
  - note: as first recorded in claim register v1: verdict cell 'Held'; evidence 'Not in the reading'; new ch '09 held'
- **3-6** edited (recorded, 2026-09-30)
  - note: status: current -> held
- **3-7** claim created · 02 (recorded, 2026-09-30)
  - claim before: —
  - claim after: The soul departs at death (Gen 35:18)
  - verdict before: —
  - verdict after: Widened
  - note: as first recorded in claim register v1: verdict cell 'Widened'; evidence 'Each part gets its own verb at death: the soul departs, the heart "does not attend" (1Sa 4:20), the spirit is "not retained" (Ecc 8:8) or "gathered back" (Job 34:14). The heart can die before the body (1Sa 25:37–38) (G §16.1, §16.8)'; new ch '09'
- **3-8** claim created · 02 (recorded, 2026-09-30)
  - claim before: —
  - claim after: The spirit returns to God (Ecc 12:7; Luk 23:46; Act 7:59; Mat 27:50)
  - verdict before: —
  - verdict after: Stands
  - note: as first recorded in claim register v1: verdict cell 'Stands'; evidence 'Text'; new ch '09'
- **3-9** claim created · 02 (recorded, 2026-09-30)
  - claim before: —
  - claim after: These verses speak of the soul delivered or brought up from Sheol: a living person rescued from death. Sheol here is death and the grave, not a destination distinct from the spirit's. Ecc 3:21 leaves the spirit's destination open ("Who knows?"). The "different destinations" argument, which the original called "the most compelling evidence", does not hold (G §16.4; dep §3.9)
  - verdict before: —
  - verdict after: Restated
  - note: as first recorded in claim register v1: verdict cell 'Restated'; evidence 'These verses speak of the soul delivered or brought up from Sheol: a living person rescued from death. Sheol here is death and the grave, not a destination distinct from the spirit\'s. Ecc 3:21 leaves the spirit\'s destination open ("Who knows?"). The "different destinations" argument, which the original called "the most compelling evidence", does not hold (G §16.4; dep §3.9)'; new ch '09'
- **3-10** claim created · 02 (recorded, 2026-09-30)
  - claim before: —
  - claim after: Conscious existence after death (Rev 6:9; Heb 12:23)
  - verdict before: —
  - verdict after: Stands
  - note: as first recorded in claim register v1: verdict cell 'Stands'; evidence 'Text'; new ch '09'
- **3-11** claim created · 02 (recorded, 2026-09-30)
  - claim before: —
  - claim after: Mat 10:28: body killed, soul not
  - verdict before: —
  - verdict after: Stands
  - note: as first recorded in claim register v1: verdict cell 'Stands'; evidence 'Text'; new ch '09'
- **3-12** claim created (recorded, 2026-09-30)
  - claim before: —
  - claim after: No verse says "they cannot kill the spirit" because the spirit is "already safe" with God
  - verdict before: —
  - verdict after: Withdrawn
  - note: as first recorded in claim register v1: verdict cell 'Withdrawn'; evidence 'Speculation from silence'; new ch '—'
- **3-12** claim withdrawn (recorded, 2026-09-30)
  - note: status: current -> withdrawn
- **3-13** claim created · 02 (recorded, 2026-09-30)
  - claim before: —
  - claim after: "The body apart from the spirit is dead" (Jam 2:26)
  - verdict before: —
  - verdict after: Stands
  - note: as first recorded in claim register v1: verdict cell 'Stands'; evidence 'Text'; new ch '09'
- **3-14** claim created · 02 (recorded, 2026-09-30)
  - claim before: —
  - claim after: The verse stands. But "the life [*nephesh*] of the child came into him again" (1Ki 17:22), and "a breath of life from God entered them" (Rev 11:11). Scripture brings life back with soul, spirit or breath. No primacy follows (dep §3.9)
  - verdict before: —
  - verdict after: Restated
  - note: as first recorded in claim register v1: verdict cell 'Restated'; evidence 'The verse stands. But "the life [*nephesh*] of the child came into him again" (1Ki 17:22), and "a breath of life from God entered them" (Rev 11:11). Scripture brings life back with soul, spirit or breath. No primacy follows (dep §3.9)'; new ch '09'
- **3-15** claim created (recorded, 2026-09-30)
  - claim before: —
  - claim after: The primacy of the spirit; the hierarchy spirit → soul → body; redemption follows the same order
  - verdict before: —
  - verdict after: Withdrawn
  - note: as first recorded in claim register v1: verdict cell 'Withdrawn'; evidence 'Built on 3-3, 3-9 and 3-14'; new ch '—'
- **3-15** claim withdrawn (recorded, 2026-09-30)
  - note: status: current -> withdrawn
- **4-1** claim created · 04 (recorded, 2026-09-30)
  - claim before: —
  - claim after: Heart = emotion, thought, will, moral centre, core self
  - verdict before: —
  - verdict after: Widened
  - note: as first recorded in claim register v1: verdict cell 'Widened'; evidence 'The heart is the centre: it says within, attends, stores, is written on, is the source of speech and deeds, is opaque to all but God, and is where God acts (dep §2.1)'; new ch '03'
- **4-2** claim created · 03 (recorded, 2026-09-30)
  - claim before: —
  - claim after: Heart + soul = the totality formula; heart + spirit = renewal
  - verdict before: —
  - verdict after: Stands
  - note: as first recorded in claim register v1: verdict cell 'Stands'; evidence 'E §13.1, §11.2'; new ch '02, 13'
- **4-3** claim created · 04 (recorded, 2026-09-30)
  - claim before: —
  - claim after: No verse says the heart is where soul and spirit meet. What the verses show: the heart is the innermost place things are put, including God's Spirit (Gal 4:6), God's law, idols and eternity. Whether the heart is *the* integrating centre is left open (dep §3.7, §5)
  - verdict before: —
  - verdict after: Restated
  - note: as first recorded in claim register v1: verdict cell 'Restated'; evidence "No verse says the heart is where soul and spirit meet. What the verses show: the heart is the innermost place things are put, including God's Spirit (Gal 4:6), God's law, idols and eternity. Whether the heart is *the* integrating centre is left open (dep §3.7, §5)"; new ch '03'
- **4-4** claim created · 04 (recorded, 2026-09-30)
  - claim before: —
  - claim after: Hebrew has no word for "mind"; it uses *lēv*
  - verdict before: —
  - verdict after: Stands
  - note: as first recorded in claim register v1: verdict cell 'Stands'; evidence 'The ESV renders *lēv* "mind" in many places (1Ki 3:9; Pro 19:21) (dep §2.1n)'; new ch '03'
- **4-5** claim created · 03 (recorded, 2026-09-30)
  - claim before: —
  - claim after: The list of faculties shifts: Mat 22:37 heart · soul · mind; Mar 12:30 adds strength; Luk 10:27 reorders; the scribe says heart · understanding · strength, dropping soul, and Jesus calls the answer wise (Mar 12:33–34). What stays constant is "all" (F §2)
  - verdict before: —
  - verdict after: Restated
  - note: as first recorded in claim register v1: verdict cell 'Restated'; evidence 'The list of faculties shifts: Mat 22:37 heart · soul · mind; Mar 12:30 adds strength; Luk 10:27 reorders; the scribe says heart · understanding · strength, dropping soul, and Jesus calls the answer wise (Mar 12:33–34). What stays constant is "all" (F §2)'; new ch '02'
- **4-6** claim created (recorded, 2026-09-30)
  - claim before: —
  - claim after: "No spirit mentioned — perhaps implied" in the love command
  - verdict before: —
  - verdict after: Withdrawn
  - note: as first recorded in claim register v1: verdict cell 'Withdrawn'; evidence 'Speculation'; new ch '—'
- **4-6** claim withdrawn (recorded, 2026-09-30)
  - note: status: current -> withdrawn
- **4-7** claim created · 09 (recorded, 2026-09-30)
  - claim before: —
  - claim after: Mind vs flesh (Rom 7:25); spirit vs mind in prayer (1Co 14:14–15)
  - verdict before: —
  - verdict after: Stands
  - note: as first recorded in claim register v1: verdict cell 'Stands'; evidence 'dep §3.4–3.5'; new ch '08'
- **4-8** claim created (recorded, 2026-09-30)
  - claim before: —
  - claim after: *Neshamah* is the physical expression of *rûaḥ*: "spirit becomes breath becomes soul"
  - verdict before: —
  - verdict after: Withdrawn
  - note: as first recorded in claim register v1: verdict cell 'Withdrawn (model) / Held (word)'; evidence '*Neshamah* is outside the reading. The model is not stated by any verse'; new ch '09 held'
- **4-8** claim withdrawn (recorded, 2026-09-30)
  - note: status: current -> withdrawn
- **4-9** claim created · 03 (recorded, 2026-09-30)
  - claim before: —
  - claim after: The verse is a wholeness formula, like "soul and body" (Mat 10:28), "heart and flesh" (Psa 73:26), "body and spirit" (1Co 7:34). Scripture names the whole person by adding terms, not by defining parts. No ranking is stated (dep §3.2)
  - verdict before: —
  - verdict after: Restated
  - note: as first recorded in claim register v1: verdict cell 'Restated'; evidence 'The verse is a wholeness formula, like "soul and body" (Mat 10:28), "heart and flesh" (Psa 73:26), "body and spirit" (1Co 7:34). Scripture names the whole person by adding terms, not by defining parts. No ranking is stated (dep §3.2)'; new ch '02'
- **4-10** claim created · 14 (recorded, 2026-09-30)
  - claim before: —
  - claim after: New heart and new spirit are both needed (Eze 11:19; 36:26)
  - verdict before: —
  - verdict after: Widened
  - note: as first recorded in claim register v1: verdict cell 'Widened'; evidence 'Also "make yourselves a new heart and a new spirit" (Eze 18:31): the person\'s task and God\'s gift (E §11.2)'; new ch '13'
- **4-11** claim created (recorded, 2026-09-30)
  - claim before: —
  - claim after: "Heart emerges as integrated centre" in the creation process
  - verdict before: —
  - verdict after: Withdrawn
  - note: as first recorded in claim register v1: verdict cell 'Withdrawn'; evidence 'No text'; new ch '—'
- **4-11** claim withdrawn (recorded, 2026-09-30)
  - note: status: current -> withdrawn
- **5-1** claim created · 06 (recorded, 2026-09-30)
  - claim before: —
  - claim after: The percentages add up to more than 100%. Recount by what each verse itself shows (559 uses): 259 clearly God's Spirit; 28 God's Spirit only because the translation capitalises it; 138 human spirit; 68 other spirit-beings; 23 "a spirit of …" dispositions; 7 temper; 41 cannot be decided, each with its reason (SC §2–3)
  - verdict before: —
  - verdict after: Restated
  - note: as first recorded in claim register v1: verdict cell 'Restated'; evidence 'The percentages add up to more than 100%. Recount by what each verse itself shows (559 uses): 259 clearly God\'s Spirit; 28 God\'s Spirit only because the translation capitalises it; 138 human spirit; 68 other spirit-beings; 23 "a spirit of …" dispositions; 7 temper; 41 cannot be decided, each with its reason (SC §2–3)'; new ch '05'
- **5-2** claim created · 06 (recorded, 2026-09-30)
  - claim before: —
  - claim after: Replaced by the profile in 05: moved, stirred, troubled, crushed, revived, fervent, ruled, self-knowing (dep §2.3b; C §11.3; B §9.3)
  - verdict before: —
  - verdict after: Restated
  - note: as first recorded in claim register v1: verdict cell 'Restated'; evidence 'Replaced by the profile in 05: moved, stirred, troubled, crushed, revived, fervent, ruled, self-knowing (dep §2.3b; C §11.3; B §9.3)'; new ch '05'
- **5-3** claim created · 06 (recorded, 2026-09-30)
  - claim before: —
  - claim after: See 9-4
  - verdict before: —
  - verdict after: Restated
  - note: as first recorded in claim register v1: verdict cell 'Restated'; evidence 'See 9-4'; new ch '05, 12'
- **6-1** claim created · 05 (recorded, 2026-09-30)
  - claim before: —
  - claim after: The shape stands. Distinct Hebrew verses by sense: soul 230, life 180, myself 126, person 83, appetite 45, dead body 13, creature 12, neck 2. Greek: soul 46, life 33, person 8, myself 6. Add throat / neck (stocktake §2)
  - verdict before: —
  - verdict after: Restated
  - note: as first recorded in claim register v1: verdict cell 'Restated'; evidence 'The shape stands. Distinct Hebrew verses by sense: soul 230, life 180, myself 126, person 83, appetite 45, dead body 13, creature 12, neck 2. Greek: soul 46, life 33, person 8, myself 6. Add throat / neck (stocktake §2)'; new ch '04'
- **6-2** claim created · 05 (recorded, 2026-09-30)
  - claim before: —
  - claim after: Most soul-and-death verses are about life delivered from death, not survival after it (see 3-9). The survival texts (Mat 10:28; Rev 6:9) stand
  - verdict before: —
  - verdict after: Restated
  - note: as first recorded in claim register v1: verdict cell 'Restated'; evidence 'Most soul-and-death verses are about life delivered from death, not survival after it (see 3-9). The survival texts (Mat 10:28; Rev 6:9) stand'; new ch '04, 09'
- **6-3** claim created · 05 (recorded, 2026-09-30)
  - claim before: —
  - claim after: *Nephesh* covers the whole person, on a physical–spiritual continuum
  - verdict before: —
  - verdict after: Stands
  - note: as first recorded in claim register v1: verdict cell 'Stands'; evidence 'From throat to corpse (dep §2.2a)'; new ch '04'
- **8-1** claim created · 10.1 (recorded, 2026-09-30)
  - claim before: —
  - claim after: Rom 5:5 says love is poured into our hearts. The verses read show inner ↔ body effects in both directions (glad heart → face; bread → heart; sight → spirit). The one-way spirit → soul → body flow is not shown (dep §3.6; A §9.3)
  - verdict before: —
  - verdict after: Restated
  - note: as first recorded in claim register v1: verdict cell 'Restated'; evidence 'Rom 5:5 says love is poured into our hearts. The verses read show inner ↔ body effects in both directions (glad heart → face; bread → heart; sight → spirit). The one-way spirit → soul → body flow is not shown (dep §3.6; A §9.3)'; new ch '10.1, 13'
- **8-2** claim created (recorded, 2026-09-30)
  - claim before: —
  - claim after: What the Spirit does not produce (memory, imagination, grief, natural fear, sexuality)
  - verdict before: —
  - verdict after: Held
  - note: as first recorded in claim register v1: verdict cell 'Held'; evidence 'Fruit lists not yet read'; new ch '13 held'
- **8-2** edited (recorded, 2026-09-30)
  - note: status: current -> held
- **8-3** claim created (recorded, 2026-09-30)
  - claim before: —
  - claim after: Health effects of each quality
  - verdict before: —
  - verdict after: Held
  - note: as first recorded in claim register v1: verdict cell 'Held'; evidence 'Science, later'; new ch '—'
- **8-3** edited (recorded, 2026-09-30)
  - note: status: current -> held
- **8-4** claim created (recorded, 2026-09-30)
  - claim before: —
  - claim after: The spirit was "dead through sin" (Eph 2:1–5)
  - verdict before: —
  - verdict after: Held
  - note: as first recorded in claim register v1: verdict cell 'Held'; evidence 'Not in the reading. Note for the check: the verse reads "you were dead", not "your spirit"'; new ch '13 held'
- **8-4** edited (recorded, 2026-09-30)
  - note: status: current -> held
- **9-1** claim created · 12 (recorded, 2026-09-30)
  - claim before: —
  - claim after: Scripture locates the source of evil chiefly in the heart: "out of the heart come evil thoughts" (Mat 15:19; Mar 7:21); "the heart is deceitful above all things" (Jer 17:9); sin "engraved on the tablet of their heart" (Jer 17:1). The vice-list catalogue is not yet read (D §11.1, §11.7)
  - verdict before: —
  - verdict after: Restated
  - note: as first recorded in claim register v1: verdict cell 'Restated (location) / Held (catalogue)'; evidence 'Scripture locates the source of evil chiefly in the heart: "out of the heart come evil thoughts" (Mat 15:19; Mar 7:21); "the heart is deceitful above all things" (Jer 17:9); sin "engraved on the tablet of their heart" (Jer 17:1). The vice-list catalogue is not yet read (D §11.1, §11.7)'; new ch '12'
- **9-2** claim created (recorded, 2026-09-30)
  - claim before: —
  - claim after: Every corruption is the soul's self-ward orientation without the spirit's governance
  - verdict before: —
  - verdict after: Withdrawn
  - note: as first recorded in claim register v1: verdict cell 'Withdrawn'; evidence 'Depends on 2-14, 2-15 and 2-2'; new ch '—'
- **9-2** claim withdrawn (recorded, 2026-09-30)
  - note: status: current -> withdrawn
- **9-3** claim created · 12 (recorded, 2026-09-30)
  - claim before: —
  - claim after: Idols are taken "into their hearts" (Eze 14:3–7); the heart "goes after" idols (Eze 20:16); a "spirit of whoredom" leads astray (Hos 4:12) (dep §2.1i, §2.3c)
  - verdict before: —
  - verdict after: Restated
  - note: as first recorded in claim register v1: verdict cell 'Restated'; evidence 'Idols are taken "into their hearts" (Eze 14:3–7); the heart "goes after" idols (Eze 20:16); a "spirit of whoredom" leads astray (Hos 4:12) (dep §2.1i, §2.3c)'; new ch '12'
- **9-4** claim created · 06 (recorded, 2026-09-30)
  - claim before: —
  - claim after: Most "spirit of …" phrases name a disposition that comes upon a person; the verse does not name a being. The same phrasing is used for good gifts: a spirit of wisdom, skill, grace, justice. Some are given by God: "the Lord has poured out upon you a spirit of deep sleep" (Isa 29:10); the harmful spirit "from the Lord" (1Sa 16:14); God "sent an evil spirit" (Judg 9:23); the Lord "put a lying spirit" in the prophets' mouths (1Ki 22:23). 2Ti 1:7 says "God gave us a spirit not of fear". Spirit-beings are real (unclean spirits cast out; the spirit of divination, Act 16:16), but the one-to-one mapping to vice families is not in the text (SC; dep §2.3c; D §11.4)
  - verdict before: —
  - verdict after: Restated
  - note: as first recorded in claim register v1: verdict cell 'Restated'; evidence 'Most "spirit of …" phrases name a disposition that comes upon a person; the verse does not name a being. The same phrasing is used for good gifts: a spirit of wisdom, skill, grace, justice. Some are given by God: "the Lord has poured out upon you a spirit of deep sleep" (Isa 29:10); the harmful spirit "from the Lord" (1Sa 16:14); God "sent an evil spirit" (Judg 9:23); the Lord "put a lying spirit" in the prophets\' mouths (1Ki 22:23). 2Ti 1:7 says "God gave us a spirit not of fear". Spirit-beings are real (unclean spirits cast out; the spirit of divination, Act 16:16), but the one-to-one mapping to vice families is not in the text (SC; dep §2.3c; D §11.4)'; new ch '05, 12'
- **9-5** claim created · 12 (recorded, 2026-09-30)
  - claim before: —
  - claim after: The foothold principle (Eph 4:26–27)
  - verdict before: —
  - verdict after: Held
  - note: as first recorded in claim register v1: verdict cell 'Held'; evidence 'Not in the reading'; new ch '12 held'
- **9-6** claim created (recorded, 2026-09-30)
  - claim before: —
  - claim after: Flesh (Jam 1:14), devil, world as three sources (Eph 2:2–3)
  - verdict before: —
  - verdict after: Held
  - note: as first recorded in claim register v1: verdict cell 'Held'; evidence 'Eph 2:2 "the spirit now at work in the sons of disobedience" is in the reading (other spirit, C §11.8). The three-source model is not yet checked'; new ch '12 held'
- **9-6** edited (recorded, 2026-09-30)
  - note: status: current -> held
- **9-7** claim created (recorded, 2026-09-30)
  - claim before: —
  - claim after: Rom 1:21–32 as a five-step descent
  - verdict before: —
  - verdict after: Held
  - note: as first recorded in claim register v1: verdict cell 'Held'; evidence 'Not read. Note: its step two is "foolish hearts were darkened"'; new ch '12 held'
- **9-7** edited (recorded, 2026-09-30)
  - note: status: current -> held
- **10-1** claim created · 14 (recorded, 2026-09-30)
  - claim before: —
  - claim after: The verses read give the Spirit into the heart (Gal 4:6; 2Co 1:22; Rom 5:5), within (Eze 36:27) and in the body (1Co 6:19), and bear witness with our spirit (Rom 8:16). The renewal texts renew heart and spirit together and replace stone with flesh (Eze 11:19; 36:26) (E §11.2)
  - verdict before: —
  - verdict after: Restated
  - note: as first recorded in claim register v1: verdict cell 'Restated'; evidence 'The verses read give the Spirit into the heart (Gal 4:6; 2Co 1:22; Rom 5:5), within (Eze 36:27) and in the body (1Co 6:19), and bear witness with our spirit (Rom 8:16). The renewal texts renew heart and spirit together and replace stone with flesh (Eze 11:19; 36:26) (E §11.2)'; new ch '13'
- **10-2** claim created · 14 (recorded, 2026-09-30)
  - claim before: —
  - claim after: "That which is born of the Spirit is spirit" (Joh 3:6)
  - verdict before: —
  - verdict after: Stands
  - note: as first recorded in claim register v1: verdict cell 'Stands'; evidence 'Text'; new ch '13'
- **10-3** claim created · 14 (recorded, 2026-09-30)
  - claim before: —
  - claim after: "Within" is already the OT promise (Eze 36:27; 37:14). The OT also has the Spirit turning a man "into another man" (1Sa 10:6)
  - verdict before: —
  - verdict after: Restated
  - note: as first recorded in claim register v1: verdict cell 'Restated'; evidence '"Within" is already the OT promise (Eze 36:27; 37:14). The OT also has the Spirit turning a man "into another man" (1Sa 10:6)'; new ch '13'
- **10-4** claim created · 14 (recorded, 2026-09-30)
  - claim before: —
  - claim after: The body's redemption at the end stands (Rom 8:23; 1Co 15:42–44), but these are not in the reading and are held. The text renews the inner self "day by day" (2Co 4:16); renewal is both God's gift (Eze 36:26) and the person's task (Eze 18:31). Assigning each phase to one component is not stated
  - verdict before: —
  - verdict after: Restated
  - note: as first recorded in claim register v1: verdict cell 'Restated'; evidence 'The body\'s redemption at the end stands (Rom 8:23; 1Co 15:42–44), but these are not in the reading and are held. The text renews the inner self "day by day" (2Co 4:16); renewal is both God\'s gift (Eze 36:26) and the person\'s task (Eze 18:31). Assigning each phase to one component is not stated'; new ch '13'
- **10-5** claim created (recorded, 2026-09-30)
  - claim before: —
  - claim after: Seven conditions (2Ch 7:14)
  - verdict before: —
  - verdict after: Held
  - note: as first recorded in claim register v1: verdict cell 'Held'; evidence 'Belongs to the Holy Spirit study'; new ch '13 held'
- **10-5** edited (recorded, 2026-09-30)
  - note: status: current -> held
- **10-6** claim created (recorded, 2026-09-30)
  - claim before: —
  - claim after: Means of grace; historical revivals
  - verdict before: —
  - verdict after: Held
  - note: as first recorded in claim register v1: verdict cell 'Held'; evidence 'Outside the reading'; new ch '13 held'
- **10-6** edited (recorded, 2026-09-30)
  - note: status: current -> held
- **10-7** claim created · 14 (recorded, 2026-09-30)
  - claim before: —
  - claim after: 1Th 5:23 as the final word
  - verdict before: —
  - verdict after: Stands
  - note: as first recorded in claim register v1: verdict cell 'Stands'; evidence 'As a wholeness prayer (see 4-9)'; new ch '13'
- **K-1** claim created (recorded, 2026-09-30)
  - claim before: —
  - claim after: "Spirit first, soul second, body third"; "inside out"
  - verdict before: —
  - verdict after: Withdrawn
  - note: as first recorded in claim register v1: verdict cell 'Withdrawn'; evidence 'Built on 3-15 and 10-4'; new ch '—'
- **K-1** claim withdrawn (recorded, 2026-09-30)
  - note: status: current -> withdrawn
- **K-2** claim created (recorded, 2026-09-30)
  - claim before: —
  - claim after: Science "catching up" with Scripture
  - verdict before: —
  - verdict after: Held
  - note: as first recorded in claim register v1: verdict cell 'Held'; evidence 'Science later'; new ch '—'
- **K-2** edited (recorded, 2026-09-30)
  - note: status: current -> held

## Structure log

| Date | Strand | Change | Reason |
|---|---|---|---|
| 2026-09-30 | origin of thought | Ch 10 → Part 10. One file per operation (10.0 opening/map + 10.1–10.9). Text moved unchanged (verified identical apart from headings). Prior file → `archive/10-the-inner-being-at-work-v1-20260930.md`. Claim-register rows 1-2, 1-4, 1-5 and 8-1 re-pointed to 10.1 / 10.8. | Every strand describes an operation, so Ch 10 would otherwise become a dumping ground. Researcher: "Chap 10 is likely to grow significantly … give careful thought on how it would like in advance." |
| 2026-09-30 | origin of thought | 10.3 Thinking reserved (option B). 10.4 Speaking reserved (NS-1, approved: "approve NS-1 speaking"). It is placed straight after Thinking because thought passes into speech on the path in 10.0. Later operations renumbered from the design proposal: Wanting 10.5 … Relating to others 10.9. | Ledger: about ten observations concern the inner being coming out through tongue, lips and mouth, with no home until now. |
| 2026-09-30 | origin of thought | Remembering not given a file. Watched (NS-2: "watch NS-2"). | Too thin so far; it currently sits within 10.2 and Ch 3. |
| 2026-09-30 | origin of thought | The thought-to-deed path goes in 10.0 (researcher: "path in 10.0"). | The path runs through several operations, so it belongs to the map of how they connect. |
| 2026-09-30 | inner seat (M47) | the narrative regenerated as chapter files (2026-09-30 reset) |  |
| 2026-10-01 | origin of thought | Woven (step 4). New: 10.3 Thinking, 10.4 Speaking. Rewritten: 10.0 (the path from a thought to a deed; where I am answerable; how the activities connect). Reshaped: Ch 3 (heart as the *place* of thinking; inner-speech verdicts by kind), 10.2 (hearing both ways), Ch 12 (Gen 6:5 with 8:21; pride as false likeness). Widened: Ch 1 (roadmap), 7, 9, 11, 13; 10.1, 10.5–10.9 (each now ends with Connections). 15 chapter files → v2 (v1s in `archive/`); claim register → v2. Ledger: 40 of 40 observations woven; quotes ESV-checked against iba.db. | Researcher: "proceed with step 4, I think we heading in the right direction." Method: weave, don't fit. |
| 2026-10-01 | origin of thought — change of character (#1919) | No new files; Ch 11 §4 grows into an account. §4 "One word, opposite values" gains the sub-section "What changes the character", the cross-cutting account that later strands add to. 10.3 gains "When thinking changes character", "Thoughts that turn on the thinker" (flow 3) and "What is devised comes back" (flow 5). 10.0 gains "The path runs back". Versions: 10.0, 10.8, 10.9, 11, 12, 13 → v3; 10.3, 10.4 → v2 (prior versions in `archive/`). Claim register → v3. Ledger → v2 (§I, §J; OT-41 to OT-53). | Researcher: "approve 1 2 3 4, proceed with the build". Key discovery: a word's character changes with its circumstances (#1919). |
| 2026-10-01 | anger (M02; #1920) | Three structure changes (researcher: "approve 1920 as recommended, remembering after 10.2"). (1) Human anger is woven by activity, not given a file (NS-M1a). 10.1 Feeling is rewritten to follow how a feeling rises, settles in the body, stays or passes, and turns, with anger as the most fully traced case. (2) New 10.3 Remembering and forgetting (NS-M3; was NS-2 "watch"). Former 10.3–10.9 are renumbered to 10.4–10.10, files renamed, and every cross-reference renumbered (53 references). (3) New Ch 13 "Under God's anger" (NS-M2a) between "goes wrong" and "made new". Former Ch 13 → 14 and Ch 14 → 15. Woven: 10.0 (the path can start with a feeling), 10.2, 10.4–10.10, Ch 1 (roadmap), 5, 6, 7, 9 (*ʾaph*: the nostrils of life and of anger), 11 (§2, §4 faces + factors, §6, §8), 12 (anger that goes wrong; false peace; Meribah), 14, 15 (strands woven, not given chapters: its last paragraph restated). Prior versions in `archive/`. Claim register → v4. | Anger has almost no presence in the narrative before this. Its human side runs through every activity; God's anger as borne by the human is a whole situation of the inner life, and the largest body of verses in the strand. |
| 2026-10-01 | (researcher ruling, #1924) | Chapter titles reduced to their subject. Ch 3 "The heart", Ch 4 "The soul", Ch 5 "The spirit", Ch 6 "Flesh", Ch 7 "Conscience and the bosom". Ch 2 "One inner person, many words" stays (researcher: *"the title is appropriate"*). Watch: a separate chapter on the role other entities play across the phenomena (God, the Spirit, other spirits, angels, other people, the physical world), which "will again vary considerably between the identities towards the inner being". It grows from what the strands record and is not started as a whole-scope task. | Researcher: the subtitles were "AI assumptions and wrong"; "I can see a separate chapter evolving over time to capture the role other entities play across the phenomena". |
| 2026-10-01 | fear (M01), unit 1 (#1927, #1928) | No structure change. Fear is woven by activity, as anger was. New sections: 10.5 "Fear and the mouth"; 10.9 "Fear before God, and the fear of God" and "'Fear not'"; 10.10 "Fear between people"; Ch 12 "Fear that goes wrong". Ch 11 §4 gains three faces (fear; the one who is feared; "do not fear") and three factors (what it is turned toward; whether the heart is in it; who speaks it, and to what end). Woven also into 10.1, 10.2, 10.7, 10.8, Ch 3, 6, 9, 13, 14, 15. Prior versions in `archive/`. Claim register → v5. | Researcher: "the ledger is approved to continue". Unit 1 = the *yārēʾ* family ("to fear, revere"), 424 hits read by surface. Units 2–4 to follow. |
| 2026-10-01 | fear (M01), unit 2 (#1929) | No structure change. New sections: 13 "Dread and trembling"; 14 "No one to make them afraid". Ch 11 §1 gains "Dread is laid on, given, and comes upon"; §4 gains three faces (dread; trembling, *rāgaz*; "none shall make you afraid") and one factor (who hears it). Woven also into 10.1, 10.2, 10.5, 10.7, 10.9, 10.10, Ch 3, 5, 6, 12, 15. Prior versions in `archive/`. Claim register → v6. | Researcher: "proceed with the weaving". Unit 2 = *paḥad* ("dread") and the trembling and shuddering words, 227 hits read by surface. |
| 2026-10-01 | fear (M01), review (#1930) | 10.1 gains a section "Fear" (what fear is; the words *yārēʾ*, *paḥad*, *ḥārad*, *rāgaz*; what fear does; the fear of God; what changes it; meeting fear). The fear passages scattered through 10.1's stages are folded into it; anger keeps the stage-by-stage course. For the researcher's review in context. The other chapters are not yet reworked. | Researcher: "We lost meaning and interpretation, it is starting to just become a list of quotes"; "you are not writing with intelligence and interpretation"; "integrate it into the narrative so I can review it in context." |
| 2026-10-01 | fear (M01), rework (#1930) | Fear rewritten for meaning across the book. 10.1's "Fear" section approved as the model (researcher: "proceed, I read in there is an improvement"). The fear passages in 10.5, 10.7, 10.9, 10.10, 12, 13, 14, 15 and Ch 11 §4 are rewritten in the same way: prose that says what the verses show, chosen verses, no repetition of 10.1, pointers back to it. 10.9's fear sections went from about 2,000 words of lists to about 1,100. Versions: 10.5, 10.7 v6; 10.9, 10.10, 11, 12, 14 v7; 13 v4; 15 v5. Correction: Job 31:34 is part of Job's oath of innocence, not his experience; 10.5 now says so. Anger not yet reworked. | Researcher: "you are not writing with intelligence and interpretation, you just doing a machanical mix and match excercise". |
| 2026-10-02 | doubt and discouragement (M20; #1931) | Accounts written for meaning, from the M20 reading already done (not re-read). 10.1 gains "Anxiety" (the words *merimnaō*, *meteōrizō*, *dāʾag*/*deʾāgāh*, *śarʿappîm*; what it does; care that is good; meeting anxiety) and "Losing heart". 10.2 gains "Perplexity", "Understanding that is hidden" and "Doubt". 10.5 gains "Grumbling" and "Whispering". 10.9 gains "When God hides his face". Versions: 10.1 v7; 10.2 v6; 10.5 v7; 10.9 v8 (2026-10-02). Proposed, not done: NS-D1, a new 10.11 "Hiding and disclosing" for the hiding and concealing verses (about 180 of 275), which have no activity home. A draft account is in the digest file. The second pass (Ch 11 §4, 10.10, 12, 3, 14, 15, 10.0) waits for review. Digest and placements: `../../../Clusters/M20 - doubt-discouragement/wa-cluster-M20-narrative-digest-v1-20261002.md`. | Researcher: "proceed with M20 - similar to the previous session" (#1931). Same order as #1930: the main accounts first, for review in context. |
| 2026-10-02 | doubt and discouragement (M20), NS-D1 + second pass (#1931) | New 10.11 "Hiding and disclosing" (NS-D1 option A; researcher: "ns-d1: select A; I reviewed the edited files, looks good."). The draft from the digest §4 is placed unchanged, with Connections added. No renumbering. Second pass: 10.0 v5 (10.11 in the map; two new connections); 10.5 v8 and 10.9 v9 (pointers); 10.10 v8 (new section "Care, discouragement and hiding between people"); Ch 11 v8 (§4 faces: care, hiding, murmuring; factors: whether it divides the person, who acts on whom); Ch 12 v8 (the hidden trap planned in the heart); Ch 3 v6 (Isa 29:15–16); Ch 14 v8 (Eze 39:29; Isa 29:24; Col 3:3); Ch 15 v6 (strand paragraph; the project word "seat" removed from a bullet). | Hiding and concealing (about 180 of M20's 275 verses) belong to the whole person and face both God and others, so no existing activity could hold them as one account. |
| 2026-10-02 | life and death (M25; #1936) | Ch 9 "Life, breath and death" moved to Ch 2 (researcher, verbatim: *"Move Ch 9 to Ch 2"*). Old Ch 2–8 become Ch 3–9; 10.x–15 unchanged. Chapter text is unchanged apart from the chapter headings, the Ch 1 roadmap and the "Chapter N" cross-references (one back-pointer in Ch 5 reworded: "I return to … in Chapter 9" → "I looked at … in Chapter 2"). Files bumped: 01 v4; 02–09 (new numbers); 10.1 v8, 10.2 v7, 10.3 v2, 10.4 v4, 10.5 v9, 10.6 v4, 10.8 v5, 10.9 v10, 11 v9, 12 v9, 15 v7. Claim register v7 ("New ch" remapped; three #1920-era pointers corrected: 10.3→10.4, 10.8→10.9, 13→14). Priors → `archive/`. Not yet done: Ch 2's opening was written for the end of the book ("This is where Scripture's inner words come closest to being separated…") and assumes the word chapters have gone before. It awaits the researcher's direction, together with the umbrella framing (OT-08). | Researcher (OT-08, `../../../cross-cluster-web/open-threads-register.md`): *"life and death is the umbrella over inner being: life is why we live and what makes living - death is the end, and the new beginning."* |
| 2026-10-02 | life and death (M25), unit 1 (#1934, #1937) | Ch 2 rewritten as the scene-setting chapter (researcher: *"the context of Ch 2 is that it sets the scene for discovering the working of the inner being within the context of what life is about and what death means"*; shape approved: *"I go along with your ch2 scene setting and the weaving suggestions"*). New opening; new sections "Where life flows from", "Life set before a person", "Life asked for", "What death is", "Made alive", "The body raised", "What follows"; existing sections kept and widened. Language drawn from the verses ("the breath of life", "the springs of life", "life and death set before you", "from death to life"); "umbrella" is not used (researcher). Woven also into Ch 4, 6; 10.2, 10.3, 10.5, 10.7, 10.9, 10.10; Ch 11 §4 ("What it is set against"); Ch 13; Ch 14. Linkage map set up: `_analytics/Clusters/M25 - life-death/life-death-linkage-map.md`. Claim register v8. | Weave by activity (#1920), with Ch 2 carrying the frame (OT-08) |
| 2026-10-03 | life and death (M25), unit 2 (#1939) | Ch 2 widened: "What death is" gains two sub-sections (*Death and sin*, *Death in the living*); new sections "Facing death" (before "Wanting to die") and "Dying to the Lord" (after "Made alive"); "After death" sets the dead seen from this side (Job 14:10; Ecc 9:5; Psa 6:5; 115:17) beside the dead with God (Luk 16:22; Rev 14:13; 2Sa 12:23), unreconciled. Short passages pointing back to Ch 2 in 10.1, 10.3–10.7, 10.9–10.11, 11 §4, 12, 13, 14. Researcher: *"proceed to weave in"*. | Unit 2 ledger `life-death-observation-ledger-unit2-v1-20261002.md` (LD-43 to LD-91); death given its own account in the scene-setting chapter (#1937) |
| 2026-10-04 | life and death (M25), unit 3 (#1940) | Two new Ch 2 sections: "Living before God" after "Life set before a person" (the oath by the Lord's life and God's own oath; the living God; the days of a life; the land of the living), and "Life weighed" before "Facing death" (life loathed, worn down, enjoyed; what life does not consist in). "Life set before a person" sets long days beside the wicked who prolongs his life (Ecc 7:15; 8:12), unreconciled. New sub-sections elsewhere: 10.4 "Thinking and life", 10.5 "The oath", 10.9 "The living God", 10.10 "Loyalty and honour"; short passages in Ch 4, 6, 10.1–10.3, 10.6, 10.7, 11 §4, 12, 13, 14. Researcher: *"approve 1940 as recommended"*. | Unit 3 ledger `life-death-observation-ledger-unit3-v1-20261003.md` (LD-92 to LD-142, with the H2416C supplement §B.19) |
| 2026-10-04 | life and death (M25), unit 4 (#1949) | New Ch 2 section "Sleep and waking", before "Life weighed": the verses' own picture of death as sleep and the hope as waking (Job 14; Jer 51:39; 2Ki 4:31; Psa 3:5; the call "Awake! Why are you sleeping, O Lord?" beside Psa 121:4; Dan 12:2). The "death as sleep" paragraph moved there from "What death is". New 10.9 sub-section "Calling on God to wake". H5782's inner-being faces handed to #1942, not woven. Researcher: *"approved, proceed with H6974 and the weave"*. | Unit 4 ledger `life-death-observation-ledger-unit4-v1-20261004.md` (LD-143 to LD-155, with the H6974 supplement §H) |
| 2026-10-04 | life and death (M25), Q2 and Q3 (#1950) | Ch 2 "The inner person dying" reworked as "Soul, spirit and heart at death": the soul's several faces at death (departs, dies, poured out, named to the end, two ends in Psalm 49, not abandoned), the spirit, and the heart named only "while they live" (no verse on the heart after death). "Delivered from death" restated by count; "After death" widened (Psa 49; Luk 23:43; Phili 1:23; 2Cor 5:8; 1Pe 4:6). Ch 4 short passage. Researcher: *"prepare 1950 for approval and then adding it to the narrative"*. | Q2/Q3 ledger `life-death-q2-q3-soul-spirit-heart-ledger-v1-20261004.md` |
| 2026-10-04 | fear (M01), units 3–4, overview (#1957, #1958, #1960, #1961) | New 10.12 "Fear", after 10.11, with no renumbering. Researcher, verbatim: *"I think you must encapsulate the full finding of fear, as it emerged from the ledgers, the cross ledger review and the co-existence review into a separate Ch10 sub chapter. Be careful not to be distracted by elements that are not inner being relevant, but don't cut out external factors impact on or related to the operation and the inner being.  This is the first step. then we will proceed with gathering similar studies of other key characteristics."* This modifies #1920 for key characteristics: each gets a full account of its own as a Ch 10 sub-chapter. First step only: 10.1 and the other chapters are not reworked. 10.1's "Fear" section now overlaps 10.12; that is held with the 10.1 frame question (OT-12, `../wa-essay-narrative-feeling-frame-question-v1-20261004.md`). | The cross-ledger overview showed that fear is not wholly a feeling: it is also a standing, an owed respect, a word for the one feared, and an act. It crosses many activities. |
| 2026-10-05 | anger (M02), units 1–5, overview v2 (#1963, #1966–#1969, #1973, #1974) | New 10.13 "Anger", after 10.12, with no renumbering, following the #1961 precedent for key characteristics. Its sections are taken from the overview, not from the 10.x headings (#1947). Researcher, verbatim: *"M47 after the overview revision; archive them, proceed through to the generation of the ch 13 narrative and the updated M47 related chapters."* Ch 13 stays as it is: it is to be consolidated into 10.13 later (OT-13, ruling 6.3), and the cross-check is a separate file. No other chapter changed in this step; the heart and spirit material follows in the M47 step. | The overview showed anger as one account across parties: the same words for God and people, with a few kept for God; the forms by party; what changes it; what it leads to; the responses to God's anger as one set. |
| 2026-10-05 | anger (M02) and the inner seat (M47): the M47 step (#1974, OT-18) | The anger material on the heart, soul, spirit, flesh and conscience woven into Chapters 4–8. New Ch 4 section "The heart and anger", placed after "The heart feels". Short additions in Ch 5 (*The soul suffers*), Ch 6 (*The human spirit*; *God's Spirit and the human person*), Ch 7 and Ch 8. Researcher, verbatim: *"M47 has already been documented in the narration and the narration must be updated with the what does this multi cluster connection actually do or mean."* No structure change. | The approved seat maps (U1 §38, U2 §66) give each heart, soul and spirit in the anger verses a role. Few of them were in the seat chapters (Ch 4 held 3). Ledger: `anger-m47-seat-ledger-v1-20261005.md`. |
| 2026-10-05 | Ch 13 into 10.13 (#1977, OT-13) | Ch 13 "Under God's anger" folded into 10.13 as its section *Living under God's anger*. Ch 13's sections become sub-sections there, the overlap with 10.13 v1 is removed, and the leaders' bearing and Daniel are merged in. Ch 13 is kept as a one-paragraph pointer. Researcher, verbatim: *"1977 - correct, ch13 becomes part of ch10.13"*. Chapters that still say "Chapter 13" (to be changed when next touched): 01, 02, 10.1, 10.2, 10.3, 10.5, 10.8, 10.9, 10.11, 10.12, 12, 14. | Ruling 6.3 (#1963): Ch 13 to be consolidated into 10.13 once 10.13 was written in full. |
| 2026-10-07 | choosing (M64) | Ch 13 becomes "Other beings", with 13.1 Divine, 13.2 Angels, 13.3 Other spirits and 13.4 Nature. 13.0 gives why the chapter is included and a pointer overview of what has been found so far. The old Ch 13 pointer moved to `archive/`; its note that "Chapter 13" for God's anger means 10.13 is kept in 13.0. Nothing is moved into the sub-chapters yet. | Researcher (#1982, D2): *"chapter 13 is redundant at the moment. This is the right place for the other beings chapter. The title is 'Other beings' and it have sub chapters for Divine, Angels, Other Spirits, Nature."* D3: no correction pass; existing sections are reset only on the researcher's individual instruction. |
| 2026-10-08 | choosing (M64), §2a (#1978) | 10.7 reframed around the account of choosing. The section now opens from Joshua 24, where the choice (24:15) and the inclined heart (24:23) stand in one speech, and is ordered as one account: the words; two sides; what a choice rests on; what draws it; whose measure; choosing before God; choosing together; a choice that is honoured; choosing from weakness; fear and choosing; setting the heart; holding a choice; life and death set before a person; what follows a choice; choices weighed by another; what changes the character. All of v9 is kept: its fear material becomes *Fear and choosing*, its heart verses become *Setting the heart* (with 1Sa 7:3 set beside Jos 24:23, the same words), and its life-and-death paragraphs become their own section. A working note at the foot lists what later reading will add and where (being chosen, others around a choice, Job's own words, death and life, will and resolve) and holds the Deu 23:16 / Deu 12 phrase. No other chapter changed in this step; Ch 11 §4, 10.6 and 13.1 are touched by the material and not yet updated. 145 quotes checked, 0 failures; quoted share 54% (v9) → 39%. | Researcher, verbatim: *"first build the 2a into the narrative 10.7.  you will need to reframe 10.7 to ensure 2a is part of a larger context of choosing and setting direction and not a disconnected list of paragraphs. you need to take into account what is already there, and also allow for other further research results that forms part of this chapter to fit in later."* Source: `../../../Clusters/M64 - will-resolve/m64-choosing-account-v1-20261007.md` and its readings. |
| 2026-10-08 | choosing (M64), §2a, change of character (#1978, #1919) | Ch 11 §4 gains the five faces of choosing (good or evil in your eyes; knowing good and evil; refusing, *māʾas*; choosing, *bāḥar*; delight, *ḥāpēṣ*), one new factor ("Whose eyes, and whose delight") and a widened factor ("What it is turned toward": refusing, knowing and choosing). No structure change. New quotes checked: 12, 0 failures. | Researcher, verbatim: *"update Ch 11 §4 with the five faces of choosing"*. Faces as in 10.7 v10 *What changes the character*. |
| 2026-10-08 | choosing (M64), §2a: 10.6 and 13.1 (#1978) | 10.6 gains a paragraph on wanting beside choosing (2Sa 19:38, where "desire" renders the choosing verb; Isa 1:29; 66:3; Pro 3:31; 3:15; 2Cor 8:11), pointing to 10.7. 13.1 Divine gets its first content, a section "Choosing": what the 21 §2a verses say of God in his own right (he chooses; his eyes and delight are the measure; he acts first; good, upright, holy; knows the heart and gives; reasons, answers, judges). Working note: God's wider choosing verses (the 166 routed to 13.1 under rule 72) are not placed, because they were grouped, not read in their passages. 13.0 God bullet points to 13.1. No structure change. New quotes: all found in the ESV text. | Researcher, verbatim: *"update 10.6 and 13.1"*. |
| 2026-10-08 | choosing (M64), §2b (#1978) | 10.7 gains the section *Being chosen*, after *Choosing before God* (the place the v10 working note reserved): the choosing comes first and the inner life of the chosen is its purpose (Isa 43:10; Eph 1:4; Jam 2:5; Psa 65:3-4), the other order when people choose (Act 6:3-5); what the chosen are moved to; what they are called to; faith and the truth; not a guarantee, and the way back; set against others. Re-read and adjusted: *The words* (God's choosing to 13.1, a person's being chosen below), *What a choice rests on* (knowing: the order runs the other way for the chosen), *Holding a choice* (2Pe 1:10 pointer), *What changes the character* (two faces: choosing a person; holiness), Connections, working note (being chosen removed). 199 quotes, 0 failures; quoted share 39% (v10) -> 41% (small rise, noted). No new file, no renumbering. | Researcher, verbatim: *"write the 2b account and weave into 10.7"*. Source: `../../../Clusters/M64 - will-resolve/m64-being-chosen-account-v1-20261008.md` (15 verses, batches 1-2). |
| 2026-10-08 | choosing (M64), §2b: Ch 11 §4 and 13.1 (#1978) | Ch 11 §4 gains two faces ("Choosing a person": God before anything in the person, people by what is seen; "Holiness": purpose in Eph 1:4, name in Col 3:12) and one factor ("Who chooses"). 13.1 gains three paragraphs from the §2b readings: he chooses before anything is in the one chosen, with his love and pleasure (Eph 1:4-5; 1Ch 28:4; 2Sa 6:21; Jam 2:5; Isa 43:8, 10); he searches hearts and acts on them, giving over those who refused the truth (2Th 2:10-11) and putting a purpose into the kings' hearts (Rev 17:17); he remembers his covenant and does not remember sins (Psa 105:8, 42; 106:45; Isa 43:25; 44:21). No structure change. New quotes all found in the ESV text. | Researcher, verbatim: *"update Ch 11 §4 and 13.1"*. |
| 2026-10-08 | choosing (M64), §2c (#1978) | 10.7 gains the section *Others around a choice*, after *Being chosen* (the place the working note reserved): at the place God chose (rejoicing, shared and grounded in the blessing; fear learned at a meal; carefulness when a case is too hard); desire near and far (Deu 12:21; 18:6); turned toward it from far off (1Ki 8:47-48; Neh 1:9); set against the one chosen (grumbling, Saul's anger, Michal's contempt, despised and abhorred, a verdict from ruin, hatred, rejection); with the chosen and for them; knowing that a choice was made, and not knowing; an inner act weighed by what God chooses (Isa 58). Re-read and adjusted: *The words* (*bāḥîr*), *Whose measure* (other people's eyes), *Being chosen* (*Standing for others*: Moses in the breach, Psa 106:23), *What changes the character* (two faces: desire beside a choice; despising), Connections, working note. 286 quote fragments, 0 failures; quoted share 39% (v11) -> 38%. No new file, no renumbering. Placements of Moses and of the Levite (Deu 18:6) are for the researcher to confirm (confirmed 2026-10-08: *confirm Moses and Levite placements as recommended*; 10.7 v13). | Researcher, verbatim: *"write the 2c account and weave into 10.7"*. Source: `../../../Clusters/M64 - will-resolve/m64-others-around-choosing-account-v1-20261008.md` (31 verses, batches 1-3). |
| 2026-10-08 | choosing (M64), §2c: Ch 11 §4 and 13.1 (#1978) | Ch 11 §4 gains three faces ("Desire beside a choice"; "Despising"; "Knowing that a choice was made"), widens the fear face (learned at a feast; on those who hear; terror at God's choice made plain) and two factors ("Whose eyes, and whose delight": the other measure held by those around God's choosing; "What it is turned toward": desire). 13.1 gains: God acting on others widened (Rom 11:8, 11; 1Pe 2:8; 1Ki 8:39, 58); he answers those set against his choosing (Num 16:11; 17:5, 10; Isa 49:7; Jer 33:24-26; Joh 15:18-19); he calls those who do not know him (Isa 45:4-6); he blesses at the place he chose and gathers those who return (Deu 16:15; Neh 1:9); what he chooses is turned toward others (Isa 58:6); his wrath turned away (Psa 106:23). No structure change. New quotes all found in the ESV text. | Researcher, verbatim: *"update Ch 11 §4 and 13.1"*. |
| 2026-10-08 | planning (M64): 13.1 (#1986) | 13.1 gains the section *Purposing*, after *Choosing*: how God's plans operate, from the 30 verses on his own purposing in the plan set (Rom 8:27 kept out, a Holy Spirit verse under #1987/OT-94). He forms a plan and makes it known; his devising answers what people devise; he states what he intends so that people may turn, and relents; he also purposes and does not turn back (both stated, not reconciled); carried out and recognised; plans for welfare; takes in what people do against him without excusing them; before the ages, not from works; turned toward those who love him; refused or served. Closing list of where the verses touch a person, held for a person's own planning (not yet woven). No structure change. 49 quote fragments, 0 failures. | Researcher, verbatim: *"the 31 God ward verses need to find their way to 13.1 with an analysis of how Gods plans operate."* Source: `../../../Clusters/M64 - will-resolve/m64-gods-plans-account-v1-20261008.md`. |
| 2026-10-08 | planning (M64): 13.1, the Spirit (#1986) | 13.1 *Purposing* gains "The Spirit intercedes according to the will of God" (Rom 8:26-27), placed before Rom 8:28. The *Choosing* line "The Holy Spirit is the subject of a separate study" is removed. All 31 God-ward plan-set verses are now placed. No structure change. | Researcher, verbatim: *"for the purpose of 13.1 (the divine) the Holy Spirit or Spirit is part of it, and should not be left untouched. Add these verses in 13.1 ."* |
| 2026-10-08 | planning (M64): the 77 inner-being verses (#1986) | Two new sections, no new file, no renumbering. 10.7 *Planning* is the account of looking ahead: weighing first, planning without knowing, a plan carries a person's word, planning together and parting, for another's good, a purpose held, devised from one's own heart, the plan and its outcome. 10.10 *Plotting against another* covers what passes between the plotter and the one plotted against. Widened: 10.4 (thought then devising, design, reckoning and being reckoned), 10.9 (plotting against God), 10.11 (the friendly word as cover), 10.13 (rage that wants to kill at once), Ch 11 §4 (faces "Purposing", "Planning ahead"). The 13 count verses go to 10.4 *It reckons*. 63 verses newly woven; 14 already placed for the same word. 129 quote fragments, 0 failures. | Researcher, verbatim: *"now weave the 77 HIB planning verses into the narrative"*. Source: `../../../Clusters/M64 - will-resolve/m64-planning-hib-weave-account-v1-20261008.md`. |
| 2026-10-08 | willing (M64): 10.7 and 13.1 (#1986) | Two new sections, no new file, no renumbering. 10.7 *Willing*, after *Planning*: the will meets what is put before it; the "no" that keeps faith and that does violence; feeling holds the will; refusing God refuses something good; where willing and planning are named together (Pro 1:29–31; Psa 81:11–12; Isa 30); a plan meets another's will; a resolve still weighed; the will steers; the willing heart; the will made absolute; a will under another. Face "Willing" added. 13.1 *Willing*: not willing to destroy, not willing to forgive, with the reasons the verses give; he does as he wills; his will brings to life and waits; the Father, the Son and the Spirit; Gethsemane. 103 quote fragments, 0 failures. Ch 4, Ch 6, 10.1, 10.6, 10.10, 10.12, 10.13 and Ch 11 are touched by the reading but not updated (instruction named 10.7 and 13.1). | Researcher, verbatim: *"weave the will notes into 10.7 and 13.1"*. Source: `../../../Clusters/M64 - will-resolve/m64-will-reading-v1-20261008.md`. |
| 2026-10-08 | willing (M64): the touched chapters (#1986) | No structure change. The will reading carried into the chapters it touches: Ch 4 (the heart named beside the will), Ch 6 (hardened and willing spirit), 10.1 (a feeling holds the will), 10.6 (a want met and refused; wanting toward harm), 10.10 (consent refused to a plot; a will pressed; intent pinned), 10.12 (fear stops the will), 10.13 (Saul's selective refusal; God's anger at unwillingness to listen), Ch 11 §4 (face "Willing"). 10.7 working note updated. 61 quote fragments, 1 corrected, 0 failures. | Researcher, verbatim: *"update Ch 4, Ch 6 and the other touched chapters"*. |
| 2026-10-08 | the 29 M64 × M47 verses: 13.1 (#1989) | No structure change. 13.1 *Choosing* gains two paragraphs on the researcher's instruction: his eyes and his heart at the place he chose (2Ch 7:12, 15–16, 20), and his servant chosen with delight and the Spirit put on him (Mat 12:18, quoting Isa 42:1, in Matthew's setting 12:14–20). Eze 14:7, Lev 7:18 and Lev 17:4 have no placement (researcher ruling). Claim register v30. |  |
| 2026-10-08 | citations needing attention (#1990, from #1987) | No structure change. Three citations corrected to their setting. 2Sa 14:14 (Ch 2, 10.4, 13.1): set inside the plea Joab "put in her mouth" (14:3); 10.4 loses "those who have put themselves outside", which the verse does not say. Psa 32:2 (Ch 6): "the righteous man" restated as the forgiven man who confessed (32:1, 5); the M64 word "counts" is now quoted. Job 7:15 (10.7 working note): Job's own voice is set beside the friends' verdicts, and 7:15 also goes with life and death. Claim register v31. |  |
| 2026-10-08 | citations to check (#1991, from #1987) | No structure change. Seven citations corrected to what the verse says. Jer 8:3 (Ch 2): "wished for and withheld" becomes "chosen over life"; Rev 9:6 is kept apart. Luk 10:42 (10.1, Ch 11 §4): "divides" (a word from 1 Cor 7:34) becomes many things against one, with 10:40 "distracted". Gen 6:5 (Ch 11 §1): the heading "Even the leaning is formed" and its word link (potter, frame) are removed; §8 quotes 6:5–6 as written. Exo 35:35 (Ch 11 §1): under the new heading "Skill and laws are put in, and minds are blinded". 1Ch 29:18 (Ch 14): given its referent, the free giving of 29:17. Psa 31:13 (10.12): the psalmist answers in his own words, not "the same way". Psa 51:12 (Ch 6): the willing spirit has no possessive. Claim register v32. |  |
| 2026-10-08 | the 18 include verses (#1992, from #1987) | No structure change. 6 were already carried (Isa 42:1 in 13.1 through Mat 12:18, with no 10.7 placement by ruling; Deu 2:30; 1Ch 28:9; 1Ch 29:18; Psa 32:2; Pro 1:29). 12 are woven as proposed: 10.7 (Deu 30:14, 17, 20; Phili 1:22–25; Luk 10:39–42; Exo 36:2; Psa 51:13; 2Sa 14:1–19 with Joab, a citation fix); Ch 2 (Job 7:13–16; Jer 8:2); 10.13 (Isa 10:12–15); Ch 12 (Rom 8:7); 10.12 (Pro 1:29; Isa 66:2, both "I read"); 10.10 (2Sa 19:23). Claim register v33. |  |
| 2026-10-09 | desire (M18) × life and death (M25), and the held items (#1993, #1942) | 10.6 given section headings (Through the eye; Aimed at nothing, and enjoyment given; As heat; Wanting speaks, and drives thinking; Beside choosing; Delight; Wanting that owns the one who wants; Unmet, and wanting against God; Shaped by fear; Evil desire; Wanting life; Wanting and death; Aimed at God; Thirst answered; A person; Jealousy and envy; Taken away; Possessions), with no text dropped. 13.1 gains *Jealousy* and *Stirring*. 13.4 gets its first content. 10.9 gains *Waiting, and pleading*. 10.10 gains *Friends, company and care*. No renumbering. | 10.6 had grown to some 20 paragraphs on many faces of wanting with no structure; the headings name the subject only (style guide). God's jealousy and his stirring of spirits had no home in 13.1. |
| 2026-10-09 | desire (M18), group A (#1993 item F) | 10.6 gains the section *Coveting* (after *Through the eye*). No other structure change. | The commandment, the see–covet–take order and the law naming the desire make one phenomenon. It had no home. |
