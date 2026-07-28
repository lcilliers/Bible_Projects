---
name: project_iba_candidate_seeding_registry_direct_noise
description: RESOLVED (07-19) IBA candidate seeding created candidates from word_strong co-occurrence (rejected route) → function-word noise; fixed to double-control-only + re-ran all books.
metadata: 
  node_type: memory
  type: project
  originSessionId: 2ee622d9-8c67-4b2e-8b05-bb085a4f2cfc
---

**RESOLVED 2026-07-19.** In the IBA app (`iba/app/db/iba.db`), candidate characteristics
(`span_candidate`) were being polluted by function words ("upon" H5921, "to be" H1961,
"day" H3117, "hand" H3027). **Root cause** (not what the original note guessed): the
`candidate.seed` handler ([`iba/app/handlers/candidate.py`](iba/app/handlers/candidate.py))
had a block that **created a candidate for any lemma whose base-Strong's was carried by any
registry word's `word_strong` list** — i.e. seeding from registry *co-occurrence*, the
route the method docs explicitly REJECT ("LORD→lust" noise;
`wa-characteristic-role-lexical-cycle-authoritative-v1-20260708.md` §4/§11). ~1,073 of 2,805
candidates were this noise.

**Fix:** registry coverage (`word_strong`) is now the **double-control ONLY** — it sets
`registry_match` on already-independent candidates, never creates candidacy. Candidacy is
meaning-based only: the migrated independent net (gloss/synonym via `char_matched`,
`ib_candidate`) + read-emergent + the editable `cfg_candidate_rule` (synonym/accept/reject,
loaded from [`iba/app/config/candidate.json`](iba/app/config/candidate.json)). Re-ran the
seed migration → **1,732 clean candidates** (was 2,805); re-stamped + re-passaged all 66
books → **18,571 passages, max length 26, only 25 needs_review** (was runaway chains).
Aligns with [[feedback_candidate_seed_independent_over_inclusive_control]] and
[[feedback_characteristic_list_validates_not_imputes]].

**Residual (by design, not a bug):** top remaining candidates are generic motion/speech
verbs (asah, bo, halak, amar, raah, shuv) promoted by the read-emergent layer with
verse-specific tags. Meaning-based and intentionally over-inclusive — the lexical (Axis B
role) stage is the definitive test; they no longer over-chain passages. Review doc:
`docs/iba-set-candidates-config-review-v1-20260719.md`.
