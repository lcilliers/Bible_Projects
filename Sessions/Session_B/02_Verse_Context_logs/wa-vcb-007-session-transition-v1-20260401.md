# wa-vcb-007-session-transition-v1-20260401.md
**Framework B — Soul Word Analysis Programme**
**VCB-007 → VCB-008 Session Transition Document**
**Version: v1 | Date: 2026-04-01 | Produced by: Claude AI**

---

## Purpose

This document provides the complete handoff from the VCB-007 classification session to whatever comes next — whether that is the VCB-007 patch construction session (Claude Code) or the VCB-008 classification session (Claude AI). Read this document in full before beginning any subsequent session.

---

## 1. Current programme state

### VCB-007 — Classification: COMPLETE
All 74 OWNER terms across Registries 057–061 have been classified. Every verse individually inspected. Observations file finalised at v2.8. All session logs produced.

### Governing instruction — UPDATED
`WA-VerseContext-Instruction-v2.2-20260401.md` is the current governing instruction. It supersedes v2.1. **All future sessions must use v2.2.** The updated file is in outputs and must be uploaded to project files to replace v2.1.

### VCB-005 patch — NOT YET APPLIED
Five flags from VCB-005 remain outstanding. These must be resolved by Claude Code at the time VCB-005 patch is applied. The flags are embedded in the VCB-005 patch file. This pre-dates VCB-007 and is a separate pending action.

### VCB-007 patch — NOT YET CONSTRUCTED
Patch construction is a separate Claude Code session. The observations file `wa-vcb-007-term-observations-v2.8-20260401.md` is the source document.

---

## 2. VCB-007 deliverables — complete inventory

All files in `/mnt/user-data/outputs/` (upload to project or hand to Claude Code as needed):

| File | Status | Purpose |
|---|---|---|
| `wa-vcb-007-term-observations-v2.8-20260401.md` | **FINAL** | Source for patch construction |
| `wa-vcb-007-session-log-batch-complete-v8-20260401.md` | **FINAL** | Full batch completion log |
| `wa-vcb-007-session-log-reg061-complete-v7-20260401.md` | Final | Registry 061 completion log |
| `wa-vcb-007-session-log-reg060-complete-v6-20260401.md` | Final | Registry 060 completion log |
| `wa-vcb-007-session-log-reg059-complete-v5-20260401.md` | Final | Registry 059 completion log |
| `wa-vcb-007-session-log-reg058-complete-v4-20260401.md` | Final | Registry 058 completion log |
| `wa-vcb-007-session-log-reg057-complete-v3-20260401.md` | Final | Registry 057 completion log |
| `wa-vcb-007-session-log-reg057-nearcompl-v2-20260401.md` | Archived | Intermediate log |
| `wa-vcb-007-session-log-reg057-partial-v1-20260401.md` | Archived | Intermediate log |
| `WA-VerseContext-Instruction-v2_2-20260401.md` | **ACTIVE** | Governing instruction — upload to project |
| `wa-vcb-007-term-observations-v1.0` through `v2.7` | Archived | Intermediate saves — not needed |

**Critical files for the next session:**
- `wa-vcb-007-term-observations-v2.8-20260401.md` — the only file Claude Code needs for patch construction
- `wa-vcb-007-extract-20260401.json` — the extract JSON (currently in uploads; Claude Code needs this for anchor reference resolution)
- `WA-VerseContext-Instruction-v2_2-20260401.md` — must be in project files before any future session

---

## 3. Batch statistics summary

| Registry | Word | Terms | Verses | Groups | Anchors | Relevant | Set aside | Yield |
|---|---|---|---|---|---|---|---|---|
| 057 | Evil | 8 | 846 | 26 | 47 | 148 | 698 | 17% |
| 058 | Experience | 4 | 297 | 16 | 27 | 187 | 110 | 63% |
| 059 | Faith | 18 | 549 | 35 | 59 | 534 | 15 | 97% |
| 060 | Faithfulness | 1 | 242 | 7 | 14 | 124 | 118 | 51% |
| 061 | Fear | 43 | 564 | 68 | 115 | 543 | 21 | 96% |
| **TOTAL** | | **74** | **2,498** | **152** | **262** | **1,536** | **962** | **61%** |

