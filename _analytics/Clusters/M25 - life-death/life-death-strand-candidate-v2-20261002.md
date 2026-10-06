# Next strand: life and death (M25), to bring Ch 9 up to date

**Date:** 2026-10-02 · **Version:** v2 (adds §6 decisions and §7 questions; v1 in `archive/`) · **Status:** strand approved; **unit 1 started** (#1932). · **Source:** iba.db (read-only), the M01 method rerun for M25

## 1. What was run

- **The M01 method, unchanged.** This is the fear web-pull query with the filter **`<> 'M25'`** (#1927 decision 1), plus the same count and surface tables as fear candidate v2 (§2–§3A).
- **New reusable script.** For M01, only the SQL was saved; the counts were run ad hoc. They are now one parameterised script: `strand-overview-v1-20261002.py <code> <slug>`. It writes:
  - the SQL
  - the web-pull CSV
  - a data file of counts
- **Files in this folder:**
  - `life-death-web-pull-query-v1-20261002.sql`
  - `life-death-web-pull-v1-20261002.csv`: 52,527 rows over 2,027 verses
  - `life-death-strand-overview-data-v1-20261002.md`: every table in full; this document summarises it
- **Scale:** **2,513 M25 hits in 2,027 verses**, under 34 Strong's numbers. In 372 verses, two or more M25 words occur together. This is about 2.4× the size of fear (1,032 hits in 916 verses).
- **Folder:** `_analytics/cross-cluster-web/life-death/`, confirmed by the researcher (#1932). *(Moved 2026-10-06 to `_analytics/Clusters/M25 - life-death/` under #1965, per the #1963 decision 6.4 filing rule.)*

## 2. M25 vocabulary (main entries)

| Strong | Gloss | Hits | Verses | T7 divine party ≤5 words | Negator ≤2 before |
| --- | --- | --- | --- | --- | --- |
| H4191 | to die | 840 | 699 | 123 | 81 |
| H2421 | to live | 282 | 257 | 46 | 20 |
| H2416A | alive | 240 | 218 | **98** | 5 |
| H4194 | death | 156 | 151 | 28 | 8 |
| H2416E | life | 143 | 135 | 20 | 2 |
| G2198 | to live | 140 | 124 | 46 | 8 |
| G2222 | life | 133 | 125 | 26 | 7 |
| G2288 | death | 120 | 106 | 20 | 12 |
| G0599 | to die | 110 | 99 | 24 | 10 |
| H2416C | living thing | 105 | 97 | 6 | 5 |
| H5782 | to rouse | 78 | 64 | 15 | 2 |
| H0748 | to prolong | 34 | 34 | 8 | 4 |
| H5397 | breath | 24 | 24 | 10 | 5 |

The other 21 entries have 23 hits or fewer each. They include G2227 "make alive" (12), H6315 and H5301 "to breathe" (14 and 12), H4241 "recovery" (8) and G1312 "decay" (6).

- **H4191 is a third of the cluster** (840 of 2,513 hits). Most of it is narrative and legal: "died", "put to death".
- **H2416A with the divine party in 98 verses.** Its commonest near pair is "alive + LORD" (64), e.g. 1Ki 17:1, 17:12, 18:10. This points to the oath "as the LORD lives". It is a pointer only; reading would confirm it.

## 3. Links to other clusters (verses; "near" = within 3 words)

The T-clusters are grammar and setting, so they are left out here. They are listed in full in the data file.

| Cluster | Verses | Near | Commonest near pairs |
| --- | --- | --- | --- |
| M47 Inner Seat | 302 | 188 | alive + flesh 13; alive + soul (living creature) 12 (Gen 1:20–21, Eze 47:9); live + soul 11 (1Co 15:45, Eze 13:18–19) |
| M72 Authority | 294 | 138 | die / live + king (mostly "long live the king", reign notices) |
| M56 Sin & Guilt | 114 | 66 | die + sin 20 (2Ki 14:6, 1Co 15:3); death + sin 15 (1Co 15:56, 1Jo 5:16–17) |
| M12 Righteousness | 114 | **76** | live + righteousness / justice / righteous (Eze 18, Eze 33, Deu 16:20, 1Pe 2:24) |
| M18 Desire & Longing | 111 | 60 | life + pleasant (2Sa 1:23, Ecc 3:12, 6:12); die + thirst (Exo 17:3) |
| M58 Wickedness | 108 | 54 | die + wicked 18 (Eze 3:18, 33:8, 33:14) |
| M24 Faintness & Despair | 95 | 43 | die + break / distress (1Sa 4:18, 2Sa 12:18) |
| M23 Strength & Courage | 87 | 36 | rouse + strength (Isa 51:9); death + power (1Co 15:56, Ecc 8:8, Heb 2:14) |
| M45 Renewal | 82 | 38 | death + rescue (2Co 1:10, Pro 10:2); die + new (Eze 18:31) |
| M03 Grief & Lament | 67 | 32 | die + mourn / weep (2Sa 11:26, Luk 8:52) |
| M01 Fear & Awe | 60 | 28 | die + fear (1Sa 4:20, 2Sa 12:18); life + fear of the LORD (Pro 14:27, 19:23, Mal 2:5) |
| M11 Turning & Repentance | 44 | 14 | live + turn (Eze 18:23, 18:32, 33:11) |
| M13 Faith | 43 | 18 | live + faith (Gal 2:20, 3:11, Heb 10:38) |
| M19 Trust & Refuge | 40 | 19 | life / die + trust (Joh 11:25–26, 1Jo 5:13) |
| M54 Torah & Obedience | 40 | 19 | die / live + law, commandment (Gal 2:19, Pro 4:4, 7:2, Deu 30:16) |
| M02 Anger & Wrath | 36 | 17 | prolong + anger (Pro 19:11, Isa 48:9); breathe + fury (Eze 21:31, 22:21) |
| M51 Love & Devotion | 34 | 14 | rouse + love 7 (Song 2:7, 3:5, 8:4; Pro 10:12) |
| M81 Memory | 33 | 11 | die + forget (Psa 31:12, Ecc 2:16); life + remember (Job 7:7) |
| M64 Will & Resolve | 21 | 5 | choose life / death (Deu 30:19, Jer 8:3, Job 7:15) |
| M20 Doubt (hiding) | 23 | 7 | life + hide (Col 3:3) |

## 3A. Surface forms: how the English renders each root

The 2,513 hits carry **204 distinct surfaces**. Each one is a pointer to a verse, not a meaning.

### 3A.1 One root, several renderings (selected; the full list is in the data file)

**H2421 "to live" (282)**
- live (129) · lived (41) · alive (21)
- **revive / revived** (12): Gen 45:27, Judg 15:19, 1Ki 17:22
- **recover / recovered** (10)
- **give me life** (8), plus gives / given me life: Psa 119
- **spared / saved alive / keep alive**: Gen 12:13, Jos 6:25, Num 31:18
- restored to life: 2Ki 8:1–5, Psa 30:3
- healed: Jos 5:8
- repaired: 1Ch 11:8
- flourish: Hos 14:7

**H2416A "alive" (240)**
- living (69) · lives (57) · alive (37)
- **fresh / raw / green**: Lev 13 (raw flesh), Psa 58:9
- **next year / spring**: Gen 18:10, 18:14, 2Ki 4:16–17
- vigorous: Psa 38:19

**H2416C "living thing" (105)**
- **beast(s)** (67), living creatures (15)
- appetite: Job 38:39

**H5782 "to rouse" (78)**
- Awake / awake (19) · stir up / stirred up (13)
- **awaken love**: Song 2:7, 3:5, 8:4
- **stirs up strife** (hatred): Pro 10:12
- awakens [my ear]: Isa 50:4
- exulted: Job 31:29
- wielded [a spear]: 2Sa 23:18

**H0748 "to prolong" (34)**
- long / prolong (days)
- **patient**: Job 6:11
- **slow [to anger]**: Pro 19:11
- **defer [anger]**: Isa 48:9
- outlived: Jos 24:31

**H6315 / H5301 "to breathe"**
- **breathes out [lies]** (5): Pro 14:5, 14:25, 19:5
- longs: Psa 12:5
- aflame: Pro 29:8
- puffs: Psa 10:5
- boiling: Job 41:20, Jer 1:13
- **fainted [her soul]**: Jer 15:9
- snort: Mal 1:13
- breathed [into his nostrils]: Gen 2:7

**H5397 "breath" (24)**
- breath (15)
- breathed (4: Jos 10:40, 11:11, 11:14, 1Ki 15:29)
- blast: 2Sa 22:16, Psa 18:15
- **spirit**: Pro 20:27 ("the spirit of man is the lamp of the LORD")

**H4194 "death" (156)**
- death (117)
- **pestilence** (5)
- deathly [panic]: 1Sa 5:11
- deadly: Psa 7:13

**Greek**
- G2227 "make alive" (12): gives life (Joh 5:21, 6:63, 2Co 3:6), made alive (1Co 15:22, 1Pe 3:18), life-giving (1Co 15:45)
- G4806 "made alive together with": Eph 2:5, Col 2:13
- G3499 "put to death": Col 3:5
- G0979 *bios*: life / property / goods / "live on" (Mar 12:44, Luk 15:12, 1Jo 3:17)

### 3A.2 One English word, many roots

| Surface | Strong's numbers behind it |
| --- | --- |
| life | 9 |
| living | 7 |
| live / lives | 6 each |
| dead / death | 5 each |
| alive / died / die | 4 each |
| breath | 3 |

As with fear, **both directions are needed**: root to surfaces, and surface to roots.

### 3A.3 Surfaces where the English is not life or death

- **H2416C**, as "beasts" (67): animals named as living things
- **H2416A**, as fresh / raw / green / spring / next year
- **H0748**, as poles / stick out (1Ki 8:8, Isa 57:4)
- **H2421**, as repaired (1Ch 11:8)
- **G0979**, as property / goods
- **H5782**, as wielded [a spear] (2Sa 23:18) and descendant (Mal 2:12)

These are **read, not dropped** (#1919). Most are likely to stay in the data, because they say nothing about the inner being. They are not proposed for re-allocation.

## 4. Where Ch 9 stands now (v4, 2026-10-01)

Ch 9 has seven sections:

1. Life breathed in
2. Breath lent, and held by God
3. Life that returns
4. Wanting to die
5. The inner person dying
6. Delivered from death
7. After death

**It is built mostly from the M47 seat words** (soul, spirit, breath, heart). M25's own roots appear only where those verses carry them:
- breathed: Gen 2:7
- revived: Judg 15:19, Gen 45:27, 1Ki 17:22
- die: 1Ki 19:4, Jon 4:3
- death: Psa 116, 56:13
- prolongs life: Pro 10:27

**The M25 roots have not been read as a strand.** What the counts show that Ch 9 does not yet cover:

| Pointer from the data | Count / refs | Possible home (to be confirmed by reading) |
| --- | --- | --- |
| "Give me life" / revive, as a prayer of the inner being | Psa 119 ×8+, Psa 80:18, 85:6 | Ch 9 "Life that returns"; 10.9 |
| Live / die tied to righteousness, wickedness and turning | Eze 18, 33 (M12 76 near, M58 54, M11 14) | Ch 9; 10.8; 14 |
| Choosing life or death | Deu 30:15–19, Jer 8:3, Job 7:15 | 10.7 |
| Rouse / awake / stir up: love, strife, the ear | Song 2:7, Pro 10:12, Isa 50:4 | 10.1, 10.6, 10.2 |
| Long of nostrils / slow / patient (H0748, the anger link) | Pro 19:11, Isa 48:9, Job 6:11 | Ch 9 already has *ʾaph*; 13 |
| Breathing out lies (H6315) | Pro 14:5, 14:25, 19:5 | 10.5 |
| "As the LORD lives" (alive + LORD 64) | 1Ki 17:1, 18:10 … | 10.5 / 10.9 |
| Death and sin; made alive (Greek) | 1Co 15:22, 56; Eph 2:5; Col 2:13, 3:3–5; Gal 2:20; Joh 5:21, 6:63 | 14 |
| Life and fear of the LORD | Pro 14:27, 19:23, Mal 2:5 | already in Ch 9 (fear strand) |
| Die + mourn / weep; die + forget | 2Sa 12:18, Luk 8:52, Psa 31:12, Ecc 2:16 | 10.1, 10.3 |

## 5. Suggested reading units (a strand, not a cluster pass)

The suggestion follows the fear rhythm: one unit per chat, then commit and close. Each unit runs pull → read by surface → ledger → approval → weave.

1. **Life given, revived and prayed for.** H2421 (revive / recover / give me life / spared), H4241, G2227, G4806, H5397 / H5301 / H6315 / H3306 / H5396 (breath). This is closest to Ch 9's existing sections.
2. **Dying and death.** H4191 / H4194 / G0599 / G2288 / G3499 / G1312.
   - Narrative "he died" and legal "put to death" are read by surface and accounted for, but mostly stay in the data.
   - The focus is the inner-being verses: wanting to die, heart dying, death and sin, fear of death.
3. **Living before God.** H2416A / H2416E / G2198 / G2222 / H0748: "as the LORD lives", prolonged days, life with righteousness and turning (Eze 18 / 33), choosing life (Deu 30).
4. **Roused and stirred.** H5782: love, strife, the ear, God roused. Its surfaces lean toward feeling and wanting rather than life and death.

## 6. Decisions (researcher, 2026-10-02, #1932)

Researcher, verbatim: *"lets start with 1 and see what comes out of it; 2 - agree, this is where the working should go; 3 - mark unit 3 and 4 of fear to be completed before proceding with a new cluster after M25. also set M12 and M64 as candidates for the next clusters to explore."*

1. **Unit 1 starts** (life given, revived, prayed for). Later units are decided after it ("see what comes out of it").
2. **Folder confirmed:** `_analytics/cross-cluster-web/life-death/`. *(Moved 2026-10-06 to `_analytics/Clusters/M25 - life-death/` under #1965, per the #1963 decision 6.4 filing rule.)*
3. **Queue after M25 (#1933):**
   - first, fear units 3 and 4, before any new cluster
   - then **M12** Righteousness & Integrity and **M64** Will & Resolve, as candidates

   This is also recorded in the fear handoff.

## 7. Questions to pursue in this strand (researcher, 2026-10-02)

These are the researcher's own questions. Each unit records what its verses say toward them, quoted and stopped. Where no verse says it, the record says so.

| # | Question (researcher) | Where the verses are likely to sit |
| --- | --- | --- |
| Q1 | **What is death?** | M25 die / death (unit 2), and death with sin (M56), with Sheol (H7585, T10) and with sleep (G2837, H3462, T3) |
| Q2 | **What happens to the spirit and soul at death?** | M47 soul and spirit with M25 (Ch 9 "The inner person dying" and "After death" already have part of this, built from the seat words) |
| Q3 | **Is anything said about the heart after death?** | M47 heart (H3820 / H3824 / G2588) in verses with M25 or Sheol. To be checked, not assumed; the answer may be "nothing is said". |
| Q4 | **How do the body and the resurrection relate, when we will have "glorified" bodies?** | Body (G4983, T14), resurrection and raising (G0386, T2; G1453, T3), transform (G3339, M45), incorruptibility (G0861, M61), perishable / mortal (G5349, G2349, T2), glory (G1391, M22): 1Co 15, 2Co 5, Php 3:21, Rom 8:11, 23 |

**Note.** Most of the words that Q1–Q4 need sit outside M25. They fall in T2 / T3 / T10 / T14, which the cluster overview leaves out as grammar, and in M47, M22, M45 and M61. So each question gets its own **focused pull**, made when the question is reached. This is not a whole-scope pass (focused capture, 2026-09-30). Q2–Q4 bear directly on Ch 9 "The inner person dying", "Delivered from death" and "After death".
