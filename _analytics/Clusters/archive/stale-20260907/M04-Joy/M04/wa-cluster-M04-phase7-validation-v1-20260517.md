# WA-M04-phase7-validation-v1-20260517

**Phase 7 validation report — AI VCG design output**

**Source files:**
- [files phase 7/WA-M04-vcg-creation-v1-20260517.json](files%20phase%207/WA-M04-vcg-creation-v1-20260517.json)
- [files phase 7/WA-M04-M04-A-vcg-design-v1-20260517.md](files%20phase%207/WA-M04-M04-A-vcg-design-v1-20260517.md)
- [files phase 7/WA-M04-M04-BCDEF-BOUNDARY-vcg-design-v1-20260517.md](files%20phase%207/WA-M04-M04-BCDEF-BOUNDARY-vcg-design-v1-20260517.md)
- [files phase 7/WA-M04-phase7-cross-routing-flags-v1-20260517.md](files%20phase%207/WA-M04-phase7-cross-routing-flags-v1-20260517.md)

**Validated against:** DB post-Phase-6 routing (1138 is_relevant vc rows · 7 sub-groups)

**Date:** 2026-05-17

---

## §1. Summary — significant divergences from M03 precedent

| Issue | Magnitude | Severity |
|---|---:|---|
| **A. JSON is incomplete** — uses `key_verses` (sample) instead of full `verses` per VCG | 23 VCGs affected | **HIGH** — JSON unusable as-is for the Phase 7 loader |
| **B. M04-A coverage gap** — 287 of 661 verses (43%) not assigned to any VCG in design | 287 verses | **HIGH** |
| **C. Cross-cluster vc_id misinclusions** — 15 vc_ids that belong to M42 included in M04 design | 15 verses | **MEDIUM** |
| **D. Phantom (non-existent) vc_ids** — 7 vc_ids that don't exist in DB | 7 verses | LOW |
| **E. Intra-sub-group duplicates** — 35 vc_ids appearing in 2+ VCGs within their sub-group | 35 verses | MEDIUM (likely intentional dual-membership but not flagged as such) |
| **F. M04-BOUNDARY explicit member list omitted** — AI stated "all 322 verses route here" but didn't enumerate | 322 verses | LOW (intent is clear, but not parser-friendly) |
| **G. File structure deviation** — AI delivered 1 doc per substantive sub-group OR combined; M03 used 1 per SG | 2 design docs vs expected 7 | LOW |

The Phase 7 brief asked for: per-VCG `verses` array (complete) in JSON, anchor as a verse-member, no phantoms, one design doc per sub-group, no cross-cluster verses. AI delivered: sample `key_verses` only, M04-BOUNDARY with 0 members enumerated, 22 invalid vc_ids, combined design doc for M04-B through M04-BOUNDARY.

---

## §2. Detailed findings

### A. JSON is incomplete

AI's JSON for each VCG has:
- `provisional_code`
- `description`
- `anchor_vc_id` + `anchor_reference` + `anchor_term`
- `key_verses` — **sample only** (sub-set of actual members)

Missing: a complete `verses` array per VCG. AI's note in the JSON says: _"vc_id lists are representative anchors and key members. CC must validate against complete is_relevant verse list per sub-group. The design documents carry the full analytical rationale. VCG verse membership is term-based: all verses of a term route to that term's primary sub-group VCG per the mapping in WA-M04-subgroup-mapping-v1-20260517.json."_

But: **the Phase 5 subgroup-mapping JSON has only term-to-sub-group routing — not term-to-VCG routing.** A term's verses inside a sub-group can split across multiple VCGs per the design rationale. The JSON doesn't carry that VCG-level granularity.

Per-sub-group totals (design member lists vs DB routing):

