# wa-vcb-006-anchor-resolution-v1-20260331.md

**Framework B — Soul Word Analysis Programme**
**VCB-006 Patch Construction — Anchor Resolution Report**
**Version:** v1 | **Date:** 2026-03-31
**Governing instruction:** WA-VerseContext-Instruction-v2.0-20260331.md
**Input files:** wa-vcb-006-term-observations-v1-20260331.md | wa-vcb-006-extract-20260331.json

---

## Summary

Pre-submission validation (Section 7.6) identified **45 verse_record_id mismatches** across **16 terms**. All mismatches have been diagnosed. No patch operations have been written.

| Category | Count | Description |
|---|---|---|
| OK — no correction needed | 1,144 | Verified against extract |
| NOT_IN_EXTRACT | 18 | Ref not in batch for any term — likely from prior batch's extract |
| CROSS_TERM | 25 | Ref found in extract but under a different mti_term_id |
| AMBIGUOUS | 2 | Ref found under multiple terms in extract |

**R4 anchor integrity risks:** 8 terms have no valid anchor after dropping mismatched refs — alternative anchor promotion proposed for each. 2 groups have no valid verses at all — researcher decision required.

---

## Resolution by Term

### mti_id=75 — H0205H (ʾāven) — evil: trouble — Registry 051

**Group 75-001:** *Iniquity and wickedness as inner moral quality — conceived, spoken, enacted*

| Ref | Obs vid | Status | Proposed action |
|---|---|---|---|
| Psa 7:14 | 12383 | NOT_IN_EXTRACT | DROP |
| Job 4:8 | 12382 | NOT_IN_EXTRACT | DROP |
| Psa 10:7 | 12384 | NOT_IN_EXTRACT | DROP |
| Psa 55:3 | 12385 | CROSS_TERM → mti_id=5157 (H6125) | DROP from this term |

**R4 RISK:** After drops, no valid anchor remains in 75-001.
**Proposed promotion:** Pro 22:8 vid=157152 → anchor
> *"Whoever sows injustice will reap calamity, and the rod of his fury will fail."*
**Valid remaining related:** Pro 22:8 (→ anchor if approved), Deu 26:14 vid=157145

---

### mti_id=92 — H0926 (bāhal) — to dismay — Registry 051

**Group 92-001:** *Dismay and terror as overwhelming inner affective state*

| Ref | Obs vid | Status | Proposed action |
|---|---|---|---|
| Zec 12:4 | 12437 | NOT_IN_EXTRACT | DROP (related only — R4 not affected) |

**R4 status:** Anchor Psa 6:3 vid=12434 is valid. No further action needed.

---

### mti_id=116 — H2201 (zeʿāqāh) — outcry — Registry 051

**Group 116-001:** *Outcry as expression of suffering, affliction and plea for help*

| Ref | Obs vid | Status | Proposed action |
|---|---|---|---|
| Exo 3:7 | 12388 | CROSS_TERM → mti_id=173 (H5065) | DROP from this term |
| Gen 18:21 | 12387 | NOT_IN_EXTRACT | DROP |
| Jer 14:2 | 157402 | CROSS_TERM → mti_id=200 (H6682) | DROP from this term |

**Group 116-002:** *Outcry as communal lamentation — grief and mourning expressed publicly*

| Ref | Obs vid | Status | Proposed action |
|---|---|---|---|
| Jer 48:5 | 12390 | NOT_IN_EXTRACT | DROP (related only — R4 not affected) |

**R4 RISK (116-001):** No valid anchor after dropping Exo 3:7.
**Proposed promotion:** Gen 18:20 vid=157315 → anchor
> *"Then the Lord said, 'Because the outcry against Sodom and Gomorrah is great and their sin is very grave…'"*
**Note:** Gen 18:20 is less direct as an anchor than Exo 3:7 would have been — it names outcry heard by God, not a personal inner expression of suffering. Researcher may wish to consider Neh 5:6 vid=12389 or Est 4:1 vid=157312 as alternatives.

Group 116-002 anchor: Isa 15:5 — valid. No further action.

---

### mti_id=147 — H3511 (keʾev) — pain — Registry 051

**Group 147-001:** *Pain as experienced inner suffering — unassuaged, incurable, of the heart*

