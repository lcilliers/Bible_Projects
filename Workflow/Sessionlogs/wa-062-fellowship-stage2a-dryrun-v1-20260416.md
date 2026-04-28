# WA — Stage 2a Dry Run Report: Registry 062 (Fellowship)
**Filename:** wa-062-fellowship-stage2a-dryrun-v1-20260416.md
**Date:** 2026-04-16
**Version:** v1.0
**Extract tested:** wa-062-fellowship-sessionb-export-v2-20260416.json
**Instruction tested:** wa-sessionb-analysis-output-v1-20260416.md (pre-fix version)
**Previous output refs:**
- wa-sessionb-analysis-output-v1-20260416.md (instruction — corrected post this run)
- wa-global-sessionb-update-tasklist-v1_17-20260416.md

---

## Purpose

Dry run of the Stage 2a instruction against the fellowship extract. Records: (1) extract completeness assessment, (2) instruction gaps identified during the run, (3) corrections applied to the instruction, (4) substantive analytical observations from the data.

---

## Part 1 — Extract Pre-flight Assessment

### S3 Correction — Confirmed

`session_b_status = 'Pre-Analysis Complete'` is present in the registry record of the extract. This is sufficient confirmation that Stage 1 is complete and the extract is the correct one. No CC check is needed. The instruction was updated to use this field rather than requesting CC confirmation.

### Extract Completeness Against Stage 2a Requirements

| Stage 2a requirement | In extract | Status |
|---|---|---|
| Registry overview fields | Full registry row present | ✓ |
| OWNER terms — 13 active, all `extracted` | Present | ✓ |
| No XREF terms | `active_xref_term_count: 0` | ✓ (Unit 2 fast-path) |
| LSJ entries (Greek terms G2842, G2844) | `lsj_parse: null` on both | ⚠ Gap — noted IG-3 |
| Meaning parse / structured senses | `senses: 0` on all 13 terms | ⚠ Gap — noted IG-4 |
| `step_search_gloss` and `short_def_mounce` | Present for Greek terms | ✓ (fallback available) |
| 19 verse context groups with descriptions | Present, all CLAUDE_AI confidence | ✓ |
| Anchor verses — 20 total | Present with full verse text | ✓ |
| Dimension assignments — all populated | Yes; 0 AUTOMATED; 0 NULL | ✓ |
| Correlation signals — ranked pairs | 0 ranked pairs | ⚠ Gap — noted IG-5 |
| Shared anchor verses | 3 present | Partial |
| Existing SD pointers | 2 present | ✓ (naming inconsistency found) |
| Existing session_b_findings | 0 | ✓ (clean) |
| Phase2 flags | 1 — already rejected in Stage 1 | ✓ (resolved) |
| Catalogue master questions | 194 | ✓ |
| Registry-specific catalogue questions | 0 | ⚠ — noted IG-6 |
| Set-aside verses with reasons | 35/40 have reasons; 5 NULL | Minor |
| Stage 1 Completion Record | Not in extract — separate document | ⚠ — noted IG-1 |

### Key Data Facts

**Term population:**
- 13 active OWNER terms: G2842 (koinōnia), G2844 (koinōnos), + 11 Hebrew ח-ב-ר root terms
- 2 deleted terms: H2269 (cha.var), H2275H (chev.ron/Hebron) — both correctly excluded
- H2275H had 57 span-filter-deleted verse records — correctly handled in Stage 1

**Verse corpus:**
- 88 total active verse records across 13 terms
- 20 anchor verses across 19 groups
- 40 set-aside verses — largest category: `physical_only` (25), meaning the tabernacle joining vocabulary was correctly excluded

**Terms with no groups (4 terms):**
H2271 (chab.bar, 1 occ), H2279 (cho.ve.ret, 4 occ), H4225 (mach.be.ret, 8 occ), H4226 (me.chab.be.rah, 2 occ).
All four have their entire verse corpus set aside (`physical_only` or `no_inner_being`). These are the tabernacle bracket/ring vocabulary. No inner-being groups formed — correct Verse Context outcome, not a data gap.

