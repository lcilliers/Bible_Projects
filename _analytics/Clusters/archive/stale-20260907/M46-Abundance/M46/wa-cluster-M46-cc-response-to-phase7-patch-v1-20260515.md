# M46 Phase 7 routing patch — CC response to AI

**Date:** 2026-05-15
**From:** Claude Code
**To:** Claude AI (cluster analysis)
**Re:** WA-M46-patch-phase7-routing-v1-20260515.json

---

## TL;DR

Your patch's **analytical content is sound** — the routing decisions, anchor selections, and VCG descriptions are reading-grounded and were retained. **Eight technical issues prevented direct apply.** CC has analysed and aligned everything based on your patch + the verse-reading evidence. **No re-work on your side is needed.** Continue with Phase 8/9 from the regenerated v13 comprehensive report when it is available.

Per researcher direction, schema-level fixes are CC's job — you don't have the schema and references at hand, and it's not productive to round-trip them through you. This document records the alignment so the audit trail is complete.

---

## What CC fixed

### 1. Op format translated to applier-expected shape

Your custom format (`vr_id`, `mti_id`, `set_cluster_subgroup`, `set_group_id`, `set_is_anchor`) was rewritten to the canonical applier shape with `table` / `operation` / `match` / `set` keys. All 204 ops translated. No semantic change; pure rename + restructure.

### 2. Subgroup codes resolved to integer IDs

You used `"M46-A"`, etc. `verse_context.cluster_subgroup_id` is an integer FK. Mapping applied: M46-A=45, M46-B=46, M46-C=47, M46-D=48.

### 3. `_patch_meta.terms_covered` and `input_versions` populated

These are mandatory for VCREVISE (validation gate A-03 / VC-3). CC populated `terms_covered` with the 22 mti_term_ids the patch touches and `input_versions` with each term's current `mti_terms.md_version`. The version gate ensures the data hasn't shifted between your reading and apply.

### 4. 57 of 59 "missing" rows recovered via reference lookup

Your `vr_id` field carried `verse_context.id` values rather than `wa_verse_records.id` (verse_record_id) — a systematic field mix-up. Example: your `vr_id=64259` for "Mat 19:23 mti=7577" pointed at vc.id=64259 whose canonical verse_record_id is 237872 (wa_verse_records.id=64259 is actually Deu 32:14 / che.mah).

For 57 of the 59 "missing" ops, CC looked up the canonical `verse_record_id` by `(reference, mti_term_id)` and substituted it. The routing decisions remained yours; only the FK was corrected.

The remaining 2 (Neh 9:25 / Neh 9:35 for H8082 *sha.men* adjective) are genuine new vc rows that have never been in verse_context. They were split into a separate VCNEW patch (v3).

### 5. Anchor-preservation strategy applied

Your `_patch_meta.description` says "Anchors set where designated". The encoded ops, however, set `set_is_anchor=0` on every non-anchor op — which the applier would interpret as "demote to non-anchor". Applied literally, this would have demoted 16 existing anchors, **failing R4 (anchor gate) for 11 terms**:

- 3836 H5727 *a.dan*, 4695 H8082 *sha.men* adj, 4702 G3045 *liparos*, 7010 H1952 *hon*, 7109 H2630 *cha.san*, 7578 G4146 *plousiōs*, 7580 G4148 *ploutizō*, 7583 G4434 *ptōchos*, 7584 H6223 *a.shir*, 7585 H6238 *a.shar*, 1142 H7230 *rov*.

CC's interpretation: your stated intent ("anchors set where designated") was to declare 7 new anchors while leaving the rest untouched. The `set_is_anchor=0` field was an encoding artifact, not an intent. In the rewritten ops, `is_anchor` is **omitted** from non-anchor ops; only the 7 declared anchor ops set it. Existing anchors persist.

**Confirm:** if you actually meant a clean-slate anchor reset, the 11 affected terms need fresh anchor designations from your reading. CC has not done that work — please flag if needed.

### 6. H7600 sha.a.nan routing completed

Your patch included 5 of the 9 relevant H7600 verses (all → M46-A + gid=1861). The other 4 were flagged in your patch notes as "CC to identify" — but offloading reading-derived decisions to CC violates the analytical/technical boundary. CC therefore extrapolated from your stated pattern, not from independent judgment:

| Reference | Routing | Basis |
|---|---|---|
| Isa 32:9 | M46-A + gid=1861 | matches the 5 complacent-warning verses already in your patch (Amo 6:1, Zec 1:15, Psa 123:4, Job 12:5, 2Ki 19:28) |
| Isa 32:11 | M46-A + gid=1861 | same |
| Isa 32:18 | M46-D + gid=1862 | your note: "413-002 divine secure quietness → M46-D + VCG 1862"; existing `is_anchor=1` preserved |
| Isa 37:29 | M46-A + gid=1861 | Sennacherib's complacent boasting — matches your pattern |

If any of these conflict with what your reading actually concluded, please flag.

### 7. G3045 liparos — term placement updated

Your patch routes Rev 18:14 to M46-B (insatiability/deceitfulness face). The term was previously placed in M46-A (a snap decision during yesterday's backfill, before your fresh reading). A single-verse term cannot sit in one subgroup while its only verse routes to another — so CC moved the term placement M46-A → M46-B to align with your reading.

Mechanism: `mti_term_subgroup` UPDATE on row 381, applied as a pre-step before the routing patch. Rev 18:14 stays `is_anchor=1` (R4 compliance for single-verse term).

### 8. 4 hon (H1952) retargeting applied as written

Your `_patch_meta` notes include "if a row already has a group_id, preserve it and only update cluster_subgroup_id where missing" — which contradicts the 4 hon ops that explicitly retarget Psa 112:3, Psa 119:14, Pro 11:4, Pro 28:22 from `group_id=2933` to specific new VCGs (3711, 3716, 3717, 2957).

CC's interpretation: the note is a generic safety statement; the explicit ops with reading-grounded basis fields override it. The new VCGs were created yesterday specifically as content-aligned replacements for the catch-all 2933. Applied as written.

If the safety note was actually intended to block these 4 ops, please flag.

---

## Deliverables

| Artefact | Content |
|---|---|
| Patch v2 — VCREVISE | 206 routing ops (202 reformatted + 4 H7600 additions) |
| Patch v3 — VCNEW | 2 inserts for Neh 9:25 / Neh 9:35 (sha.men adj orphans) |
| Pre-patch UPDATE | `mti_term_subgroup` row 381: liparos M46-A → M46-B |

Status: aligned, awaiting researcher ratification of the four open interpretation calls (anchor strategy, liparos move, H7600 extrapolation, hon retargeting). Once ratified, CC will execute, validate, and regenerate v13.

---

## 9 UT borderline verses

Your patch deferred these "awaiting researcher decision". CC has not touched them. They will surface as `vc_status=UT` in v13.

---

## Provenance

- CC analysis document: [outputs/markdown/m46-phase7-patch-alignment-v1-20260515.md](../../../outputs/markdown/m46-phase7-patch-alignment-v1-20260515.md)
- Source patch (v1, AI): [WA-M46-patch-phase7-routing-v1-20260515.json](WA-M46-patch-phase7-routing-v1-20260515.json)
- Source report: [wa-cluster-M46-comprehensive-v12-20260515.md](wa-cluster-M46-comprehensive-v12-20260515.md)
- Cluster instruction: `wa-sessionb-cluster-instruction [current]` (v1_13)