| Ref | Obs vid | Status | Proposed action |
|---|---|---|---|
| Psa 69:26 | 12392 | NOT_IN_EXTRACT | DROP (related only — R4 not affected) |

**R4 status:** Anchor Isa 17:11 vid=157406 is valid. No further action needed.

---

### mti_id=200 — H6682 (ṣevāḥāh) — outcry — Registry 051

**Group 200-001:** *Outcry as expression of inner pain, anguish and distress — from heart to voice*

| Ref | Obs vid | Status | Proposed action |
|---|---|---|---|
| Isa 65:14 | 12394 | CROSS_TERM → mti_id=147 (H3511) | DROP from this term |
| Jer 4:31 | 12395 | NOT_IN_EXTRACT | DROP |

**R4 RISK:** No valid anchor after drops.
**Proposed promotion:** Psa 144:14 vid=157404 → anchor
> *"…may there be no cry of distress in our streets!"*
**Note:** Psa 144:14 is collective/negated — a weaker anchor than a positive personal outcry. Researcher may wish to consider Isa 24:11 vid=157401 (*"There is an outcry in the streets over the wine"*) or Jer 46:12 vid=157403. The term H6682 has only 4 verses total; all four should be reviewed for anchor suitability.

---

### mti_id=204 — H6696A (ṣûr) — to confine — Registry 051

**Group 204-001:** *Being hemmed in, distressed and confined — the experience of inner constraint before God or suffering*

| Ref | Obs vid | Status | Proposed action |
|---|---|---|---|
| 1Sa 28:15 | 156989 | CROSS_TERM → mti_id=215 (H6887B) | DROP from this term |
| 2Sa 1:26 | 156993 | CROSS_TERM → mti_id=215 (H6887B) | DROP from this term |
| 2Ch 28:22 | 156991 | CROSS_TERM → mti_id=215 (H6887B) | DROP from this term |
| 2Ch 33:12 | 156992 | CROSS_TERM → mti_id=215 (H6887B) | DROP from this term |
| Psa 31:9 | 157006 | CROSS_TERM → mti_id=215 (H6887B) | DROP from this term |
| Psa 69:17 | 157007 | CROSS_TERM → mti_id=215 (H6887B) | DROP from this term |
| Jer 10:18 | 157001 | CROSS_TERM → mti_id=215 (H6887B) | DROP from this term |
| Zep 1:17 | 157008 | CROSS_TERM → mti_id=215 (H6887B) | DROP from this term |

**R4 status for 204-001:** Anchor Psa 139:5 vid=156931 is valid. Anchor intact.

**Group 204-002:** *Iniquity bound up — stored guilt as inner moral condition*

| Ref | Obs vid | Status | Proposed action |
|---|---|---|---|
| Hos 13:12 | 156997 | CROSS_TERM → mti_id=215 (H6887B) | DROP from this term |

**⚠ R4 RISK — GROUP CANNOT BE PATCHED:** After dropping Hos 13:12, group 204-002 has no valid verses at all. Hos 13:12 belongs to H6887B (to constrain), not H6696A (to confine).

**Context note:** The observations narrative for H6696A describes Hos 13:12 as passing the filter ("iniquity bound up — metaphor for stored guilt; inner moral condition — Pass"). However, Hos 13:12 belongs to H6887B's verse set in this extract, not H6696A's. The underlying question is whether H6696A has a verse instantiating the "stored guilt" sense. H6696A's actual 32-verse set does not include Hos 13:12.

**Decision required:** Dissolve group 204-002 (no valid verses for this term), or identify an alternative verse from H6696A's actual verse set (vid range 12448–156932) that carries the bound-iniquity sense.

---

### mti_id=205 — H6696B (ṣûr) — to provoke — Registry 051

**Group 205-001:** *Provocation and harassment as hostile inner-driven action — stirring up enmity and opposition*

| Ref | Obs vid | Status | Proposed action |
|---|---|---|---|
| Deu 2:9 | 12452 | NOT_IN_EXTRACT | DROP (related only — R4 not affected) |

**R4 status:** Anchor Deu 14:25 vid=158055 is valid per extract. No further action needed.

---

### mti_id=208 — H6862A (ṣar) — narrow — Registry 051

**Group 208-001:** *Narrowness and constraint as inner-bearing experience of distress and limitation*

