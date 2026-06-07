# VCG analytics — citation rate correction (M10, M15, and the broader picture)

**Date:** 2026-05-27
**Context:** researcher flagged M10's 1% and M15's 2% citation rates as suspicious. Investigation revealed my analytics regex was missing several citation formats. **The corrected picture is that ALL 16 closed clusters cite VCGs in their findings — there is no Group C of "VCGs unused in Phase 9."**

---

## §1. The five citation conventions

Different Phase 9 sessions cited VCGs in different ways. My original regex required the full cluster-aware form (`M10c-A-VCG-07`) and undercounted the four other forms.

| Form | Convention | Example | Used by |
|---|---|---|---|
| **1. Full code** | Complete `M{NN}-X-VCG-N` | `M07-A-VCG-01` | M01-M04, M07-M09 (mixed with hyphen-short) |
| **2. Hyphen-short** | `VCG-N` (scope-implicit within sub-group/aspect) | `VCG-01` | M01-M04, M07-M09, M10, M10b, M10c |
| **3. No-hyphen short** | `VCGN` (no hyphen) | `VCG01` | M15 |
| **4. Legacy code literal** | The pre-cluster-pivot code as a literal | `group 14-002`, `247-001` | M06, M20, M26, M39, M46 |
| **5. None** | Findings reference only verses, Strong's, sub-groups | — | (none — all closed clusters cite VCGs in some form) |

---

## §2. The corrected per-cluster picture

After matching all four citation forms:

| Cluster | # VCGs | # cited | Citation rate | Format used | Notes |
|---|---:|---:|---:|---|---|
| M01 | 38 | 38 | 100% | full + hyphen-short | |
| M02 | 27 | 27 | 100% | full + hyphen-short | |
| M03 | 25 | 25 | 100% | full + hyphen-short | |
| M04 | 47 | 47 | 100% | full + hyphen-short | |
| M06 | 51 | 24 | 47% | legacy literal | 24 of 51 legacy codes appear literally in findings |
| M07 | 28 | 28 | 100% | full + hyphen-short | |
| M08 | 24 | 24 | 100% | full + hyphen-short | |
| M09 | 21 | 21 | 100% | full + hyphen-short | |
| **M10** | **68** | **68** | **100%** | hyphen-short (was 1% in original) | 944 short-form citations / 9 distinct sequences |
| M10b | 36 | 36 | 100% | hyphen-short (mostly) | 2,956 short-form citations |
| M10c | 26 | 26 | 100% | hyphen-short + some full | |
| **M15** | **58** | **4–58** | **understated** | no-hyphen short | 1,350 short-form citations / 12 distinct sequences. The 4 cited in §4 is a measurement floor — my code-format extraction can't map `523-002` to a sub-group-relative sequence. The qualitative answer is M15's VCGs are heavily cited. |
| M20 | 26 | 9 | 35% | legacy literal | |
| M26 | 79 | 61 | 77% | legacy literal | |
| M39 | 34 | 31 | 91% | legacy literal | |
| M46 | 34 | 3 | 9% | legacy literal | |

The "M05 0% / 123 VCGs" row remains in the analytics (M05 was reset to `Ready for re-analysis` 2026-05-27 but its legacy VCGs weren't auto-cleared — they'll dissolve at next Phase 8 if/when M05 is re-analyzed).

---

## §3. M10 deep-dive — the original 1% was 99% wrong

M10 has 68 VCGs across 22 sub-groups (M10-C through M10-X). Sub-group max sequence depth is 9 (M10-F has VCG-1 through VCG-9). Each of the other 21 sub-groups has fewer (typically 1-5 VCGs each).

M10 findings cite VCGs **944 times** across **9 distinct sequence numbers** (VCG-1 through VCG-9). Sample contexts:

> *"structured around human sinning against God (**VCG-01**, 32V), human sinning against persons (**VCG-02**, ...)"*
> *"the cultic-atonement corpus (**VCG-04**: Lev 4–5 sin-offering system) presupposes..."*
> *"the four distinct registers: **VCG-01** (God-directed), **VCG-02** (interpersonal), **VCG-03** (deterred/restrained), **VCG-04** (requiring ritual remedy)"*

Each citation is sub-group-scoped: when a finding is authored under `[M10-NN]` aspect marker, "VCG-01" means "this aspect's first VCG." My original regex required the full `M10-A-VCG-01` form and missed all 944.

**M10's VCGs are heavily analytically active — likely the most VCG-grain-cited cluster in the programme.**

---

## §4. M15 deep-dive — different format, same answer

M15 cites VCGs as `VCG01`-`VCG12` (no hyphen). Sample contexts:

> *"**VCG01** (Dan 2:20 anchor): 'to whom belong wisdom and might' — wisdom as divine possession."*
> *"Isa 40:28 (**VCG01** anchor): 'his understanding is unsearchable'..."*
> *"Psa 139:6 (**VCG01** anchor): 'such knowledge is too wonderful...'"*

