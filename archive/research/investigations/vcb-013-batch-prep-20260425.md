# VCB-13 — batch preparation brief

**Date:** 2026-04-25
**Author:** Claude Code
**Governing instruction:** [wa-versecontext-instruction-v3_9-20260425.md](../../data/imports/WA/Workflow/Framework_B/Session_B/wa-versecontext-instruction-v3_9-20260425.md)
**Companion patch instruction:** wa-patch-instruction-v2_9 (current)
**Predecessor session:** VCB-11 — applied 2026-04-25T14:42Z (15 terms, 5 registries, 47 cumulative vc_completed terms)
**Numbering note:** VCB-12 is intentionally skipped — `vcb-012-batch-prep-20260425.md` is retained as the historical record of a deferred-partials concept that was overtaken when VCB-11 absorbed all 15 terms in one session.

---

## 1. Composition

Continues the VCB-10/11 pattern: **5 three-term registries**, all currently at `verse_context_status='Complete'` (legacy), all per-term postures **RE-EVALUATION** (`vc_status='not_done'`, `md_version=1`).

| Reg | Word | OWNER terms (active) | Active verses | Notes |
|----:|------|----------------------|--------------:|-------|
| 067 | goodness   | G0019, G5544, H2896A | 317 | ⚠ tov heavy partial (141 unclassified) |
| 069 | gratitude  | G2168, G2169, G2170  |  54 | clean RE-EVAL |
| 092 | integrity  | G0861, H8538, H8549G |  62 | ⚠ tāmim heavy partial (45 unclassified) |
| 127 | reasoning  | G1256, G1258, G1261  |  33 | ⚠ dialektos minor partial (1 unclassified) |
| 171 | whoredom   | H2181, H2183, H2184  | 102 | ⚠ zānah moderate partial (12 unclassified) |
| **Totals** | — | **15 terms** | **568 verses** | 4 partial / 11 clean |

Verse budget 568 — within the §5.2 ~1,500 soft session budget but materially heavier than VCB-10/11. Driven by mti=884 *tov* alone (306 verses, 141 unclassified). If the researcher prefers, *tov* can be split out as its own dedicated session — see §3 below.

## 2. Per-term detail

| mti_id | Strongs | Translit | Gloss | Reg | Active groups | Active vc rows | Active verses | Posture |
|-------:|--------:|----------|-------|----:|--------------:|---------------:|--------------:|---------|
|   885 | G0019   | agathōsynē  | goodness         | 067 | 1 |   4 |   4 | clean RE-EVAL |
|   886 | G5544   | chrēstotēs  | kindness         | 067 | 2 |   7 |   7 | clean RE-EVAL |
|   884 | H2896A  | ṭov         | pleasant/good    | 067 | 6 | 165 | 306 | ⚠ partial 165/306 |
|  5480 | G2168   | eucharisteō | to thank         | 069 | 1 |  38 |  38 | clean RE-EVAL |
|   891 | G2169   | eucharistia | thankfulness     | 069 | 1 |  15 |  15 | clean RE-EVAL |
|  5481 | G2170   | eucharistos | thankful         | 069 | 1 |   1 |   1 | clean RE-EVAL |
|   935 | G0861   | aftharsia   | incorruptibility | 092 | 2 |   6 |   6 | clean RE-EVAL |
|   933 | H8538   | tum·māh     | integrity        | 092 | 1 |   5 |   5 | clean RE-EVAL |
|   934 | H8549G  | tā·mim      | unblemished      | 092 | 2 |   6 |  51 | ⚠ partial 6/51 |
|  1080 | G1256   | dialegō     | to dispute       | 127 | 1 |  13 |  13 | clean RE-EVAL |
|  6065 | G1258   | dialektos   | language         | 127 | 1 |   5 |   6 | ⚠ partial 5/6 |
|  1081 | G1261   | dialogismos | reasoning        | 127 | 2 |  14 |  14 | clean RE-EVAL |
|  1221 | H2181   | zā·nah      | to fornicate     | 171 | 5 |  71 |  83 | ⚠ partial 71/83 |
|  1220 | H2183   | zĕ·nu·nim   | fornication      | 171 |  1 |  10 |  10 | clean RE-EVAL |
|  1222 | H2184   | zĕ·nut      | fornication      | 171 |  1 |   9 |   9 | clean RE-EVAL |

## 3. ⚠ Partial-completion analysis

Four terms have prior `verse_context` rows that don't cover every active verse. Per VC-Instruction §6.2 Step 2, this is technically a stop-flag condition. VCB-11 demonstrated the classifier can absorb partial-completion terms inline (NEW-ONLY routing for the unclassified verses) — the partials there were 916, 1364, 5111 with 21 unclassified verses combined, which sailed through.

This batch's partial workload is heavier:

- **mti=884 H2896A *ṭov*** — **141 unclassified verses** against 6 already-shaped groups. Largest single-term workload in the programme to date. Worth considering as its own dedicated session (VCB-14 or similar) where the classifier can give the term focused attention. Existing groups for *ṭov* already cover the principal inner-being roles (likely covenantal pleasantness, moral excellence, benevolent disposition, etc. — to confirm in the `.md`). The 141 unclassified verses are a mix of physical-only (food, lands, wealth being "good") and inner-being (heart-good, soul-pleasant, moral-good) — a substantial classification burden.
- **mti=934 H8549G *tā·mim*** — 45 unclassified verses; manageable inline though significant.
- **mti=6065 G1258 *dialektos*** — 1 unclassified verse; trivial inline.
- **mti=1221 H2181 *zā·nah*** — 12 unclassified verses; manageable inline.

