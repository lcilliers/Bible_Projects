# M46 Phase 7 routing patch — CC alignment analysis

**Date:** 2026-05-15
**Source patch:** [Sessions/Session_Clusters/M46/WA-M46-patch-phase7-routing-v1-20260515.json](../../Sessions/Session_Clusters/M46/WA-M46-patch-phase7-routing-v1-20260515.json)
**Source report:** [Sessions/Session_Clusters/M46/wa-cluster-M46-comprehensive-v12-20260515.md](../../Sessions/Session_Clusters/M46/wa-cluster-M46-comprehensive-v12-20260515.md)
**Status:** CC analysis complete — recommended alignment outlined; awaiting researcher ratification before execution.

---

## 1. Summary

AI submitted a 204-op Phase 7 routing patch derived from a full re-read of every M46 verse. The analytical content (routing decisions, VCG descriptions, anchor selections) is high-quality and reading-grounded. **The technical encoding has eight defects that prevent the patch from applying as written.** None require AI to redo analytical work; all can be resolved by CC because they are format/schema/lookup issues.

Per researcher direction (2026-05-15): "AI does not have the full schema and references at hand, and getting AI to fix it is of no value." This document records the alignment work CC will perform.

---

## 2. Defects found

### 2.1 BLOCKING — Wrong op format (custom vs applier-expected)

AI used a custom JSON shape:

```json
{"op_id": "OP-001", "operation": "VCREVISE", "vr_id": 1134, "mti_id": 111,
 "set_cluster_subgroup": "M46-C", "set_group_id": 50, "set_is_anchor": 0, ...}
```

`apply_session_patch.py` expects the standard table/operation/match/set shape:

```json
{"op_id": "OP-001", "table": "verse_context", "operation": "update",
 "match": {"verse_record_id": 1134, "mti_term_id": 111},
 "set": {"group_id": 50, "cluster_subgroup_id": 47}}
```

Field renames required: `vr_id` → `verse_record_id`; `mti_id` → `mti_term_id`; `set_group_id` → `set.group_id`; `set_cluster_subgroup` (string "M46-A") → `set.cluster_subgroup_id` (integer); `set_is_anchor` → `set.is_anchor`.

**Resolution (CC):** mechanical rewrite of all 204 ops.

### 2.2 BLOCKING — Subgroup codes are strings, applier needs integers

AI emitted `"set_cluster_subgroup": "M46-A"`. The applier has zero code paths that resolve subgroup codes; verse_context.cluster_subgroup_id is an integer FK.

Mapping (current DB):

| Code | id |
|---|---|
| M46-A | 45 |
| M46-B | 46 |
| M46-C | 47 |
| M46-D | 48 |

**Resolution (CC):** translate during rewrite.

### 2.3 BLOCKING — Patch missing `_patch_meta.terms_covered` and `input_versions`

VCREVISE patches are required to declare `terms_covered` (array of mti_term_ids) and `input_versions` (map of `{mti_term_id: md_version}`). Validation gate A-03 rejects the patch outright.

**Resolution (CC):** populate from DB. 22 mti_term_ids; current md_versions:

| mti_id | strongs | md_version |
|---|---|---|
| 111 | H1878 | 2 |
| 413 | H7600 | 2 |
| 681 | H2633 | 2 |
| 1142 | H7230 | 2 |
| 3836 | H5727 | 1 |
| 4695 | H8082 | 2 |
| 4696 | H4924B | 2 |
| 4697 | H8080 | 2 |
| 4702 | G3045 | 2 |
| 4898 | G0842 | 1 |
| 7010 | H1952 | 3 |
| 7109 | H2630 | 1 |
| 7577 | G4145 | 2 |
| 7578 | G4146 | 2 |
| 7579 | G4147 | 2 |
| 7580 | G4148 | 2 |
| 7581 | G4149 | 2 |
| 7582 | G4433 | 2 |
| 7583 | G4434 | 2 |
| 7584 | H6223 | 2 |
| 7585 | H6238 | 2 |
| 7586 | H6239 | 2 |

### 2.4 BLOCKING — 57 of 59 "missing" ops actually use wrong vr_id