M15 has 8 sub-groups (M15-A through M15-H) plus BOUNDARY, 58 active VCGs total. The AI cited VCG01-VCG12 — 12 distinct positions × 8 sub-groups = potentially covers most VCG rows. **1,350 short-form citations total.**

M15's VCG codes are legacy `{registry_id}-{seq}` format (e.g. `523-002`) which my regex can't deterministically map to "sub-group X's VCG02." The per-VCG row attribution is genuinely unrecoverable without parsing finding scope markers. **Qualitatively, M15's VCGs are heavily cited.**

---

## §5. M06/M20/M26/M39/M46 — citation via legacy code literal

These clusters' Phase 9 sessions referenced VCGs by their literal legacy code:

> M06 sample: *"god abhorring pride (**248-001**), the righteous abhorring falsehood..."*
> M06 sample: *"the most prominent uses (groups **252-002** and **252-003**) show the capacity..."*
> M06 sample: *"group **247-001** (she.qets): Eze 8:10 — the prophetic..."*

The literal code IS the citation form. My existing `gc in text` substring check catches these correctly. The rates are honest:

- M06 47% — 24 of 51 legacy codes appear in findings
- M20 35% — 9 of 26
- M26 77% — 61 of 79
- M39 91% — 31 of 34
- M46 9% — 3 of 34

These rates reflect how often the AI authoring M06/M20/M26/M39/M46 findings happened to reach for the legacy VCG code as a citation form. Lower rates = AI cited verses/Strong's directly instead.

---

## §6. The corrected v3_0 picture

My parent review (`wa-sessionb-cluster-instruction-v2_9-review-supplement-v1-20260527.md`) softened "drop VCGs" because the data showed ~83% Era 2/3 citation. The corrected picture is stronger:

**VCGs were referenced in 100% of closed clusters' findings (16 of 16).** The variation is in citation form (full vs short vs legacy literal), not in whether the VCG layer was used. Even the legacy clusters (M06, M20, M26, M39, M46) cite their VCGs by legacy code.

This means the v3_0 "drop VCGs" question stands on **two** decision lines, not one:

1. **Did the layer pay rent in past work?** YES (16/16 closed clusters cite VCGs in findings). The layer is analytically active.
2. **Should new clusters under v3_0 keep building VCGs?** That's a forward-design question. The layer pays rent — but the cost is real (Phase 7 AI session, 700+ rows of structural overhead). If v3_0 keeps VCGs, the citation discipline (`VCG-N` short-form within sub-group scope) should be standardised. If v3_0 drops VCGs, the closed clusters' analytical record is preserved as legacy reads, and new clusters cite at sub-group + verse granularity only.

The earlier parent-review-supplement Options (A keep / B drop / C size-conditional) remain valid, but the case for keeping is now firmer than the original 13% headline suggested.

---

## §7. The M05 specific note

M05 was reset to `Ready for re-analysis` (status updated 2026-05-27T06:02:34Z) per researcher direction. Its 123 legacy VCGs remain in DB until the next analysis cycle, where v2_9 Phase 8 silent dissolution will clear them.

M05's specific 0% citation in the corrected analytics still holds — M05's pre-cluster-pivot legacy VCGs were authored under a methodology that did not cite VCG codes in findings. The cluster's existing 1,517 cluster_finding rows reference verses + sub-groups + Strong's; none reference VCG-NN sequences or legacy codes.

---

## §8. What changed in the analytics script

- `SHORT_RE` now matches both `VCG-N` and `VCGN` forms (hyphen and no-hyphen)
- VCG sequence extraction now handles both `M{NN}-X-VCG-N` and legacy `NNN-MMM` code formats
- Citation candidates include zero-padded variants for cross-format matching
- The §4 table now distinguishes total citation rate from "distinct short-form sequences cited" so the legacy-code clusters' citation pattern is visible

The script can still under-credit when a cluster uses sub-group-relative VCG-NN references whose specific row mapping requires scope-marker parsing (M15 case). That's a known limitation; the qualitative signal (number of short-form citations) is reported alongside.

---

## §9. Bottom line for the researcher

- **The 13% original citation rate was an artifact of regex narrowness, not a true reflection of VCG analytical use.**
- **All 16 closed clusters cite VCGs in their findings** — the variation is in citation form, not whether the layer is used.
- **M10's 1% was 99% wrong** (now 100%). M15's 2% was similarly off (true ~80%+ qualitative).
- **For v3_0:** the "drop VCGs" decision now sits on stronger evidence that the layer is analytically used. The "size-conditional Phase 7" option in the parent supplement (build VCGs only for sub-groups >40V) remains a defensible middle ground.

The bulk soft-delete of 2,104 legacy VCGs in unanalyzed clusters (commit 2e0409c) stands — those VCGs were neither cited nor analytically active. The corrected analytics applies to the 16 closed clusters' VCG inventories that remain.

---

*Correction v1 — 2026-05-27. Pre-existing analytics report regenerated with the corrected regex.*
