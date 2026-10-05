# Anger: the fear process applied, proposal (v1)

**Date:** 2026-10-05 · **Author:** Claude Code · **Status:** **approved 2026-10-05 (#1963), with the rulings in §7.** Filed in the M02 folder per ruling 6.4.
**Researcher, verbatim (2026-10-05):** *"during the previous session I following a process for fear to review all the ledgers with several different cycles and then to create a dedidated file for it. Do the same for anger, which was previously processed but need to go through the same type of process as fear."*
**Standing direction it follows (#1961):** *"then we will proceed with gathering similar studies of other key characteristics."*

## 1. What the fear process was

| Step | Fear: what was done | Output |
|---|---|---|
| 1 | Four **unit ledgers** by word family, covering every M01 Strong's: Hebrew *yārēʾ* family; *paḥad* and trembling; terror and horror; Greek | `fear-observation-ledger-*` (FE-01 to FE-162) |
| 2 | Each unit: pull every hit with the ESV text (`strand-unit-pull`), **read by surface first**, assign a **face** to every hit, observation rows with a "meaning in setting, and what it implies" column (from unit 3), a "what differs" table (§C), speakers named | unit pull CSV, faces CSV, ledger |
| 3 | **Quote check** of every quote against iba.db `verse` | `fear-quote-check-v1-20261001.py` |
| 4 | **Reconciliation** of the four ledgers against the full vocabulary. It found a gap (H4172A), closed by an addendum | `…unit3-addendum-H4172A…` (FE-163 to FE-167) |
| 5 | **Cross-ledger overview**: A what the verses say it is · B its forms (faces merged) · C what influences its nature (#1919) · D what it leads to · E held · F with the other characteristics (co-existence) | `fear-cross-ledger-overview-v1-20261004.md` |
| 6 | **Sub-chapter 10.12 "Fear"** built from 1–5. No other chapter reworked | `10-12-fear-v1-20261004.md`, claim register v15 |

## 2. What anger has now, and what it lacks

**Has** (`_analytics/Clusters/M02 - anger-wrath/`):
- U1 `wa-cluster-M02-phenomena-v2-20260928.md`: human anger, 246 verses, phenomena §1–§35, co-existence §37 (approved #1888)
- U2 `wa-cluster-M02-unit2-phenomena-v3-20260929.md`: God's anger as the human bears it, 394 verses, §1–§64, co-existence §65 (approved #1898)
- the strand ledger `anger-strand-observation-ledger-v1-20261001.md` (AN-xx, §L change of character), woven 2026-10-01
- the #1890 and #1892 investigations, and the 48-verse "outside M02" pull

**Lacks, measured against the fear process:**
1. **No word-by-word reading.** U1/U2 were read **by phenomenon and by side** (human / God), before the surface rule (2026-10-01, memory `feedback_surface_is_the_sensitivity_lens`). No hit has a face, and there is no per-word "what differs" table. §L of the strand ledger covers *aph* in detail and the other words in brief.
2. **No coverage reconciliation.** The live M02 vocabulary in iba.db is **65 Strong's (40 Hebrew, 25 Greek), 919 hits in 681 verses** (Hebrew 809 hits / 587 verses; Greek 110 hits / 94 verses; measured 2026-10-05, `cluster_strong` M02, not deleted). **Checked 2026-10-05:** the M02 phenomena ledger (`wa-cluster-M02-phenomena-ledger-v5-20260929.csv`) has all 681 live verses, no more and no fewer, each with a side (divine 302, human 220, both-sides B1–B9 118, none 39, other 2) and a phenomenon (41 blank, the none/other rows). So **every verse is accounted for**. What is missing is the level below: the 919 individual hits (a verse can hold several M02 words) have no face.
3. **No meaning column, no quote check run** on the anger material as a whole.
4. **No cross-ledger overview** and **no single account**. Anger is spread across the activity sections (10.1, 10.3, 10.10 and others) and Ch 13 "Under God's anger".

## 3. Proposed process (same shape as fear)

**Step 1. Unit ledgers, by word family** (exact split fixed after the vocabulary listing in the first unit):

| Unit | Words | Approx. hits |
|---|---|---|
| 1 | *ʾaph* (H0639G, 225) and *ḥēmāh* (H2534, 125): the two main nouns | ~350 |
| 2 | the verbs of burning and provoking: *ḥārāh* (H2734, 91), *kāʿas* (H3707/H3708A, 75), *ḥārôn* (H2740, 41) | ~210 |
| 3 | the remaining Hebrew and Aramaic: *ʿebrāh*, *qāṣap̄/qeṣep̄*, *zaʿam*, *zaʿap̄* and the rest | ~250 |
| 4 | the Greek: *orgē* (G3709), *thymos* (G2372) and the rest | ~110 |

Each unit uses the fear unit 3/4 format: pull with `strand-unit-pull-v1-20261002.py`; read by surface; a face for every hit; observation rows (AG-xx, a new series so they do not clash with AN-xx) with basis S/R, speaker named, meaning column; a "what differs" table; dispositions; quote check. The fear format is **tightened as set out in §3A** (#1944–#1947).
**Prior work is re-used, not redone** (memory `project_analysis_phase_augment_not_harvest_or_redo`). It stays where it is, in `_analytics/Clusters/M02 - anger-wrath/`, and the new files cite it. In detail:

| Prior work | How it is used |
|---|---|
| Phenomena ledger v5 (681 verses, side + phenomenon) | **Joined into each unit pull**: every hit arrives already carrying its verse's side and U1/U2 phenomenon code. The reading adds the face (from the surface), the meaning and the chain; it does not re-decide side or phenomenon unless the word-level reading shows it is wrong, and then the change is recorded |
| U1 and U2 (phenomena, co-existence, seat maps) | Cited by section in each ledger row instead of being restated. U1 §37 and U2 §65 are the base for overview part F |
| Strand ledger AN-01 to AN-xx, its §L change of character, §M held items | Unit rows cite the AN id where they repeat it. §L is the starting point for each word's "what differs" table. §M held items are carried into the open threads register. §Q (where each was woven) feeds the #1947 appendix |
| #1890, #1892 investigations | Cited as they stand where the units touch God's heart and hand |
| Outside-M02 pull (48 verses) | Kept as the record of the same words outside the tag (#1919); not re-pulled |

What is new: the face of every hit, read by surface; meaning, implication and stated chain on every row (§3A); and the per-word "what differs" tables. Reading cost is lower than fear's because side and phenomenon arrive pre-filled.

**Step 2. Reconciliation** of units 1–4 against the 65 Strong's and the 919 hits. Verse coverage is already complete (above), so this is a hit-level check: every hit has a face, and every Strong's is in a unit. Any gap gets an addendum (as H4172A for fear).

**Step 3. Cross-ledger overview** `anger-cross-ledger-overview-v1-<date>.md`, parts A–F as for fear, plus two parts that fear did not have (§3A): **G. Chains the verses state** and **H. What emerged, and what it changes**. Part F (anger and the other characteristics) draws on U1 §37 and U2 §65, and on the fear overview where the two meet.

**Step 4. Sub-chapter "Anger"** as **10.13**, after 10.12, with no renumbering. Its sections are **taken from the overview** (what the verses say anger is, its forms, what changes it, what it leads to), not from the 10.x activity headings (§3A, #1947). No other chapter reworked in this first step (fear precedent). Claim register updated in the same pass.

## 3A. The intended behaviour from #1944–#1947, built in

Those four items (raised 2026-10-04) ask for a revisit of Part 10 for: missing meaning (#1944); missing emerging findings and their impacts (#1945); chain operations, "this item cause the following, or this happens because of that" (#1946); and the harm of fitting verses into a fixed list of operations, "the wrong way around" (#1947). The revisit itself is not in this plan; the items stay open for it. What this plan does is **work the anger strand in the intended way from the start**, so it does not add to the problem. Measured against the fear process, the fear work met #1944 only in part (a meaning column from unit 3 on), and #1945–#1947 were not designed in. The changes:

| Item | What the fear process did | What the anger process does |
|---|---|---|
| **#1944 missing meaning** | Meaning column from unit 3 on; not every row carried it | **Every** observation row carries *setting*, *meaning there* and *what it implies* (implication marked R). No row is a quote alone. The overview and 10.13 keep the meaning beside each verse; a verse that cannot be given a meaning in its setting stays in the ledger as data |
| **#1945 emerging findings and impacts** | Not designed in; new things surfaced only in the "what differs" table | Each unit ledger ends with **"What emerged"**: what this unit shows that the narrative does not yet say, and **what it changes elsewhere** (which existing statement it confirms, narrows or contradicts, with the location). Overview part **H** gathers these across the units. Feeds #1945 when that revisit runs |
| **#1946 chain operations** | Partly: part D "what fear leads to" and "because" clauses, not as a column | A **chain column** on each row: *leads to* / *because of*, filled **only where the verse states the link** (S; for example Gen 27:42 "comforts himself … by planning to kill you"; Pro 15:1 "a harsh word stirs up anger"). Overview part **G** lists the chains with their verses. No chain is built from two verses that do not join themselves (cfg_behaviour_rule 69) |
| **#1947 fitting verses to the operations list** | Ledger "touches" and "disposition" columns pointed each row at an existing 10.x heading; the 2026-10-01 anger ledger did the same (W = woven into 10.x) | The ledger **names the concept from the verses first**. The "touches" column is kept only as a pointer to where the concept also appears, not as the place it must go. 10.13's sections come from the overview. Where the old anger placements in 10.x (§Q of the 2026-10-01 ledger) cut a verse's meaning to fit a heading, the overview lists the place in an appendix, as input for #1947. They are not reworked now |

**Held as for M25 (OT-08):** where the anger verses cross into life and death, those rows are held, so this plan does not reopen the M25 placement (#1943, #1948).

**Rhythm** (as fear): each unit is one chat; pull → read → ledger → your approval → records → session-close (commit + push). The weave is held until the overview, as it was for fear units 3–4.

## 4. Guards

- Let Scripture speak (cfg_behaviour_rule 69); readings marked "I read"; no uncounted superlatives.
- Every quote checked against iba.db `verse`.
- Open threads register checked before each unit pull and added to at each approval.
- Life-and-death crossings held under OT-08, as for fear.

## 5. Cost

About four unit chats plus one each for the overview and the sub-chapter, comparable to fear. The anger sources (U1 + U2 ≈ 375 KB) are large; each unit reads only the U1/U2 sections its words touch, not both files in full.

## 6. Decisions for you

1. **Process:** the four steps above as proposed, or adjusted (for example, a different unit split).
2. **God's own anger.** Most *ʾaph*/*ḥēmāh* hits have God as the one who is angry. Fear's B.5 ("the one who makes afraid") is the precedent for including the external party. Proposed: the units read every hit, God's anger included, and the faces separate *who is angry* from *who bears it*.
3. **10.13 and Ch 13.** Proposed: 10.13 is the full account of anger (both sides, as 10.12 holds "Dread laid on others"); Ch 13 "Under God's anger" is left unchanged in this step, and the overlap is logged as an open thread, as 10.1 and 10.12 were (OT-12). The alternative is to fold Ch 13 into 10.13 now.
4. **Folder.** Proposed: `_analytics/cross-cluster-web/anger/`, beside `fear/`. The existing M02 files stay where they are and are cited. (Why the prior work is not here: the 2026-10-01 anger ledger was filed beside its sources in the M02 cluster folder, per the weave method; fear's strand was started in `cross-cluster-web/` from the beginning.) Or file the new work in `_analytics/Clusters/M02 - anger-wrath/`.
5. **#1944–#1947 (§3A).** Proposed: the tightened format is used from anger unit 1 on, and the old 10.x anger placements are only listed (overview appendix) for the later Ch 10 revisit, not reworked in this plan. The alternative is to rework them as part of step 4.

## 7. Rulings (researcher, 2026-10-05, #1963)

Researcher, verbatim: *"decisions: 6.1 as proposed; 6.2 although God's anger is important, other parties role in anger is equally important;  6.3 ch 13 must be consolidated into 10.13 ultimately, however, I am OK if you do it as a separate tread if it helps to keep the focus on first generating 10.13 in full, and then cross check to ch 13 later.  6.4  cluster work should be in the cluster sub folder - fear was incorrectly placed in cross-cluster-web. the rule should be that all single cluster verse analysis should be in the cluster subs, and only true multi-cluster work in cross-cluster-web.  6.5 these escalations are anchors to get the reading methods correctly adjusted. what is happening at the moment is that fear and now anger is showing that the entire chapter 10 will be retuned, but not yet.  if you are ready to proceed with 1963 you can do so."*

| # | Ruling | How it is applied |
|---|---|---|
| 6.1 | The four steps as proposed | Units 1–4 as in §3, starting with unit 1 (*ʾaph*, *ḥēmāh*) |
| 6.2 | God's anger and **other parties' roles are equally important** | Every hit is read. The faces record, for each hit, **who is angry**, **at whom or what**, **who bears it**, and **who provokes, intercedes, turns it away or carries it out** (people, kings, nations, the prophet, Moses, spirits, the land and creatures), each as the verse names them. No party is subsumed under God's side or the human side. Overview part B is laid out by party, as fear's B.1–B.5 were |
| 6.3 | Ch 13 to be consolidated into 10.13 ultimately; may be a separate thread | 10.13 is written in full first; then a cross-check against Ch 13 and the consolidation. Open thread **OT-13** |
| 6.4 | Single-cluster verse analysis in the cluster subfolder; only true multi-cluster work in `cross-cluster-web/` | All anger files go in `_analytics/Clusters/M02 - anger-wrath/` (this proposal moved here). Rule proposed into config: **#1964** (`report.cluster_folder_naming_convention`). Relocation of the misplaced `fear/` and `life-death/` folders: **#1965** |
| 6.5 | #1944–#1947 are anchors for adjusting the reading method; Ch 10 will be retuned, not yet | §3A applied from unit 1. Old 10.x placements are listed, not reworked. Open thread **OT-14**. OT-12 (the 10.1 frame) is triggered by 10.13 and noted there |
