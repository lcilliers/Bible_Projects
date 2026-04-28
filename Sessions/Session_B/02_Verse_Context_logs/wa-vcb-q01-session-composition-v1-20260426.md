# VCB-Q01 — Quality Pinpoint Pass · Session Composition

_Session id: **VCB-Q01** · prepared 2026-04-26 12:42Z · governing instruction: `wa-versecontext-instruction-v3_10-20260425.md`_

## Purpose

Off-stream session targeting the 6 OWNER terms with **unresolved quality flags** that put a question mark on existing verse-context groups, per `outputs/investigations/vc-quality-flags-practical-view-v1-20260426.md`.

This is **not** a sequential rolling VCB — it is a pinpoint quality pass. Three of the six items are likely **verify-and-close** (current DB state appears to satisfy the flag); three need active review.

## Composition

- **Terms:** 6
- **Verses (active):** 84
- **Posture:** all RE-EVALUATION (each term has prior `verse_context` rows)

## Per-term focus and expected outcome

| reg | term | mti | mdv | verses | groups (a/d) | vc_status | flag | focus | expected outcome |
|---:|---|---:|---:|---:|---:|---|---|---|---|
| 4 | anger `G3948` | 1562 | 1 | 2 | 2/0 | not_done | PH2-004-006 | pos/neg sense split (Acts 15:39 vs Heb 10:24) | first v3 classification; verify groups carry sense distinction |
| 50 | disobedience `G3878` | 5111 | 2 | 2 | 1/0 | vc_completed | VCB11-SB-002 | Mar 5:36 overhear vs Mat 18:17 refuse-to-listen | verify Mar 5:36 set_aside_wrong_face suffices; likely empty-ops VCREVISE |
| 165 | unbelief `G0570` | 1198 | 2 | 11 | 8/0 | vc_completed | apistia 8-fragment SB | group fragmentation | verify 8 active groups match SB rec; likely empty-ops VCREVISE |
| 165 | unbelief `G0544` | 1199 | 2 | 14 | 5/0 | vc_completed | apeitheo 165<->50 boundary | registry-boundary question | review 5 active groups for cross-registry leak |
| 181 | zeal `G4710` | 1268 | 2 | 12 | 11/0 | vc_completed | spoude 11-fragment SB | group fragmentation | verify 11 active groups match SB rec; likely empty-ops VCREVISE |
| 94 | intercession `H6293` | 937 | 2 | 43 | 2/0 | vc_completed | PH2-212-001 HIGH | 3-sense split (meet / attack / intercede) | review 2 current groups (post-VCB-014) vs 3-sense rec; likely VCREVISE |

## Input file list

- [wa-004-anger-G3948-session_a-20260426.md](../../data/exports/session_a/terms/wa-004-anger-G3948-session_a-20260426.md) — mti=1562, md_v=1
- [wa-050-disobedience-G3878-session_a-20260426.md](../../data/exports/session_a/terms/wa-050-disobedience-G3878-session_a-20260426.md) — mti=5111, md_v=2
- [wa-165-unbelief-G0570-session_a-20260426.md](../../data/exports/session_a/terms/wa-165-unbelief-G0570-session_a-20260426.md) — mti=1198, md_v=2
- [wa-165-unbelief-G0544-session_a-20260426.md](../../data/exports/session_a/terms/wa-165-unbelief-G0544-session_a-20260426.md) — mti=1199, md_v=2
- [wa-181-zeal-G4710-session_a-20260426.md](../../data/exports/session_a/terms/wa-181-zeal-G4710-session_a-20260426.md) — mti=1268, md_v=2
- [wa-094-intercession-H6293-session_a-20260426.md](../../data/exports/session_a/terms/wa-094-intercession-H6293-session_a-20260426.md) — mti=937, md_v=2

## A-03 input_versions map

```json
{
    "1562": "1",
    "5111": "2",
    "1198": "2",
    "1199": "2",
    "1268": "2",
    "937": "2"
}
```

## Classifier handoff notes

Process per `wa-versecontext-instruction-v3_10` §6 with these flag-driven priorities:

### Verify-and-close candidates (likely empty-ops VCREVISE → flag resolves)

1. **G0570 apistia (165 unbelief, mti=1198)** — current 8 active groups already match SB_FINDING text "apistia (G0570) operates across 8 distinct inner-being roles". Confirm group descriptions still cover the 8-role distinction; emit empty-ops VCREVISE if no change needed; flag closure goes via VCSBFLAGS.
2. **G4710 spoudē (181 zeal, mti=1268)** — current 11 active groups already match SB_FINDING text "spoudē (G4710) operates across 11 distinct inner-being roles". Same verify-and-close pattern.
3. **G3878 parakouo (50 disobedience, mti=5111)** — Mar 5:36 already `set_aside_reason=wrong_face` (handles overhear sense); Mat 18:17 in group 5111-001 (refuse-to-listen). Confirm this satisfies VCB11-SB-002; verify-and-close pattern.

### Active review needed

4. **G3948 paroxusmos (4 anger, mti=1562)** — `vc_status=not_done`. 2 verses, 2 pre-existing groups (legacy era — prior to v3 contracts). First v3 classification. Attend to PH2-004-006: Acts 15:39 (negative, sharp dispute) and Heb 10:24 (positive, stir up to love) carry inverted relational sign — group descriptions must distinguish.
5. **G0544 apeitheō (165 unbelief, mti=1199)** — `vc_completed v2`, 5 active groups across 14 verses. PH2 boundary flag: this term straddles the 165<->50 boundary (refuse to believe / refuse to obey). Review whether all 14 verses belong in 165, or whether some should be flagged as cross-registry pointers to 50 disobedience.
6. **H6293 paga (94 intercession, mti=937)** — `vc_completed v2` post-VCB-014. 43 verses, 2 active groups. PH2-212-001 (HIGH priority) says paga has 3 distinct senses: (1) meet/encounter (Gen 23:8), (2) fall upon/attack (Num 35:19), (3) intercede/entreat (Isa 53:12). Review whether 2 current groups handle the split, or whether a 3-group structure is warranted (likely VCREVISE).

### Flag-resolution patches

After classification, emit VCSBFLAGS patches to set `resolved=1` on the corresponding rows in `wa_session_research_flags` for any flag confirmed-addressed.

## Excluded from this batch

| reg | term | reason |
|---:|---|---|
| 98 justice | H4639H, H4639I | 0 verses each (extracted_thin shells); cannot classify. PH2-98-012/013 flags need term-status fix or independent verse research, not VC. |
| 103 love | H7356B rachamim | already `vc_status=to_revise`. Will be addressed in the love-registry reset workflow per Q12 (2026-04-19); separate stream. |

## Side-line: registry 48 diligence

Separate finding from the practical-view scan: `verse_context_status=Complete` but **0 active verse_context_groups** across 6 OWNER terms with 82 active verses. Status is unsupported by data — the classification work was either lost or never imported, or the status flag is wrong. Worth a focused investigation **outside this batch** before any downstream stage trusts diligence.