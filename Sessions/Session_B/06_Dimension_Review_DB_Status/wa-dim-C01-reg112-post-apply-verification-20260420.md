# C01 r112 DIMREVIEW Patch — Post-Apply Verification — 2026-04-20

| Field | Value |
|---|---|
| Filename | wa-dim-C01-reg112-post-apply-verification-20260420.md |
| Patch applied | `PATCH-20260420-DIMREVIEW-C01-REG112-V2` |
| Applied at | 2026-04-20T10:42Z |
| Verification basis | FF-1..FF-11 checks per post-patch plan (`dim-c01-post-patch-plan-20260420.md` §2.3) |
| Live DB state | Schema v3.11.0 |
| Status | **ALL CHECKS PASS** |
| Produced | 2026-04-20 |

---

## 1. Patch summary

Original patch (`wa-dim-c01-reg112-patch-v1-20260420.json`) had 85 ops. **Pre-apply FF-11 (schema compatibility)** caught one defect: OP-075 targeted `wa_dimension_index.context_description` — a column dropped in M25 (2026-04-19). v2 patch produced with OP-075 removed (op was redundant: OP-074 already updates canonical `verse_context_group.context_description`). v2 has 84 ops.

**v2 apply outcome:**

| Operation | Count | Notes |
|---|---:|---|
| `wa_dimension_index update` | 73 | All 73 r112 groups assigned dimension + dominant_subject + unlocked |
| `verse_context_group update` | 1 | Phase B QA-VAGUE correction for 1010-001 nefros |
| `wa_session_b_findings insert` | 4 | DIM-112-004..007 (DIMENSIONAL_PATTERN findings) |
| `wa_session_research_flags insert` | 5 | DIM-112-SD003..SD007 (SD pointers) |
| `word_registry update` | 1 | r112 stamped: `dim_review_status = Complete`, `dim_review_version = wa-dimensionreview-instruction-v3_3-20260418` |

**Applicator library fix** (bonus): `scripts/apply_session_patch.py` paths for `wa_session_b_findings insert` and `wa_session_research_flags insert` updated to accept both `record` and `values` keys in op payloads (they previously hardcoded `record`). This patch used `values`. Fix durable; consistent with other op handlers.

---

## 2. FF-1..FF-11 results

### FF-1 Vocabulary vintage (r112)

| Metric | Result |
|---|---:|
| Total active groups | 73 |
| On current §7.7 vocabulary | **73** ✓ |
| On legacy vocabulary | 0 |
| NULL dimension | 0 |

**PASS.** r112 is now fully current-vocabulary post-apply. No legacy labels remain.

### FF-2 Manual-override lock post-apply

| manual_override | Count |
|---:|---:|
| 0 | 73 |
| 1 | 0 |

**PASS with observation.** Patch explicitly unlocked all 73 groups (previously: 71 locked + 2 open). Analytical semantic: `dim_review_status = Complete` on the registry is the authoritative anchor for these assignments; per-group `manual_override=1` is reserved for researcher-locked exceptions. This is an intentional shift in how lock status signals review completeness — **candidate for DV-7 pre-check pattern** (flag registries going into DimReview where the lock-then-unlock cycle is expected).

### FF-3 dominant_subject distribution

| Value | Count |
|---|---:|
| HUMAN | 58 |
| NONE | 10 |
| GOD | 5 |
| OTHER_HUMAN / UNSEEN | 0 |

**PASS.** All values in valid vocabulary. 10 NONE values are intentional per session log §2.5 (groups where description names both divine and human agents acting together — 7 of these 10 are correctly at `11 Divine-Human Correspondence`). No literal-`'NONE'` OT-DBR-012 leakage.

### FF-4 dimension_confidence stamp

| Value | Count |
|---|---:|
| CLAUDE_AI | 73 |

**PASS.** All 73 groups stamped at CLAUDE_AI confidence. No KEYWORD_*/UNCLASSIFIED/NULL residue.

### FF-5 DR status transition (r112)

| Field | Value |
|---|---|
| `word_registry.no` | 112 (mind) |
| `dim_review_status` | **Complete** ✓ |
| `dim_review_version` | `wa-dimensionreview-instruction-v3_3-20260418` |

**PASS.** Registry stamp applied. Version string uses actual governing instruction (per researcher-directed departure from stale template per session log §2.2).

### FF-6 Cross-registry coherence (Dimension 11 spot-check)

