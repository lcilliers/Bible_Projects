---
name: feedback_test_dimensions_for_reader_drift
description: "A dimension's vocabulary can drift with reading-order (process, not text); band-test before trusting it."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 6b56630f-0f9e-4733-abf8-f856527e68ee
---

A re-read dimension can silently record the **reading process rather than the text** — its controlled vocabulary drifts as the reader calibrates across the book. Proven on Psalms `type(102)`: `type=faculty` exists only in Ps 76–138; `action` is 0% in Ps 1–25 then 50% mid-book; `affect`/`volition`/`cognition` vanish through the middle and return. `locus(116)` was a blanket 100% `internal:ib-state` in Ps 1–25 (early convention) before differentiating. A whole-book profile of such a dimension is a reading-order timestamp, not a finding — it broke the AI's I-3 (faculty↔inward) headline.

**Why:** reliability is **two-axis** — (1) *stability* (does the vocabulary drift with position?) and (2) *provenance* (read vs derived). `type` fails stability; `effect`/`intensity`/`specifier` fail provenance (derived floor); `direction`/`device` pass both. A dimension can be honest on one axis and worthless on the other; vouching for "the dimensions" without testing each is the error I made.

**How to apply:** run the band-drift screen (`scripts/_check_dimension_band_drift_v1`) on any re-read dimension before analysis — split the book into chapter-bands, flag any common value that is 0% in a band. Confirm reader-drift vs genuine text-silence with an a-priori test (a value that *cannot* truly be absent from a whole region = drift). Free-text dims aren't testable this way. Ground findings on **stable** dimensions (`direction`) + **invariant** keys (`lemma`), never on `type`. See [[project_ve_lexical_is_verse_first]], [[feedback_no_stats_trends_review_fabricated_data]]. Register: `outputs/projections/WA-dimension-reliability-register-v1-20260714.md`.
