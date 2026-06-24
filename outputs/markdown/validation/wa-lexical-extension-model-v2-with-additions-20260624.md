# Extended lexical model — v2 (five additions folded in)

- **File:** wa-lexical-extension-model-v2-with-additions-20260624.md · **v2 · 2026-06-24 · Author:** Claude Code.
- **Supersedes the model in** `wa-lexical-extension-deepdive-into-01b-DESIGN-v1` **for the points below** (the design v1 still holds for the framing, the two scopes, type-conditioned expectedness, and re-run principles R1–R6). This folds in the **five additions** the tamim/cleanness test exposed, so the next clusters are run against the refined model. Destination: **01b v3** + the `ve_lexical` collection layer.

## The refined `object_type` + five additions

**A1 — `object_type` with a BEARER-CLASS sub-tag.** object_type is decided from per-verse-varying evidence, **and** sub-tagged by who/what bears it:
- `bearer = human-faculty` → CHARACTERISTIC (a person's faculty-in-operation);
- `bearer = divine` or `bearer = object/thing/way` → **QUALITY** (a property predicated of God or a thing, not a human inner characteristic).
- *Why:* tamim is a characteristic in "walk before me and be blameless" (human bearer) but a quality in "his way is perfect" (divine/way bearer) — same lemma, split by **bearer**, read per verse. Generalises the v1 "bivalent-faculty": **bivalence is by bearer and by valence.**

**A2 — intrinsic-faculty escape (resolves the characteristic↔faculty deadlock).** A CHARACTERISTIC *must* name a faculty (type-conditioned expectation), but we must not read it off the lemma-constant per verse. **Escape:** the required faculty may be supplied by the lemma's **intrinsic faculty** *as a collection-level property of the characteristic* (declared once, `derivation=intrinsic`), **not** asserted as a per-verse seat. So "tamim is conscience/integrity-faculted" is a property of the characteristic; it is **not** a claim that each verse seats conscience. (Per-verse seat still requires per-verse co-seating evidence.) This keeps P1/the validation rule intact while letting a characteristic satisfy its faculty-expectation.

**A3 — `transition-trigger.manner` slot {inner · ceremonial/bound-rite · NONE}.** For STATE/IDENTITY mutability, the trigger that changes the state carries a manner sub-slot — **homes the act-lemma how-gap**: cleansing's manner is `ceremonial/bound-rite` (the atonement procedure), not an inner disposition; a willing repentance would be `inner`. This captures *why* the how-field was empty on the act (the manner is bound/ceremonial), as a value, not a gap.

**A4 — inner-vs-outer REALM sub-register on STATE.** A state carries `realm = ritual/bodily · inner/moral · forensic · eschatological` (read per verse from object/co-seating). Cleanness is mostly `ritual/bodily` but flips to `inner/moral` in "clean of heart" (Psa 24:4, 2Ch 30:19) — captured as a realm sub-register, not lost. (This is the grounded form of the PU-1/PU-2 split — it lives as a realm tag on one state-family, not two imposed units, unless the realms are lexically distinct families.)

**A5 — enriched `compound`/`binding` as a real PER-VERSE role field.** Replace the coarse 3-value role (94% "partner") with a per-verse role-type: `partner · qualifier · object · cause · manner · expresses · seat · pole-opposite · unmarked`. The **binding** (synthesis-relevant subset = roles manner/expresses/seat/pole-opposite) is read per verse, so it **varies by situation** (confirmed by hand). This is the prerequisite for the binding-web; it is also a re-deep-dive driver (enriching it re-runs affected verses).

## Carried forward from v1 (unchanged)
- Two scopes (per-verse + collection); object_type closes 01b §8.
- Type-conditioned expectedness = the LRT made canonical (a STATE must say of-what/who-set/can-change/what-changes; a CHARACTERISTIC must have a faculty; etc.).
- New items mutability, transition-trigger, binding, pole-relation.
- Re-run R1–R6 (mechanical-vs-captured split; reset scopes; versioned re-assess-with-diff; idempotence=drift-detector; pipeline re-run for parked clusters; recovery-as-rule).

## Open (to surface as we run more clusters)
- Is a 7th object-type needed (e.g. a pure RELATION/bond, or a PROCESS)? Watch M16/others.
- Does `realm` (A4) generalise to all states, or only purity?
- How many compound roles are really needed (A5) — converge the vocabulary over clusters.

*Model v2 — object_type now bearer-class-aware (A1) with an intrinsic-faculty escape (A2); transition-trigger carries manner (A3); STATE carries a realm sub-register (A4); compound/binding is a real per-verse role field (A5). Run the next clusters against this; fold the convergent result into 01b v3.*
