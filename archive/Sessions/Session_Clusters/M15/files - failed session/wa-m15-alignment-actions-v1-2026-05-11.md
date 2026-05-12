# WA-M15 VCG Alignment Action List
**File:** wa-m15-alignment-actions-v1-2026-05-11.md
**Date:** 2026-05-11
**Purpose:** Sub-group by sub-group comparison of current DB VCG assignments against derived VCG groupings in v2 files. Every verse and VCG addressed. Used to compile the final directive or patch.
**Previous output:** wa-m15-a-verse-meanings-v2-2026-05-11.md (and all other v2 files)

---

## How to read this file

Each sub-group section lists:
- **VCG actions** — changes needed to existing VCG descriptions, new VCGs to create, VCGs to retire
- **Verse actions** — individual verse moves, status changes, and confirmations
- **Action codes:** MOVE = reassign verse to different VCG | CONFIRM = verse correctly placed, no action | RENAME = VCG description needs updating | CREATE = new VCG needed | RETIRE = VCG no longer needed | STATUS = change verse status (G/SA/P)

---

## M15-A — Wisdom as holistic inner character and orientation

### Current VCGs in DB vs derived VCGs

| DB VCG | DB Description | DB Count | Derived VCG | Alignment |
|---|---|---|---|---|
| 528-001 | cha.kham as constituted inner quality of the person | 77 | VCG-A-01 | CONFIRM — correct grouping; description may need minor refinement |
| 528-003 | cha.kham wisdom turned back on itself / self-attributed | 11 | VCG-A-05 | CONFIRM — correct grouping; absorb VCG-A-06 uses here too |
| 528-004 | cha.kham and cha.shav as Spirit-given craft skill | 29 | VCG-A-07 + VCG-A-08 | SPLIT NEEDED — secular craft uses do not fit the Spirit-given sacred description |
| 528-005 | cha.kham as governance qualification / institutional role | 26 | VCG-A-02 + VCG-A-03 | SPLIT NEEDED — governance qualification and institutional class are distinct |
| 527-001 | tu.shiy.yah as sound wisdom / effective resource | 12 | VCG-A-11 | CONFIRM — correct; one verse disputed (Job 30:22) |
| 525-001 | se.khel as practical inner quality | 19 | VCG-A-12 | CONFIRM |
| 532-002 | chokh.mah as divine gift | 19 | VCG-A-13 + VCG-A-15 partial | PARTIAL FIT — some verses belong in VCG-A-15 (wisdom in Christ); review needed |
| 532-003 | sofia visible in a person | 14 | VCG-A-17 partial + VCG-A-15 partial | RENAME/REFINE — description too narrow |
| 3459-001 | fronimos as practical shrewdness | 14 | VCG-A-18 | CONFIRM |
| 996-001 | froneō as inner orientation of the whole person | 19 | VCG-A-19 + VCG-A-20 | NOTE — v1 file already notes these are two uses; keep in one VCG or split |
| 6668-001 | chak.kim as the court wise-men class | 13 | VCG-A-03 | CONFIRM |
| 6696-001 | sofos as divine attribute / wisdom belonging to God | 11 | VCG-A-15 partial | RENAME — current description does not match all verses (e.g. Luk 7:35, Mat 11:19) |
| 4458-001 | sofia/sofos — human wisdom overturned by the cross | 37 | VCG-A-14 | CONFIRM core; MOVE required for misrouted verses (see below) |
| 1174-001 | cha.shav as creative inner faculty of design | 1 | VCG-A-10 | MOVE to M15-E (divine purposive devising) |
| 1174-002 | cha.shav as inner scheming against another | 3 | VCG-A-09 | MOVE to M15-E (3334-001) |
| 6676-001 | asofos as absence of wisdom | 1 | (stand-alone) | CONFIRM |
| — | — | — | VCG-A-16 (sofia appearance without substance) | CONFIRM existing assignments — Col 2:23, Jam 3:15 already in 4458-001; may need own sub-group |
| — | — | — | VCG-A-21 (sofizo — two opposite uses) | ACTION NEEDED — both 2Ti 3:15 and 2Pe 1:16 currently in 4458-001; must be separated |

---

### M15-A Verse-level actions

#### cha.shav (mti_id=1174) verses — MOVES REQUIRED

| vr_id | Reference | Current VCG | Action | Destination |
|---|---|---|---|---|
| 54622 | Exo 36:8 (cha.shav) | 4458-001 | MOVE | 528-004 (sacred craft group) |
| 54608 | 2Ch 2:14 (cha.shav) | 4458-001 | MOVE | 528-004 (sacred craft group) |
| 54610 | 2Sa 14:14 (cha.shav) | 1174-001 | MOVE | M15-E — divine purposive planning (new VCG or 3334-002) |
| 54612 | Est 8:3 (cha.shav) | 1174-002 | MOVE | M15-E 3334-001 (devising evil against) |
| 54613 | Est 9:25 (cha.shav) | 1174-002 | MOVE | M15-E 3334-001 |
| 54626 | Psa 35:20 (cha.shav) | 1174-002 | MOVE | M15-E 3334-001 |

