# VCB-012 — partial-completion handling brief

**Date:** 2026-04-25
**Author:** Claude Code
**Governing instruction:** [wa-versecontext-instruction-v3_9-20260425.md](../../data/imports/WA/Workflow/Framework_B/Session_B/wa-versecontext-instruction-v3_9-20260425.md)
**Companion patch instruction:** wa-patch-instruction-v2_9 (current)
**Sibling session:** [VCB-011](vcb-011-batch-prep-20260425.md) — 13 standard RE-EVALUATION terms (the rest of the original VC-11 candidate set).

---

## 1. Why this batch is separate

Both terms have **partial-completion legacy state** — prior `verse_context` rows exist for some active verses but not all. Per VC-Instruction §6.2 Step 2 *Partial completion rule*, this is a structural error condition that triggers an **immediate stop** for the affected term and requires researcher disposition before classification proceeds. Splitting them out keeps VCB-011 clean while letting these two run through their own session with explicit guidance.

Probable cause for both: the registries reached legacy-Complete before subsequent `audit_word` re-runs added more verses to these terms; the original VC pass never came back to cover the additions. This pattern is part of the broader "174 legacy-Complete registries pending under v3_8 contracts" task (tasks.md In Progress). Treating these two as the canonical recipe for resolving partial-completion legacy state will set the template for the remaining backlog.

## 2. Scope

| mti_id | Strongs | Translit | Gloss | Reg | Active groups | Active vc rows | Active verses | Unclassified |
|-------:|--------:|----------|-------|----:|--------------:|---------------:|--------------:|-------------:|
|  5111 | G3878 | parakouō | to ignore   | 050 disobedience   | 1 |  1 |  2 |  1 |
|  1364 | H2498 | chā·laph | to pass     | 202 transformation | 4 | 10 | 27 | 17 |
| **Totals** | — | — | — | — | **5 active groups** | **11 prior rows** | **29 verses** | **18 to classify** |

Verse budget 29 — well under the §5.2 ~1,500 soft session budget. The work, however, is concentrated in mti=1364 because of the spread across 17 unclassified verses against 4 already-shaped groups.

## 3. Per-term partial-state detail

### 3.1 mti=5111 G3878 *parakouō* — registry 050 disobedience

Currently 1 active group, 1 anchor verse, 1 unclassified verse:

| Verse | Status | vc.id | Group | is_relevant | is_anchor | is_related |
|-------|--------|------:|-------|------------:|----------:|-----------:|
| Mat 18:17 | classified | 12307 | 5111-001 | 1 | 1 | 0 |
| Mar 5:36  | **unclassified** | — | — | — | — | — |

Active group 5111-001 description: *"Term names the wilful refusal to hear — the inner orientation of closed attention or contempt expressed through the repeated failure to receive the voice of the community"*

Mar 5:36 context (from Greek): Jesus to the synagogue ruler — *parakousas* in this verse is conventionally rendered "overheard" / "ignoring what they said" (variant readings exist). Likely a *wrong-face* or *no_inner_being* set-aside if the verse describes Jesus' physical act of overhearing rather than disobedience as inner orientation. The classifier should not assume — apply the §3 filter to the verse text in the `.md`.

**Action expected from classifier:** insert a per-verse `verse_context` row for Mar 5:36 (vrid=155905, mti=5111). Either is_relevant=1 (assigned to existing group 5111-001 if it fits, or a new group if a different inner-being characteristic) or is_relevant=0 with a `set_aside_reason` from the controlled vocabulary.

### 3.2 mti=1364 H2498 *chā·laph* — registry 202 transformation

Currently 4 active groups covering 10 of 27 active verses (37% coverage). 17 verses unclassified:

**Existing groups (all active):**

- 1364-001: *"Term describes the inner renewal of strength and vitality that comes through waiting on or turning to God"* — anchor Isa 40:31; related Job 29:20, Isa 41:1
- 1364-002: *"Term expresses the transience of human life and creation — the rapid passing that characterises human existence"* — anchor Psa 90:5; related Job 9:26, Psa 90:6, Psa 102:26
- 1364-003: *"Term describes the wilful overriding of divine covenant — an inner act of defiance against binding obligation"* — anchor Isa 24:5
- 1364-004: *"Term describes the passing of God or divine spirit near the person, engaging the person's inner capacity for perception or producing inner dread"* — anchor Job 9:11; related Job 4:15

**Unclassified verses (17):**

