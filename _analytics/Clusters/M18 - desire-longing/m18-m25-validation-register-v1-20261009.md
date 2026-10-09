# M18 × M25: read-back of the narrated cluster (report)

**Date:** 2026-10-09 · **Escalation:** #1993 (handoff item B) · **Status:** done and **woven on instruction** (2026-10-09, researcher: *"update M25-M18 findings into the narrative as per your findings"*). §4 is the probing reading in [`m18-m25-inner-being-reading-v1-20261009.md`](m18-m25-inner-being-reading-v1-20261009.md). The held items were read and woven in the same pass: [`m18-held-items-reading-v1-20261009.md`](m18-held-items-reading-v1-20261009.md).

**Rule (researcher, verbatim, 2026-10-09):** *"a) why would the verse not be narrated in the first place, is it because something was missed - fix it; b) does the new reading add new perspective to the narration, maybe from a different angle - validate this new perspective and add it c) is there a fundamental error that need to be re-alligned. It is very important to work with the analysis already generated in the cluster work to avoid re-doing investigatory work alraedy done."*

**Files:**
- Decisions, one per verse: [`m18-m25-validation-register-v1-20261009.csv`](m18-m25-validation-register-v1-20261009.csv). Built by `m18-m25-validation-register-build-v1-20261009.py`, which holds each decision with its reason.
- Working sheet: [`m18-m25-validation-worksheet-v1-20261009.md`](m18-m25-validation-worksheet-v1-20261009.md), built by `m18-m25-validation-worksheet-build-v1-20261009.py`. For each verse it shows the passage, the M25 face(s), every M25 ledger line that cites it, and where the narrative places it now.

## 1. Scope and how it was done

- There are 111 M18 × M25 verses. **22 of them are also M47 and were decided in the M47 pass.** That leaves 89.
- 3 of the 89 are also M02 (Job 5:2, Eze 35:11, Psa 30:5). All three are already narrated and are confirmed here. They do not need to be read again in the M02 step.
- The existing analysis was the starting point. Every one of the 89 has an M25 face from the unit 1–4 face files, and most have a line in a unit ledger (LD-nn) or the Q2/Q3 ledger. No verse was investigated afresh. Each was read in its passage (two verses either side) beside its ledger line and beside what the narrative already says.
- Quote check: every fragment quoted from a verse in the register was checked against the ESV in iba.db (93 fragments, 0 failures).

## 2. Result

| Decision | Verses | What it means |
|---|---|---|
| **a. Missed, add** | 26 | Read in the M25 work, or not narrated at all, and the M18 side never reached the narrative |
| **b. New perspective, add** | 12 | Narrated for life or death, but the M18 word in the verse is not said. Two of them (Psa 119:40 in Ch 2, Exo 17:3 in 10.5) were quoted as bare citations the cross-reference parser missed (handoff item I), found by a direct text search |
| **c. Error, realign** | 0 | None found. Two sentences were restated, because each claimed "the one place" and these verses add a second (10.7 on Isa 1; 13.1 on Gethsemane) |
| Confirmed | 21 | Narrated, sound, and placed right |
| Carried by a parallel | 8 | For example Judg 8:32 and 1Ch 29:28 by Gen 25:8 ("a good old age"), and Song 3:5 and 8:4 by Song 2:7 |
| No inner-being bearing for the M18 word (route C) | 22 | *ṭôb* as a qualifier or an idiom ("seems good to you", "good in the eyes"), "by the will of God" as a letter opening, "far", "mocking" (Isa 57:4, whose passage is woven through 57:5), and literal thirst in a taunt or in judgement |

Nothing is held.

## 3. (a) Why the verses were not narrated

The reason is the same as for M47. **The M25 units read the life and death words. The desire side of each verse was left for this strand.** The M25 ledgers often quote the verse in full, but they quote it for its life or death word:
- Psa 34:12, "desires life", is quoted for "long days" (LD-101).
- Joh 4:14, "never be thirsty again", is quoted for "living water" (LD-121).
- Ecc 5:18, "find enjoyment", is quoted for "life enjoyed, as given" (LD-115). That ledger line was woven into Ch 2. 10.6 gained Ecc 2:24–26 in the M47 pass, but not the three verses that say the same thing (3:12; 5:18; 8:15).

Three verses (Exo 14:12, Psa 34:12, Pro 8:35–36) also have a Ch 2 side. I first treated Ch 2 as closed to them. That was my over-reading of OT-08, corrected in §6.

## 4. The reading, and where it was woven

The placements come from [`m18-m25-inner-being-reading-v1-20261009.md`](m18-m25-inner-being-reading-v1-20261009.md), which reads the additions by phenomenon for the inner being's workings. The held items come from [`m18-held-items-reading-v1-20261009.md`](m18-held-items-reading-v1-20261009.md). The script is `m18-m25-held-narrative-weave-v1-20261009.py`. 10.6 and 13.4 were rewritten by hand.

