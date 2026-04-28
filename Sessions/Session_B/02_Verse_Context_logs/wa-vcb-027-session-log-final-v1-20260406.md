# wa-vcb-027-session-log-final-v1-20260406

**Framework B — Soul Word Analysis Programme**
**Batch:** VCB-027 | **Session type:** Classification + Patch construction (combined)
**Date:** 2026-04-06 | **Status:** Complete — patch ready for Claude Code
**Observations file at time of this log:** wa-vcb-027-term-observations-v1.5-20260406.md

---

## Session overview

VCB-027 was initially received on 2026-04-05 with 126 terms but was returned to Claude Code after a pre-classification inspection identified 25 phantom duplicate mti_terms records. A clean revised extract was received on 2026-04-06. Classification and patch construction were completed in a single session.

**Governing instruction:** WA-VerseContext-Instruction-v2.4-20260403.md
**Previous output:** wa-vcb-027-session-log-diagnostic-v1-20260405.md (phantom issue record)

---

## Batch scope (revised extract)

- **Registries:** Reg 197 (authority) — all terms already complete; Reg 199 (dominion) — 30 terms to classify
- **Terms classified this session:** 30 (all Reg 199)
- **Verses classified:** 380
- **Terms reviewed (already complete):** 72

---

## Per-term classification table

| # | mti | Strong's | Transliteration | Gloss | Verses | Groups | Relevant | Set aside | Anchors |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 1358 | G0932 | basileia | kingdom | 88 | 5 | 64 | 25 | 5 |
| 2 | 2945 | G0933 | baseleion | palace | 1 | 0 (AVF) | 0 | 1 | 0 |
| 3 | 2946 | G0934 | basaleios | kingly | 1 | 1 | 1 | 0 | 1 |
| 4 | 2942 | G0936 | basileuō | to reign | 18 | 3 | 10 | 8 | 4 |
| 5 | 2943 | G0937 | basilikos | royal | 5 | 1 | 1 | 4 | 1 |
| 6 | 2947 | G0938G | basilissa | queen | 1 | 1 | 1 | 0 | 1 |
| 7 | 2992 | G2634 | katakurieuō | to master | 4 | 1 | 4 | 0 | 2 |
| 8 | 1357 | G2961 | kurieuō | to lord over | 7 | 2 | 6 | 1 | 3 |
| 9 | 2944 | G4821 | sumbasileuō | to reign with | 2 | 1 | 2 | 0 | 1 |
| 10 | 2979 | H1166H | ba.al | rule: to rule | 2 | 1 | 1 | 1 | 1 |
| 11 | 2980 | H1166I | ba.al | rule: to marry | 11 | 2 | 7 | 4 | 3 |
| 12 | 2981 | H1167G | ba.al | master | 31 | 1 | 5 | 26 | 1 |
| 13 | 2982 | H1167H | ba.al | master: husband | 14 | 1 | 7 | 7 | 2 |
| 14 | 2983 | H1167I | ba.al | master: men | 13 | 1 | 5 | 8 | 2 |
| 15 | 2985 | H1167J | ba.al | master: owning | 9 | 1 | 5 | 4 | 2 |
| 16 | 2984 | H1167K | ba.al | master: [master of] | 13 | 1 | 6 | 7 | 2 |
| 17 | 2988 | H1168I | ba.al | [Bamoth]-baal | 64 | 1 | 28 | 36 | 2 |
| 18 | 2987 | H1172 | ba.a.lah | mistress | 3 | 1 | 2 | 1 | 1 |
| 19 | 2960 | H2508 | cha.laq | portion | 3 | 1 | 2 | 1 | 1 |
| 20 | 2954 | H4436G | mal.kah | Queen [of Sheba] | 8 | 1 | 8 | 0 | 2 |
| 21 | 2951 | H4436H | mal.kah | queen | 26 | 2 | 11 | 15 | 2 |
| 22 | 2953 | H4468 | mam.la.khut | kingdom | 9 | 1 | 1 | 8 | 1 |
| 23 | 2974 | H4896 | mish.tar | rule | 1 | 1 | 1 | 0 | 1 |
| 24 | 2908 | H4951 | mis.rah | dominion | 2 | 1 | 2 | 0 | 1 |
| 25 | 2993 | H7300 | rud | to roam | 4 | 1 | 4 | 0 | 2 |
| 26 | 2975 | H7860 | sho.ter | official | 25 | 1 | 4 | 21 | 2 |
| 27 | 2976 | H7862 | shay | gift | 3 | 1 | 3 | 0 | 1 |
| 28 | 2978 | H7886 | shi.loh | tribute | 1 | 1 | 1 | 0 | 1 |
| 29 | 1355 | H7985 | shol.tan | dominion | 9 | 1 | 6 | 3 | 2 |
| 30 | 2909 | H8280 | sa.rah | to strive | 2 | 1 | 2 | 0 | 1 |
| **TOTAL** | | | | | **380** | **38** | **203** | **179** | **54** |

Dual-context verses: 2 (vid=54379 Heb 12:28 and vid=87904 2Th 1:5 — both in Groups 1358-004 and 1358-005)

---

## Flag register summary

| Flag | Term | Finding | Decision |
|---|---|---|---|
| DF-001 | G0933 baseleion (mti=2945) | All-verses-fail — 1 verse (Luk 7:25); term names physical palace with no inner-being engagement at term level | Option A confirmed — AVF. No vc records inserted. |

No Session B flags raised.

---

## Patch summary

**File:** wa-vcb-027-patch-v1-20260406.json
**Patch type:** VERSECONTEXT
**Total operations:** 420
- Group inserts: 38
- Verse_context inserts: 382 (380 verses + 2 extra rows for dual-context)
- Relevant verses: 203
- Set-aside verses: 179
- Anchor verses: 54
- Dual-context verses: 2

**Validation:** R1–R4 pre-check — all pass. Coverage check — 380/380 ✓

---

## Handoff to Claude Code

```
PATCH SUBMISSION TO CLAUDE CODE

Patch file: wa-vcb-027-patch-v1-20260406.json
Patch type: VERSECONTEXT

Action required:
  1. Apply patch — insert verse_context_group and verse_context records
  2. Resolve group_code strings to integer ids for all new groups
  3. Validate consistency rules R1–R4 after application
  4. Run integrity validation
  5. Handle XREF coverage check for Reg 199 (dominion)
  6. For Reg 199: run completion check
     - If all OWNER terms now classified AND all XREF terms covered:
       SET verse_context_status = 'Complete', re-export full word JSON
     - Note: Reg 197 (authority) was already fully classified in prior batches
       and does not need re-checking unless XREF coverage was pending
  7. Report: records inserted, registries advanced to Complete,
     XREF coverage status, any integrity violations, next batch status

Notes:
  - mti=2945 (G0933 baseleion): AVF confirmed — 1 set-aside record only, no groups
  - Group_id references in patch are group_code strings (e.g. "1358-001");
    Claude Code resolves to integer ids at apply time
  - No Session B flags file produced (none raised)
```

---

## Reg 199 (dominion) — completion outlook

VCB-027 classifies 30 of Reg 199's terms. Whether Reg 199 can now advance to Complete depends on:
1. Whether all remaining OWNER terms in Reg 199 now have verse_context records (Claude Code to verify)
2. Whether all XREF terms in Reg 199 have an OWNER classified elsewhere

Claude Code to confirm and report.

---

*Governing instruction: WA-VerseContext-Instruction-v2.4-20260403.md*
*Observations file: wa-vcb-027-term-observations-v1.5-20260406.md*
*Patch: wa-vcb-027-patch-v1-20260406.json*