---

## Part 2 — Instruction Gaps Found and Corrections Applied

Ten instruction gaps (IG) identified during the dry run. All applied to the instruction as corrections.

| Code | Where | Issue | Fix applied |
|------|-------|-------|-------------|
| IG-1 | What to Attach + S2 + S3 | Stage 1 Completion Record not specified as named attachment; S3 required unnecessary CC check when `session_b_status` field is sufficient | (a) What to Attach: named the Completion Record explicitly with filename pattern and stop condition. (b) S2: added stop if not present. (c) S3: replaced CC check with `session_b_status = 'Pre-Analysis Complete'` check — no CC required |
| IG-2 | Unit 2 | No fast-path when zero XREF terms — instruction proceeds as if they exist | Added: if `active_xref_term_count = 0`: record and proceed immediately |
| IG-3 | Unit 3 | No guidance when `lsj_parse = NULL` for Greek OWNER terms — both G2842 and G2844 lack LSJ data | Added: note as data gap, proceed from `step_search_gloss` and `short_def_mounce` |
| IG-4 | Unit 3 | No guidance when `meaning_parse.senses = 0` and `meaning = NULL` — all 13 terms have empty structured meaning data | Added: note as data gap, proceed from gloss fields and verse evidence |
| IG-5 | Unit 5 | No guidance when correlation signals are entirely absent (`ranked_pairs: 0`) — fellowship has zero ranked pairs | Added: if all signal counts = 0, record the absence and note that cross-registry connections will be identified through verse evidence |
| IG-6 | Stage 2b | No guidance when `catalogue_questions_registry = 0` — fellowship has no word-specific questions yet indexed | Added: if zero registry-specific questions, skip Pass A entirely and proceed to Pass B (universal questions) |
| IG-7 | Unit 7 | No handling for active OWNER terms with zero groups because all verses were set aside | Added: explicit handling before set-aside verse review — record the term, its set-aside reasons, and note it contributes root vocabulary context only |
| IG-8 | Unit 6 | No check for SD pointer naming inconsistency — fellowship has `DIM-62-SD001` (should be `062-SD001`) | Added: naming convention check; inconsistency goes to patch accumulator as Path 1 correction |
| IG-9 | — | Not an instruction gap — analytical observation about `dominant_subject = HUMAN` on all groups including divine-human correspondence groups. Recorded in Part 3. | No fix needed |
| IG-10 | Session start S0 (Readiness) | Version increment pattern used period notation `v[n.1]` which is ambiguous in filenames | Clarified with example: `v1 → v1.1` becomes `wa-062-fellowship-sessionb-observations-v1.1-20260416.md` |

---

## Part 3 — Substantive Analytical Observations from the Data

These are the analytical observations produced during the dry run. They constitute the start of the Stage 2a observations log for fellowship and will carry forward into the live Stage 2a session.

---

### Unit 1 — Registry Overview Observations

**OBS-001:** Fellowship entered the programme as a `Missing Inner Being Words` addition — not in the original source list. This matters: the vocabulary was identified by programme gap-finding rather than systematic extraction, which may mean the Hebrew vocabulary is broader than inner-being relevance strictly warrants. The large set-aside corpus (40 verses) relative to the active corpus (88 verse records) is consistent with this — a significant portion of the vocabulary is physically grounded.

**OBS-002:** Six dimensions are assigned across 19 groups: Relational Disposition, Moral Character, Transformation, Divine-Human Correspondence, Emotion — Positive, Cognition. The vocabulary reaches further than might be expected for "fellowship" — Transformation (disciplinary wound, restored oneness) and Cognition (joining words in speech) are both present. This breadth is a signal worth interrogating in Stage 2a: does the ח-ב-ר root carry inner-being content beyond the relational cluster, or does the analysis expose the edge of what belongs in this registry?

