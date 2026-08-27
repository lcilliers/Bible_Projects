# WA-FlagResolution-VCB003-v1-20260331.md

**Framework B — Soul Word Analysis Programme**
**Flag Resolution Record — VCB-003 Researcher Decisions**
**Date: 2026-03-31**
**Reference: WA-SessionLog-VCB003-Final-v1-20260331.md**

---

## Researcher Decisions — All 15 Flags

| # | Registry | Term | mti_id | Decision | Effect |
|---|---|---|---|---|---|
| F-001 | 19 | G1161 (de) | 725 | **Set aside confirmed** | All 60 verses set aside, no groups, no anchor |
| F-002 | 19 | G1577 (ekklēsia) | 4833 | **Set aside confirmed** | All 85 verses set aside, no groups, no anchor |
| F-003 | 19 | G4377 (prosfōneō) | 721 | **Set aside confirmed** | All 7 verses set aside, no groups, no anchor |
| F-004 | 19 | G5456H (fōnē noise) | 4840 | **KEEP** — Joh 3:8 retained | Group 4840-001 stands; anchor: Joh 3:8 |
| F-005 | 19 | H4744 (miq.ra) | 4827 | **Set aside confirmed** | All 22 verses set aside, no groups, no anchor |
| F-006 | 19 | H7121J (qa.ra read-out) | 4824 | **Set aside confirmed** | All 37 verses set aside, no groups, no anchor |
| F-007 | 19 | H7122H (qa.ra toward) | 4826 | **Set aside confirmed** | All 39 verses set aside, no groups, no anchor |
| F-008 | 23 | H7356A (ra.cham womb) | 729 | **KEEP** — Isa 46:3 retained | Group 729-001 stands; anchor: Isa 46:3 |
| F-009 | 23 | H7358 (re.chem womb) | 1613 | **Set aside confirmed** | All 25 verses set aside, no groups, no anchor |
| F-010 | 24 | G0178 (akatakritos) | 4847 | **Set aside confirmed** | All 2 verses set aside, no groups, no anchor |
| F-011 | 24 | H4941I (mish.pat rule) | 3191 | **Set aside confirmed** | All 15 verses set aside, no groups, no anchor |
| F-012 | 24 | H4941J (mish.pat custom) | 3190 | **Set aside** — Judg 13:12 not accepted | All 24 verses set aside, no groups, no anchor |
| F-013 | 28 | H6944H (qo.desh Most Holy) | 4876 | **Set aside confirmed** | All 10 verses set aside, no groups, no anchor |
| F-014 | 31 | H4889 (mash.chit) | 746 | **Set aside** — Pro 18:9 not accepted | All 12 verses set aside, no groups, no anchor |
| F-015 | 31 | H4893A (mish.chat) | 4905 | **KEEP** — Isa 52:14 retained | Group 4905-001 stands; anchor: Isa 52:14 |

---

## Terms with Active Groups — Post-Resolution

Terms where a borderline was accepted (KEEP) and a group stands:

| Term | mti_id | Group | Anchor |
|---|---|---|---|
| G5456H (fōnē noise) | 4840 | 4840-001 | Joh 3:8 |
| H7356A (ra.cham womb) | 729 | 729-001 | Isa 46:3 |
| H4893A (mish.chat) | 4905 | 4905-001 | Isa 52:14 |

---

## Terms Fully Set Aside — Post-Resolution

Terms where all verses are set aside and no patch operations are required beyond is_relevant = 0 records:

| Term | mti_id | Verses set aside | Reason |
|---|---|---|---|
| G1161 (de) | 725 | 60 | Conjunction particle — no inner-being content |
| G1577 (ekklēsia) | 4833 | 85 | Institutional community term |
| G4377 (prosfōneō) | 721 | 7 | Vocal addressing act |
| H4744 (miq.ra) | 4827 | 22 | Liturgical assembly category |
| H7121J (qa.ra read-out) | 4824 | 37 | Public reading sub-sense |
| H7122H (qa.ra toward) | 4826 | 39 | Hostile military encounter |
| H7358 (re.chem womb) | 1613 | 25 | Physical womb throughout |
| G0178 (akatakritos) | 4847 | 2 | Legal status without inner-being |
| H4941I (mish.pat rule) | 3191 | 15 | Prescribed quantities/procedures |
| H4941J (mish.pat custom) | 3190 | 24 | Manner/custom sub-sense — borderline not accepted |
| H6944H (qo.desh Most Holy) | 4876 | 10 | Architectural inner sanctuary |
| H4889 (mash.chit) | 746 | 12 | Destruction as physical force — borderline not accepted |

---

## Patch Construction Handoff — Status

All classification decisions are now final. The patch construction session may proceed.

**Inputs required for patch construction session:**
1. This file: `WA-FlagResolution-VCB003-v1-20260331.md`
2. Final observations file: `wa-vcb-003-term-observations-v1.4-20260331.md`
3. Final session log: `WA-SessionLog-VCB003-Final-v1-20260331.md`
4. Extract JSON: `wa-vcb-003-extract-20260331.json`
5. Governing instruction sections 7–7.6: `WA-VerseContext-Instruction-v1.8-20260331.md`
6. Patch specification: `patch_specification_v1_6-20260330.md`

**Patch construction session must:**
- Apply flag resolutions above before building any operations
- Work through 9 deferred large terms (1,339 verses) using the group structures in the observations file
- Verify all anchor references against `verse_record_ids` in the extract JSON
- Run pre-submission validation (Section 7.6) before producing output
- Produce: `wa-vcb-003-patch-{YYYYMMDD}.json`

---

*WA-FlagResolution-VCB003-v1-20260331.md | All 15 flags resolved | Classification complete — ready for patch construction*
