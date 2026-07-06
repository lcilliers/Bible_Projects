# Gate-1 orphan terms — FINAL registry mapping + onboarding execution plan (v2)

> Supersedes v1. Incorporates the researcher's 2026-07-06 directives: registry need not be perfect — each term just needs a home; **no owner reassignment** (Group A keeps its surviving homes); **§3.4** — Satan = third-party (→ `spiritual powers`, reference role), vileness = wickedness, the rest of §3.4 onboarded but roled as **qualifiers**; **§3.1–§3.2 accepted as suggested** (collapsed to a single home each). **All 97 covered; 53 target registries; 1 new registry (`salvation`).** Render/validate: `scripts/_build_gate1_registry_final_map_v1_20260706.py`.

---

## 1. Final mapping — by target registry (= onboarding batches)

`*` = qualifier/reference role (not a characteristic); the term is still onboarded and gets a home, its role lives on `ve_lexical`. **`salvation` is the only new REGISTER.**

- **agony** (1): H2427 agony
- **anguish** (1): H2342 to twist/tremble
- **betrayal** (1): H5800 to forsake
- **bitterness** (1): H2556 to leaven*
- **blessing** (1): H0835 blessed (ʼashrê)
- **contempt** (4): H3887 to mock, H3932 to mock, H3933 derision, H7047 derision
- **contentment** (1): H7646 to satisfy
- **contrition** (1): H1793 contrite
- **corruption** (1): H0444 to corrupt
- **covetousness** (1): H1214 to cut off
- **craving** (1): H6770 to thirst
- **deceit** (5): H2665 plot, H3576 to lie, H3577 lie, H6601 to open wide*, H7723 vanity/false
- **delight** (1): H6149 to please
- **desire** (1): H3970 desire
- **disobedience** (3): H7683 to go astray, H7686 to wander, H8582 to go astray
- **distress** (3): H6323 to distract*, H6817 to cry out*, H6962 to loathe *(Group A: keep)*
- **doubt** (3): H5640 to close*, H5641 to hide, H7279 to grumble
- **evil** (1): H2154 evil (zimmah)
- **foolishness** (2): H0981 to speak rashly, H6612 simple
- **gentleness** (1): H6039 affliction *(Group A: keep)*
- **grief** (1): H8428 to wound
- **heart** (1): H5036 foolish *(Group A: keep)*
- **hope** (2): H3684 fool *(Group A: keep)*, H3689 loins/hope*
- **humility** (1): H8217 low
- **hypocrisy** (1): H2611 profane*
- **longing** (3): H3642 to pine, H6165 to long for, H8373 to long for
- **love** (1): H2898 goodness *(Group A: keep)*
- **mourning** (1): H7908 bereavement
- **obedience** (1): H5341 to watch/keep
- **peace** (1): H1747 silence*
- **perverseness** (1): H6141 twisted
- **praise** (1): H7321 to shout
- **pray** (1): H6419 to pray
- **prayer** (1): H8605 prayer
- **pride** (3): H6277 arrogant, H7342 broad*, H7426 be exalted
- **purity** (4): H1249 pure, H1252 cleanness, H1305 to purify, H2135 to clean
- **rebellion** (1): H4784 to rebel
- **rejection** (3): H2186 to reject, H3988 to reject, H5010 to disown
- **rejoicing** (3): H5937 to exult, H5970 to rejoice, H7832 to laugh/rejoice
- **salvation** **[NEW]** (4): H3468 salvation, H4190 salvation, H5826 to help, H8668 deliverance
- **shame** (2): H5949 wantonness *(Group A: keep)*, H7045 curse *(Group A: keep)*
- **spiritual powers** (1): H7854 Satan* *(third party)*
- **strife** (3): H4066 strife, H7283 to throng*, H7853 to oppose
- **surrender** (1): H8444 outgoing *(Group A: keep)*
- **temptation** (2): H0974 to test, H5254 to test
- **terror** (1): H1161 terror
- **testimony** (1): H5046 to tell/declare
- **weakness** (6): H0536 weak, H2489 helpless, H3021 be weary, H5848 to faint, H6199 destitute, H7326 be poor
- **whoredom** (1): H5003 to commit adultery
- **wickedness** (4): H2149 vileness, H2555 violence, H6231 to oppress, H8496 oppression*
- **wisdom** (2): H2451 wisdom, H4148 discipline (musar)
- **worth** (2): H3365 be precious, H3368 precious
- **wrath** (2): H5359 vengeance, H5360 vengeance