| Sub-group | DB verses | Design (sum across VCGs' member lists) | Gap |
|---|---:|---:|---:|
| M04-A | 661 | 433 | **−228** |
| M04-B | 10 | 10 | 0 |
| M04-C | 16 | 16 | 0 |
| M04-D | 24 | 24 | 0 |
| M04-E | 28 | 28 | 0 |
| M04-F | 77 | 77 | 0 |
| M04-BOUNDARY | 322 | 0 (term-based intent) | −322 |
| **TOTAL** | **1138** | **588 explicit + 322 implicit term-based** | |

M04-B through M04-F are clean. M04-A and M04-BOUNDARY are the problem children.

### B. M04-A coverage gap — 287 verses

After deduping (some verses appear in multiple VCGs within M04-A): **287 of 661 M04-A verses do not appear in any VCG's explicit member list.**

The M04-A design doc ends with an "Additional M04-A verses not yet assigned above" section that names a few residual term→VCG assignments (ma.s.vo.s, cha.phets, re.na.nah) but the bulk of the 287 are not addressed. AI's own statement: _"The JSON provides the complete authoritative vc_id list per VCG."_ — but the JSON has only `key_verses` (samples).

So the design's M04-A is materially incomplete — only ~57% of M04-A's verses are explicitly placed in a VCG.

### C. Cross-cluster vc_id misinclusions (15)

AI included these vc_ids in M04 design VCGs, but they belong to **M42 Speech, Voice and Cry**:

| vc_id | Reference | Strong's | Translit | Owning cluster |
|---:|---|---|---|---|
| 23441 | Psa 118:15 | H7440 | rin.nah | M42 |
| 23471 | Jer 11:14 | H7440 | rin.nah | M42 |
| 23549 | Psa 95:1 | H7442B | ra.nan | M42 |
| 23551 | Psa 98:4 | H7442B | ra.nan | M42 |
| 23554 | Psa 132:16 | H7442B | ra.nan | M42 |
| 23555 | Psa 145:7 | H7442B | ra.nan | M42 |
| 23563 | Isa 26:19 | H7442B | ra.nan | M42 |
| 23564 | Isa 35:2 | H7442B | ra.nan | M42 |
| 23565 | Isa 35:6 | H7442B | ra.nan | M42 |
| 23566 | Isa 42:11 | H7442B | ra.nan | M42 |
| 23573 | Jer 31:7 | H7442B | ra.nan | M42 |
| 23574 | Jer 31:12 | H7442B | ra.nan | M42 |
| 23576 | Lam 2:19 | H7442B | ra.nan | M42 |
| 23577 | Zep 3:14 | H7442B | ra.nan | M42 |
| 23578 | Zec 2:10 | H7442B | ra.nan | M42 |

These are rin.nah (shouting/cry) and ra.nan (sing-for-joy / shout) — both **shouting/singing speech-acts**, owned by R208 shouting / M42 Speech. They are NOT in M04's term universe. AI conflated joy-register vocabulary with M04 cluster membership.

This is an analytical error: AI treated these as M04 because they carry joy-shouting semantics, ignoring the registry/cluster ownership. **They must be dropped from the M04 Phase 7 design.**

(Note: there's a separate term H7442A ra.nan-quavering that IS in M04 — but those are different vc_ids.)

### D. Non-existent vc_ids (7 hallucinations)

| vc_id | Status |
|---:|---|
| 23476 | Does not exist |
| 23480 | Does not exist |
| 23489 | Does not exist |
| 23493 | Does not exist |
| 23503 | Does not exist |
| 23517 | Does not exist |
| 23519 | Does not exist |

These are AI typos or invented vc_ids. Drop.

### E. Intra-sub-group duplicates (35)

35 vc_ids appear in 2+ VCGs within M04-A. Most are M04-A-VCG-01 (Exultation in God) overlapping with another M04-A VCG. These are plausibly intentional dual-memberships at the VCG level — same verse fits "joy directed toward YHWH" + another register. Resolution per M03 precedent: pick primary VCG (first occurrence or anchor-membership), record secondary in `verse_context.notes`. Pattern is fine; just needs explicit dual-membership flagging in the JSON.

### F. M04-BOUNDARY enumeration

AI stated: _"All 322 verses of the 15 BOUNDARY terms route to this VCG"_ but didn't list them. Intent is clear (term-based routing — every is_relevant vc of a BOUNDARY term goes to M04-BOUNDARY-VCG-01). CC can mechanically expand from the term list. Anchor: vc_id 32636 (Gen 8:21 ni.cho.ach) — confirmed valid in DB.

### G. File structure deviation

Brief asked for: 7 design docs (one per substantive sub-group + BOUNDARY).
AI delivered: 2 design docs (M04-A alone, M04-B/C/D/E/F/BOUNDARY combined).

Functionally the content is there. Not a blocker.

---

## §3. Path-forward options

### Option A — Send back to AI for completion (recommended for strict spec compliance)

Reject and re-request with corrections:
1. Drop 22 invalid vc_ids (15 M42 misinclusions + 7 phantoms)
2. Identify and assign the 287 uncovered M04-A verses to specific VCGs (full enumeration)
3. Deliver complete JSON with `verses` arrays per VCG (not `key_verses` samples)
4. Enumerate M04-BOUNDARY-VCG-01's 322 members (or accept term-based note + CC expansion)
5. Flag the 35 intra-sub-group duplicates explicitly as `dual_membership` entries
6. Optionally: split combined design doc into 6 separate files per brief spec

**Pros:** Strict enforcement; AI carries the analytical decisions. The 287 M04-A assignments require analytical judgment (which sub-VCG a verse fits) that AI is better positioned to make.

**Cons:** Cost (re-running a 661-verse pass for M04-A); time.

### Option B — CC reconstruct (faster, less analytically clean)

CC builds a complete JSON from the design doc evidence:
1. Drop 22 invalid vc_ids
2. For each of the 287 uncovered M04-A verses: route by term to the VCG where the term has the most existing primary members (default rule — "term's primary VCG within sub-group")
3. Expand M04-BOUNDARY-VCG-01 to all 322 active vc_ids per term-based intent
4. Resolve 35 duplicates: keep first occurrence as primary, log others as secondary

**Pros:** No AI re-run cost; CC mechanically resolves remaining issues.

**Cons:** Default-routing the 287 by "term's dominant VCG" loses analytical nuance. Some verses might fit a different VCG within the same sub-group than the default suggests. Researcher would not have AI's per-verse reasoning for those 287.

### Option C — Hybrid (recommended path)

CC handles the mechanical issues (drops, expansions, BOUNDARY enumeration); AI re-runs only on the 287 M04-A uncovered verses to assign them to specific VCGs.

- CC: drop 22 invalid; expand M04-BOUNDARY; produce a "287-verse assignment task" file
- AI: receive 287 verses + the 10 M04-A VCG descriptions, return atomic per-row assignments
- CC: merge AI's atomic-per-row output into the complete JSON; apply Phase 7

**Pros:** Minimises AI re-run scope (287 atomic decisions, not whole-cluster re-do); keeps analytical control with AI for the genuinely undecided verses; CC handles all deterministic cleanup.

**Cons:** Two-step AI workflow.

---

## §4. Recommendation

**Option C (Hybrid).**

The 287-verse gap is too large to mechanically default-route (Option B) without losing analytical signal. The 22 invalid vc_ids are clear CC drops. The 35 duplicates and BOUNDARY enumeration are mechanical. The genuine remaining decision — which sub-VCG within M04-A each of the 287 verses fits — is analytical and belongs to AI.

CC's task: produce a 287-verse assignment input file (sample format below) that AI can return atomic decisions on. CC then merges and applies.

```text
M04-A VCG-by-VCG context summaries:
  VCG-01 — Exultation in God: Joy Directed Toward YHWH as Object
  VCG-02 — Joy at God's Saving Acts: Gladness at What He Has Done
  VCG-03 — Divine Joy / God's Delight Directed Toward His People
  ...

Assign each of the 287 verses below to ONE M04-A VCG (or mark dual-membership):

vc_id=NNN, Ref="Psa X:Y", term=sa.mach, meaning="..."
→ assignment: M04-A-VCG-??

(× 287 rows)
```

Awaiting researcher decision before proceeding.

---

*End of validation report.*