**CRITICAL FINDING — CONFIRMS OT-DBR-015:**

| Cluster | Word | Dimension label | Groups |
|---|---|---|---:|
| **C01** | mind (r112) | **`11 Divine-Human Correspondence`** (current) | 12 |
| C01 | Soul | `Theological/Divine-Human` (legacy) | 16 |
| C01 | spirit | `Theological/Divine-Human` (legacy) | 17 |
| C01 | flesh | `Theological/Divine-Human` (legacy) | 8 |
| C01 | heart | `Theological/Divine-Human` (legacy) | 8 |
| C01 | being | `Theological/Divine-Human` (legacy) | 3 |
| C08 | counsel | `Theological/Divine-Human` (legacy) | 1 |
| C04 | desire | `Theological/Divine-Human` (legacy) | 1 |
| C17 | forgiveness | `Theological/Divine-Human` (legacy) | 1 |
| C02 | intention | `Theological/Divine-Human` (legacy) | 1 |
| C05 | mourning | `Theological/Divine-Human` (legacy) | 2 |
| C02 | purpose | `Theological/Divine-Human` (legacy) | 1 |
| C02 | thought | `Theological/Divine-Human` (legacy) | 1 |
| C05 | weeping | `Theological/Divine-Human` (legacy) | 1 |

**Interpretation:** The same analytical concept (divine-human correspondence) is now labelled two different ways in the live DB. Any cross-registry aggregation that groups by `dimension` string will fragment. This is the concrete manifestation of OT-DBR-015 requiring decision (see §5 below — Option 1/2/3).

**Does NOT fail** — this is an expected post-apply state given C01 is mixed-vintage. The check correctly surfaces the heterogeneity for researcher decision.

### FF-7 SD pointer increment

**PASS.** r112 SD pointers now:

| Pointer | Origin |
|---|---|
| `112-SD001..SD010` | Pre-existing (pre-DIM prefix format — OT-DBR for reconciliation) |
| `DIM-112-SD001..SD002` | Pre-existing (DIM-prefix format) |
| **`DIM-112-SD003..SD007`** | **From this patch** ✓ |

5 new pointers added correctly. Numbering continues from DIM-112-SD002. No duplicates. Legacy `112-SD0xx` format noted as pointer-format reconciliation item (session log §2.3).

### FF-8 Scope integrity

Only `wa_dimension_index.last_modified >= 10:56` rows belong to registry 112. No unintended changes to other registries. **PASS.**

### FF-9 Coverage verification

73 active `wa_dimension_index` rows for r112. Expected 73. **PASS.**

### FF-10 Q-COV question linkage (optional)

Not run this cycle — no VERSE_EVIDENCE_* flags on r112's OWNER terms require Q-COV surfacing. Will apply when a registry with evidence-family flags enters DimReview. Framework ready.

### FF-11 Schema compatibility (NEW — added today)

**PASS — defect caught pre-apply.**

OP-075 referenced `wa_dimension_index.context_description` (dropped in M25). v2 patch produced with OP-075 removed. Remaining 84 ops all column-clean.

**Folding into DV pre-checks:** add **DV-6** "Patch schema compatibility check" to `build_dimension_extract.py` pre-check bundle + also to `apply_session_patch.py`-side pre-validation. Pattern: for every `set` clause in any `update`/`insert` op, verify column exists in target table via `PRAGMA table_info`. If missing, either (a) drop column silently with [NOTE] print (pattern already used for word_registry), or (b) error out and require patch revision. Recommend (a) for optional-sync fields, (b) for critical fields.

---

## 3. Cumulative learning → DV-6+ pre-checks (candidate additions)

From this apply cycle, four new pre-check candidates for `build_dimension_extract.py --bundle` and/or `apply_session_patch.py` pre-validation:

| Code | Check | Trigger from this apply |
|---|---|---|
| **DV-6** | Patch-op schema compatibility — every `set` column exists in current schema | FF-11 caught OP-075 against dropped column |
| **DV-7** | MO-lock-then-unlock expectation note — declare that patch will unlock existing MO=1 groups under researcher block auth | FF-2 showed intentional lock→unlock transition; handoff should declare it |
| **DV-8** | Cross-registry coherence — pre-apply report of how the target's new dimensions map against legacy labels in other registries sharing the same analytical concept | FF-6 exposed C01 mixed-vintage state |
| **DV-9** | Op-payload key normalisation — applicator accepts `record` ∪ `values` consistently | Applicator library fix this apply |