---

## 2. Onboarding paths differ by group

| Group | Count | State | Path |
|---|---:|---|---|
| **A — already OWNER** | 8 | inventory OWNER row survived; only `mti_terms` deleted (OT-DBR-009) | **Reconcile** — recreate the `mti_terms` row against the existing inventory/registry; GAP_FILL any missing verse-records; cluster-assign. No new REGISTER, no re-fetch. |
| **B — XREF only** | 8 | cross-ref in other registries, never OWNER | **OWNER-promote** into the assigned home registry via curated onboarding. |
| **C — no inventory** | 81 | truly un-onboarded | **Full onboarding** via curated audit_word. |

Group A: H2898, H3684, H5036, H5949, H6039, H6962, H7045, H8444.
Group B: H2154, H2451, H3689, H3970, H4066, H6419, H7832, H8605.

---

## 3. The per-term recipe (established tooling, curated gate)

Per the validated onboarding memory — **use the curated-extract path, NOT `--fetch-step`** (which cascades STEP `relatedNos` noise into the DB):

1. `python scripts/word_study_extract.py --word <english> --anchors <strongs…>` → **trim the extract's `terms` array to exactly the wanted strong(s)** (the contamination gate) → save curated JSON.
2. New registry only (`salvation`): `python -m engine.engine --register --word="salvation" --source="gate1-recovery"` first.
3. `python -m engine.engine --mode=audit_word --registry=N --extract-file=<curated.json>` → builds `wa_file_index`, `mti_terms` (owned), `wa_term_inventory` (OWNER), `wa_verse_records` for **all** occurrences programme-wide, meaning, flags, WR-audit.
4. Finishing fields the engine leaves NULL: `mti_terms.status='extracted'`, `delete_flagged=0`, `owning_registry_fk`, `cluster_code`; `wa_term_inventory.term_owner_type='OWNER'`; `wa_file_index.testament_coverage`.
5. `python scripts/_apply_create_vc_for_onboarded.py --registries N` → `verse_context`.
6. Cluster assignment (`mti_term_subgroup`) — per the cluster mapping in `wa-psalms-gate1-new-terms-cluster-and-occurrence-gap-20260706.md`.
7. `python scripts/_apply_generate_ve_lexical_v2.py --live --vcids @file` (scopes to `cluster_code IS NOT NULL`, so do after step 6).
8. **Re-run Psalms role** so the now-onboarded spans carry their role on the proper foundation; validate Gate-1 the established way.

**Integrity gate around every write:** backup DB → `_check_integrity_controls.py --snapshot` (pre) → write → snapshot (post) → `--compare` (expect exactly +terms/+verses/+reg, **no new invariant breach**). On unexpected deltas, restore and redo.

---

## 4. Recommended sequencing — PILOT first

53 registries × (STEP pull + audit + VC + cluster + integrity) is a large, careful operation the onboarding memory says to run deliberately (not bulk-blast). Proposed:

1. **Pilot: the new `salvation` registry** (4 terms) end-to-end through steps 1–7 + integrity — proves the full chain on a fresh REGISTER and a multi-anchor batch.
2. **Then Group C existing-registry batches**, a handful of registries at a time, integrity-gated.
3. **Then Group B** (OWNER-promotion) and **Group A** (light mti reconcile).
4. **Finally** re-run role + Gate-1 validation across all onboarded terms.

*Filed 2026-07-06. All 97 terms verified covered. Nothing written to the DB by this document — awaiting GO on the pilot.*
