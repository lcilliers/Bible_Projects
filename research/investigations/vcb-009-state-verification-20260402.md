# VCB-009 Database State Verification Report

**Date:** 2026-04-02
**Instruction:** wa-vcb-009-claudecode-instruction-v1-20260402.md
**Governing:** WA-VerseContext-Instruction-v2.3-20260401.md

---

## Step 1: Terms with no verse_context records (Registries 73–89)

**36 terms found** with active verse records but no verse_context records.

| Strong's | Transliteration | Gloss | mti_id | Registry | Verses |
|----------|----------------|-------|--------|----------|--------|
| G0157 | aitiama | charge | 2425 | 73-guilt | 1 |
| G4893 | suneidesis | conscience | 53 | 73-guilt | 29 |
| G4642 | skleros | hard | 1818 | 74-hardness | 5 |
| G4644 | sklerotrachelos | stiff-necked | 1819 | 74-hardness | 1 |
| G4645 | skleruno | to harden | 1817 | 74-hardness | 6 |
| G0037 | hagiazo | to sanctify | 2280 | 76-holiness | 25 |
| G0040H | hagios | holy: saint | 2279 | 76-holiness | 52 |
| H6665 | tsidqah | righteousness | 3598 | 77-honesty | 1 |
| G3784 | ofeilo | to owe | 2606 | 78-hope | 35 |
| G4253 | pro | before | 2629 | 78-hope | 48 |
| H3684 | kesil | fool | 2622 | 78-hope | 63 |
| H3685H | kesil | constellation | 2625 | 78-hope | 1 |
| H3687 | kesilut | stupidity | 2626 | 78-hope | 1 |
| H4723A | qoveh | Kue | 2607 | 78-hope | 2 |
| H4723C | miqveh | collection | 2608 | 78-hope | 3 |
| H5033 | nevekh | spring | 2618 | 78-hope | 1 |
| H6957A | qav | cord | 2614 | 78-hope | 2 |
| H6957B | qav | line | 2613 | 78-hope | 13 |
| H6978 | qavqav | might | 2615 | 78-hope | 2 |
| H7954 | sheleh | be safe | 2633 | 78-hope | 1 |
| H8615A | tiqvah | cord | 2612 | 78-hope | 2 |
| H1530G | gal | heap | 4148 | 83-idolatry | 15 |
| H1530H | gal | heap: wave | 4147 | 83-idolatry | 16 |
| H1534 | galgal | wheel | 4150 | 83-idolatry | 11 |
| H1536 | gilgal | wheel | 4158 | 83-idolatry | 1 |
| H1538 | gulgolet | head | 4149 | 83-idolatry | 12 |
| H1543 | gullah | bowl | 4152 | 83-idolatry | 9 |
| H1550A | galil | turned | 4159 | 83-idolatry | 1 |
| H1550B | galil | circuit | 4155 | 83-idolatry | 2 |
| H1552 | gelilah | border | 4153 | 83-idolatry | 5 |
| H1556 | galal | to roll | 4144 | 83-idolatry | 18 |
| H1557 | galal | dung | 4156 | 83-idolatry | 2 |
| H1561 | gel | dung | 4154 | 83-idolatry | 3 |
| H4039 | megillah | scroll | 4146 | 83-idolatry | 19 |
| H7914 | sekhiyyah | craft | 1829 | 85-imagination | 1 |
| H7915 | sakkin | knife | 1830 | 85-imagination | 1 |

---

## Step 2: Cross-reference against confirmed flags

All 6 confirmed all-verses-fail flags **already have verse_context records in the database** — they were handled by the VCB-009 patch. No action needed for these:

| Flag | Strong's | mti_id | VC records | Status |
|------|----------|--------|-----------|--------|
| R74-001 | H5796 | 5510 | 1 | Already handled |
| R74-002 | H5798G | 5507 | 8 | Already handled |
| R74-003 | H5808 | 5508 | 2 | Already handled |
| R74-004 | H5822 | 5509 | 2 | Already handled |
| R75-001 | H7850 | 5519 | 1 | Already handled |
| R76-001 | G0039G | 909 | 9 | Already handled |

---

## Step 3: Findings

**All 36 unclassified terms are OUTSIDE the confirmed flag list.** These are unexpected gaps — not the flagged all-verses-fail terms.

**Critical finding: 5 registries marked Complete have unclassified OWNER terms:**

| Registry | Status | Unclassified terms | Total unclassified verses |
|----------|--------|--------------------|--------------------------|
| 74-hardness | **Complete** | 3 | 12 |
| 76-holiness | **Complete** | 2 | 77 |
| 77-honesty | **Complete** | 1 | 1 |
| 78-hope | **Complete** | 13 | 174 |
| 83-idolatry | **Complete** | 13 | 114 |
| 85-imagination | **Complete** | 2 | 2 |
| 73-guilt | In Progress | 2 | 30 |

The 5 Complete registries were advanced prematurely. Their completion check passed because these terms' OWNER ti records may not have been detected by the completion query.

---

## Recommended Action

Per Step 4: **Do not apply supplemental inserts for the 36 additional terms without Claude AI review.** These are not confirmed all-verses-fail — they are terms that were missed from the VCB-009 batch or patch entirely.

**Immediate actions required:**
1. **Reverse verse_context_status** for the 5 affected Complete registries back to `In Progress`
2. Report the 36 unclassified terms to Claude AI for classification
3. Investigate why the completion check did not catch these terms

---

*Produced 2026-04-02 by Claude Code per wa-vcb-009-claudecode-instruction-v1-20260402.md*
