# VCB-011 — batch preparation brief

**Date:** 2026-04-25
**Author:** Claude Code
**Governing instruction:** [wa-versecontext-instruction-v3_9-20260425.md](../../data/imports/WA/Workflow/Framework_B/Session_B/wa-versecontext-instruction-v3_9-20260425.md)
**Companion patch instruction:** wa-patch-instruction-v2_9 (current)
**Predecessor session:** VC-10 — applied 2026-04-25T05:36–37Z (12 terms, 5 three-term registries, 73 active vc rows)
**Sibling session:** [VCB-012](vcb-012-batch-prep-20260425.md) — the two partial-completion terms (mti=5111, mti=1364) split out into their own session for separate handling.

---

## 1. Composition

Two partial-completion terms originally grouped here (mti=5111 G3878, mti=1364 H2498) were split out to VCB-012 (researcher decision 2026-04-25). VCB-011 is now **13 OWNER terms across 5 registries**, all `verse_context_status='Complete'` (legacy), all per-term postures **RE-EVALUATION** (`vc_status='not_done'`, `md_version=1`).

| Reg | Word | OWNER terms (active, in VCB-011) | Active verses |
|-----|------|----------------------------------|---------------|
| 050 | disobedience   | G0543, G3876                     |  9 |
| 085 | imagination    | G1760, G1761, H4906              | 13 |
| 115 | passion        | G3116, G3392, G3394              |  6 |
| 193 | craving        | G3552, G3554, G3713              | 13 |
| 202 | transformation | G3339, G3445                     |  5 |
| **Totals** | — | **13 terms** | **46 verses** |

Verse budget 46 — well under the §5.2 ~1,500 soft session budget.

Reg 050 retains 2 of 3 OWNER terms in VCB-011; reg 202 retains 2 of 3. Aggregate registry-completion check at end of session will not advance these two registries because their split-out terms (mti=5111 and mti=1364) remain pending. Both registries advance only after VCB-012 also closes successfully.

## 2. Per-term detail

| mti_id | Strongs | Translit | Gloss | Reg | Active groups | Active vc rows | Active verses |
|-------:|--------:|----------|-------|----:|--------------:|---------------:|--------------:|
|   819 | G0543 | apeitheia    | disobedience | 050 | 2 |  6 |  6 |
|   820 | G3876 | parakoē      | disobedience | 050 | 1 |  3 |  3 |
|  3392 | G1760 | enthumeomai  | to reflect on | 085 | 1 |  3 |  3 |
|   917 | G1761 | enthumēsis   | reflection   | 085 | 1 |  4 |  4 |
|   916 | H4906 | mas.kit      | figure       | 085 | 1 |  3 |  6 |
|  1432 | G3116 | makrothumōs  | patiently    | 115 | 1 |  1 |  1 |
|  5948 | G3392 | miainō       | to stain     | 115 | 1 |  4 |  4 |
|  1023 | G3394 | miasmos      | defilement   | 115 | 1 |  1 |  1 |
|  1295 | G3552 | noseō        | be sick      | 193 | 1 |  1 |  1 |
|  7222 | G3554 | nosos        | illness      | 193 | 1 | 11 | 11 |
|  1296 | G3713 | oregō        | to aspire    | 193 | 1 |  1 |  1 |
|  1362 | G3339 | metamorfoō   | to transform | 202 | 2 |  4 |  4 |
|  7377 | G3445 | morfoō       | to form      | 202 | 1 |  1 |  1 |

All 13 terms have prior `verse_context` row counts matching their active verse counts → standard RE-EVALUATION posture, no partial-completion stops expected.

The two partial-completion terms originally surveyed for this batch (mti=5111 G3878, mti=1364 H2498) are split out into [VCB-012](vcb-012-batch-prep-20260425.md) for separate handling.

## 4. Skipped sibling terms (non-blocking)

These OWNER terms exist in scope but are excluded from the batch because the applicator's aggregate registry-completion check filters by `status IN ('extracted','extracted_thin')` + `EXISTS(verse_records)`. Non-eligible siblings do not block registry advancement.

| Reg | Strongs | Trans | Reason |
|----:|--------:|-------|--------|
| 050 | G0545 | apeithēs | status=delete, 0 verses |
| 085 | H7914 | sĕ·khī·yāh | status=delete, 0 verses |
| 085 | H7915 | sak·kīn | status=delete, 0 verses |
| 115 | G3958 | paschō | status=delete, 0 verses |
| 193 | G3553 | nosēma | status=candidate_delete, 0 verses |

