# Autonomous progress log — lexical deep-dive refinement (2026-06-24)

- **File:** wa-autonomous-progress-log-lexical-refinement-20260624.md · **2026-06-24 · Author:** Claude Code.
- **For:** the researcher's return. What I did autonomously, the state, and what's next. Everything is committed; nothing touched the DB.

## What I did (the loop you asked for: capture deep-dive · check missing/expected/derivable · record Q&A · build back into 01b + ve_lexical)

1. **Folded the five additions** from the tamim/cleanness test → **model v2** (`wa-lexical-extension-model-v2-with-additions`): object_type bearer-class (A1), intrinsic-faculty escape (A2), transition-trigger.manner (A3), STATE realm sub-register (A4), enriched per-verse compound roles (A5).
2. **Opened the discovery register** (`wa-lexical-discovery-register-v1`) — the running Q&A: *what's missing / expected / derived-in-collection / how-derived*, with status (folded / open).
3. **Ran the collection-lexical deep-dive on five more clusters** under the model, each LRT-gated, object-type from per-verse-varying evidence only, every value tagged mechanical-vs-captured:
   - **M13 Truth · M14 Deceit · M16 Folly** (Round 1) — `Sessions-v2/M{13,14,16}-*/findings/wa-m*-collection-lexical-v1`.
   - **M19 Trust · M20 Doubt** (Round 2) — same.
4. **Built it back into the canonical guide:** **01b → v3, new Part C** (the COLLECTION layer) — two scopes, `object_type` (resolves 01b's parked §8), type-conditioned expectedness (= the LRT made canonical), the new collection items, re-run principles R1–R6, and the `ve_lexical` term-scope storage (C.6). Round-2 confirmations firmed in.

## The headline — the model converged

Tested across **six clusters** (M12/M13/M14/M16/M19/M20 + the two-term test), spanning state-heavy (purity), quality/characteristic (truth), rich-mixed (deceit), multi-kind (folly), and affect/volition (trust/doubt):

- **The six object-types are STABLE — no 7th was needed on any cluster.** characteristic · state/condition · expression · qualifier · identity · bivalent-faculty.
- **~78–81% of every cluster's values are mechanical-rule** (regenerate idempotently) — clears the reproducibility aim (R1); the rest is captured-read (preserved).
- **The discipline held throughout** — not one object-type was read off a lemma-constant; the faculty-tag (the M10/M11 trap) was refused every time.
- **Confirmed + firmed (multi-cluster):** `transitivity` (load-bearing — it *predicts* bivalence), `membership_scope` (bivalent = per-occurrence), `role-in-cluster` (+`alien` for provenance-intruders), the **bivalent object-discriminator** (the object/aim sets valence — trust in God vs in wealth), `cognate-link` (act↔state↔identity of one root), and the realm/manner vocabularies (extended per cluster).
- **The model even refined an OLD cluster:** run on M20 (old 4 chars) it held 3/4 and **correctly split the 4th** (Doubt+Indecision → Doubt + Perplexity).

## State of the fact-base
- **01b is now v3** with Part C — the canonical home of the deep-dive understanding, captured for re-use.
- **Discovery register** holds Rounds 0–2 (the Q&A) + the folded-into-01b log.
- **Still [prov]** (not yet exercised, awaiting the right cluster): `classifier` (needs an identity-heavy cluster), `asah`-deed override (needs a deed cluster).
- **Main build prerequisite:** the **enriched per-verse compound field (A5)** — the live field is still ~90% flat "partner"; the binding-web needs it. This is a *code* change to the VE generator (not yet done).

## What's next (for your steer)
1. **Build the A5 enriched compound field** in the VE generator (the one prerequisite) → then the binding-web becomes real.
2. **Build the collection-lexical generator** (object_type + the C.4 items from the per-verse rows + cross-verse rules) → so the collection layer is *generated*, not hand-built, and regenerates per R1–R6.
3. **Confirm the [prov] items** by running an identity-heavy / deed cluster (e.g. an "office/role" or "deed" cluster).
4. Keep widening coverage (more clusters) if you want more confidence before locking, but the model has converged — I'd lean to **building the generator next** over more hand-runs.

## BUILD PHASE (2026-06-24, later) — the collection-lexical generator is LIVE in the DB

On your go-ahead to build incl. the DB:
- **New additive table `term_collection_lexical`** (term-scope: ve_label · value · derivation · model_version · source_ref). Created without touching the per-verse `ve_lexical` or the engine's schema_version (lowest risk; a formal migration/version-bump can follow).
- **Generator `scripts/_apply_generate_collection_lexical_20260624.py`** — reads the DB per-verse `ve_lexical` (via `verse_context.mti_term_id`), derives object_type + collection items by deterministic rule, writes term-scope rows. Idempotent per cluster (R4).
- **The object_type rule was TUNED against the hand-built M12 map (the validation):** dropped faculty as a driver (the lemma-constant trap it kept re-introducing — katharos/hagnos were wrongly "characteristic"); thresholded bivalence (naqi's stray sinful no longer mis-fires); bivalent-faculty = real-bivalence + faculty-engaged (else a valence-varying STATE with a realm split, e.g. tum.ah); action→expression; status/quality→state; **characteristic and faculty-gap bivalence deferred to read-promotable CANDIDATE flags** (honest R1 — mechanical-first, read-promote).
- **LIVE on 6 clusters** (M12/M13/M14/M16/M19/M20): **1,035 rows**; object_type = state 117 · expression 55 · bivalent-faculty 11 · UNRESOLVED 5; +23 `bivalence_candidate` +12 `characteristic_candidate` flags.
- **Generalises to UNSEEN clusters** (dry-run, no hand-analysis): M17 Counsel · M18 Hope · M21 Prayer · M23 Strength · M28 Envy · M29 Desire · M33 Peace all produced sensible distributions (Prayer expression-heavy; Envy/Desire/Counsel show bivalent). Runs on any cluster via `--cluster Mxx --live`.

### Known limits (logged, not blockers)
- **Faculty signal-list gap** under-detects bivalent-faculty for untagged faculties (e.g. *trust* ba.tach has valence flipping righteous/sinful but faculty=0 rows → called expression + `bivalence_candidate`). Fix = extend the faculty lemma-list (then bivalent auto-detects).
- **`characteristic` is not auto-called** (the faculty trap) — surfaced as `characteristic_candidate` for read-promotion (e.g. tamim).
- **A5 enriched per-verse compound** still pending — the binding-web needs it (live field ~90% flat "partner").
- Valence coverage varies per cluster (drives bivalent detection).

### Next
1. **Extend the faculty signal-list** (cheap, high-value — unlocks bivalent auto-detection for trust/affect-volition lemmas).
2. **Build A5** (enriched per-verse compound role) → the binding-web.
3. **Populate the collection layer across all clusters** (the generator is ready; a `--live` sweep) — your call on scope (incl. parked/old clusters).
4. A read pass to promote the candidate flags (characteristic / bivalence) where the evidence supports.

*Autonomous session — model v2 → 6 clusters collection-lexical → 01b v3 Part C → Round-2 firm-ups → the collection-lexical GENERATOR built + LIVE in the DB (1,035 rows, 6 clusters, generalises to all). Six object-types stable, ~80% mechanical, discipline intact (faculty trap caught + removed during the build). Next: extend faculty list + build A5 compound + sweep all clusters.*
