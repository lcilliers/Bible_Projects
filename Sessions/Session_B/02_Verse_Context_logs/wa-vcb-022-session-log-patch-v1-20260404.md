# wa-vcb-022-session-log-patch-v1-20260404
**Batch:** VCB-022 | **Session type:** Patch construction
**Date:** 2026-04-04 | **Governing instruction:** WA-VerseContext-Instruction-v2.4-20260403.md
**Observations file at session start:** wa-vcb-022-term-observations-v2.8-20260404.md
**Prior output:** wa-vcb-022-patch-handoff-v1-20260404.md

---

## Session scope

Patch construction for VCB-022 (120 terms, 2,470 verses, registries 187–196 excl. 195).
Input files: extract JSON, observations v2.8, governing instruction §§7–7.7.

---

## Pre-construction validation findings

### §7.7 programmatic validation results

**Anchor reference verification:** All 275 anchors confirmed present in extract. Zero failures.

**Coverage check:** Initiated by building a complete vid→term map across all 2,470 vids. No vid appeared in more than one term. All vids verified to have exactly one home at completion.

**Duplicate key check:** Zero (vid, mti, group_id) duplicates in the final patch.

**R1–R4 pre-check:** All four rules passed at zero violations before patch was written.

---

## Issues resolved during session

### Issue A — ma.qom H4725 (mti=6989): duplicate group assignment
**Finding:** vids 218993 (Jer 32:37) and 218994 (Jer 33:10) were listed in both Group 003 related and the revised Group 004 related list.
**Decision (researcher):** Both vids → Group 003 (moral-covenantal conditions of dwelling).
**Patch consequence:** Group 004 related = {219093} only (3 verses total: 2 anchors + 1 related).

### Issue B — ba.rakh H1288 (mti=1299): no explicit vid lists for groups 001–003
**Finding:** The observations file recorded group criteria descriptively ("all verses where God is the subject of ba.rakh...") without naming the 239 individual verse_record_ids for groups 001–003. Only Group 004 (8 verses) had an explicit related list. Anchors (8) and set-aside (2) were explicit.
**Cause:** The classification session applied programmatic pattern-matching to determine group membership but did not write individual vid assignments to the observations file. The vid-by-vid record required for patch construction was absent.
**Decision (researcher):** Option A — re-classify all 249 ba.rakh verses directly from the extract JSON in the patch construction session.
**Outcome:** All 249 verses classified. The derived counts differ from the observations file SUMMARY (which was annotated before full individual inspection was complete):
- G001 (God blesses): 89 total (obs said 91)
- G002 (human blesses God): 54 total (obs said 50)
- G003 (human blesses human): 91 total (obs said 98)
- G004 (ironic/euphemistic): 13 total (obs said 8)
- Set aside: 2 (unchanged)

**Net change:** 5 additional verses assigned to G004 (ironic/distorted use) vs. observations file, reflecting full application of the classification criteria to each verse individually. Researcher confirmed Option A takes precedence over observations file SUMMARY counts.

Notable G004 additions: 226072 (1Ki 21:10), 226073 (1Ki 21:13) — euphemistic "blessing" = legal charge of cursing; 226212 (Zec 11:5) — cynical doxology by exploitative shepherds; 226187 (Psa 49:18) — wicked man's self-congratulatory self-blessing; 226189 (Psa 62:4) — blessing with mouth while cursing inwardly.

### Systemic finding — observations file related-list completeness
During programmatic validation, 15 additional terms were found to have unassigned vids in the constructed classification (vids present in the extract but not captured by the parser from the observations file). Root cause: the observations file uses "all remaining relevant vids" descriptions without listing every verse_record_id, and in some cases the Related list was abbreviated in the observations text. All cases were resolved by reading the verse texts directly from the extract and applying group criteria. Key terms affected and resolution counts:

| mti | Term | Unassigned resolved | Method |
|---|---|---|---|
| 1270 | H1058 ba.khah (weep) | 32 | Read from extract, applied group criteria |
| 7181 | G3842 pantote (always) | 32 | Compute: all_vids minus named SA |
| 7092 | H5923 ol (yoke) | 4 | Read from extract (2Ch Rehoboam passages → G001) |
| 7112 | H5956 a.lam (conceal) | 4 | Full obs section read; SA computed |
| 1298 | G2127 eulogeō (bless) | 4 | Read from extract (Luk 1:28, 2:34; Mar 10:16; 1Cor 14:16) |
| 659 | H4581 ma.oz (security) | 1 | 2Sa 22:33 → G001 |
| 6889 | H6106G e.tsem (bone) | 1 | Psa 22:17 → G002 |
| 7092 | H5923 ol (yoke) | 1 | 2Ch 10:4 → G001 |