---

### Unit 2 — XREF Terms
Zero XREF terms. No borrowings from other registries.

---

### Unit 3 — OWNER Terms: Lexical Foundation

**OBS-003: The two-corpus structure is the primary analytical fact about fellowship.**
The registry has two completely distinct vocabulary families with no lexical overlap and no shared verse corpus:
- **Greek: KOINŌN root** (G2842 koinōnia, G2844 koinōnos). Mounce: "fellowship, the close association between persons"; "partner, participant." Root: KOINŌN — participant. Related: G2839 (koinos — common/shared). 21 + 15 = 36 occurrences. NT only.
- **Hebrew: ח-ב-ר root** (H2266 cha.var and 10 derivative terms). Step_search_gloss: "to unite" (H2266), "companion" (H2270), "wound" (H2250), "spell/charm" (H2267), "joining" (H4225), etc. 11 terms, all Hebrew, all physical/relational root. LSJ and full meaning parse absent for all — meaning work depends entirely on gloss and verse evidence.

These are not just different languages — they are semantically divergent. The Greek vocabulary is about participation and shared life. The Hebrew vocabulary is about physical joining (tabernacle brackets), relational companionship (cha.ver — companion), forbidden alliance (cha.var to idols), and disciplinary wounding (chab.bu.rah). The word "fellowship" in the registry title is entirely a Greek concept. The Hebrew root enters through Verse Context grouping under themes of inner-being alliance, companionship, and moral alignment — but the etymological grounding is physical union.

**OBS-004: Hebrew meaning data is almost entirely absent from the extract.** All 11 Hebrew terms have: `meaning = NULL`, `meaning_numbered = NULL`, `lsj_parse = NULL`, `meaning_parse.senses = 0`. Root family entries: 0 for all Hebrew terms. The only lexical data available is `step_search_gloss` and `word_analysis_gloss`. All Hebrew related_words entries point to neighbours in the ח-ב-ר cluster (H2249 Habor, H2248 crime) — not to cross-registry vocabulary. **The Hebrew meaning work in Stage 2a depends entirely on verse evidence, not on lexical data in the extract.** This is a data gap that the programme should note for future extraction refinement.

**OBS-005: Greek meaning data is thin but usable.** G2842 Mounce: "fellowship, the close association between persons, sharing, participation"; G2844 Mounce: "partner, participant, one who joins in with." Root: KOINŌN. G2844 related words include G2839/G2839H (koinos — common/shared/profane). The koinōn- root carries both the positive sense (shared life, participation) and the neutral/negative sense (common = unclean in Jewish thought). This polarity is analytically significant and should be investigated in anchor verse reading.

**OBS-006: Four terms contribute root vocabulary only (no inner-being groups).** H2271 (chab.bar — associate), H2279 (cho.ve.ret — set), H4225 (mach.be.ret — joining bracket), H4226 (me.chab.be.rah — clamp). Their verse corpora are entirely physical or structural — tabernacle construction, joining rings, brackets. They confirm the physical grounding of the ח-ב-ר root but carry no inner-being content. Their presence in the registry confirms the breadth of the root; their exclusion from the active analysis is correct.

---

### Unit 4 — Group Landscape

**OBS-007: All 19 groups have `dominant_subject = HUMAN`.** This is notable. Two groups are dimensioned `Divine-Human Correspondence` (group 873-001 for G2842 and group 5367-001 for G2844) — yet even these groups classify the human as dominant subject. The reading is: the human is the one who participates; God or Christ is the object or ground of participation, not the grammatical subject. Verse 1 Jo 1:3 ("fellowship with us; and indeed our fellowship is with the Father and with his Son") and Phil 3:10 ("that I may know him and the power of his resurrection, and may share his sufferings") both confirm this — the human does the participating. The divine is not absent but is the destination, not the actor.