#### cha.kham (mti_id=528) verses — MOVES REQUIRED

| vr_id | Reference | Current VCG | Action | Destination | Reason |
|---|---|---|---|---|---|
| 7343 | 1Ki 2:9 | 4458-001 | MOVE | 528-005 (governance qualification) | Positive wisdom attribution to Solomon, not cross-opposition |
| 208338 | 1Cor 3:10 (sofos) | 4458-001 | MOVE | 532-003 (sofia visible in person) or 532-002 | "Skilled master builder" — commendation, not cross-opposition |

#### sofos/sofia (mti_id=4458/532) verses — MOVES REQUIRED

| vr_id | Reference | Current VCG | Action | Destination | Reason |
|---|---|---|---|---|---|
| 7454 | 2Ti 3:15 (sofizo mti_id=530) | 4458-001 | MOVE | NEW VCG under mti_id=530 — "making wise" positive use | Scripture making wise for salvation — positive, not cross-opposition |
| 7455 | 2Pe 1:16 (sofizo mti_id=530) | 4458-001 | MOVE | NEW VCG under mti_id=530 — "cleverly devised myths" negative | Must be in a separate group from 2Ti 3:15 |
| 7499 | Jam 3:13 (sofia mti_id=532) | 4458-001 | MOVE | 532-003 (sofia visible in person's conduct) | Wisdom visible in meek conduct — positive characterisation |
| 208344 | Jam 3:13 (sofos mti_id=4458) | 4458-001 | MOVE | 532-003 or new VCG | Same verse, sofos row — same reasoning |
| 7500 | Jam 3:15 (sofia) | 4458-001 | CONFIRM or create VCG-A-16 | False/earthly wisdom — belongs in 4458-001 or own group | Currently correct in 4458-001 (cross-opposition pattern); confirm |
| 7501 | Jam 3:17 (sofia) | 532-002 | CONFIRM | Wisdom from above — correct in gift VCG | |

#### sofos (mti_id=4458) verses in 6696-001 — VCG DESCRIPTION ISSUE

| vr_id | Reference | Current VCG | Action | Note |
|---|---|---|---|---|
| 208351 | Rom 16:27 | 6696-001 | CONFIRM | "Only wise God" — divine attribute; correctly placed |
| 7478 | 1Cor 1:24 (sofia) | 6696-001 | CONFIRM | "wisdom of God" — divine attribute |
| 7491 | Eph 3:10 (sofia) | 6696-001 | CONFIRM | "manifold wisdom of God" |
| 7492 | Col 2:3 (sofia) | 6696-001 | CONFIRM | "hidden in Christ" |
| 7464 | Luk 7:35 (sofia) | 6696-001 | MOVE | 532-003 (sofia visible in a person/deeds) | "Wisdom justified by her children/deeds" — not a divine attribute statement |
| 7466 | Luk 11:49 (sofia) | 6696-001 | CONFIRM | "The Wisdom of God said" — divine attribute / personification |
| 7476 | Rev 7:12 (sofia) | 6696-001 | CONFIRM | Doxological — belongs to God |
| 7472 | Rom 11:33 (sofia) | 6696-001 | CONFIRM | "Oh the depth of riches and wisdom of God" |
| 7577 | Mat 11:19 (sofia) | 6696-001 | MOVE | 532-003 or new VCG | "Wisdom justified by her deeds" — not a divine attribute |
| 7595 | Luk 11:49 — already listed |  |  |  |

#### All other M15-A verses — CONFIRMED correctly placed

The following verse groups are confirmed correct — no action needed:

**528-001 (cha.kham as constituted inner quality):** All 77 Proverbs/Ecclesiastes/narrative cha.kham verses correctly in this group. Includes Judg 5:29, Psa 49:10, Psa 107:43, Hos 13:13, Hos 14:9, and all Proverbs wisdom-character verses. CONFIRM all.

**528-003 (self-attributed/misdirected wisdom):** Deu 32:6, Pro 3:7, Pro 3:35, Pro 26:5/12/16, Pro 28:11, Job 37:24, Isa 5:21, Jer 4:22, Jer 8:8/9, Jer 9:12, Jer 9:23, Jer 10:7. CONFIRM all.

**528-004 (sacred craft group):** All Exodus tabernacle/vestment cha.shav and cha.kham verses (Exo 26:1, 26:31, 28:3, 28:6, 28:15, 31:4, 31:6, 35:10, 35:25, 35:32, 35:35, 36:1, 36:2, 36:4, 36:8 [cha.kham row], 36:35, 38:23, 39:3, 39:8); 1Ch 22:15, 2Ch 2:7, 2:13, 2:14 [cha.kham row]; Amos 6:5; Isa 40:20; Eze 27:8/9; Jer 10:9; 2Ch 26:15. CONFIRM all.
NOTE: Isa 40:20 (idol craftsman) and Jer 10:9 (idol craftsmen) and Eze 27:8/9 (ship pilots/caulkers) are secular craft uses that do not fit the Spirit-given sacred description. These should be in a separate VCG or the VCG description must be widened. FLAG for description update.

**528-005 (governance/institutional):** Gen 41:8, 41:33, 41:39, Exo 7:11, Deu 1:13, 1:15, Deu 16:19, Est 1:13, Est 6:13, Job 15:2, 15:18, Job 17:10, Job 34:2, 34:34, 1Ki 3:12, 1Ki 5:7, Isa 3:3, Isa 19:11/12, Isa 29:14, Isa 31:2, Isa 44:25, Jer 18:18, Jer 50:35, Jer 51:57, Eze 28:3. CONFIRM all. Note 1Ki 2:9 needs moving out (see above).

**527-001 (tu.shiy.yah):** All 12 verses confirmed. Job 30:22 is a disputed translation — FLAG for review but no action needed now.

**525-001 (se.khel):** All 19 verses confirmed. Dan 8:25 (cunning) is correctly in this group — se.khel is directionally neutral.

**532-002 (chokh.mah/sofia as gift):** Ezr 7:25, Dan 2:20, 2:21 [chokh.mah], 2:23, 2:30, 5:11, 5:14; NT: 1Cor 1:30, 2:6, 2:7, 2:13, 1Cor 12:8, Eph 1:8, 1:17, Col 1:9, 1:28, Col 3:16, Jam 1:5, Jam 3:17, Rev 5:12, Rev 13:18, Rev 17:9. CONFIRM all. Note Col 3:16 [sofia] and Jam 3:17 correct. 2Pe 3:15 (sofia given to Paul) also confirm.

**532-003 (sofia visible in person):** Luk 2:40, 2:52, Luk 7:35 [MOVE — see above], Luk 11:31, Luk 21:15, Act 6:3, 6:10, 7:10, 7:22, Mar 6:2, Mat 12:42, Mat 13:54, Col 4:5, 2Pe 3:15. CONFIRM most. Luk 7:35 flagged above.

**4458-001 (human wisdom / cross-opposition — sofia/sofos):** 1Cor 1:17, 1:19 [both sofia and sofos], 1:20 [both], 1:21, 1:22, 1:25, 1:26, 1:27, 2Cor 1:12, 1Cor 2:1, 2:4, 2:5, 3:19 [both], 3:20, 3:18, 1Cor 6:5, Eph 5:15 [sofos], Col 2:23, Jam 3:15, Luk 10:21 [sofos], Mat 11:25 [sofos], Mat 23:34 [sofos], Rom 1:14, 1:22, 16:19 [all sofos], 2Cor 11:19 [fronimos — note: fronimos is in 3459-001; this is a different row]. CONFIRM core group.

**3459-001 (fronimos):** Mat 7:24, 10:16, 24:45, 25:2/4/8/9, Luk 12:42, 16:8, 1Cor 4:10, 10:15, 2Cor 11:19, Rom 11:25, Rom 12:16. CONFIRM all.

**996-001 (froneō):** Mat 16:23, Mar 8:33, Act 28:22, Rom 8:5, 12:3, 12:16, 14:6, 15:5, 1Cor 13:11, 2Cor 13:11, Gal 5:10, Col 3:2, Phili 1:7, 2:2, 2:5, 3:15, 3:19, 4:2, 4:10. CONFIRM all.

**6668-001 (chak.kim):** Dan 2:12, 2:13, 2:14, 2:18, 2:21, 2:24, 2:27, 2:48, 4:6, 4:18, 5:7, 5:8, 5:15. CONFIRM all.

**6696-001 (sofos/sofia as divine attribute):** See verse-level actions above — most confirmed; Luk 7:35 and Mat 11:19 need moving.

**6676-001 (asofos):** Eph 5:15. CONFIRM.

**1174-001 (cha.shav creative/providential):** 2Sa 14:14 only — MOVE to M15-E (see above).

**1174-002 (cha.shav scheming):** Est 8:3, Est 9:25, Psa 35:20 — all MOVE to M15-E 3334-001.

---

### M15-A VCG Description Updates Required

| VCG | Current description issue | Required action |
|---|---|---|
| 528-004 | Described as "Spirit-given, directed toward sacred construction" but includes secular craft (Isa 40:20, Jer 10:9, Eze 27:8/9, Amo 6:5, 2Ch 26:15) | UPDATE description to: "cha.kham and cha.shav name an inner capacity for skilled craft work — in the primary cluster Spirit-given for sacred construction, but extending to skilled work in secular, commercial, and military contexts." OR create a split VCG for secular craft |
| 528-005 | "Wisdom as qualification for institutional responsibility" conflates governance qualification and court wise-men class | UPDATE description or split into 528-005a (governance qualification) and 528-005b (institutional class / court wise men) |
| 6696-001 | "Wisdom as divine attribute" does not fit Luk 7:35 and Mat 11:19 (personified wisdom justified by deeds) | UPDATE: move those two verses to 532-003; tighten description to doxological and strictly divine-attribute uses |
| 4458-001 | Holds sofizo (2Ti 3:15 and 2Pe 1:16) which are opposite uses | SEPARATE: create new VCG for sofizo positive (making wise) and keep 2Pe 1:16 in 4458-001 or a separate sofizo negative group |

---

### M15-A New VCGs Required

| New VCG | Term | Key verses | Description needed |
|---|---|---|---|
| sofizo positive | G4679 sofizo (mti_id=530) | 2Ti 3:15 | "The act of making wise — Scripture's transformative work producing inner wisdom oriented toward salvation through faith in Christ Jesus" |
| sofizo negative | G4679 sofizo (mti_id=530) | 2Pe 1:16 | "The inner capacity for clever construction turned to fabrication — what the apostles explicitly did not do" |

---

## M15-B — Understanding as inner perceptive faculty

### VCG-level actions

| DB VCG | DB Count | Action | Note |
|---|---|---|---|
| 932-001 (bin constituted faculty) | 69 | CONFIRM | Core group correct |
| 932-002 (bin seeking/receiving understanding) | 37 | CONFIRM | Core group correct |
| 932-003 (God's comprehension of persons) | ~11 | CONFIRM | Core group correct |
| 932-004 (failed/withheld/absent understanding) | 52 | REFINE NEEDED | Holds 4 distinct patterns — see below |
| 523-002 (bi.nah) | ~16 | CONFIRM | Core group correct |
| 524-002 (te.vu.nah) | ~30 | DESCRIPTION UPDATE | Holds sacred craft, divine attribute, protective quality, and non-sacred uses — needs refining |
| 816-002 (sunesis/understanding of mystery) | varies | CONFIRM | Cross-term VCG — verify |
| 531-001 (fronesis) | ~2 | CONFIRM | Luk 1:17, Eph 1:8 |
| 1207-001 (epistēmōn) | 1 | CONFIRM | Jam 3:13 — single verse |
| Various suniēmi/sunetos/asunetos VCGs | ~52 | CONFIRM core | See specific moves below |

### M15-B Verse-level actions

| vr_id | Reference | Current VCG | Action | Destination | Reason |
|---|---|---|---|---|---|
| 27692 | Dan 11:30 (bin "attention") | 932-004 | MOVE | 932-001 or new directional-attending group | "Pay attention to" is directional attending, not failure of understanding |
| 27694 | Dan 11:37 (bin "attention") | 932-004 | MOVE | 932-001 or same new group | Same reason |
| 7105 (te.vu.nah) | Hos 13:2 | 524-002 | FLAG / MOVE | New VCG or 524-003 — non-sacred craft te.vu.nah | Craft skill for idols — does not fit "wisdom, right conduct, and discernment" description |
| te.vu.nah | Eze 28:4 | 524-002 | FLAG / MOVE | New VCG — self-enriching understanding | Self-enriching understanding — does not fit 524-002 description |
| bin row | Isa 10:13 | 932-004 | FLAG | May need own group — self-attributed understanding | King claims understanding as self-sourced; not failure of understanding |
| bi.nah rows | Deu 4:6 | 816-002 | FLAG | May fit better in 932-001/523-002 | Primary meaning is understanding demonstrated through obedience |
| bin row | Deu 4:6 | 816-002 | FLAG | Same as above | |

All other M15-B verses: CONFIRM as correctly placed.

---

## M15-C — Knowledge as inner content and covenantal knowing

### VCG-level actions

| DB VCG | Current description | Action | Note |
|---|---|---|---|
| 958-001 (covenantal knowing) | Covenantal/relational knowing between God and Israel | CONFIRM core; NOTE holds 4 sub-patterns | Pattern (b) — "then you shall know" — is the largest and most distinctive |
| 958-002 (self-knowledge/inner moral knowing) | Self-knowledge of inner moral condition | CONFIRM | |
| 958-003 (God's knowing of persons) | God's comprehensive knowing of motives, character | CONFIRM | |
| 958-004 (moral knowledge guiding action) | Moral knowledge | CONFIRM | |
| 958-005 (God's revelatory self-disclosure) | God's revelatory self-disclosure | CONFIRM | |
| 955-001 (da.at as inner possession) | da.at as inner content of the wise person | CONFIRM | |
| 955-002 (da.at of God) | Knowledge of God's ways | CONFIRM | |
| 955-003 (da.at as divine attribute) | da.at belonging to God | CONFIRM | |
| 955-004 (da.at as intent) | da.at determining moral status of act | CONFIRM | |
| 955-005 (absent/hollow da.at) | Empty speech without knowledge | CONFIRM | |
| 959-001 (de.ah divine attribute) | Knowledge as divine attribute | CONFIRM | |
| 959-002 (de.ah eschatological) | Universal knowledge of God filling the earth | CONFIRM | |
| 961-001 (de.a formed opinion) | Inner formed opinion | CONFIRM | |
| 961-002 (de.a divine knowing) | Divine perfect knowing | CONFIRM | |
| 962-001 (man.da as gift) | Knowledge as divine gift | CONFIRM | |
| 962-002 (man.da as reason) | Reason as defining inner seat of humanness | CONFIRM | HIGHLIGHT for Session D |
| 963-001 through 963-005 (oida) | Various oida patterns | CONFIRM core | |
| 1838-001 (agnoeō) | Culpable spiritual ignorance | SPLIT NEEDED | Two uses conflated — culpable vs neutral informational |

### M15-C Verse-level actions

| Reference | Current VCG | Action | Destination | Reason |
|---|---|---|---|---|
| Hos 6:6 (da.at) | 1838-001 | MOVE | 955-002 (da.at of God) | "Knowledge of God rather than burnt offerings" is positive statement of what God desires, not culpable ignorance |
| Psa 19:2 (da.at) | 1838-001 | MOVE | 955-001 (da.at as inner possession/disclosure) | "Night reveals knowledge" — positive disclosure through creation |
| Multiple agnoeō P/SA verses | 1838-001 | REVIEW | Split into 1838-001 culpable and new VCG for neutral informational | Rom 1:13, Rom 6:3, Rom 7:1, 1Cor 10:1, 1Cor 12:1, 1Th 4:13, Heb 5:2, 2Cor 1:8, 2Cor 6:9, Gal 1:22, Mar 9:32, Luk 9:45 — these use agnoeō in neutral informational sense |

All other M15-C verses: CONFIRM as correctly placed.

---

## M15-D — Discernment and practical judgment

### VCG-level actions

| DB VCG | Action | Note |
|---|---|---|
| 3335-001 (moral imputation) | CONFIRM | Correct — divine moral crediting |
| 3335-002 (evaluative regard of persons/things) | CONFIRM; NOTE thin inner-being in classificatory uses | Territorial/legal uses have marginal IB content — flag for future set-aside review |
| 3336-001 (inner forming of judgment from observation) | CONFIRM | |
| 3336-002 (evaluative regard) | CONFIRM; NOTE thin IB in some uses | Same as 3335-002 |
| 519-001 (sa.khal prudent discernment) | CONFIRM | |
| 519-002 (sa.khal wisdom-in-action producing success) | CONFIRM | |
| 4487-001 (a.rum prudent positive) | CONFIRM | |
| 4487-002 (a.rum crafty negative) | CONFIRM | |
| 4486-001 (a.rom learnable prudence) | CONFIRM | |
| 4486-002 (a.rom cunning negative) | CONFIRM | |
| 5099-001 (ta.am discernment through tasting) | CONFIRM | |
| 5099-002 (ta.am abstaining as inner state) | MISASSIGNMENT — three verses need moving | See below |
| 1285-001 (diakrinō discriminating judgment) | CONFIRM | |
| 1285-002 (diakrinō inner self-division) | CONFIRM | |
| 3409-001 (logismos conflicting thoughts) | CONFIRM | |
| 818-001 (aisthētērion cultivated discernment) | CONFIRM | Single verse Heb 5:14 |

### M15-D Verse-level actions

| vr_id | Reference | Current VCG | Action | Destination | Reason |
|---|---|---|---|---|---|
| (sa.khal) | Gen 3:6 | 5099-002 | MOVE | 519-001 (sa.khal prudent discernment) | Desire for wisdom, not taste abstaining |
| (a.rum) | Job 5:12 | 5099-002 | MOVE | 4487-002 (a.rum crafty/cunning) | Craftiness that God frustrates, not taste |
| (cha.shav H) | Isa 53:3 | 5099-002 | MOVE | 3335-002 (evaluative regard — persons regarded negatively) | "We esteemed him not" = evaluative regard, not taste |
| (cha.shav H) | Mal 3:16 | 3335-001 | MOVE | 3335-002 (evaluative regard — persons assessed as worthy) | Human esteeming of God's name, not divine imputation to human |
| (cha.shav J) | Jer 23:27 | 3336-001 | MOVE | M15-E 3334-001 (devising evil) | "Think to make my people forget my name" — deliberate plotting, not self-examination |

---

## M15-E — Deliberative planning, counsel, and purposive intent

### VCG-level actions

| DB VCG | Action | Note |
|---|---|---|
| 749-001 (ya.ats human counsel) | CONFIRM | |
| 749-002 (ya.ats hostile counsel / moral-character expression) | CONFIRM | |
| 749-003 (ya.ats divine sovereign counsel) | CONFIRM | |
| 3334-001 (cha.shav devising harm) | CONFIRM; NOTE receives several moves from M15-A and M15-D | |
| 3334-002 (cha.shav purposive planning) | CONFIRM | |
| 509-001 (boulomai human volitional will) | CONFIRM | |
| 509-002 (boulomai divine purposive will) | CONFIRM | |
| 1001-001 (gnōmē personal judgment) | CONFIRM | |
| 1001-002 (gnōmē shared purpose) | CONFIRM | |
| 3578-A (shit active attending) | CONFIRM | |
| 3578-B (shit failure of attending) | CONFIRM | |
| 2109-001 (bouleuō deliberate decision-making) | CONFIRM | |
| 2109-002 (bouleuō deliberate harmful resolve) | CONFIRM | |
| 3280-001 (protithēmi purposive intention) | CONFIRM | |
| 847-001 (za.mam human purposeful resolve) | CONFIRM | |
| 847-002 (za.mam divine irresistible purposing) | CONFIRM | |
| 1179-001 (chesh.bon rational faculty) | CONFIRM | |
| 3373-001 (pronoia governance foresight/provision) | CONFIRM | |
| 754-001 (uts communal purposing) | CONFIRM | |
| 3445-001 (a.shat appeal for divine attending) | CONFIRM | |
| 3482-001 (a.shit royal planning) | CONFIRM | |

### M15-E Verse-level actions — RECEIVES moves from other sub-groups

| Reference | Source VCG | Action | Destination in M15-E | Reason |
|---|---|---|---|---|
| 2Sa 14:14 (cha.shav) | 1174-001 (M15-A) | MOVE IN | 3334-002 (purposive divine planning) | Divine purposive devising of means for mercy |
| Est 8:3 (cha.shav) | 1174-002 (M15-A) | MOVE IN | 3334-001 (devising harm) | Evil plan devised against Jews |
| Est 9:25 (cha.shav) | 1174-002 (M15-A) | MOVE IN | 3334-001 | Same |
| Psa 35:20 (cha.shav) | 1174-002 (M15-A) | MOVE IN | 3334-001 | Devising words of deceit |
| Jer 23:27 (cha.shav J) | 3336-001 (M15-D) | MOVE IN | 3334-001 | Deliberate plotting to displace God's name |
| 1Ch 28:19 (sa.khal) | Listed in M15-E table | MOVE OUT to M15-D | 519-001 | sa.khal is M15-D term; divine disclosure of building plan |

Additional: Jon 1:4 (cha.shav "threatened") currently in 3334-002 — FLAG for review. The ship threatening to break up is an unusual anthropomorphising use; may warrant set-aside or a note.

---

## M15-F — Meditative and reflective inner activity

### VCG-level actions

All existing M15-F VCGs confirmed. The following are the relevant group confirmations:

| DB VCG | Action | Note |
|---|---|---|
| 242-001 (si.ach meditation on God's works) | CONFIRM | |
| 242-002 (si.ach complaint/telling) | CONFIRM | NOTE: Psa 69:12 is "talk of those at the gate" — others' si.ach about the psalmist; confirm or flag |
| 975-001 (si.chah all-day meditation) | CONFIRM | |
| 896-001 (ha.gig musing-to-groaning) | CONFIRM | |
| 977-001 (ha.gut heart-meditation producing understanding) | CONFIRM | |
| 5883-001 (hig.ga.von) | CONFIRM — NOTE Psa 92:3 correctly SA | |
| 5662-001 (se.khal contemplative attention) | CONFIRM | Single verse Dan 7:8 |
| 1181-001 (se.ach God declaring human thought) | CONFIRM | Single verse Amo 4:13 |
| 1081-001 (dialogismos evil from heart) | CONFIRM | |
| 1081-002 (dialogismos disputed opinions) | CONFIRM | |
| 1184-001 (dialogizomai individual reasoning) | CONFIRM | |
| 1184-002 (dialogizomai communal deliberation) | CONFIRM | |
| 917-001 (enthumēsis perceived thoughts) | CONFIRM | |
| 3392-001 (enthumeomai deliberate reflection) | CONFIRM | |

### M15-F Verse-level actions

No moves required. All verses confirmed correctly placed.

Set-aside confirm: Psa 92:3 (hig.ga.von = "melody") correctly SA as no_inner_being. Judg 5:10 (si.ach) correctly SA. Job 12:8 (si.ach) correctly SA.

---

## M15-G — Inner thought-content

### VCG-level actions

| DB VCG | Action | Note |
|---|---|---|
| 960-001 (mad.da governance-knowledge) | CONFIRM | |
| 960-002 (mad.da thought-life moral seat) | CONFIRM | Single verse Ecc 10:20 |
| 3449-001 (ra.yon revelation-alarmed thoughts) | CONFIRM | All 6 Daniel uses correctly placed |
| 3453-001 (re.a thoughts known by God) | CONFIRM | Psa 139:2 and 139:17 |
| 1178-001 (ash.tut ease-contempt) | CONFIRM | Single verse Job 12:5 |
| 3442-001 (esh.to.nah plans perishing at death) | CONFIRM | Single verse Psa 146:4 |
| 1188-001 (noēma contested cognitive faculty) | CONFIRM | All 6 uses correctly placed |
| 2493-001 (frēn mature thinking faculty) | CONFIRM | Single verse 1Cor 14:20 |
| 3372-001 (ennoia heart's thoughts) | CONFIRM | Heb 4:12 and 1Pe 4:1 |
| 3375-001 (epinoia purposeful intent) | CONFIRM | Single verse Act 8:22 |
| 3408-001 (dianoēma hidden thoughts known to Jesus) | CONFIRM | Single verse Luk 11:17 |

### M15-G Verse-level actions

NOTE on ra.yon: Dan 4:19 and Dan 5:6 were flagged in session memory as appearing in M15-A verse table. Confirm that these ra.yon rows are correctly in M15-G (3449-001) and the M15-A appearance is because these verses also have cha.kham/chokh.mah spans. No move needed — ra.yon rows are in M15-G, cha.kham rows in M15-A. Confirm both.

No moves required from M15-G. All verses confirmed correctly placed.

---

## BOUNDARY — Functional, supporting, and cluster-reassignment candidates

### VCG-level actions

| DB VCG | Action | Note |
|---|---|---|
| 1080-001 (dialegō reasoned discourse) | CONFIRM | |
| 1171-001 (logos inner-dwelling word) | CONFIRM G-status verses | Multiple SA verses correctly set aside |
| 454-001 (suneidō conscious awareness) | CONFIRM | |
| 6085-001 (pe.sher interpretive wisdom) | CONFIRM | Single verse Ecc 8:1 |
| 6256-001 (tir.gal intimate teaching) | CONFIRM | Single verse Hos 11:3; NOTE connection to M15-C covenantal knowing |
| 973-001 (methermēneuō translation) | CONFIRM | Mat 1:23 only G-status |
| 7085-001 (diabebaioō outward insistence) | CONFIRM | |
| 7333-001 (eikō simile for inner state) | CONFIRM | |
| 7419-001 (gumnazō training toward godliness) | CONFIRM | |
| 7419-002 (gumnazō training toward vice) | CONFIRM | |
| 5864-001 (hermēneia interpretation gift) | CONFIRM | |
| 5865-001 (diermēneutēs interpreter absent) | CONFIRM | |

### BOUNDARY Verse-level actions

| vr_id | Reference | Current status | Action | Note |
|---|---|---|---|---|
| Act 13:8 (methermēneuō) | P | CONFIRM P-status | Factual name translation; no inner-being content in span |
| Act 23:15, 24:22 (diaginōskō) | NR | CONFIRM NR | Legal determination; not inner-being |
| Luk 12:14 (meristēs) | P | CONFIRM P | Arbitrator role; no inner-being in span |

All G-status BOUNDARY logos verses: CONFIRM correctly placed.
All SA logos verses: CONFIRM correctly set aside.

---

## Summary of all actions by type

### MOVE actions (verse reassignments)

| # | vr_id / Reference | From | To | Reason |
|---|---|---|---|---|
| 1 | Exo 36:8 cha.shav (vr_id 54622) | 4458-001 | 528-004 | Sacred craft — not cross-opposition |
| 2 | 2Ch 2:14 cha.shav (vr_id 54608) | 4458-001 | 528-004 | Sacred craft — not cross-opposition |
| 3 | 1Ki 2:9 cha.kham (vr_id 7343) | 4458-001 | 528-005 | Governance qualification — positive attribution |
| 4 | 1Cor 3:10 sofos (vr_id 208338) | 4458-001 | 532-003 | Skilled master builder — commendation not cross-opposition |
| 5 | Jam 3:13 sofia (vr_id 7499) | 4458-001 | 532-003 | Wisdom visible in meek conduct — positive |
| 6 | Jam 3:13 sofos (vr_id 208344) | 4458-001 | 532-003 | Same verse — sofos row |
| 7 | 2Ti 3:15 sofizo (vr_id 7454) | 4458-001 | NEW sofizo VCG (positive) | Making wise through Scripture |
| 8 | 2Pe 1:16 sofizo (vr_id 7455) | 4458-001 | NEW sofizo VCG (negative) or own group | Cleverly devised myths — opposite of 2Ti 3:15 |
| 9 | 2Sa 14:14 cha.shav (vr_id 54610) | 1174-001 | M15-E 3334-002 | Divine purposive devising of means |
| 10 | Est 8:3 cha.shav (vr_id 54612) | 1174-002 | M15-E 3334-001 | Devising evil against Jews |
| 11 | Est 9:25 cha.shav (vr_id 54613) | 1174-002 | M15-E 3334-001 | Same |
| 12 | Psa 35:20 cha.shav (vr_id 54626) | 1174-002 | M15-E 3334-001 | Devising words of deceit |
| 13 | Luk 7:35 sofia (vr_id 7464) | 6696-001 | 532-003 | Wisdom justified by deeds — not divine attribute |
| 14 | Mat 11:19 sofia (vr_id 7458) | 6696-001 | 532-003 | Wisdom justified by her deeds — same |
| 15 | Gen 3:6 sa.khal | 5099-002 | 519-001 | Desire for wisdom, not taste abstaining |
| 16 | Job 5:12 a.rum | 5099-002 | 4487-002 | Craftiness frustrated by God, not taste |
| 17 | Isa 53:3 cha.shav H | 5099-002 | 3335-002 | Evaluative regard — not esteemed |
| 18 | Mal 3:16 cha.shav H | 3335-001 | 3335-002 | Human esteeming God, not divine imputation |
| 19 | Jer 23:27 cha.shav J | 3336-001 | M15-E 3334-001 | Deliberate plotting, not self-examination |
| 20 | Dan 11:30 bin | 932-004 | 932-001 or new directional group | Directional attending, not understanding failure |
| 21 | Dan 11:37 bin | 932-004 | Same | Same reason |
| 22 | Hos 13:2 te.vu.nah | 524-002 | New VCG — non-sacred te.vu.nah | Craft for idols — description mismatch |
| 23 | Eze 28:4 te.vu.nah | 524-002 | New VCG — self-enriching understanding | Description mismatch |
| 24 | 1Ch 28:19 sa.khal | M15-E table | M15-D 519-001 | sa.khal is M15-D term |
| 25 | Hos 6:6 da.at | 1838-001 | 955-002 | Positive statement, not culpable ignorance |
| 26 | Psa 19:2 da.at | 1838-001 | 955-001 | Positive disclosure, not ignorance |

### VCG DESCRIPTION UPDATES required

| # | VCG | Action |
|---|---|---|
| 1 | 528-004 | Update description to include secular craft use; or split into 528-004a (sacred) and 528-004b (secular) |
| 2 | 528-005 | Update or split to separate governance qualification from institutional class |
| 3 | 6696-001 | Tighten to strictly divine-attribute uses after moving Luk 7:35 and Mat 11:19 |
| 4 | 524-002 | Update to acknowledge multiple te.vu.nah use types; after moves of Hos 13:2 and Eze 28:4 |
| 5 | 1838-001 | Split into culpable ignorance group and neutral informational awareness group |

### NEW VCGs required

| # | Sub-group | Term | Key verses | Description |
|---|---|---|---|---|
| 1 | M15-A | G4679 sofizo | 2Ti 3:15 | Scripture making the person wise for salvation — positive, transformative |
| 2 | M15-A | G4679 sofizo | 2Pe 1:16 | Cleverly devised myths — the fabricating use the apostles explicitly did not do |
| 3 | M15-B | H0995 bin | Dan 11:30, 11:37 | Directional attending — bin as perceptive attention directed toward/away from an object |
| 4 | M15-B | H8394 te.vu.nah | Hos 13:2, Eze 28:4 | te.vu.nah applied to non-sacred or self-serving purposes |
| 5 | M15-C | G0050 agnoeō | Various neutral informational uses | Neutral informational unawareness — distinct from culpable spiritual ignorance |

### FLAGS for future review (no immediate action)

| # | Reference | Issue |
|---|---|---|
| 1 | Job 30:22 (tu.shiy.yah "toss") | Disputed translation — meaning unclear; currently in 527-001 |
| 2 | Jon 1:4 (cha.shav "threatened") | Anthropomorphising storm — outlier in 3334-002; consider set-aside |
| 3 | Deu 4:6 (bin and bi.nah rows) | Both assigned to 816-002; primary meaning is understanding through covenant obedience — review |
| 4 | Isa 10:13 (bin "I have understanding") | Assyrian king's self-attributed understanding in 932-004; may need own group |
| 5 | Multiple 1838-001 agnoeō neutral uses | Mar 9:32, Luk 9:45, Rom 1:13, 6:3, 7:1, 1Cor 10:1, 12:1, 1Th 4:13, Heb 5:2 — review for split |
| 6 | Isa 40:20, Jer 10:9, Eze 27:8/9 (cha.kham secular craft) | Currently in 528-004 but described as sacred/Spirit-given — VCG description mismatch |
| 7 | 528-005 institutional class (Jer 50:35, 51:57) | Destruction-of-wise-men verses vs governance-qualification verses in same VCG |
| 8 | 932-004 (four sub-patterns) | Judicial withholding / universal failure / limits before mystery / directional attending — should these be split? |

---

*End of action list. Total actions: 26 verse moves, 5 VCG description updates, 5 new VCGs required, 8 flags for future review.*
*Next step: compile these actions into a directive or patch instruction for Claude Code to execute against bible_research.db.*