DV-6 and DV-9 are library-level fixes (one-off). DV-7 and DV-8 are reporting enhancements to the handoff generator.

---

## 4. Registry state post-apply

| Field | Before (pre-patch) | After (post-patch) |
|---|---|---|
| r112 dim_review_status | NULL | Complete |
| r112 dim_review_version | NULL | `wa-dimensionreview-instruction-v3_3-20260418` |
| r112 dim_index rows current vocab | 2 | 73 |
| r112 dim_index rows legacy vocab | 71 | 0 |
| r112 MO=1 groups | 71 | 0 |
| r112 SB findings | 3 (DIM-112-001..003) | 7 (+DIM-112-004..007) |
| r112 SD pointers | 12 | 17 (+DIM-112-SD003..SD007) |
| Phase B description correction (1010-001) | old "inner faculty… searched by Christ" | **revised:** "the deep inner life — the hidden motives and affections of the person open only to divine searching" |

---

## 5. OT-DBR-015 status update — Option 1/2/3 question for researcher

Per post-patch plan §3. Post-apply, C01 is now confirmed mixed-vintage:

| Cluster | Word | Current state |
|---|---|---|
| C01 | r112 mind | ✓ Current vocabulary (73 groups) |
| C01 | r183 heart | Legacy vocabulary (pending Phase C) |
| C01 | r182 Soul | Legacy vocabulary (Complete under prior version) |
| C01 | r184 spirit | Legacy vocabulary (Complete under prior version) |
| C01 | r185 flesh | Legacy vocabulary (Complete under prior version) |
| C01 | r211 being | Legacy vocabulary (Complete under prior version) |

**Scope expansion:** programme scan shows the `Theological/Divine-Human` legacy label alone appears in 10 registries across 6 clusters. Full legacy-vocab programme scan needed (on the OT-DBR-015 action list).

**Three options still on table** (per post-patch plan §3):

- **Option 1:** Accept mixed-vintage. Not recommended.
- **Option 2:** Full re-review of r182/r184/r185/r211 (C01) + every other Complete-under-legacy registry. Thorough, expensive.
- **Option 3 (CC recommendation):** Mapping patch using OT-DBR-015 mapping table (legacy → current). Mechanical where mapping is clean; researcher-only decision for the 40 C01 groups with unmapped legacy labels (Spiritual/God-ward 25, Identity/Selfhood 9, Somatic/Embodied 6).

**Decision deferred to researcher** — awaits direction. See §6 below for what this blocks or doesn't.

---

## 6. What's unblocked and what awaits

### Unblocked by this apply

- r112 now DR=Complete — DataPrep gate for r112 is structurally open (still requires VC Complete + other gates)
- 5 new SD pointers (DIM-112-SD003..SD007) queued for Session D
- 4 new SB findings queued (DIM-112-004..007)

### Still pending

- **RD-PHASE-C-112-001** — Dimension 11 scope for 3 God-ward mind groups (dianoia 995-001, froneō 996-001, cha.shav-impute 3335-001). Patch encoded Dimension 11; researcher may direct alternative (04 Volition or 06 Relational Disposition). If changed later → minor correction patch, not a revision of this apply.
- **Phase C r183** — paused on 4 RD items + awaits verse-evidence verification per Directive `DIR-20260420-001`. CC will execute the directive next (read-only verse extract).
- **FLAG-010** — DR instruction audit deferred under researcher-authorised INSTRUCTION-NOTE. Not blocking.
- **Pointer format reconciliation** — 10 legacy-format `112-SD0xx` pointers can be reformatted to `DIM-112-SD0xx` in a cleanup cycle.
- **Stamp string template update** — instruction templates reference stale version string; not blocking.

---

## 7. Artefacts produced or modified by this apply

- Backup: `backups/bible_research_pre_C01_dimreview_r112_20260420_103945.db` (pre-apply)
- Patch v2: `data/imports/WA/Patches/wa-dim-c01-reg112-patch-v2-20260420.json` (OP-075 removed)
- Patch v2 archived post-apply: `archive/patches/wa-dim-c01-reg112-patch-v2-20260420.json`
- Applicator library fix: `scripts/apply_session_patch.py` — consistent record/values key acceptance (2 sites)
- This verification report

---

*End of r112 post-apply verification. Awaiting researcher direction on §5 Option 1/2/3 before r183 handoff. Executing DIR-20260420-001 directive next.*