---

## 4. Programme flags from VCB-007 — status

Both flags have been resolved by incorporation into `WA-VerseContext-Instruction-v2.2`:

| Flag | Status | Action taken |
|---|---|---|
| PF-VCB007-001 | **RESOLVED** | Section 3.5 added to instruction v2.2 |
| PF-VCB007-002 | **RESOLVED** | Section 6.2 Step 1 amended in instruction v2.2 |

No flags carried forward to VCB-008.

---

## 5. Researcher decisions from VCB-007 — status

| Decision | Status |
|---|---|
| RD-VCB007-001 — H7490 re.a all-verses-fail | **CLOSED** — confirmed and recorded |

No open researcher decisions.

---

## 6. All-verses-fail terms — VCB-007

| Term | mti_id | Verses | Basis |
|---|---|---|---|
| H1992 hem.mah | 848 | 189 | Pronoun — full inspection, no inner-being content |
| H4177 mo.rah | 280 | 3 | Homograph — razor sense, not fear sense |

Both confirmed by full individual inspection per PF-VCB007-002.

---

## 7. Next session — Option A: VCB-007 patch construction (Claude Code)

**Session type:** Claude Code — programmatic patch construction
**Governing instruction:** `WA-VerseContext-Instruction-v2.2-20260401.md`
**Patch spec:** `bible-projects-patch-spec-v1.1` (must be present in session)

**Inputs required:**
1. `wa-vcb-007-term-observations-v2.8-20260401.md` — upload to chat
2. `wa-vcb-007-extract-20260401.json` — upload to chat
3. `WA-VerseContext-Instruction-v2.2-20260401.md` — in project files or upload to chat
4. `bible-projects-patch-spec-v1.1` — must be present (owned by Claude Code)

**What Claude Code must do:**
1. Read the observations file in full
2. Build the anchor reference lookup: `mti_term_id → reference → verse_record_id`
3. For every term: verify every anchor reference resolves against the extract JSON
4. Flag any unresolvable anchors to researcher before proceeding
5. Programmatically construct all `verse_context_group` inserts and `verse_context` inserts
6. Run R1–R4 rule compliance check
7. Run coverage validation (every verse in the extract has a verse_context record)
8. Run duplicate-key check
9. Check all-verses-fail terms appear correctly as set_aside = 0 (no records or all is_relevant = 0)
10. Output: `wa-vcb-007-patch-v1-20260401.json`

**Known issues for Claude Code to verify:**
- H4172A mo.rah (mti_id 270) and H4172B mo.ra (mti_id 271) share the same verse corpus but have different verse_record_ids. Both must be patched independently using their own verse_record_ids.
- Several terms in Registries 057–061 contain verses that appear in other terms' corpora via XREF relationships. Verify no cross-term verse_record_id collisions.
- Book abbreviations in extract JSON: confirm `Mar` (not `Mark`), `Joe` (not `Joel`), `Amo` (not `Amos`), `Phili` (not `Phil`) before anchor resolution.

---

## 8. Next session — Option B: VCB-008 classification (Claude AI)

**Session type:** Claude AI — verse context classification
**Governing instruction:** `WA-VerseContext-Instruction-v2.2-20260401.md`

**Prerequisite:** VCB-007 patch must be applied by Claude Code before VCB-008 begins (so the database is current and the next batch JSON can be correctly constructed).

**Anticipated batch scope (Claude Code determines actual scope):**