### Duplicate vid assignments resolved
Eight terms had vids appearing in two group related lists simultaneously (obs file listed a vid in an original group, then in a revised group, without removing from the original). All resolved by applying the principle: anchor designation takes priority; otherwise assign to the group whose description better fits the verse content.

Key resolutions:
- mti=7030 vid=220644 (Psa 60:12): listed as G002 related AND G004 anchor → assigned G004 anchor
- mti=7092 vids 221566,221564,221565,221568 (Jer 27–28): listed in G001 and G003 → assigned G003 (divine discipline dimension)
- mti=1270 vids 221750,221749 (2Ki 8:11–12): listed in G001 and G004 → assigned G004 (prophetic weeping; 221750 is explicit G004 anchor)
- mti=7112 vid=221707 (Lev 20:4): listed in G001 and G003 → assigned G003 (deliberate moral blindness)

### Minor observations file SUMMARY count corrections
Three terms had SUMMARY annotation counts that did not match the actual vid lists:
- mti=6965 H3581B ko.ach: SUMMARY says 98 relevant, vid lists yield 99. Patch reflects 99.
- mti=1276 H7043 qa.lal: SUMMARY says 48 relevant (using an incorrect group-count annotation), vid lists yield 46. Patch reflects 46.
- mti=6948 H3286 ya.eph: SUMMARY corrected within the observations file itself; restructured to 2 groups, 4 anchors, 8 relevant, 1 set aside. Patch reflects corrected structure.
- mti=1298 G2127 eulogeō: vid 224806 appeared in G003 related list but is not in the extract for this term (cross-reference artefact from mti=1290 section). Removed from classification; G003 related = 2 vids.

---

## Patch output

**File:** wa-vcb-022-patch-v1-20260404.json
**Patch ID:** PATCH-20260404-VCB022-VERSECONTEXT-V1

### Final patch summary

| Metric | Value |
|---|---|
| Total operations | 2,629 |
| Group inserts | 159 |
| Group updates | 0 |
| Verse context inserts | 2,470 |
| Verse context updates | 0 |
| Relevant verses | 1,412 |
| Set aside verses | 1,058 |
| Anchor verses | 275 |
| Dual context verses | 0 |
| Revisions to prior | 0 |

**Variance from handoff totals:**
The handoff document projected 1,438 relevant and 1,032 set aside. The patch reflects 1,412 relevant and 1,058 set aside. The variance of 26 verses arises from:
(a) ba.rakh reclassification shifting some verses across groups without changing the relevant total materially, but the group-level re-read found that the observations file had overcounted relevant for qa.lal (-2) and correctly added ko.ach (+1);
(b) multiple terms where "all remaining" relevant was fewer than the SUMMARY annotation implied once individual vids were enumerated.
The total of 2,470 is unchanged (all vids accounted for exactly once).

### Pre-submission validation results

| Check | Result |
|---|---|
| All 275 anchors in extract | ✓ |
| Zero duplicate (vid, mti, group_id) keys | ✓ |
| Every vid has exactly one verse_context row | ✓ |
| R1 (set-aside rows clean) | ✓ 0 violations |
| R2 (anchor rows clean) | ✓ 0 violations |
| R3 (related rows have anchor in group) | ✓ 0 violations |
| R4 (no anchor+related simultaneously) | ✓ 0 violations |
| Group count | ✓ 159 |
| Anchor count | ✓ 275 |

---

## Observations file corrections required

The following corrections should be applied to the observations file before it is archived:

1. **mti=1299 ba.rakh SUMMARY:** Update group counts to G001=89, G002=54, G003=91, G004=13. Add note: "Vid lists derived in patch construction session 2026-04-04; full re-read applied."
2. **mti=6965 ko.ach SUMMARY:** Change relevant from 98 to 99, set aside from 22 to 21.
3. **mti=1276 qa.lal SUMMARY:** Change relevant from 48 to 46, set aside from 31 to 33. Correct G001 related annotation from "19 verses" to "23 verses."
4. **mti=6948 ya.eph:** The corrected SUMMARY is already in the obs file. No further action.
5. **mti=1298 eulogeō G003:** Remove vid=224806 from related list (not in extract).
6. **General note:** 15 terms had unassigned vids resolved in patch construction; their individual group assignments are captured in this session log and in the patch file itself.

---

## No Session B flags

No Session B flags were raised during this batch. No sessionB-flags document required.

---

## Next steps

1. Claude Code to apply patch wa-vcb-022-patch-v1-20260404.json
2. Claude Code to validate consistency rules R1–R4 after application
3. Claude Code to run XREF coverage check for all affected registries (187–196 excl. 195)
4. Claude Code to run completion check and advance verse_context_status to Complete for each completed registry; re-export full word JSON per registry
5. Session B DataPrep for earlier completed batches (VCB-015 flags file queued: wa-vcb-015-sessionB-flags-v1-20260403.md, registries 124, 126, 128, 140, 142)
6. Correct observations file SUMMARY lines as noted above