**Two options:**

1. **Ship all 15 as VCB-13** (default): classifier absorbs all partials inline as in VCB-11. Single session, all 5 registries advance to fully-closed under v3_9 contracts. Workload heavier but proven pattern.
2. **Split *tov* (mti=884) out**: VCB-13 carries 14 terms (~262 verses); VCB-14 carries just mti=884 with focused attention on its 141 unclassified verses. 4 of 5 registries (069, 092, 127, 171) advance after VCB-13; reg 067 advances after VCB-14.

The other 3 partials (934, 6065, 1221) are light enough to keep inline either way.

Auto-defaulting to **Option 1** (all 15 as VCB-13). Researcher can reroute to Option 2 by saying "split tov".

## 4. Skipped sibling terms (non-blocking)

| Reg | Strongs | Trans | Reason |
|----:|--------:|-------|--------|
| 127 | G0483 | antilegō | status=delete, 0 verses |
| 127 | G0557 | apelegmos | status=delete, 0 verses |
| 127 | G1246 | diakatelenchomai | status=delete, 0 verses |
| 127 | G1649 | elegxis | status=delete, 0 verses |
| 127 | G1650 | elenchos | status=delete, 0 verses |
| 127 | G1651 | elenchō | status=delete, 0 verses |
| 127 | G1827 | exelenchō | status=delete, 0 verses |
| 127 | G1951 | epilegō | status=delete, 0 verses |
| 127 | G2639 | katalegō | status=delete, 0 verses |
| 127 | G3004H | legō | status=delete, 0 verses |
| 127 | G4302 | prolegō | status=delete, 0 verses |

Reg 127 reasoning has 11 sibling OWNER terms in `status=delete` with 0 verses — a notable cluster. Likely candidates for the long-running housekeeping task on stuck `status=delete` rows whose registries should advance (raised in VC-10 prep, still open).

## 5. Files prepared

15 per-term Session A `.md` files at [data/exports/session_a/terms/](../../data/exports/session_a/terms/), dated 2026-04-25:

```
wa-067-goodness-G0019-session_a-20260425.md     (20.0 KB)
wa-067-goodness-G5544-session_a-20260425.md     (20.5 KB)
wa-067-goodness-H2896A-session_a-20260425.md   (100.7 KB)  ⚠ heavy
wa-069-gratitude-G2168-session_a-20260425.md    (18.0 KB)
wa-069-gratitude-G2169-session_a-20260425.md    (12.1 KB)
wa-069-gratitude-G2170-session_a-20260425.md     (8.0 KB)
wa-092-integrity-G0861-session_a-20260425.md    (14.0 KB)
wa-092-integrity-H8538-session_a-20260425.md    (13.6 KB)
wa-092-integrity-H8549G-session_a-20260425.md   (24.5 KB)
wa-127-reasoning-G1256-session_a-20260425.md    (13.7 KB)
wa-127-reasoning-G1258-session_a-20260425.md    (11.2 KB)
wa-127-reasoning-G1261-session_a-20260425.md    (12.3 KB)
wa-171-whoredom-H2181-session_a-20260425.md     (33.0 KB)
wa-171-whoredom-H2183-session_a-20260425.md     (11.2 KB)
wa-171-whoredom-H2184-session_a-20260425.md     (10.8 KB)
```

Total `.md` payload ~333 KB (vs. VCB-11's ~177 KB). All carry `md_version=v1` headers.

## 6. Programme state after VCB-13 close (projected)

If all 15 terms reach `vc_completed` (Option 1):

- mti_terms at vc_completed: 47 → 62 (of ~3,891 active OWNER terms)
- 5 additional registries advance to fully-closed under v3_9 contracts. Cumulative: 21 of 214 registries with at least one term completed; 10 of those fully closed (excluding the one-term backlog — see §7).

If Option 2 (tov split out):
- After VCB-13 (14 terms): 47 → 61, 4 registries fully closed.
- After VCB-14 (just tov): 61 → 62, reg 067 fully closed.

## 7. Suggested next actions

1. Researcher reviews this brief — particularly §3 partial-completion analysis (especially mti=884 *tov* 141 unclassified).
2. If Option 1 (default): hand the 15 `.md` files (§5) to a Claude AI classification session as VCB-13.
3. If Option 2 (split tov): say so and CC will lift mti=884 out, leaving 14 terms for VCB-13.
4. After VCB-13 patches return, follow normal apply sequence (§7.9.2: VCNEW → VCREVISE → VCSBFLAGS → VCSDPOINTERS) with R1–R4 + arithmetic checks.

## 8. Eligibility horizon (for next-after-VCB-13 planning)

After VCB-13 (Option 1) closes, remaining 3-term-or-lighter registries pending:

- **3-term:** 204 name (495v) — heaviest single 3-term registry
- **2-term:** 077 honesty (332v), 091 insight (163v), 155 submission (36v), 110 memory (26v), 114 obedience (16v), 212 pray (14v), 029 contentment (3v)
- **1-term:** 060 faithfulness (242v), 093 intention (9v), 131 rejection (1v)

Natural VCB-14 candidate sets: (a) the 1-term + 2-term lighter registries paired (e.g. 029, 110, 114, 131, 212 — 5 registries, 8 terms, ~60 verses), (b) honesty + insight pair (2 registries, 4 terms, 495v), (c) larger registries (≥4 terms) which I haven't surveyed yet.