A housekeeping pass on stuck `mti_terms.status='delete'` rows whose registries should advance was already noted on commit 3824f06 (VC-10 prep) — same follow-up applies.

## 5. XREF awareness

Several XREF terms in these registries point to OWNERs whose VC has not yet run. This is not a VC-11 blocker — XREF coverage is achieved when those OWNERs reach `vc_completed` (per §13.2). Listed for situational awareness only.

| Reg | XREF Strongs | OWNER reg | OWNER vc_status |
|----:|-------------:|----------:|------------------|
| 050 | G3982 | 163 trust | not_done |
| 085 | H7907 | 183 heart | not_done |
| 115 | G2371, G2373 | 4 anger | not_done |
| 115 | G3356, G4834, G4835 | 23 compassion | to_revise |
| 115 | G3713 | 193 craving | not_done (this batch) |
| 115 | G3715 | 43 desire | not_done |
| 193 | H0183, H1942, H8378 | 43 desire | not_done |
| 193 | H1934 | 198 might | not_done |
| 193 | H5314, H5315G–N | 182 Soul | not_done |
| 202 | G0276, G3338, G3340, G3341, G3346 | 135 repentance | not_done |
| 202 | G0303 | 51 distress | not_done |
| 202 | G0341, G0342, H2475, H2487, H2500, H4252, H4253 | 134 renewal | vc_completed |
| 202 | G2537 | 34 covenant | not_done |
| 202 | G3328 | 112 mind | not_done |

Notable: registry 202 transformation has 7 XREFs to registry 134 renewal (already `vc_completed` from the VC-7 pilot). When 202's OWNER terms complete, the renewal-as-XREF coverage flips to derived-complete — small downstream win.

## 6. Files prepared

13 per-term Session A `.md` files in scope for VCB-011 at [data/exports/session_a/terms/](../../data/exports/session_a/terms/), dated 2026-04-25:

```
wa-050-disobedience-G0543-session_a-20260425.md   (10.0 KB)
wa-050-disobedience-G3876-session_a-20260425.md    (9.0 KB)
wa-085-imagination-G1760-session_a-20260425.md     (9.4 KB)
wa-085-imagination-G1761-session_a-20260425.md     (9.7 KB)
wa-085-imagination-H4906-session_a-20260425.md     (9.9 KB)
wa-115-passion-G3116-session_a-20260425.md        (10.1 KB)
wa-115-passion-G3392-session_a-20260425.md        (11.4 KB)
wa-115-passion-G3394-session_a-20260425.md        (10.1 KB)
wa-193-craving-G3552-session_a-20260425.md        (16.2 KB)
wa-193-craving-G3554-session_a-20260425.md        (18.6 KB)
wa-193-craving-G3713-session_a-20260425.md        (16.3 KB)
wa-202-transformation-G3339-session_a-20260425.md (14.6 KB)
wa-202-transformation-G3445-session_a-20260425.md (12.6 KB)
```

The two `.md` files **not in this batch** (handed to VCB-012):

- `wa-050-disobedience-G3878-session_a-20260425.md`  (8.9 KB)
- `wa-202-transformation-H2498-session_a-20260425.md` (18.8 KB)

All carry `md_version=v1` headers — A-03 version-gate value the classifier must echo into `_patch_meta.input_versions` per term.

## 7. Programme state after VCB-011 close (projected)

If all 13 terms reach `vc_completed`:
- mti_terms at vc_completed: 32 → 45 (of ~3,891 active OWNER terms)
- 3 registries (085 imagination, 115 passion, 193 craving) advance from legacy-Complete to v3_8-Complete via aggregate check.
- 2 registries (050 disobedience, 202 transformation) hold at legacy-Complete pending VCB-012 closure of mti=5111 and mti=1364.

## 8. Suggested next actions

1. Hand the 13 `.md` files (§6) to a Claude AI classification session as VCB-011.
2. After VCB-011 patches return, follow normal apply sequence (§7.9.2: VERSECONTEXT → VCREVISE → VCSBFLAGS → VCSDPOINTERS) with R1–R4 + arithmetic checks.
3. Process [VCB-012](vcb-012-batch-prep-20260425.md) (the two partial-completion terms) in a separate session — independent ordering from VCB-011.
4. Once VCB-012 closes, registries 050 and 202 can advance.