| Ref | Obs vid | Status | Proposed action |
|---|---|---|---|
| 1Sa 13:6 | 12397 | CROSS_TERM → mti_id=173 (H5065) | DROP from this term |
| Job 36:16 | 12398 | NOT_IN_EXTRACT | DROP |

**R4 status:** Anchor Num 22:26 vid=12396 is valid. No further action needed.

---

### mti_id=214 — H6869C (ṣārāh) — vexer — Registry 051

**Group 214-001:** *The vexer as source of inner distress — provocation grieving the spirit*

| Ref | Obs vid | Status | Proposed action |
|---|---|---|---|
| 1Sa 1:6 | 12453 | NOT_IN_EXTRACT | DROP |

**R4 RISK:** No valid anchor after drop. This term has only 2 verses: Psa 9:9 vid=157063 and Psa 10:1 vid=157062.
**Proposed promotion:** Psa 9:9 vid=157063 → anchor
> *"The Lord is a stronghold for the oppressed, a stronghold in times of trouble."*
**Note:** Psa 9:9 names the vexer-condition (oppressed, times of trouble) as the context for divine shelter — inner-being relevant as the condition needing refuge. Psa 10:1 names divine hiddenness in times of trouble. Both are usable; Psa 9:9 is slightly more direct.

---

### mti_id=215 — H6887B (ṣārar) — to constrain — Registry 051

**Group 215-001:** *Being in distress, constrained and afflicted — inner experience of pressure and suffering*

| Ref | Obs vid | Status | Proposed action |
|---|---|---|---|
| Num 33:55 | 12454 | CROSS_TERM → mti_id=217 (H6887D) | DROP from this term |
| Psa 129:1 | 12455 | CROSS_TERM → mti_id=217 (H6887D) | DROP from this term |

**R4 status:** Anchor 1Sa 25:29 vid=156988 is valid. No further action needed.

---

### mti_id=216 — H6887C (ṣārar) — to distress — Registry 051

**Group 216-001:** *Distress as acute inner condition — the moment of extremity, terror, and desperate appeal to God*

| Ref | Obs vid | Status | Proposed action |
|---|---|---|---|
| 2Sa 24:14 | 12457 | NOT_IN_EXTRACT | DROP |

**R4 RISK:** No valid anchor after drop. This term has 4 verses: Psa 59:16 vid=157045, Psa 102:2 vid=157044, Jer 48:41 vid=157042, Jer 49:22 vid=157043.
**Proposed promotion:** Psa 59:16 vid=157045 → anchor
> *"But I will sing of your strength; I will sing aloud of your steadfast love in the morning. For you have been to me a fortress and a refuge in the day of my distress."*
**Note:** Psa 59:16 is a strong anchor — explicit "day of my distress" with inner response (singing, trust). Well suited.

---

### mti_id=218 — H6887E (ṣārar) — to rival — Registry 051

**Group 218-001:** *Rivalry as relational dynamic producing inner jealousy and distress*

| Ref | Obs vid | Status | Proposed action |
|---|---|---|---|
| 1Sa 1:6 | 12460 | NOT_IN_EXTRACT | DROP |