| Chapter | New version | What was woven |
|---|---|---|
| 10.6 *Wanting* | v11 | Given section headings. New: *Through the eye* (Gen 2:9, 3:6; Ecc 7:26), enjoyment given and the rich fool compared (Ecc 3:12, 5:18–20, 6:12, 8:15), heat (Isa 57:5), *Wanting that owns the one who wants* (Tit 3:3–5, 2:11–14; Luk 8:14; Pro 23:35), unmet wanting (Hag 1:6; Isa 29:8; Exo 17:3 against Judg 15:18; Eze 23:21–22), *Shaped by fear* (Jer 42; Exo 14:12), *Wanting life* (Psa 34:10–14; 1Pe 3:9–10; Job 7:7), *Aimed at God* (Psa 27; 16; 119:37, 40), *Thirst answered* (Joh 4, 6; Jer 2:13), *A person* (Song 2:7, 3:5, 8:4–7, 5:2–6), *Jealousy and envy* (1Ki 19; Num 11:29; Psa 73; Pro 23:17–18; Jam 3:13–16), *Taken away* (Joe 1:5), *Possessions* (Mat 19:22; Pro 15:27), delight list (Psa 119:75–77; 68:30) |
| 10.7 *Choosing and setting direction* | v20 | Mat 19 (and the Isaiah 1 "one place" sentence restated); Joh 5:40–44; Ruth 3:10–13, 4:4–6; 2Ti 3:11–12; Joh 21:18–22; 2Ch 19:2–3; Pro 14:13–14; Dan 11:25; Isa 47:13–14 |
| 13.1 *Divine* | v11 | *Delight*: no pleasure in death (Eze 18, 33), Psa 116:15, 1Sa 2:25 (the tension left standing), Pro 8:34–36. *Willing*: Joh 5:21, 6:38–40 (the Gethsemane "one place" sentence restated), 21:22–23. New *Jealousy* and *Stirring*. *He is good*: Lam 3:24–25, Psa 125:4 |
| 13.2 *Angels* | v3 | Zec 4:1–2 |
| 13.4 *Nature* | v2 | First content: God's look on what he made (Gen 1:21, 25, 31); the creatures' thirst met (Psa 104:10–15, 27–28; 42:1); the ostrich (Job 39:14–17) |
| 10.10 *Relating to others* | v15 | 1Sa 19:1–7 in *Loyalty and honour*; Deu 19:6 in *Anger between people*; new *Friends, company and care* (Job 6:15–18; Ecc 4:9–11; Job 31:19–20; Job 17:8–9 against 31:29–30; Pro 10:12; Song 2:7) |
| 10.9 *Relating to God* | v16 | Psa 73:3, 20 with 73:16–17; new *Waiting, and pleading* (Lam 3:24–26; Hezekiah, Isa 38:2–5); *Calling on God to wake* rewritten from a summary into the grounds of each call, Bildad, and Isaiah's call answered (51:9, 17; 52:1; 64:7–8), Psa 57:6–8, Judg 5:12 |
| 10.12 *Fear* | v5 | Exo 14:12 |
| Ch 2 | v15 | Isa 38:3, 5 (*Life asked for*); Psa 34:12 with Job 7:7 (*Life weighed*); Exo 14:12 (*Wanting to die*); Pro 8:35–36 (*Life set before a person*) |
| Ch 4 | v14 | Song 5:2–6; Psa 39:1–4; Pro 6:21–22; Hos 7:7 |
| Ch 6 | v12 | The stirred spirit widened (Ezr 1:5; Hag 1:6, 12–14; 1Ch 5:25–26; Jer 51:11) |
| 10.2 | v10 | Isa 50:4–6; Zec 4:1–2; Jos 23:14–15 |
| 10.5 | v14 | Psa 39:1–4 (*The pause between*) |
| 10.8 | v6 | Psa 125:3–4 |
| Ch 11 | v21 | §4: five new faces (eat-drink-be-merry; jealousy; rousing oneself; the redeemer's will; whom the need is spoken to) and Haggai's order. §5: three more voices (Lam 3:24; Psa 57:8; Pro 6:22) |
| Ch 12 | v15 | Isa 44:15–20 and 47:14 in *Idols taken inside* |

**Quote check:** every new quotation was checked against the ESV in iba.db. The only failures left are:
- section titles
- glosses
- the literal Hebrew "while his heart is hot", marked as such
- quotations that span two verses, each of which was checked separately
- flags that were already there before this pass

## 5. Held items: closed

All of them were read in the same pass (held-items reading):
- **OT-95:** 10 jealousy verses.
- **OT-96:** 10 *ṭôb* verses from the M47 pass, plus Gen 1:25 and Ecc 6:12.
- **OT-15:** all 19 H2552 verses.
- **#1942:** all 46 H5782 inner-being verses from unit 4 §E, with LD-155 (H6974).

The rest of the M18 jealousy words (112 hits) are read with the M18 words themselves (item F), not held.

**Notes for item F (the M18 words themselves):**
- Pro 21:26 "craves and craves", the verse after 21:25
- the kings who "did as he pleased" (Dan 8:4; 11:3, 16, 36)

## 6. Ch 2

OT-08 is closed: the researcher ruled on 2026-10-09 that it is *"no longer relavant"*. Ch 2 had no block. The first version of this report treated it as blocked, and the M47 pass avoided Ch 2 on the same wrong reading. Psa 49:7–8 went to Ch 5 because of it, and it stays there. Ch 2 v15 carries this pass's four additions.

## 7. Next

**M02** (handoff item C). It has 59 verses. 5 are M47 (done) and 3 are also M25 (confirmed here), so 51 remain, with OT-19.
