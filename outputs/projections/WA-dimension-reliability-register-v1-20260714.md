# Dimension reliability register — re-read projection (v1, 2026-07-14)

**Why this exists.** The AI's round-2 Psalms pass retracted its own headline (I-3, faculty↔inward) after finding
that `type(102)` **records the reading process, not the text**: `type=faculty` exists only in Ps 76–138,
`action` is 0% in Ps 1–25 then 50% mid-book, `affect`/`volition`/`cognition` vanish through the middle and
return. My first assessment vouched for the dimensions **without testing them for drift** — that was the error.
This register is the corrective: every dimension classified on **two independent axes**, with a reusable test.

Diagnostic: `scripts/_check_dimension_band_drift_v1_20260714.py` (band-drift screen). Reports:
`outputs/projections/{psalms,proverbs}_dimension_drift_report_v1_20260714.md`.

## The two axes

- **Stability** — does the dimension's *vocabulary* drift with chapter position (reader calibration) or is it a stable text property? Tested by the band-drift screen; confirmed by an a-priori check (a value that *cannot* be truly absent from a whole region — e.g. `action` across 25 psalms — is drift).
- **Provenance** — is the value **read** off the verse or **derived** (a regex floor over the reading prose)? Derived values are honest but conservative; `NONE` is a floor, not a measured silence.

A dimension is trustworthy only if it passes **both**. `type` fails stability; `effect` fails provenance — different failures, both real.

## The register (Psalms; Proverbs noted where it differs)

| ve | dim | stability | provenance | **use it for** |
|---|---|---|---|---|
| 118 | direction | **stable** (band-flat 45.9–50.9% toward-god) | **read** | ✅ trustworthy — movement vector |
| 117 | device | **stable** | **read** | ✅ trustworthy — imagery/figure (vehicle as text; 5 span-edges) |
| 115 | role | stable | read | ✅ characteristic/qualifier/standalone |
| 104 | seat | stable | read | ✅ but named in only ~4.8% of readings (mostly assessed-none) |
| 105 | bearer | stable (Psalms) | read | ✅ Psalms. ⚠ Proverbs `bearer` flags on the screen — **likely genuine** (righteous/wicked material clusters), not drift; confirm before positional use |
| 101/114/106/103/108/112/113 | sense/reading/operation/source/manner/coupling/prohibition | free-text (N/A) | read | ✅ **evidence prose** — the primary text; not a controlled vocab |
| 116 | locus | ⚠ **early-band drift** — Ps 1–25 is **100% internal:ib-state** (blanket convention); differentiates only from ~Ps 26 | read | ⚠ trustworthy from ~Ps 26 on; **do not use for Ps 1–25**; Proverbs clean |
| 107 | target | ⚠ recording-practice drift on `none` (0–37% across bands) | read | ⚠ substantive targets ok; the `none` rate is a reader artefact |
| 109/110/111 | intensity/specifier/effect | stable vocab | ⚠ **derived (floor)** | ⚠ indicative only; `effect` NONE is not measured silence — real read scheduled (`WA-psalms-effect-read-phase2-spec-v1`) |
| 102 | **type** | ❌ **reader-drift (CONFIRMED)** — process, not text | read | ❌ **do not use** for positional / cross-section / cross-book analysis. A whole-book type profile is a reading-order timestamp. Drifts in both books. |

## What this does to the round-1 findings

- **I-3 (faculty↔inward) — RETRACTED.** It rested on `type`, which drifts; `type=faculty` only exists Ps 76+. Correct call by the analyst.
- **M-01 (seat-word inwardness) — STANDS**, re-grounded on **lemma** (invariant, and what the original-language rule requires): seat-words (leb/lebab/nephesh/ruach) read `inward` far above every other lemma and `static` far below, holding across all chapter bands (not a Ps-119 effect). Non-tautological: God-ward seat-readings (e.g. "Bless the LORD, O my soul", Ps 103:1) tag `toward-god`, not `inward` — `direction` reads the **act**, not the word. It survives because it uses `direction` (stable) + `lemma` (invariant), avoiding `type`/`locus`.

## DQ-05 — direction inconsistency (bounds M-01)

Psa 86:12 and Psa 111:1 are identical on every field — `heart` (H3824) / operation `give thanks` / "with the whole heart" — yet Psa 86:12 heart tags `inward` and Psa 111:1 heart tags `toward-god`. ~20% inconsistency on that subset. Does not overturn the ~27× seat-word differential, but bounds how hard M-01 can be pushed before an audit. **Logged for a direction-consistency pass on the seat-word + give-thanks subset.**

## Remedies (proposed, not yet done)

1. **`type(102)`** — retire from analytical use, or re-read to a fixed controlled vocabulary in one pass (it is currently a reading-order record). Highest priority — it is a core dimension currently misleading.
2. **`locus(116)` Ps 1–25** — re-read to break the 100% internal:ib-state blanket (the early calibration band).
3. **`effect(111)`** — the scheduled Phase-2 real read (separate from drift).
4. **DQ-05** — direction-consistency audit on the seat-word subset.
