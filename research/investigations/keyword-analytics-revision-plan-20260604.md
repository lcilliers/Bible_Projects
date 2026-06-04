# Keyword analytics — revision plan (phrase-aware, two-axis)

> **Parked 2026-06-04 — to come back to.** Captures why the first keyword analytics were misleading and
> how to rebuild them. Triggered by the bias-trap review (`keyword-bias-extract-20260604.md`), which is
> itself parked.

## The flaw in the first cut

The first analytics (`anchor-meaning-analytics-20260604.md`) included a **single-token** frequency table.
That was misleading: it split each keyword phrase into words and pooled, e.g., `will` (70) across ~70
*different* interpretive claims (`will turning`, `will refusing`, `will captive`, `will oriented evil`…).
The phrase — not the token — is the unit of meaning.

## What the keywords actually are (probed 2026-06-04, n=1,207 over 226 anchors)

- **Word-count:** 1-word **81** · 2-word **1,098 (91%)** · 3-word **28**.
- **Grammar of the 2-word phrases:** `[HEAD] [QUALIFIER]`, noun-then-modifier (reversed from English).
  - **HEAD = inner-being faculty / entity** (the *subject* axis): will, guilt, sin, conscience, heart,
    salvation, inner, defilement, judgment, forgiveness, rescue, transgression, atonement, faith…
  - **QUALIFIER = interpretive predicate** (the *judgment* axis — **where bias concentrates**): divine,
    **eschatological**, absent, moral, corrupted, removed, saving, restored, active, received, covered…
- **1-word phrases** are a different shape — usually a state/verb with no head (`atoned`, `ransomed`,
  `rescued`, `delivered`); treat as QUALIFIER-only (or their own class).
- **Normalisation debt:** 34 phrases carry hyphens; the same concept splits on hyphen/spacing
  (`god-saving`/`god saving`; `christ-saving`/`christ saving`; `sin-laden`/`sin laden`) and on stem
  (`corrupt`/`corrupted`/`corruption`).

## Proposed rebuild

**1. Parse, don't tokenise.** For each keyword: lowercase → hyphen→space → split. Classify as
`(head, qualifier)` for 2-word, `(head, qual1+qual2)` or `(head, qualifier)` for 3-word, `(—, word)` for
1-word. Keep the **phrase** as the primary unit; the two axes are derived views.

**2. Three analytic cuts replace the token table:**
   - **HEAD axis** — which faculties/entities the meanings invoke (the inner-being map), overall + per cluster.
   - **QUALIFIER axis** — the interpretive predicates, overall + per cluster. *This is the audit's worklist.*
   - **HEAD × QUALIFIER** — e.g. does `will` attract `turning`/`refusing` (volitional) vs `captive`
     (bondage)? does `salvation` attract `eschatological` everywhere regardless of verse?

**3. Normalisation rules (the "rules in the words" you raised).** Open design choice — pick one:
   - *(a) Post-hoc canonicalisation* in the analytics only: a small synonym/stem map (hyphen-collapse,
     `corrupt*`→`corrupt`, `christ saving`=`christ-saving`). Cheap, non-invasive, but per-run.
   - *(b) Controlled vocabulary at source* — a canonical HEAD list (the faculties) and a governed
     QUALIFIER list, enforced when **Pass A emits keywords** (§c). Robust and reusable, but changes the
     emission contract and needs back-fill for the 226 already done.
   - Likely answer: **(a) now** for analytics, **(b) later** as part of the verse-meaning audit.

**4. Bias analysis rebuild.** Bias lives in the QUALIFIER axis. Re-aim the bias-trap from "pick a word"
to: **rank qualifiers by interpretive risk** (eschatological, corrupted, perverted, defiled, …) and pull
the verse+meaning for each, as in the parked extract — but driven by the qualifier list, and with the
HEAD held alongside (so `salvation eschatological` is judged against the verse's actual time-horizon).

## Scripts to revise (when un-parked)
- `_exploratory_anchor_meaning_analytics_v1_20260604.py` → v2: drop the single-token table; add HEAD,
  QUALIFIER, and HEAD×QUALIFIER cuts with normalisation.
- `_exploratory_keyword_bias_extract_v1_20260604.py` → v2: drive from a qualifier-risk list; carry HEAD.

## Open questions for the researcher (on return)
1. Normalisation: post-hoc map now, controlled vocabulary later — agree?
2. Should the **HEAD list be the faculties** (tie to the inner-being constitution / tiers), making the
   HEAD axis a direct map onto the study's faculty model?
3. Is keyword **structure itself a Pass-A rule** worth adding (always `[faculty] [predicate]`), so the
   data is born analysable? (Bears on the verse-meaning audit and §c keyword emission.)