**R4 RISK:** No valid anchor after drop. This term has only 1 verse: Lev 18:18 vid=157064.
**Proposed promotion:** Lev 18:18 vid=157064 → anchor
> *"And you shall not take a woman as a rival wife to her sister, uncovering her nakedness while her sister is still alive."*
**Note:** Lev 18:18 is a single-verse term. The classification notes 1Sa 1:6 as the intended anchor (Hannah's rival). That verse is not in this term's verse set. Lev 18:18 carries the structural concept of rivalry — it is the only available verse, and it must serve as anchor.

---

### mti_id=226 — H7185 (qāshāh) — to harden — Registry 051

**Group 226-001:** *Hardening of heart and stubborn will — inner moral resistance to God*

| Ref | Obs vid | Status | Proposed action |
|---|---|---|---|
| 1Sa 6:6 | 12465 | NOT_IN_EXTRACT | DROP (related only) |
| Deu 31:27 | 157870 | CROSS_TERM → mti_id=5192 (H7186) | DROP from this term |

**R4 status:** Anchor Psa 95:8 vid=157858 is valid. No further action needed.

**Group 226-002:** *Inner character of harshness and severity — expressed in speech, conduct and rule*

| Ref | Obs vid | Status | Proposed action |
|---|---|---|---|
| Eze 3:7 | 157881 | CROSS_TERM → mti_id=5192 (H7186) | DROP from this term |
| 1Sa 1:15 | 157862 | CROSS_TERM → mti_id=5192 (H7186) | DROP from this term |
| 1Sa 25:3 | 157864 | CROSS_TERM → mti_id=5192 (H7186) | DROP from this term |
| 2Sa 3:39 | 157868 | AMBIGUOUS → mti_id=5192 or mti_id=237 | DROP from this term |
| 1Ki 12:13 | 157859 | CROSS_TERM → mti_id=5192 (H7186) | DROP from this term |
| 2Ch 10:13 | 157865 | CROSS_TERM → mti_id=5192 (H7186) | DROP from this term |
| Isa 48:4 | 157889 | CROSS_TERM → mti_id=5192 (H7186) | DROP from this term |
| Eze 2:4 | 157880 | CROSS_TERM → mti_id=5192 (H7186) | DROP from this term |

**R4 RISK:** No valid anchor after drops. Valid related: 2Sa 19:43 vid=157840 only.
**Proposed promotion:** 2Sa 19:43 vid=157840 → anchor
> *"But the words of the men of Judah were fiercer than the words of the men of Israel."*
**Note:** 2Sa 19:43 names verbal fierceness as inner character expression — serviceable anchor for harshness as inner character quality, though limited in scope. The group description references harshness expressed in speech, conduct and rule — this verse covers the speech dimension. Researcher may wish to review whether other verses in H7185's actual set (vid range 12464–157858) could serve better.

**Group 226-003:** *Fierceness of love — inner intensity and consuming passion*

| Ref | Obs vid | Status | Proposed action |
|---|---|---|---|
| Song 8:6 | 157894 | AMBIGUOUS → mti_id=5192 (H7186) or mti_id=344 (H7068) | DROP from this term |

**⚠ R4 RISK — GROUP CANNOT BE PATCHED:** After dropping Song 8:6, group 226-003 has no valid verses. Song 8:6 does not appear in H7185's verse set in this extract.

**Decision required:** Dissolve group 226-003, or identify a verse from H7185's actual verse set (see list below) that carries the fierceness-of-love sense. H7185's verse set includes Isa 8:21 (distressed and hungry, enraged), Gen 49:7 (cruel anger), 2Sa 19:43 (fierceness of words) — none are obvious candidates for love's intensity.

**H7185 actual verse set (active, 28 verses):** Gen 35:16, 35:17, 49:7, Exo 7:3, 13:15, Deu 1:17, 2:30, 10:16, 15:18, 1Sa 5:7, 20:10, 25:3 [actually H7186 — already flagged], 2Sa 2:17, 19:43, 1Ki 12:4, 14:6, 2Ki 2:10, 17:14, 2Ch 10:4, 30:8, 36:13, Neh 9:16, 9:17, 9:29, Job 9:4, Pro 28:14, 29:1, Psa 60:3, Psa 95:8, Isa 8:21, 19:4, 21:2, 27:1, 27:8, 48:4 [H7186], Eze 2:4 [H7186], 3:7 [H7186], Song 8:6 [H7186/H7068].

---

### mti_id=235 — H7451A (raʿ) — bad: harmful — Registry 057

**Group 235-001:** *The harmful and destructive moral quality in persons — inner character of wickedness*

| Ref | Obs vid | Status | Proposed action |
|---|---|---|---|
| Ecc 8:11 | 156469 | CROSS_TERM → mti_id=237 (H7451I) | DROP from this term |

**R4 RISK:** No valid anchor after drop.
**Proposed promotion:** 2Sa 13:22 vid=155949 → anchor
> *"But Absalom spoke to Amnon neither good nor bad, for Absalom hated Amnon, because he had violated his sister Tamar."*
**Note:** 2Sa 13:22 is not an obviously strong anchor for the group description (harmful moral quality as inner character). The verse illustrates suppressed hatred — inner but specific. Researcher should confirm or select an alternative from H7451A's valid verse set.

---

### mti_id=237 — H7451I (raʿāh) — distress: evil — Registry 051

**Group 237-002:** *Evil as experienced suffering — distress, harm, and calamity borne by persons*

| Ref | Obs vid | Status | Proposed action |
|---|---|---|---|
| Psa 34:19 | 12413 | NOT_IN_EXTRACT | DROP (related only — R4 not affected) |
| Psa 88:3 | 12414 | NOT_IN_EXTRACT | DROP (related only — R4 not affected) |
| Jer 17:17 | 12409 | NOT_IN_EXTRACT | DROP (related only — R4 not affected) |

**R4 status:** Anchor Gen 50:20 vid=156483 is valid. No further action needed.

---

### mti_id=242 — H7878 (sîaḥ) — to muse — Registry 051

**Group 242-002:** *Complaint and lament as inner expression of distress*

| Ref | Obs vid | Status | Proposed action |
|---|---|---|---|
| Psa 142:2 | 12469 | NOT_IN_EXTRACT | DROP (related only — R4 not affected) |

**R4 status:** Anchor Job 7:11 vid=12470 is valid. No further action needed.

---

## Decisions Required — Summary

Before patch construction can proceed, the following items require researcher approval:

| # | Term | Issue | Proposed resolution |
|---|---|---|---|
| D-001 | H0205H mti_id=75 group 75-001 | No valid anchor after drops | Promote Pro 22:8 vid=157152 to anchor |
| D-002 | H2201 mti_id=116 group 116-001 | No valid anchor after drops | Promote Gen 18:20 vid=157315 to anchor — or researcher nominates alternative (Neh 5:6, Est 4:1) |
| D-003 | H6682 mti_id=200 group 200-001 | No valid anchor after drops | Promote Psa 144:14 vid=157404 to anchor — or researcher nominates alternative (Isa 24:11, Jer 46:12, Jer 4:31 outside extract) |
| D-004 | H6696A mti_id=204 group 204-002 | No valid verses in group | Dissolve group 204-002, OR identify alternative H6696A verse for bound-iniquity sense |
| D-005 | H6869C mti_id=214 group 214-001 | No valid anchor after drops | Promote Psa 9:9 vid=157063 to anchor |
| D-006 | H6887C mti_id=216 group 216-001 | No valid anchor after drops | Promote Psa 59:16 vid=157045 to anchor |
| D-007 | H6887E mti_id=218 group 218-001 | No valid anchor after drops (1-verse term) | Promote Lev 18:18 vid=157064 to anchor |
| D-008 | H7185 mti_id=226 group 226-002 | No valid anchor after drops | Promote 2Sa 19:43 vid=157840 to anchor |
| D-009 | H7185 mti_id=226 group 226-003 | No valid verses in group | Dissolve group 226-003, OR identify alternative H7185 verse for fierceness-of-love sense |
| D-010 | H7451A mti_id=235 group 235-001 | No valid anchor after drops | Promote 2Sa 13:22 vid=155949 to anchor — or researcher nominates alternative |

---

## Automatic Resolutions (no decision required)

The following are unambiguous drops — related-verse refs that do not affect R4. These will be silently applied in patch construction:

- H0926 group 92-001: drop Zec 12:4 vid=12437
- H3511 group 147-001: drop Psa 69:26 vid=12392
- H6696B group 205-001: drop Deu 2:9 vid=12452
- H6862A group 208-001: drop 1Sa 13:6 vid=12397; drop Job 36:16 vid=12398
- H6887B group 215-001: drop Num 33:55 vid=12454; drop Psa 129:1 vid=12455
- H6887B group 215-001: Hos 13:12, 1Sa 28:15, 2Sa 1:26, 2Ch 28:22, 2Ch 33:12, Psa 31:9, Psa 69:17, Jer 10:18, Zep 1:17 — these are valid H6887B vids; they will be included correctly under H6887B's classification (204 obs cross-write; H6887B anchor remains valid at 1Sa 25:29)
- H7451I group 237-002: drop Psa 34:19, Psa 88:3, Jer 17:17
- H7878 group 242-002: drop Psa 142:2 vid=12469
- H7185 group 226-001: drop 1Sa 6:6 vid=12465; drop Deu 31:27 vid=157870

---

*wa-vcb-006-anchor-resolution-v1-20260331.md | VCB-006 patch construction | Anchor resolution report | Awaiting researcher decisions D-001 through D-010 | 2026-03-31*