| Registry | Word | OWNER terms | Active verses | Cluster |
|---|---|---|---|---|
| 062 | Fellowship | 2 | 27 | C17 |
| 063 | Foolishness | 12 | 100 | C22 |
| 064 | Forgiveness | 7 | 190 | C17 |
| 065 | Generosity | 28 | 1,096 | C08 |
| 066 | Gentleness | 7 | 93 | C08 |
| 067 | Goodness | 39 | 1,707 | C10 |
| 068 | Grace | 10 | 285 | C17 |
| 069 | Gratitude | 3 | 54 | C03 |
| 070 | Greed | 5 | 28 | C13 |
| 071 | Grief | 52 | 226 | C05 |
| 072 | Groaning | 10 | 71 | C05 |
| 073 | Guilt | 56 | 2,150 | C13 |

**Batch sizing note:** The 2,000–2,500 verse target means R067 Goodness (1,707v / 39 OWNER terms) may occupy a batch by itself, or may be combined with small adjacent registries. R073 Guilt (2,150v / 56 OWNER terms) is also large enough to form its own batch. Claude Code determines the actual scope at batch construction time.

**Analytical notes for VCB-008 — carry-forward observations:**

*R064 Forgiveness:* Expect high inner-being yield. The semantic range (sending away, releasing, covering over) is directly inner-being. G0863G (aphiemi) with 66 verses is the largest term. Look for the inner-being consequences of withholding forgiveness.

*R065 Generosity:* Registry 065 contains multiple H3027 (yad/hand) variant terms. These are anatomical terms registered for their inner-being functions — similar in character to H4310 mi in VCB-007. Apply Section 3.5 (grammatical/functional particle filter) logic: the hand passes the filter when the giving discloses an inner orientation, not when it is purely administrative or mechanical. This is the same principle as na.tan in R060.

*R067 Goodness:* Very large registry (39 OWNER terms, 1,707v). Contains many H5927 (ʿalah/to go up) and H5921 (ʿal/upon) variants alongside goodness terms. Expect significant set-aside volume for the grammatical/locative uses. Filter carefully per Section 3.5.

*R071 Grief:* 52 OWNER terms; H7451C (ra/evil-as-grief) is the largest term (151v). Note that H7451C was the term whose group code collision caused the VCB-006 patch defect — Section 6.2 Step 6 classification block integrity rules (unique group codes, SUPERSEDED marking) were added specifically to prevent recurrence. The classification block integrity rules are now explicit in v2.2 Section 6.2 Step 6.

*R073 Guilt:* 56 OWNER terms, 2,150 verses. This will likely be a large batch in its own right.

**Session startup instruction for VCB-008:**
At session start, confirm:
> "Governing instruction loaded: WA-VerseContext-Instruction-v2.2-20260401.md. Observations file starting at v1.0: wa-vcb-008-term-observations-v1.0-[date].md. Extract JSON loaded: wa-vcb-008-extract-[date].json. Ready to begin."

---

## 9. Project file update required

The following file must be uploaded to project files (replacing the previous version) before any future session:

**`WA-VerseContext-Instruction-v2_2-20260401.md`**

This is the current governing instruction. Without it in project files, new sessions will load the superseded v2.1.

---

## 10. Accumulated programme progress

| Stage | Status |
|---|---|
| VCB-001 (Registries 001–006) | Complete — patch applied |
| VCB-002 (Registries 006–018) | Complete — patch applied |
| VCB-003 (Registries 019–032) | Complete — patch applied |
| VCB-004 (Registries 032–043) | Complete — patch applied |
| VCB-005 (Registries 043–051) | Classification complete — **patch pending** (5 flags outstanding) |
| VCB-006 | Classification complete — patch status unknown |
| VCB-007 (Registries 057–061) | Classification complete — **patch pending** |
| VCB-008 onward | Not yet started |

---

*wa-vcb-007-session-transition-v1-20260401.md | VCB-007 handoff | Governing instruction: WA-VerseContext-Instruction-v2.2-20260401.md*