| Verse | Note |
|-------|------|
| Gen 31:7 | Laban changing wages — physical/transactional? |
| Gen 31:41 | Laban changing wages — same |
| Gen 35:2 | "change garments" — physical |
| Gen 41:14 | Joseph changing garments before Pharaoh — physical |
| Lev 27:10 | substituting one animal for another — ritual/physical |
| Judg 5:26 | Jael's hammer "passing through" Sisera — physical |
| 1Sa 10:3 | "men going up to God" — geographic passing |
| 2Sa 12:20 | David changing clothes after the child's death |
| Job 11:10 | "if he passes through and shuts up" — God's action |
| Job 14:7 | tree sprouting again — natural renewal |
| Job 20:24 | bronze arrow passing through — physical |
| Song 2:11 | winter is past — temporal |
| Isa 2:18 | idols pass away — physical/eschatological |
| Isa 8:8 | flood passing through Judah — physical |
| Isa 9:10 | sycamores changed for cedars — replacement |
| Isa 21:1 | whirlwinds passing through the Negeb — physical |
| Hab 1:11 | "wind sweeping past" — physical/military |

Most of the unclassified verses look likely **set-aside** territory under §3.2 (physical-only motion, garment-change, plant growth, military movement, transactional substitution). Several may genuinely fit existing group 1364-002 (transience) — Song 2:11 winter passing, Isa 9:10 replacement, possibly Isa 2:18 idols-pass-away. A handful may engage genuinely (Job 11:10, Isa 8:8 — God's action passing through the inner-being scene).

**Action expected from classifier:** apply §3 filter to all 17 unclassified verses; emit `insert` per-verse rows for each — assigning to existing groups where they fit (the 4 groups are already well-shaped), creating new groups only if the §3 grouping criterion warrants, or setting aside with controlled-vocab reason. Re-evaluation self-check (§6.2 Step 6) is mandatory because prior records exist; arithmetic must balance over all 27 verses.

## 4. Files prepared

Two per-term Session A `.md` files at [data/exports/session_a/terms/](../../data/exports/session_a/terms/), already rendered 2026-04-25:

- `wa-050-disobedience-G3878-session_a-20260425.md`   (8.9 KB) — mti=5111, md_version=v1
- `wa-202-transformation-H2498-session_a-20260425.md` (18.8 KB) — mti=1364, md_version=v1

Both `.md` files surface the prior `verse_context_group` and per-verse classification state in the Verses section, with the unclassified verses showing no Prior classification block — the classifier sees exactly which verses need new rows.

## 5. Patch routing — likely shape

Per VC-Instruction v3_9 §7.9.3 per-term patch-routing classifier:

- **mti=5111 G3878:** ≤1 new insert against an existing group (or set-aside) and possibly 0 updates → routes to **VCNEW** (NEW-ONLY) most likely, or **VCREVISE** if the classifier judges that the existing classification of Mat 18:17 also needs adjustment given the broader corpus visibility.
- **mti=1364 H2498:** 17 inserts likely + possibly 0–10 updates if any of the existing 10 classifications need revision under fresh review → routes to **VCNEW** (NEW-ONLY) if all prior 10 confirmed unchanged, or **MIXED** routing into both VCNEW and VCREVISE if revisions surface.

Final routing is determined per the §7.9.3 classifier at end of session — Claude Code will produce the patch file(s) accordingly.

## 6. Programme state after VCB-012 close (projected)

If both terms reach `vc_completed`:

- mti_terms at vc_completed: VCB-011 close (45) → 47 (or 32 → 34 if VCB-011 not yet closed).
- Registries 050 disobedience and 202 transformation can advance to v3_8-Complete via aggregate check (assuming VCB-011 also closed; both registries depend on both batches because their three OWNER terms are split across the two sessions).

## 7. Suggested next actions

1. Researcher reviews this brief — particularly §3.2 unclassified verse list for mti=1364 (17 verses, mostly likely set-asides but a few candidates for existing groups).
2. Hand the two `.md` files (§4) to a Claude AI classification session as VCB-012. Can run independently of VCB-011 (no shared dependency on order).
3. Classifier follows §6.2 Step 2 partial-completion path: state stop posture explicitly per term, then proceed to classify the missing verses under the same `md_version=v1` gate.
4. After VCB-012 patches return, follow normal apply sequence (§7.9.2: VERSECONTEXT → VCREVISE → VCSBFLAGS → VCSDPOINTERS) with R1–R4 + arithmetic checks (must balance over all 2 / 27 active verses respectively).
5. Once VCB-011 and VCB-012 both close, advance registries 050 and 202.

## 8. Template note for the broader 174-registry backlog

If this session works cleanly, the recipe — *render per-term `.md`, classifier consumes prior state from header, classifier inserts only for verses with no active row and updates only where prior rows need revision* — becomes the standard partial-completion handling pattern. CC can sweep the 174 legacy-Complete registries detecting this same "term has prior rows but not all verses covered" signature and surface them in dedicated batches alongside ordinary RE-EVALUATION batches. Worth raising as a follow-up after these two terms land.