**OBS-008: Two analytical axes are visible from the group landscape before reading a single verse:**
- **Axis 1 — Vertical:** inner-spiritual participation upward toward the divine (873-001, 5367-001) — koinōnia with God/Christ/Spirit; divine nature; suffering
- **Axis 2 — Horizontal:** relational disposition toward other humans (873-002, 7565-001, 7566-001, 7566-002, 7566-003, 7576-001) — companionship, moral alignment, covenantal bond

**OBS-009: The Hebrew groups add a third axis not visible in the Greek vocabulary alone:**
- **Axis 3 — Moral joining:** the cha.var root applied to forbidden alliance (7565-001 — Ephraim joined to idols), occult practice (7565-002, 7569-001 — charming/enchanting), and moral character marked indelibly (7573-001 — leopard cannot change its spots). This is the dark side of joining — alliance as spiritual contamination.

**OBS-010: The Transformation dimension is unexpected.** Two groups (7566-004 — Ezekiel's dry bones becoming one; 7568-001 and 7568-002 — wounds as moral purification and redemptive healing) carry a Transformation dimension. The ח-ב-ר root applied to transformation: joining that changes something fundamentally. Isa 53:5 in group 7568-002 places the disciplinary wound (chab.bu.rah) of the suffering servant as the instrument of inner healing. This is the word for "stripes" in the classic messianic passage. Stage 2a should examine whether this constitutes a genuine Transformation dimension in inner-being terms or whether the transformative work is external to the person.

---

### Unit 5 — Correlation Signals

**OBS-011: Zero ranked correlation signals.** Fellowship has no programme-wide correlation pairs, no xref sharing, no verse co-occurrence data. This reflects the registry's small active verse corpus (88 records) and its late entry into the programme. Three shared anchor verses exist: 2Pe 1:4 (with yielding/Reg 180), and two others identified in the data. Stage 2a cross-registry observations will come entirely from direct verse reading, not from signal data.

**SD POINTER: C17 internal — koinōnia and its cluster.** Fellowship is in C17 (covenantal cluster) with mercy, love, compassion, grace, forgiveness, peace. The absence of correlation signals is a programme gap, not an analytical gap — it means other C17 words haven't had Session B run against the same verse corpus yet. When they do, xref sharing with koinōnia terms will likely appear.

---

### Unit 6 — Existing SD Pointers and Findings

**OBS-012: Two existing SD pointers, one with naming inconsistency.**
- `DIM-062-SD001`: "Scripture's use of physical and structural joining vocabulary (chavar root family) is entirely set aside as non-inner-being — SD pointer for Session D on whether the physical joining image illuminates the inner-being meaning" — HIGH priority. Correctly scoped: the physical corpus is relevant to Session D precisely because the root's concrete referent (joining, binding) shapes the metaphorical inner-being usage.
- `DIM-62-SD001`: "Reg 62 (fellowship) has four groups that together trace three axes of koinōnia: divine-human participation, horizontal communal belonging, moral alignment toward/away from good." — Naming uses `62` not `062`. **Path 1 patch item:** correct to `DIM-062-SD002`.

**OBS-013: Zero existing session_b_findings.** Clean slate for Stage 2b.

---

### Unit 7 — Anchor Verse Reading (selected observations)

**OBS-014: 1 Jo 1:3 (873-001 — Divine-Human Correspondence)**
"that which we have seen and heard we proclaim also to you, so that you too may have fellowship with us; and indeed our fellowship is with the Father and with his Son Jesus Christ."
Fellowship (koinōnia) here has two layers simultaneously: horizontal (with us — the apostolic community) and vertical (with the Father and the Son). The horizontal is the entry point; the vertical is the substance. This is the classic koinōnia structure: one does not have fellowship with God apart from fellowship with the community that bears witness to him. This is an inner-being characteristic with an irreducibly communal structure — it cannot be held privately.
Cross-registry: (1) This verse pairs koinōnia with the proclamation of what was seen and heard — a cognitive and volitional act precedes the relational union. Possible SD pointer: does fellowship require a prior cognitive act (recognition, proclamation) that links it to registry 100 (knowledge)? (2) "our fellowship is with the Father" — divine-human correspondence; parallels with love (registry 103, 1 Jo 4).

**OBS-015: Phil 3:10 (873-001 — Divine-Human Correspondence)**
"that I may know him and the power of his resurrection, and may share his sufferings, becoming like him in his death."
Koinōnia here is koinōnia of sufferings — participation in. The inner-being content is volitional ("that I may") and transformative (becoming like him in death). Fellowship is not passive reception but active participation in the pattern of Christ's life. The Transformation dimension connects here to the Hebrew axis OBS-010 (wounds as instrument of inner purification). Cross-registry: this verse pairs koinōnia directly with knowing (cognitive — Reg 100) and becoming like (transformation, likeness — possibly Reg 209).

**OBS-016: Psa 119:63 (7566-001 — Relational Disposition)**
"I am a companion of all who fear you, of those who keep your precepts."
cha.ver (companion) as chosen moral alignment. The companionship here is defined by a shared inner orientation — fear of God — not by proximity or preference. This is the Hebrew equivalent of what koinōnia does in Greek: relational bond grounded in something shared at a deeper level. The alignment is volitional ("I am a companion of...") and explicitly moral (fear of God, keeping precepts).
Cross-registry: fear of God (Reg 61) and fellowship — a notable co-occurrence. Does the fear of God generate or enable this kind of companionship?

**OBS-017: Isa 53:5 (7568-002 — Transformation)**
"he was pierced for our transgressions; he was crushed for our iniquities; upon him was the chastisement that brought us peace, and with his stripes (chab.bu.rah) we are healed."
chab.bu.rah — wound/stripe — is used here for the suffering servant's stripes as the instrument of inner healing. The word is in this registry because Verse Context found inner-being content in the healing result. The wound itself is physical; the healing is inner (the stripes → healing is a substitutionary inner transaction). This is the most theologically dense use of any term in this registry.
Cross-registry: This verse carries the word for peace (shalom — Reg 117), healing, and the servant's suffering. Multiple SD pointer candidates.

**OBS-018: Hos 4:17 (7565-001 — Relational Disposition, Moral Character)**
"Ephraim is joined to idols; leave him alone."
cha.var — joined to — used for spiritual apostasy. The joining is inner and volitional — Ephraim has chosen alliance with idols, and the result is abandonment ("leave him alone"). The inner-being content: the capacity for joining can be directed toward the wrong object, producing a state of irretrievable alliance. This is the negative of koinōnia — not fellowship with God but with what opposes God.
Cross-registry: strong pairing with idolatry and its inner-being consequences; relevant to the moral cluster.

**OBS-019: Mal 2:14 (7576-001 — Relational Disposition)**
"Because the Lord was witness between you and the wife of your youth, to whom you have been faithless, though she is your companion (cha.ve.ret) and your wife by covenant."
cha.ve.ret — female form, companion — used for the marriage covenant. Fellowship/companionship as the inner dimension of covenantal fidelity. The unfaithfulness is not just legal breach but inner betrayal of a companion. This is the closest the Hebrew vocabulary comes to the Greek koinōnia's sense of deep shared life.
Cross-registry: love (Reg 103 — covenant love/chesed), faithfulness (Reg 60), covenant (Reg 34).

**OBS-020: Eze 37:19 (7566-004 — Transformation)**
"Behold, I am about to take the stick of Joseph... and join it with the stick of Judah, and make them one stick, that they may be one in my hand."
cha.var — to unite/join — used for the divine act of national reunification. The joining is physical (sticks) but the inner-being content is the eschatological restoration of divided Israel into one people with one inner life before God. The Transformation dimension is correct: this is joining that creates a new corporate inner-being reality.
Cross-registry: the restored inner-being oneness of a people — linked to the corporate dimension of the programme's governing question.

---

### Unit 8 — Thin-Evidence Phase2 Flags

One phase2 flag: G2842 SEMANTIC_RANGE_BREADTH, already rejected in Stage 1 with full reasoning (`delete_flagged = 1`, `obsolete_reason` populated). No active thin-evidence flags. Unit 8 complete immediately.

---

### Unit 9 — Existing Findings

Zero existing session_b_findings. Unit 9 complete immediately.

---

## Part 4 — Stage 2a Sign-Off Assessment

Running the sign-off checklist against the dry run:

| Unit | Status | Notes |
|------|--------|-------|
| 1 Registry overview | COMPLETE | 2 observations |
| 2 XREF terms | COMPLETE | Zero — fast-path |
| 3 OWNER terms lexical | COMPLETE | 4 observations; data gaps noted |
| 4 Group landscape | COMPLETE | 4 observations; two axes identified |
| 5 Correlation signals | COMPLETE | Zero signals; SD pointer noted |
| 6 Existing SD pointers and findings | COMPLETE | 2 observations; naming inconsistency identified |
| 7 Anchor verse reading | COMPLETE (20 verses) | 7 observations; 4 SD pointer candidates |
| 8 Thin-evidence flags | COMPLETE | Zero active flags |
| 9 Existing findings | COMPLETE | Zero findings |

**Path 3 notes from Stage 1:** None present in the extract — the Stage 1 observations log was not attached to this run. This confirms IG-1: the Completion Record must be attached for Stage 2a to process Path 3 items.

**SD Pointer Accumulator (from this dry run):**

| Seq | Target | Evidence |
|-----|--------|----------|
| SD-DR-001 | Reg 100 (knowledge) | 1 Jo 1:3 — proclamation precedes fellowship; Phil 3:10 — "that I may know him" paired with fellowship in suffering |
| SD-DR-002 | Reg 117 (peace) | Isa 53:5 — chastisement that brought peace; fellowship of suffering produces peace |
| SD-DR-003 | Reg 61 (fear) | Psa 119:63 — companion of all who fear you; fear of God generates fellowship |
| SD-DR-004 | C17 internal | koinōnia connections with mercy, love, compassion not yet signalled due to programme state — flag for Session D when signals populate |

---

## Part 5 — Summary Findings for Instruction Update

### What worked well

- Reading sequence (Units 1–9) is correct and complete
- The group landscape read before anchor verses (Unit 4 before Unit 7) is essential — it set the axes that made the verse reading coherent
- Correlation signals read before verses (Unit 5 before Unit 7) confirmed the absence of signals before the verse reading began — correct orientation
- The five cross-registry questions fired naturally during anchor verse reading — no forcing required

### What needed fixing (all applied)

Ten instruction gaps identified and corrected. The most significant:
- **IG-1 (S3):** `session_b_status` in the extract is sufficient confirmation — no CC check needed
- **IG-5:** Zero correlation signals is a legitimate state — the instruction must handle it without confusion
- **IG-7:** Terms with all verses set aside and no groups need an explicit handling path

### One remaining design question

**The Stage 1 Completion Record as a separate input.** In this dry run the Completion Record was not available as a separate document — it exists in the Stage 1 observations log from the other chat. The instruction now specifies it must be attached, but the programme needs a convention for how it is extracted and transferred. The natural approach: the Stage 1 session log (produced at Stage 1 close) should include a copy of the Completion Record as a section, making it portable. This is a programme convention to establish, not an instruction gap.

---

*End of wa-062-fellowship-stage2a-dryrun-v1-20260416.md*
*Instruction corrections applied to wa-sessionb-analysis-output-v1-20260416.md*
*Substantive observations (OBS-001 through OBS-020) form the seed content for the live Stage 2a observations log*