Pre-flight reported 59 ops where the `(vr_id, mti_id)` tuple has no verse_context row. Deeper investigation: AI populated the `vr_id` field with **verse_context.id values** (the patch's `vr_id=64259` for "Mat 19:23 mti=7577" actually resolves to vc.id=64259, whose canonical verse_record_id is 237872). This is a systematic encoding error — `vr_id` was meant to be `verse_record_id` but AI used `verse_context.id`.

Re-classification by `(reference, mti_id)` lookup:

| Category | Count | Action |
|---|---|---|
| Recoverable — vc row exists at correct verse_record_id, patch had wrong number | **57** | Replace patch's vr_id with canonical lookup |
| Truly orphan — no vc row anywhere for this (reference, mti_id) | **2** | See §2.5 |

The 2 truly-orphan ops are both H8082 *sha.men* adjective (mti=4695):
- Neh 9:25 (patch_vr=139377)
- Neh 9:35 (patch_vr=139378)

These are genuinely new verses for this term that have never been in verse_context.

**Resolution (CC):**
- 57 recoverable ops: look up correct `verse_record_id` by `(reference, mti_term_id)` via `wa_verse_records`. Mechanical fix.
- 2 orphan ops: see §2.5.

### 2.5 BLOCKING — 2 orphan ops need VCNEW not VCREVISE

VCREVISE updates existing rows. The 2 sha.men adj orphans need INSERT. Cannot mix VCNEW and VCREVISE in a single patch (`patch_type` is global).

**Resolution (CC):** split into two patches:
- **Patch v2 (VCREVISE):** 202 reformatted routing ops
- **Patch v3 (VCNEW):** 2 inserts for Neh 9:25 / Neh 9:35 (sha.men adj)

The VCNEW inserts must obey the v1_13 §5.1.1 provisional-anchor rule: first relevant insert for an anchorless term gets `is_anchor=1`. Sha.men adj currently has 1 anchor (Hab 1:16). See §2.6 for anchor handling — if Hab 1:16 stays anchored, the 2 new inserts can be `is_anchor=0`.

### 2.6 BLOCKING — Wholesale anchor demotion across the cluster (R4 would fail for 11 terms)

The patch's 7 declared anchors (`set_is_anchor=1`) plus 197 non-anchor ops (`set_is_anchor=0`) would, if applied literally, demote 16 existing anchors. For 11 terms this leaves zero anchors → R4 anchor gate fails:

| mti_id | Strongs | Term | Current anchor(s) demoted | New anchor declared by patch | R4 result |
|---|---|---|---|---|---|
| 3836 | H5727 | a.dan | Neh 9:25 | — | **FAIL** |
| 4695 | H8082 | sha.men (adj) | Hab 1:16 | — | **FAIL** |
| 4702 | G3045 | liparos | Rev 18:14 | — | **FAIL** (single-verse term) |
| 7010 | H1952 | hon | Psa 119:14, Pro 18:11 | — | **FAIL** |
| 7109 | H2630 | cha.san | Isa 23:18 | — | **FAIL** (single-verse term) |
| 7577 | G4145 | plousios | Mat 19:23, Luk 16:19 | Rev 3:17 | OK (1 new) |
| 7578 | G4146 | plousiōs | 1Ti 6:17 | — | **FAIL** (single-verse term) |
| 7580 | G4148 | ploutizō | 2Cor 6:10 | — | **FAIL** |
| 7583 | G4434 | ptōchos | Mat 5:3 | — | **FAIL** |
| 7584 | H6223 | a.shir | 2Sa 12:4 | — | **FAIL** |
| 7585 | H6238 | a.shar | Gen 14:23 | — | **FAIL** |
| 1142 | H7230 | rov | Lam 3:32, Isa 1:11 | — | **FAIL** |

AI's _patch_meta says "Anchors set where designated" — this suggests intent was to set 7 new anchors while **leaving other anchor states untouched**. The encoding error: AI included `set_is_anchor=0` in every non-anchor op, which the applier interprets as "set is_anchor=0" rather than "no change".

**Resolution (CC):** in the rewritten ops, **omit `is_anchor` from the `set` dict on non-anchor ops**. Only the 7 designated anchor ops set `is_anchor=1`. Existing anchors are preserved unless the same `(verse_record_id, mti_term_id)` row is one of the 7 new anchors.

This matches AI's stated intent and respects the existing analytical work.

### 2.7 NON-BLOCKING — H7600 *sha.a.nan* routing incomplete (4 verses missing)

Patch contains 5 H7600 ops (all → M46-A + gid=1861 / 413-001 complacent ease). Four relevant H7600 verses are not in the patch:

| Reference | Current DB state | Suggested routing |
|---|---|---|
| Isa 32:9 | gid=1861, anchor=0 | M46-A + gid=1861 (complacent warning, pattern matches the 5 in patch) |
| Isa 32:11 | gid=1861, anchor=0 | M46-A + gid=1861 (same pattern) |
| Isa 32:18 | gid=1862, anchor=1 | **M46-D + gid=1862** (per AI's note: 413-002 divine quietness → M46-D) |
| Isa 37:29 | gid=1861, anchor=0 | M46-A + gid=1861 (Sennacherib's complacent boasting, same pattern) |

AI's patch notes acknowledge this gap ("CC to identify these from the per-term section"). The routing for Isa 32:9/11/37:29 follows the same pattern as AI's 5 ops; Isa 32:18 follows AI's stated 413-002 → M46-D mapping. Isa 32:18 already carries `is_anchor=1` in DB — preserve.

**Resolution (CC):** add 4 ops to the rewritten patch.

### 2.8 NON-BLOCKING — G3045 *liparos* term placement vs verse routing mismatch

- Term G3045 mti=4702 sits in `mti_term_subgroup` → **M46-A** (placed 2026-05-14T19:06:06Z by yesterday's backfill script).
- Patch routes Rev 18:14 (the term's only verse) to **M46-B + gid=3709**, with reading-grounded basis: "soul longed for luxurious goods — insatiability/deceitfulness face".

A single-verse term cannot logically straddle two sub-groups. AI's fresh reading shifts the analytical home from M46-A (inner closure) to M46-B (insatiability). Both are defensible, but AI's reading post-dates the M46-A placement and is grounded in specific verse evidence; the M46-A placement was a snap decision during the previous evening's backfill.

**Resolution (CC):** Move term placement M46-A → M46-B as a separate `mti_term_subgroup` update (Phase 6 reassignment). Document in patch metadata. This is not part of the VCREVISE patch — it's a `mti_term_subgroup` UPDATE outside the verse_context flow.

Per cluster-instruction v1_13's directive-packaging discipline (§2.5), this could be packaged with the v2 routing patch as a small upstream operation. Simplest path: an inline `mti_term_subgroup` UPDATE before the patch is applied, recorded in the alignment notes.

Confirming the v1.13 anchor rule: Rev 18:14 must remain `is_anchor=1` to keep R4 satisfied for liparos (only verse).

### 2.9 NON-BLOCKING — 4 hon (H1952) verses re-routed from existing VCG

Four verses currently in `group_id=2933` are retargeted by the patch to specific content-aligned VCGs:

| Reference | Current gid | Target gid | Target VCG description |
|---|---|---|---|
| Psa 112:3 | 2933 | 2957 (681-001) | wealth as moral category |
| Psa 119:14 | 2933 | 3717 (7586-002) | riches as gift/fruit of ordered life |
| Pro 11:4 | 2933 | 3716 (7586-001) | riches as misplaced trust |
| Pro 28:22 | 2933 | 3711 (7579-001) | drive to become rich |

AI's `_patch_meta` notes include the line "if a row already has a group_id, preserve it and only update cluster_subgroup_id where missing" — which contradicts these 4 ops. The note is plausibly a generic safety statement that doesn't apply to retargeting decisions made by the reading. The new VCGs were created yesterday specifically as content-aligned replacements for the catch-all 2933.

**Resolution (CC):** apply the retargeting as written. The reading-grounded routing wins over a generic preservation note. Document the conflict + resolution in patch metadata so it's auditable.

---

## 3. Proposed deliverables

### 3.1 Three artefacts

| Artefact | Content | Patch type |
|---|---|---|
| Patch v2 (main) | 202 reformatted routing ops + 4 added H7600 ops = **206 ops** | VCREVISE |
| Patch v3 (orphan inserts) | 2 new vc rows for Neh 9:25 / Neh 9:35 sha.men adj | VCNEW |
| Pre-patch update | `mti_term_subgroup` row for G3045 liparos: M46-A → M46-B | inline UPDATE (not patch) |

### 3.2 Order of operations

1. Update `mti_term_subgroup` row 381 (G3045 liparos) → M46-B id=46 (transactional, with timestamp).
2. Apply patch v3 (VCNEW: Neh 9:25 + Neh 9:35 inserts for sha.men adj).
3. Apply patch v2 (VCREVISE: 206 routing ops).
4. Re-run pre-flight verifier: R4 anchor count per term, group_id assignment completeness, subgroup routing match.
5. Regenerate comprehensive report v13.

### 3.3 Risk register

| Risk | Mitigation |
|---|---|
| Misinterpretation of the 4 hon retargeting (AI's intent ambiguous) | Documented in patch metadata; researcher can revert specific ops if disagreed |
| H7600 Isa 32:9/11/37:29 routing extrapolated from pattern | Pattern matches AI's stated logic ("M46-A for complacent verses"); confirm with researcher before apply |
| liparos term-move M46-A → M46-B | Documented; reversible by mti_term_subgroup update |
| Anchor preservation (omitting is_anchor from non-anchor ops) may diverge from AI's actual intent | Documented; if AI did intend a clean-slate anchor reset, the 11 R4 failures should be resolved by adding 11 explicit `is_anchor=1` ops — but that requires fresh anchor designations from the reading |
| `_patch_meta.input_versions` md_version mismatches | Reading current md_version at v2-build time; if any changes between now and apply, the version gate will reject (correct behaviour) |

---

## 4. Open questions for the researcher

1. **Anchor preservation strategy** — do we preserve existing anchors except for the 7 newly-declared ones (CC's recommended interpretation of "Anchors set where designated"), or did AI intend a clean-slate anchor reset (which would require fresh anchor designations for 11 more terms — not in this patch)?

2. **liparos term placement** — confirm move M46-A → M46-B is acceptable, or push the verse routing back to M46-A to match the existing placement?

3. **H7600 four added ops** — confirm the pattern extrapolation (Isa 32:9/11/37:29 → M46-A + gid=1861; Isa 32:18 → M46-D + gid=1862) is acceptable, or wait for AI's explicit routing?

4. **4 hon retargeting** — apply as written, or escalate back to AI as ambiguous?

5. **9 UT borderline verses** — AI excluded these "awaiting researcher decision". Surface now or after this patch lands?

---

## 5. Response document to AI

A separate response document for AI: [Sessions/Session_Clusters/M46/WA-M46-cc-response-to-phase7-patch-v1-20260515.md](../../Sessions/Session_Clusters/M46/WA-M46-cc-response-to-phase7-patch-v1-20260515.md).
