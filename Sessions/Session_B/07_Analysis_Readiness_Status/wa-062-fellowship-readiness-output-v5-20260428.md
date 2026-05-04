# wa-062-fellowship — Analysis Readiness Output (v2)

_Pilot v2 generation · 2026-04-28T06:24:53Z · schema 3.17.0_

_Strategy: vc-corrective-strategy-v2 §4 · sections aligned with `wa-sessionb-analysis-output-v1_1` reading units 1-9._

_Source of truth: live DB at generation time. Regenerate to refresh._

**Section map:**

- A. Registry overview — Unit 1
- B. Stage 1 Completion Record (synthesised) — instruction S2 prerequisite
- C. Term inventory — Unit 1 prep
- D. OWNER terms — lexical foundation — Unit 3
- E. XREF terms — Unit 2
- F. Verse context groups landscape — Unit 4 (with dimension assignments)
- G. Correlation signals — Unit 5 (computed)
- H. Existing SD pointers + session_b_findings — Units 6 + 9
- I. Thin-evidence phase2 flags — Unit 8
- J. Anchor verse material — Unit 7 (full verbatim verse text)
- K. Legacy-VC terms — UNVERIFIED — v2 strategy mandate
- L. Stage 2b reference — observation question catalogue
- N. Open Session B items (carried forward; must resolve this session)
- M. Readiness verification

---

## A. Registry Overview

- **Registry no:** `62` · **word:** `fellowship`
- **verse_context_status:** `Complete`
- **session_b_status:** `Verse Context Reset`
- **dim_review_status:** `Complete` (version `WA-DimensionReview-Instruction-v2.2-2026-04-11`)
- **cluster_assignment:** `C17`
- **sb_classification:** `NULL`
- **carry_forward:** `1`
- **dimensions (registry-level):** `Relational Disposition; Moral Character; Transformation; Divine-Human Correspondence; Emotion — Positive; Cognition`

**Phase 1 (registry-scoped):**
- `phase1_status`: `Complete`
- `phase1_term_count`: 15  (programme-wide aggregate including XREF and historical terms — current OWNER count is 13, XREF 0)
- `phase1_verse_count`: 152  (programme-wide aggregate; current registry verse counts shown per term in §C)

**Open flags:** 11 unresolved · **Existing session_b_findings:** 16

**Description:**

> Fellowship is the experience of genuine shared life with others — not just being in the same place but actually participating together in something real. The Greek koinōnia carries the sense of having in common, sharing in, participating in. It is used of the fellowship of the Spirit, the fellowship of suffering, the fellowship of the Lord's Supper. Biblical fellowship is always anchored in something shared at a deeper level than preference or proximity: a shared life in God, a shared story, a shared hope.

---

## B. Stage 1 Completion Record (synthesised from DB state)

_The Analysis Output instruction's S2 expects a Stage 1 Completion Record from the Analysis Readiness session. Under the v2 strategy the readiness `.md` IS that record. The synthesised confirmation below derives the seven-domain pass criteria from current DB state at generation time._

- **Generation timestamp:** `2026-04-28T06:24:53Z`
- **Schema version:** `3.17.0`
- **OWNER term md_versions present:** `[1]`
  (this is the project's audit equivalent of `meta.export_version`)
- **OWNER terms vc_completed:** 0 / 13
- **OWNER terms legacy-VC (not_done):** 13 / 13

**Synthesised seven-domain pass status:**

| Domain | Check | Status |
|---|---|---|
| A — Data completeness | Registry status fields populated | ✓ |
| A — Data completeness | OWNER terms have md_version | ✓ |
| B — VC completeness | All OWNER terms vc_completed | partial — 13 legacy-VC remain (handled per §K) |
| C — Group integrity | Active groups present per OWNER term | ✓ (see §F) |
| D — Verse coverage | All OWNER terms have ≥1 active verse | see §C term inventory |
| E — Cross-registry | XREF terms documented (§E) | ✓ |
| F — Flag closure | All resolved flags closed | see §H open flags |
| G — Researcher fields | inference_note / word_synopsis preserved | ✗ — researcher narrative absent |

---

## C. Term Inventory — OWNER Terms

| strongs | translit | gloss | lang | status | vc_status | md_v | verses | groups (a/d) | vc rel/sa | anchors |
|---|---|---|---|---|---|---:|---:|---:|---|---:|
| `H2250` | chab.bu.rah | wound | H | `extracted` | **`to_revise`** | 1 | 6 | 2/0 | 4/2 | 2 |
| `H2266` | cha.var | to unite | H | `extracted` | **`to_revise`** | 1 | 25 | 4/0 | 9/16 | 4 |
| `H2267` | che.ver | spell | H | `extracted` | **`to_revise`** | 1 | 4 | 2/0 | 4/0 | 2 |
| `H2270` | cha.ver | companion | H | `extracted` | **`to_revise`** | 1 | 11 | 4/0 | 7/4 | 4 |
| `H2271` | chab.bar | associate | H | `extracted` | **`to_revise`** | 1 | 1 | 0/0 | 0/1 | 0 |
| `H2272` | cha.var.bu.rah | spot | H | `extracted` | **`to_revise`** | 1 | 1 | 1/0 | 1/0 | 1 |
| `H2274` | chev.rah | company | H | `extracted` | **`to_revise`** | 1 | 1 | 1/0 | 1/0 | 1 |
| `H2278` | cha.ve.ret | consort | H | `extracted` | **`to_revise`** | 1 | 1 | 1/0 | 1/0 | 1 |
| `H2279` | cho.ve.ret | set | H | `extracted` | **`to_revise`** | 1 | 3 | 0/0 | 0/3 | 0 |
| `H4225` | mach.be.ret | joining | H | `extracted` | **`to_revise`** | 1 | 7 | 0/0 | 0/7 | 0 |
| `H4226` | me.chab.be.rah | clamp | H | `extracted` | **`to_revise`** | 1 | 2 | 0/0 | 0/2 | 0 |
| `G2842` | koinōnia | participation | G | `extracted` | **`to_revise`** | 1 | 17 | 2/0 | 14/0 | 3 |
| `G2844` | koinōnos | participant | G | `extracted` | **`to_revise`** | 1 | 10 | 2/0 | 8/0 | 2 |

---

## D. OWNER Terms — Lexical Foundation [Unit 3]

Per term: structured meaning parse (`wa_meaning_parsed` / `wa_meaning_sense`), root family, related-words sample, and LSJ data where available.

### `H2250` — chab.bu.rah "wound"

**Identity:** mti=7568 · ti=7732 · language=Hebrew · status=`extracted` · md_v=1

**Meaning parse** (parser v1.0.0, parsed 2026-04-13T05:57:16): 1 top senses · 0 stems · causative=False · domain_tags=False

Senses (top-level):
- `1`: bruise, stripe, wound, blow
Aramaic equivalent: cha.vu.lah (חֲבוּלָא "crime" H2248)

**Related words (22 total; sample of 22):**
- `H2248` cha.vu.la "crime"
- `H2249` cha.vor "Habor"
- `H2266` cha.var "to unite"
- `H2267` che.ver "spell"
- `H2268G` che.ver "Heber"
- `H2268H` che.ver "Heber"
- `H2268I` che.ver "Heber"
- `H2268J` che.ver "Heber"
- `H2270` cha.ver "companion"
- `H2271` chab.bar "associate"
- `H2272` cha.var.bu.rah "spot"
- `H2274` chev.rah "company"
- `H2275A` chev.ron "Hebron"
- `H2275B` chev.ron "Hebron"
- `H2275H` chev.ron "Hebron [Valley]"
- … and 7 more shown of 22 total

### `H2266` — cha.var "to unite"

**Identity:** mti=7565 · ti=7729 · language=Hebrew · status=`extracted` · md_v=1

**Meaning parse** (parser v1.0.0, parsed 2026-04-13T05:57:16): 1 top senses · 0 stems · causative=True · domain_tags=False

Senses (top-level):
- `1`: to unite, join, bind together, be joined, be coupled, be in league, heap up, have fellowship with, be compact, be a charmer

Sub-senses (depth > 1): 11 entries — present in DB; first 15:
  - `1a` (under `None`): (Qal)
  - `1a1` (under `None`): to unite, be joined
  - `1a2` (under `None`): to tie magic charms, charm
  - `1b` (under `None`): (Piel)
  - `1b1` (under `None`): to unite with, make an ally of
  - `1b2` (under `None`): to unite, join, ally
  - `1c` (under `None`): (Pual)
  - `1c1` (under `None`): to be allied with, be united
  - `1c2` (under `None`): to be joined together
  - `1d` (under `None`): (Hiphil) to join together, pile up (words)
  - `1e` (under `None`): (Hithpael) to join oneself to, make an alliance, league together

**Related words (22 total; sample of 22):**
- `H2249` cha.vor "Habor"
- `H2250` chab.bu.rah "wound"
- `H2267` che.ver "spell"
- `H2268G` che.ver "Heber"
- `H2268H` che.ver "Heber"
- `H2268I` che.ver "Heber"
- `H2268J` che.ver "Heber"
- `H2269` cha.var "fellow"
- `H2270` cha.ver "companion"
- `H2271` chab.bar "associate"
- `H2272` cha.var.bu.rah "spot"
- `H2274` chev.rah "company"
- `H2275A` chev.ron "Hebron"
- `H2275B` chev.ron "Hebron"
- `H2275H` chev.ron "Hebron [Valley]"
- … and 7 more shown of 22 total

### `H2267` — che.ver "spell"

**Identity:** mti=7569 · ti=7734 · language=Hebrew · status=`extracted` · md_v=1

**Meaning parse** (parser v1.0.0, parsed 2026-04-13T05:57:16): 3 top senses · 0 stems · causative=False · domain_tags=False

Senses (top-level):
- `1`: association, company, band
- `2`: shared, association, society
- `3`: a magician, charmer, spell

**Related words (21 total; sample of 21):**
- `H2249` cha.vor "Habor"
- `H2250` chab.bu.rah "wound"
- `H2266` cha.var "to unite"
- `H2268G` che.ver "Heber"
- `H2268H` che.ver "Heber"
- `H2268I` che.ver "Heber"
- `H2268J` che.ver "Heber"
- `H2270` cha.ver "companion"
- `H2271` chab.bar "associate"
- `H2272` cha.var.bu.rah "spot"
- `H2274` chev.rah "company"
- `H2275A` chev.ron "Hebron"
- `H2275B` chev.ron "Hebron"
- `H2275H` chev.ron "Hebron [Valley]"
- `H2275I` chev.ron "Hebron"
- … and 6 more shown of 21 total

### `H2270` — cha.ver "companion"

**Identity:** mti=7566 · ti=7730 · language=Hebrew · status=`extracted` · md_v=1

**Meaning parse** (parser v1.0.0, parsed 2026-04-13T05:57:16): 1 top senses · 0 stems · causative=False · domain_tags=False

Senses (top-level):
- `1`: adj
1) united
n m
2) associate, fellow, worshippers
3) companion

**Related words (23 total; sample of 23):**
- `H2249` cha.vor "Habor"
- `H2250` chab.bu.rah "wound"
- `H2266` cha.var "to unite"
- `H2267` che.ver "spell"
- `H2268G` che.ver "Heber"
- `H2268H` che.ver "Heber"
- `H2268I` che.ver "Heber"
- `H2268J` che.ver "Heber"
- `H2269` cha.var "fellow"
- `H2271` chab.bar "associate"
- `H2272` cha.var.bu.rah "spot"
- `H2273` chav.rah "associate"
- `H2274` chev.rah "company"
- `H2275A` chev.ron "Hebron"
- `H2275B` chev.ron "Hebron"
- … and 8 more shown of 23 total

### `H2271` — chab.bar "associate"

**Identity:** mti=7572 · ti=7737 · language=Hebrew · status=`extracted` · md_v=1

**Meaning parse** (parser v1.0.0, parsed 2026-04-13T05:57:16): 1 top senses · 0 stems · causative=False · domain_tags=False

Senses (top-level):
- `1`: associate, partner (in trade)

**Related words (21 total; sample of 21):**
- `H2249` cha.vor "Habor"
- `H2250` chab.bu.rah "wound"
- `H2266` cha.var "to unite"
- `H2267` che.ver "spell"
- `H2268G` che.ver "Heber"
- `H2268H` che.ver "Heber"
- `H2268I` che.ver "Heber"
- `H2268J` che.ver "Heber"
- `H2270` cha.ver "companion"
- `H2272` cha.var.bu.rah "spot"
- `H2274` chev.rah "company"
- `H2275A` chev.ron "Hebron"
- `H2275B` chev.ron "Hebron"
- `H2275H` chev.ron "Hebron [Valley]"
- `H2275I` chev.ron "Hebron"
- … and 6 more shown of 21 total

### `H2272` — cha.var.bu.rah "spot"

**Identity:** mti=7573 · ti=7738 · language=Hebrew · status=`extracted` · md_v=1

**Meaning parse** (parser v1.0.0, parsed 2026-04-13T05:57:16): 1 top senses · 0 stems · causative=False · domain_tags=False

Senses (top-level):
- `1`: spots, stripe, mark

**Related words (21 total; sample of 21):**
- `H2249` cha.vor "Habor"
- `H2250` chab.bu.rah "wound"
- `H2266` cha.var "to unite"
- `H2267` che.ver "spell"
- `H2268G` che.ver "Heber"
- `H2268H` che.ver "Heber"
- `H2268I` che.ver "Heber"
- `H2268J` che.ver "Heber"
- `H2270` cha.ver "companion"
- `H2271` chab.bar "associate"
- `H2274` chev.rah "company"
- `H2275A` chev.ron "Hebron"
- `H2275B` chev.ron "Hebron"
- `H2275H` chev.ron "Hebron [Valley]"
- `H2275I` chev.ron "Hebron"
- … and 6 more shown of 21 total

### `H2274` — chev.rah "company"

**Identity:** mti=7574 · ti=7739 · language=Hebrew · status=`extracted` · md_v=1

**Meaning parse** (parser v1.0.0, parsed 2026-04-13T05:57:16): 1 top senses · 0 stems · causative=False · domain_tags=False

Senses (top-level):
- `1`: company, association

**Related words (21 total; sample of 21):**
- `H2249` cha.vor "Habor"
- `H2250` chab.bu.rah "wound"
- `H2266` cha.var "to unite"
- `H2267` che.ver "spell"
- `H2268G` che.ver "Heber"
- `H2268H` che.ver "Heber"
- `H2268I` che.ver "Heber"
- `H2268J` che.ver "Heber"
- `H2270` cha.ver "companion"
- `H2271` chab.bar "associate"
- `H2272` cha.var.bu.rah "spot"
- `H2275A` chev.ron "Hebron"
- `H2275B` chev.ron "Hebron"
- `H2275H` chev.ron "Hebron [Valley]"
- `H2275I` chev.ron "Hebron"
- … and 6 more shown of 21 total

### `H2278` — cha.ve.ret "consort"

**Identity:** mti=7576 · ti=7741 · language=Hebrew · status=`extracted` · md_v=1

**Meaning parse** (parser v1.0.0, parsed 2026-04-13T05:57:16): 1 top senses · 0 stems · causative=False · domain_tags=False

Senses (top-level):
- `1`: companion, wife, consort

**Related words (21 total; sample of 21):**
- `H2249` cha.vor "Habor"
- `H2250` chab.bu.rah "wound"
- `H2266` cha.var "to unite"
- `H2267` che.ver "spell"
- `H2268G` che.ver "Heber"
- `H2268H` che.ver "Heber"
- `H2268I` che.ver "Heber"
- `H2268J` che.ver "Heber"
- `H2270` cha.ver "companion"
- `H2271` chab.bar "associate"
- `H2272` cha.var.bu.rah "spot"
- `H2274` chev.rah "company"
- `H2275A` chev.ron "Hebron"
- `H2275B` chev.ron "Hebron"
- `H2275H` chev.ron "Hebron [Valley]"
- … and 6 more shown of 21 total

### `H2279` — cho.ve.ret "set"

**Identity:** mti=7570 · ti=7735 · language=Hebrew · status=`extracted` · md_v=1

**Meaning parse** (parser v1.0.0, parsed 2026-04-13T05:57:16): 2 top senses · 0 stems · causative=False · domain_tags=False

Senses (top-level):
- `1`: junction, a thing joined
- `2`: curtain pieces of the tabernacle

**Related words (21 total; sample of 21):**
- `H2249` cha.vor "Habor"
- `H2250` chab.bu.rah "wound"
- `H2266` cha.var "to unite"
- `H2267` che.ver "spell"
- `H2268G` che.ver "Heber"
- `H2268H` che.ver "Heber"
- `H2268I` che.ver "Heber"
- `H2268J` che.ver "Heber"
- `H2270` cha.ver "companion"
- `H2271` chab.bar "associate"
- `H2272` cha.var.bu.rah "spot"
- `H2274` chev.rah "company"
- `H2275A` chev.ron "Hebron"
- `H2275B` chev.ron "Hebron"
- `H2275H` chev.ron "Hebron [Valley]"
- … and 6 more shown of 21 total

### `H4225` — mach.be.ret "joining"

**Identity:** mti=7567 · ti=7731 · language=Hebrew · status=`extracted` · md_v=1

**Meaning parse** (parser v1.0.0, parsed 2026-04-13T05:57:16): 1 top senses · 0 stems · causative=False · domain_tags=False

Senses (top-level):
- `1`: thing joined, joint, seam, place of joining

Sub-senses (depth > 1): 2 entries — present in DB; first 15:
  - `1a` (under `None`): thing joined
  - `1b` (under `None`): place of joining

**Related words (21 total; sample of 21):**
- `H2249` cha.vor "Habor"
- `H2250` chab.bu.rah "wound"
- `H2266` cha.var "to unite"
- `H2267` che.ver "spell"
- `H2268G` che.ver "Heber"
- `H2268H` che.ver "Heber"
- `H2268I` che.ver "Heber"
- `H2268J` che.ver "Heber"
- `H2270` cha.ver "companion"
- `H2271` chab.bar "associate"
- `H2272` cha.var.bu.rah "spot"
- `H2274` chev.rah "company"
- `H2275A` chev.ron "Hebron"
- `H2275B` chev.ron "Hebron"
- `H2275H` chev.ron "Hebron [Valley]"
- … and 6 more shown of 21 total

### `H4226` — me.chab.be.rah "clamp"

**Identity:** mti=7571 · ti=7736 · language=Hebrew · status=`extracted` · md_v=1

**Meaning parse** (parser v1.0.0, parsed 2026-04-13T05:57:16): 1 top senses · 0 stems · causative=False · domain_tags=False

Senses (top-level):
- `1`: binder, clamp, joint

**Related words (21 total; sample of 21):**
- `H2249` cha.vor "Habor"
- `H2250` chab.bu.rah "wound"
- `H2266` cha.var "to unite"
- `H2267` che.ver "spell"
- `H2268G` che.ver "Heber"
- `H2268H` che.ver "Heber"
- `H2268I` che.ver "Heber"
- `H2268J` che.ver "Heber"
- `H2270` cha.ver "companion"
- `H2271` chab.bar "associate"
- `H2272` cha.var.bu.rah "spot"
- `H2274` chev.rah "company"
- `H2275A` chev.ron "Hebron"
- `H2275B` chev.ron "Hebron"
- `H2275H` chev.ron "Hebron [Valley]"
- … and 6 more shown of 21 total

### `G2842` — koinōnia "participation"

**Identity:** mti=873 · ti=911 · language=Greek · status=`extracted` · md_v=1

**Meaning parse** (parser v1.0.0, parsed 2026-04-13T05:57:16): 1 top senses · 0 stems · causative=False · domain_tags=False

Senses (top-level):
- `1`: fellowship, the close association between persons, emphasizing what is common between them; by extension: participation, sharing, contribution, gift, the outcome of such close relationships 
fellowship, partnership, Acts 2:42; 2Cor. 6:14; 13:13; Gal. 2:9; Phil. 3:10; 1Jn. 1:3; participation, communion, 1Cor. 10:16; aid, relief, Heb. 13:16; contribution in aid, Rom. 15:26

**Root family:**
- `KOINŌN` (Greek): participant — Backfilled 2026-04-09 from wa_term_related_words clustering

**Related words (1 total; sample of 1):**
- `G2844` koinōnos "participant"

**LSJ:** _not parsed for this term (LSJ data is sparse — meaning work proceeds without it)._

### `G2844` — koinōnos "participant"

**Identity:** mti=5367 · ti=5481 · language=Greek · status=`extracted` · md_v=1

**Meaning parse** (parser v1.0.0, parsed 2026-04-13T05:57:16): 1 top senses · 0 stems · causative=False · domain_tags=False

Senses (top-level):
- `1`: partner, participant, one who joins in with another in some enterprise or activity, in business or ministry 
a fellow, partner, companion, Mt. 23:30; Lk. 5:10; 1Cor. 10:18, 20; 2Cor. 8:23; Phlm. 17; Heb. 10:33; a sharer, partaker, 2Cor. 1:7; 1Pet. 5:1; 2Pet. 1:4*

**Root family:**
- `KOINŌN` (Greek): participant — Backfilled 2026-04-09 from wa_term_related_words clustering

**Related words (6 total; sample of 6):**
- `G2839G` koinos "common: unsanctified"
- `G2839H` koinos "common: shared"
- `G2841` koinōneō "to participate"
- `G2842` koinōnia "participation"
- `G2843` koinōnikos "generous"
- `G4791` sunkoinōnos "sharer"

**LSJ:** _not parsed for this term (LSJ data is sparse — meaning work proceeds without it)._

---

## E. XREF Terms [Unit 2] (0)

_None._

---

## F. Verse Context Groups — Landscape [Unit 4]

Per OWNER term: all active groups with descriptions, **dimension assignments** (from `wa_dimension_index`), anchor counts, and relevant counts.

### `H2250` — 2 groups

- **`7568-001`** — 2 relevant · 1 anchor verse(s) · dimension: `08 — Transformation` · cluster: `C17`
  - *disciplinary wound as instrument of inner moral purification*
- **`7568-002`** — 2 relevant · 1 anchor verse(s) · dimension: `08 — Transformation` · cluster: `C17`
  - *redemptive wound producing inner healing and restoration*

### `H2266` — 4 groups

- **`7565-001`** — 5 relevant · 1 anchor verse(s) · dimension: `06 — Relational Disposition` · cluster: `C17`
  - *idolatrous or wrongful relational alliance as volitional inner joining*
- **`7565-002`** — 2 relevant · 1 anchor verse(s) · dimension: `05 — Moral Character` · cluster: `C17`
  - *occult charming as forbidden inner-spiritual practice*
- **`7565-003`** — 1 relevant · 1 anchor verse(s) · dimension: `03 — Cognition` · cluster: `C17`
  - *joining words as inner rhetorical expression*
- **`7565-004`** — 1 relevant · 1 anchor verse(s) · dimension: `01 — Emotion — Positive` · cluster: `C17`
  - *communal participation as ground of inner hope*

### `H2267` — 2 groups

- **`7569-001`** — 2 relevant · 1 anchor verse(s) · dimension: `05 — Moral Character` · cluster: `C17`
  - *occult charming as forbidden spiritual practice*
- **`7569-002`** — 2 relevant · 1 anchor verse(s) · dimension: `05 — Moral Character` · cluster: `C17`
  - *reliance on occult power as spiritual misdirection and arrogance*

### `H2270` — 4 groups

- **`7566-001`** — 2 relevant · 1 anchor verse(s) · dimension: `06 — Relational Disposition` · cluster: `C17`
  - *companionship as chosen moral and spiritual alignment*
- **`7566-002`** — 3 relevant · 1 anchor verse(s) · dimension: `06 — Relational Disposition` · cluster: `C17`
  - *companionship as moral alignment with wickedness*
- **`7566-003`** — 1 relevant · 1 anchor verse(s) · dimension: `06 — Relational Disposition` · cluster: `C17`
  - *companionship as mutual relational support*
- **`7566-004`** — 1 relevant · 1 anchor verse(s) · dimension: `08 — Transformation` · cluster: `C17`
  - *divinely-willed communal restoration as inner-being oneness*

### `H2271` — 0 groups

_No active groups (term may be legacy-VC or set-aside-only)._

### `H2272` — 1 groups

- **`7573-001`** — 1 relevant · 1 anchor verse(s) · dimension: `05 — Moral Character` · cluster: `C17`
  - *indelibly formed inner moral character depicted as fixed marking*

### `H2274` — 1 groups

- **`7574-001`** — 1 relevant · 1 anchor verse(s) · dimension: `05 — Moral Character` · cluster: `C17`
  - *keeping company with evildoers as moral alignment*

### `H2278` — 1 groups

- **`7576-001`** — 1 relevant · 1 anchor verse(s) · dimension: `06 — Relational Disposition` · cluster: `C17`
  - *covenantal companionship as the relational bond that faithlessness violates*

### `H2279` — 0 groups

_No active groups (term may be legacy-VC or set-aside-only)._

### `H4225` — 0 groups

_No active groups (term may be legacy-VC or set-aside-only)._

### `H4226` — 0 groups

_No active groups (term may be legacy-VC or set-aside-only)._

### `G2842` — 2 groups

- **`873-001`** — 8 relevant · 2 anchor verse(s) · dimension: `11 — Divine-Human Correspondence` · cluster: `C17`
  - *Vertical fellowship with God — the inner-relational participation in divine nature, the Son, and the Spirit that constitutes the believer's communion with God*
  - notes: Phase B.5 characteristic-perspective rewrite — WA-DimensionReview-Instruction-v2.2-2026-04-11
- **`873-002`** — 6 relevant · 1 anchor verse(s) · dimension: `06 — Relational Disposition` · cluster: `C17`
  - *Horizontal fellowship among believers — the inner-relational bond of mutual belonging, shared commitment, and generous participation arising from shared life in Christ*
  - notes: Phase B.5 characteristic-perspective rewrite — WA-DimensionReview-Instruction-v2.2-2026-04-11

### `G2844` — 2 groups

- **`5367-001`** — 5 relevant · 1 anchor verse(s) · dimension: `11 — Divine-Human Correspondence` · cluster: `C17`
  - *Inner-spiritual participation — the disposition of the person as sharer in divine nature, suffering, comfort, or cultic alignment through inner orientation*
  - notes: Phase B.5 characteristic-perspective rewrite — WA-DimensionReview-Instruction-v2.2-2026-04-11
- **`5367-002`** — 3 relevant · 1 anchor verse(s) · dimension: `05 — Moral Character` · cluster: `C17`
  - *Moral alignment through participation — the inner orientation that places a person in solidarity with righteousness or complicity with wickedness*
  - notes: Phase B.5 characteristic-perspective rewrite — WA-DimensionReview-Instruction-v2.2-2026-04-11

---

## G. Correlation Signals [Unit 5] (computed)

Three signal types computed at generation time from DB state:
- **XREF sharing** — registries that own terms appearing as XREF in this registry
- **Verse co-occurrence** — same verse classified is_relevant=1 in this registry AND another (≥3 shared verses)
- **Shared anchors** — same verse appears as is_anchor=1 in this registry AND another

### G.1 XREF sharing

_No XREF sharing._

### G.2 Verse co-occurrence (≥3 shared)

| Other registry | shared verses |
|---|---:|
| 43 desire | 6 |
| 59 faith | 3 |
| 68 grace | 3 |
| 167 unity | 3 |
| 184 spirit | 3 |
| 187 strength | 3 |
| 192 comfort | 3 |

### G.3 Shared anchors

| Other registry | shared anchor verse |
|---|---|
| 30 contrition | Isa 53:5 |
| 51 distress | Hos 4:17 |
| 120 perverseness | Jer 13:23 |
| 150 sorcery | Isa 47:9 |
| 151 sorrow | Isa 53:5 |
| 180 yielding | 2Pe 1:4 |
| 186 gladness | Jer 13:23 |
| 187 strength | Isa 47:9 |
| 196 power | Jer 13:23 |
| 209 likeness | Phili 3:10 |
| 210 deadness | Phili 3:10 |

---

## H. Existing SD Pointers + session_b_findings [Units 6 + 9]

### H.1 Existing session_b_findings (16)

#### `062-STRUCT-001` — `STRUCTURAL_DISPOSITION`

- **status:** `confirmed` · **thin_evidence:** 0 · **raised:** 2026-04-16 · **term_id:** -

> Fellowship originates from multiple sources: divine granting through promises enabling participation in divine nature, volitional inner alignment where humans choose moral/spiritual direction, and divine unification action where God actively joins divided elements into unity. Fellowship's structural disposition is relational participation rather than solitary experience.

**Anchor verses cited:** 2Pe 1:4, Psa 119:63, Isa 1:23, Eze 37:19

#### `062-OPER-001` — `OPERATION_MODES`

- **status:** `confirmed` · **thin_evidence:** 0 · **raised:** 2026-04-16 · **term_id:** -

> Fellowship operates in six distinct modes: ontological participation in divine nature, moral complicity creating culpability, volitional alignment choosing moral/spiritual direction, transformational mechanism through wounds producing purification and healing, spiritual bondage through joining with idols, and cognitive construction joining words for rhetorical effect.

**Anchor verses cited:** 2Pe 1:4, Mat 23:30, Psa 119:63, Isa 1:23, Pro 20:30, Isa 53:5, Hos 4:17, Job 16:4

#### `062-INNER-001` — `INNER_BEING_EFFECTS`

- **status:** `confirmed` · **thin_evidence:** 0 · **raised:** 2026-04-16 · **term_id:** -

> Fellowship produces varied inner-being effects determined by the fellowship object: capacity for divine nature participation, hope grounded in communal participation, moral responsibility and potential culpability, inner purification through disciplinary wounds, healing through redemptive wounds, and spiritual bondage when aligned with idols. Effect quality depends entirely on the fellowship object.

**Anchor verses cited:** 2Pe 1:4, Ecc 9:4, Mat 23:30, Pro 20:30, Isa 53:5, Hos 4:17

#### `062-RELAT-001` — `RELATIONAL_POSITIONING`

- **status:** `confirmed` · **thin_evidence:** 0 · **raised:** 2026-04-16 · **term_id:** -

> Fellowship fundamentally transforms relational positioning by creating horizontal fellowship chains grounded in vertical fellowship, establishing mutual support systems, creating moral alignment with righteousness or wickedness, potentially violating existing covenantal bonds through faithlessness, and requiring moral/spiritual compatibility where righteousness cannot fellowship with lawlessness.

**Anchor verses cited:** 1Jo 1:3, Ecc 4:10, Psa 119:63, Isa 1:23, Mal 2:14, 2Cor 6:14

#### `062-DIVINE-001` — `DIVINE_DISPOSITION`

- **status:** `confirmed` · **thin_evidence:** 0 · **raised:** 2026-04-16 · **term_id:** -

> Fellowship reveals God's disposition as enabling and unifying: God grants precious and great promises to enable human participation in divine nature, God actively joins divided elements into unity through divine fellowship action, and God serves as witness to covenant fellowship violations, caring about relational faithfulness. God's disposition is toward inclusion in divine fellowship rather than exclusion.

**Anchor verses cited:** 2Pe 1:4, Eze 37:19, Mal 2:14

#### `062-TEMP-001` — `TEMPORAL_OPERATION`

- **status:** `confirmed` · **thin_evidence:** 0 · **raised:** 2026-04-16 · **term_id:** -

> Fellowship describes both one-time acts and ongoing conditions. One-time acts include divine promises enabling nature participation and active divine joining of divided elements. Ongoing conditions include companionship with those who fear God, being joined with all the living as hope foundation, and covenantal companionship in marriage. Fellowship can be both initiating event and sustaining condition.

**Anchor verses cited:** 2Pe 1:4, Eze 37:19, Psa 119:63, Ecc 9:4, Mal 2:14

#### `062-ENABLE-001` — `ENABLING_CAPACITY`

- **status:** `confirmed` · **thin_evidence:** 0 · **raised:** 2026-04-16 · **term_id:** -

> Fellowship produces enabling capacity across multiple dimensions: capacity for divine nature participation through escape from corruption, capacity for mutual support enabling lifting up of fallen companions, and capacity for shared suffering and resurrection power fellowship. Fellowship enables ontological, relational, and transformational capacities that were previously unavailable.

**Anchor verses cited:** 2Pe 1:4, Ecc 4:10, Phili 3:10

#### `062-CHAR-001` — `CHARACTER_FORMATION`

- **status:** `confirmed` · **thin_evidence:** 0 · **raised:** 2026-04-16 · **term_id:** -

> Fellowship produces character quality aligned with its object: participation in divine character through divine nature fellowship, righteous alignment through fear-of-God companionship, wicked character through evil companionship, and faithlessness through covenant violation. Fellowship amplifies and conforms character to the fellowship object's nature.

**Anchor verses cited:** 2Pe 1:4, Psa 119:63, Isa 1:23, Job 34:8, Mal 2:14

#### `062-EXPR-001` — `RELATIONAL_EXPRESSION`

- **status:** `confirmed` · **thin_evidence:** 0 · **raised:** 2026-04-16 · **term_id:** -

> Fellowship expresses relationally through proclaiming to create fellowship chains, mutual support in falling and restoration, moral alignment choice between righteous and wicked companionship, generous participation and shared commitment among believers, and avoiding incompatible fellowships.

**Anchor verses cited:** 1Jo 1:3, Ecc 4:10, Psa 119:63, Isa 1:23, 2Cor 6:14

#### `062-GROUN-001` — `GROUND_CONDITION`

- **status:** `confirmed` · **thin_evidence:** 0 · **raised:** 2026-04-16 · **term_id:** -

> Genuine fellowship requires specific inner orientation: fear of God and precept-keeping as companionship foundation, escape from corruption enabling divine nature participation, and moral/spiritual compatibility where righteousness cannot fellowship with lawlessness. The ground is moral and spiritual alignment rather than preference or proximity.

**Anchor verses cited:** Psa 119:63, 2Pe 1:4, 2Cor 6:14

#### `062-SEQUE-001` — `OPERATIONAL_SEQUENCE`

- **status:** `confirmed` · **thin_evidence:** 0 · **raised:** 2026-04-16 · **term_id:** -

> Fellowship follows discernible sequences: divine promises leading to corruption escape leading to divine nature participation; knowing Christ leading to sharing sufferings leading to resurrection power fellowship; proclamation leading to hearing leading to fellowship creation; and wounding leading to purification leading to healing through fellowship vocabulary. Fellowship operates through prerequisite-to-participation sequences.

**Anchor verses cited:** 2Pe 1:4, Phili 3:10, 1Jo 1:3, Pro 20:30, Isa 53:5

#### `062-ORIG-001` — `ORIGINATING_SOURCE`

- **status:** `confirmed` · **thin_evidence:** 0 · **raised:** 2026-04-16 · **term_id:** -

> Fellowship originates from multiple sources: divine source through God granting precious and great promises, divine action where God actively joins divided elements, and human volitional choice in companionship with those who fear God. Both divine initiative and human response generate fellowship.

**Anchor verses cited:** 2Pe 1:4, Eze 37:19, Psa 119:63

#### `062-RESPO-001` — `INNER_RESPONSE`

- **status:** `confirmed` · **thin_evidence:** 0 · **raised:** 2026-04-16 · **term_id:** -

> Fellowship produces natural inner responses: hope grounded in communal participation, moral responsibility sense from shared complicity, desire for further fellowship extension through proclamation, and mutual support instinct for lifting fallen companions. Fellowship generates fellowship-seeking and fellowship-extending responses.

**Anchor verses cited:** Ecc 9:4, Mat 23:30, 1Jo 1:3, Ecc 4:10

#### `062-EXTEN-001` — `EXTENSION_REASON`

- **status:** `confirmed` · **thin_evidence:** 0 · **raised:** 2026-04-16 · **term_id:** -

> Divine fellowship extension is based on divine character where God grants promises to enable divine nature participation rather than recipient merit. Human fellowship extension is based on recipient's moral/spiritual alignment including fear of God and precept-keeping as companionship basis.

**Anchor verses cited:** 2Pe 1:4, Psa 119:63

#### `062-EXTRE-001` — `EXTREMITY_DEPTH`

- **status:** `confirmed` · **thin_evidence:** 0 · **raised:** 2026-04-16 · **term_id:** -

> Fellowship in extremity reveals profound depth of operation: fellowship through substitutionary wounds operates at the deepest level of vicarious suffering, fellowship through disciplinary wounds reaches innermost parts for evil cleansing, and fellowship through joining with Christ's sufferings and death indicates fellowship operates even through mortality threshold.

**Anchor verses cited:** Isa 53:5, Pro 20:30, Phili 3:10

#### `062-GRAMM-001` — `GRAMMATICAL_SUBJECT`

- **status:** `confirmed` · **thin_evidence:** 0 · **raised:** 2026-04-16 · **term_id:** -

> Fellowship shows mixed grammatical subjects: divine subjects where God grants promises and actively joins divided elements, human subjects choosing companionship and participating, and mixed agency where divine and human subjects interact in fellowship chains. All groups show human as dominant subject but divine agency is significantly present.

**Anchor verses cited:** 2Pe 1:4, Eze 37:19, Psa 119:63, Hos 4:17, Mat 23:30, 1Jo 1:3

### H.2 Open SD pointers + research flags (11)

| flag_code | label | priority | session | raised |
|---|---|---|---|---|
| `DIMREVIEW_SESSION_D` | DIM-62-SD001 | MEDIUM | D | 2026-04-11 |
| `SD_POINTER` | 062-SD003 | MEDIUM | D | 2026-04-16 |
| `SD_POINTER` | 062-SD005 | MEDIUM | D | 2026-04-16 |
| `SD_POINTER` | 062-SD008 | MEDIUM | D | 2026-04-16 |
| `SD_POINTER` | 062-SD010 | MEDIUM | D | 2026-04-16 |
| `SD_POINTER` | DIM-062-SD001 | HIGH | D | 2026-04-13 |
| `SD_POINTER` | 062-SD002 | HIGH | D | 2026-04-16 |
| `SD_POINTER` | 062-SD004 | HIGH | D | 2026-04-16 |
| `SD_POINTER` | 062-SD006 | HIGH | D | 2026-04-16 |
| `SD_POINTER` | 062-SD007 | HIGH | D | 2026-04-16 |
| `SD_POINTER` | 062-SD009 | HIGH | D | 2026-04-16 |

#### DIM-62-SD001

> Reg 62 (fellowship) has four groups that together trace three axes of koinōnia: (1) the divine-human correspondence axis (5367-001 — partaking of divine nature; 873-001 — communion with Father and Son), (2) the moral-character axis (5367-002 — solidarity/complicity), and (3) the horizontal-relational axis (873-002 — mutual belonging among believers). These three axes are not independent — the horizontal fellowship among believers (873-002) is explicitly grounded in the vertical fellowship with God (1Jo 1:3). Session D should examine whether the fellowship vocabulary of Reg 62 encodes a structural relationship: that genuine human inner-relational community (C17's relational-disposition cluster) is grounded in and derives from participation in the divine community (Father-Son-Spirit). This would make Reg 62 (fellowship) functionally analogous to Reg 34 (covenant) as a structural container: covenant names the bond, fellowship names the participatory inner reality of that bond.

#### 062-SD003

> Fellowship as moral complicity mechanism. Mat 23:30 uses fellowship language for moral participation in evil. Session D investigation: How does fellowship vocabulary relate to moral responsibility and guilt by association? What is the relationship between relational alignment and moral culpability? Cross-registry targets: guilt, conscience, moral character registries.

#### 062-SD005

> Fear of God as fellowship foundation. Psa 119:63 grounds companionship in fear of God and precept-keeping. Session D investigation: How does fear of God and precept obedience create the inner-being foundation for righteous fellowship? Cross-registry targets: fear of God, obedience registries.

#### 062-SD008

> Covenant fellowship violations. Mal 2:14 connects companionship, covenant, and faithlessness in marriage context. Session D investigation: How does fellowship vocabulary illuminate the inner-being dynamics of covenant violation and marital faithlessness? Cross-registry targets: covenant, faithfulness, marriage registries.

#### 062-SD010

> Fellowship moral/spiritual compatibility requirements. 2Cor 6:14 presents fellowship as requiring moral/spiritual compatibility between righteousness and lawlessness, light and darkness. Session D investigation: How does fellowship vocabulary illuminate the inner-being incompatibility between righteousness and lawlessness, light and darkness? Cross-registry targets: righteousness, light/darkness, moral incompatibility registries.

#### DIM-062-SD001

> Scripture's use of physical and structural joining vocabulary (chavar root family, Registry 62 fellowship) as analogical illumination of inner-being realities. During VCB-037 Verse Context classification, a substantial corpus of physical_only set-asides was identified across the chavar root family: tabernacle curtain coupling (Exo 26:3, 26:6, 26:9, 26:11, 36:10, 36:13, 36:16, 36:18), priestly garment joining (Exo 28:7, 39:4), joining-seam vocabulary (H4225 mach.be.ret, 7 verses), curtain-set vocabulary (H2279 cho.ve.ret, 3 verses), and building clamps (H4226 me.chab.be.rah, 2 verses). The researcher identified that Scripture frequently illuminates inner-being realities indirectly through physical description, structural imagery, and implicit analogy — the physical term functions as a lens through which inner-being truth becomes visible without the connection being stated explicitly. This cannot be resolved at Verse Context or Session B stage. Session D investigation question: Where does the physical and structural vocabulary of the fellowship and joining root (chavar family) illuminate inner-being realities of unity, covenant, and belonging through analogy or implicit comparison? Specific candidates: (1) Exo 26:6 and 36:13 — tabernacle curtains coupled into a single whole — does this structural unity carry analogical weight about inner-being or covenantal oneness? (2) Psa 122:3 — Jerusalem bound firmly together (set aside as spatial_only at VC stage) — does urban structural unity illuminate gathered community inner-being solidarity? (3) H4225 mach.be.ret — the seam or joining-point of the ephod — does structural joining in sacred garments carry analogical inner-being significance? (4) The two-becoming-one pattern across the tabernacle joining corpus — does this structure speak to inner-being pairing or covenant? Cross-registry partners to examine: unity, covenant, belonging, wholeness — whichever registries carry those words. Session B instruction: when analysing Registry 62 anchor verses, note without resolving any verse where physical usage appears to carry analogical illumination of inner-being realities, and raise this SD pointer reference in the Session B observations log.

#### 062-SD002

> Divine nature participation as ontological fellowship. 2Pe 1:4 presents fellowship (koinōnia) as participation in divine nature enabled by escape from corruption. Session D investigation: What is the inner-being transformation that enables divine nature participation? What are the characteristics of this ontological fellowship? Cross-registry targets: divine nature registries, transformation cluster.

#### 062-SD004

> Fellowship as spiritual adultery/bondage. Hos 4:17 presents idolatrous joining as complete spiritual bondage warranting divine abandonment. Session D investigation: How does fellowship/joining vocabulary illuminate the inner-being dynamics of spiritual adultery and idolatrous alliance? Cross-registry targets: idolatry, spiritual adultery, faithlessness registries.

#### 062-SD006

> Divine fellowship action in restoration. Eze 37:19 presents God as actively joining divided sticks into one — physical metaphor for community restoration. Session D investigation: How does divine joining/fellowship action restore divided communities into unified wholes? What is the inner-being mechanism of divinely-accomplished fellowship? Cross-registry targets: unity, restoration, covenant registries.

#### 062-SD007

> Fellowship through transformative wounding. Pro 20:30 and Isa 53:5 present fellowship vocabulary for transformative wounding — disciplinary and redemptive wounds. Session D investigation: How does fellowship vocabulary (chavar root family) illuminate the inner-being mechanism by which suffering produces purification and healing? Cross-registry targets: suffering, purification, healing, atonement registries.

#### 062-SD009

> Fellowship through suffering-death-resurrection trajectory. Phili 3:10 links knowing Christ, sharing sufferings, and resurrection power in single fellowship trajectory. Session D investigation: How does fellowship with Christ's sufferings relate to fellowship with resurrection power? What is the inner-being mechanism of suffering-death-resurrection fellowship? Cross-registry targets: suffering, resurrection, conformity registries.

---

## I. Thin-Evidence Phase2 Flags [Unit 8]

_No phase2 flags on any OWNER term._

---

## J. Anchor Verse Material — All Verbatim Verse Text [Unit 7]

Each verse listed with: group code · `is_relevant` (✓/✗) · `is_anchor` (🔵 marker) · `set_aside_reason` if set aside · `target_word` · full verse text. **Anchor verses (🔵) are the primary reading targets per Unit 7.**

### `H2250` — 6/6 classified · 2 anchor verse(s)

**Group `7568-001`** (2 verses — anchors: Pro 20:30)

- **Pro 20:30** 🔵 (✓) *target: Blows*
  > Pro 20:30 Blows that wound cleanse away evil ; strokes make clean the innermost parts .
- **Psa 38:5** (✓) *target: wounds*
  > Psa 38:5 My wounds stink and fester because of my foolishness ,

**Group `7568-002`** (2 verses — anchors: Isa 53:5)

- **Isa 53:5** 🔵 (✓) *target: wounds*
  > Isa 53:5 But he was pierced for our transgressions ; he was crushed for our iniquities ; upon him was the chastisement that brought us peace , and with his wounds we are healed .
- **Isa 1:6** (✓) *target: bruises*
  > Isa 1:6 From the sole of the foot even to the head , there is no soundness in it, but bruises and sores and raw wounds ; they are not pressed out or bound up or softened with oil .

**Group `SET-ASIDE`** (2 verses)

- **Gen 4:23** (✗) [set_aside: physical_only] *target: striking me*
  > Gen 4:23 Lamech said to his wives : “ Adah and Zillah , hear my voice ; you wives of Lamech , listen to what I say : I have killed a man for wounding me, a young man for striking me .
- **Exo 21:25** (✗) [set_aside: no_inner_being] *target: stripe*
  > Exo 21:25 burn for burn , wound for wound , stripe for stripe .

### `H2266` — 25/25 classified · 4 anchor verse(s)

**Group `7565-001`** (5 verses — anchors: Hos 4:17)

- **Hos 4:17** 🔵 (✓) *target: joined*
  > Hos 4:17 Ephraim is joined to idols ; leave him alone .
- **2Ch 20:35** (✓) *target: joined*
  > 2Ch 20:35 After this Jehoshaphat king of Judah joined with Ahaziah king of Israel , who acted wickedly .
- **2Ch 20:36** (✓) *target: joined*
  > 2Ch 20:36 He joined him in building ships to go to Tarshish , and they built the ships in Ezion-geber .
- **2Ch 20:37** (✓) *target: joined*
  > 2Ch 20:37 Then Eliezer the son of Dodavahu of Mareshah prophesied against Jehoshaphat , saying , “Because you have joined with Ahaziah , the Lord will destroy what you have made .” And the ships were wrecked and were not able to go to Tarshish .
- **Psa 94:20** (✓) *target: allied*
  > Psa 94:20 Can wicked rulers be allied with you, those who frame injustice by statute ?

**Group `7565-002`** (2 verses — anchors: Psa 58:5)

- **Psa 58:5** 🔵 (✓) *target: enchanter*
  > Psa 58:5 so that it does not hear the voice of charmers or of the cunning enchanter .
- **Deu 18:11** (✓) *target: charmer*
  > Deu 18:11 or a charmer or a medium or a necromancer or one who inquires of the dead ,

**Group `7565-003`** (1 verse — anchors: Job 16:4)

- **Job 16:4** 🔵 (✓) *target: join*
  > Job 16:4 I also could speak as you do, if you were in my place; I could join words together against you and shake my head at you.

**Group `7565-004`** (1 verse — anchors: Ecc 9:4)

- **Ecc 9:4** 🔵 (✓) *target: joined*
  > Ecc 9:4 But he who is joined with all the living has hope , for a living dog is better than a dead lion .

**Group `SET-ASIDE`** (16 verses)

- **Gen 14:3** (✗) [set_aside: no_inner_being] *target: joined*
  > Gen 14:3 And all these joined forces in the Valley of Siddim ( that is, the Salt Sea ).
- **Exo 26:3** (✗) [set_aside: physical_only] *target: coupled*
  > Exo 26:3 Five curtains shall be coupled to one another , and the other five curtains shall be coupled to one another .
- **Exo 26:6** (✗) [set_aside: physical_only] *target: couple*
  > Exo 26:6 And you shall make fifty clasps of gold , and couple the curtains one to the other with the clasps , so that the tabernacle may be a single whole .
- **Exo 26:9** (✗) [set_aside: physical_only] *target: couple*
  > Exo 26:9 You shall couple five curtains by themselves, and six curtains by themselves, and the sixth curtain you shall double over at the front of the tent .
- **Exo 26:11** (✗) [set_aside: physical_only] *target: couple*
  > Exo 26:11 “You shall make fifty clasps of bronze , and put the clasps into the loops , and couple the tent together that it may be a single whole .
- **Exo 28:7** (✗) [set_aside: physical_only] *target: attached*
  > Exo 28:7 It shall have two shoulder pieces attached to its two edges , so that it may be joined together .
- **Exo 36:10** (✗) [set_aside: physical_only] *target: coupled*
  > Exo 36:10 He coupled five curtains to one another , and the other five curtains he coupled to one another .
- **Exo 36:13** (✗) [set_aside: physical_only] *target: coupled*
  > Exo 36:13 And he made fifty clasps of gold , and coupled the curtains one to the other with clasps . So the tabernacle was a single whole .
- **Exo 36:16** (✗) [set_aside: physical_only] *target: coupled*
  > Exo 36:16 He coupled five curtains by themselves , and six curtains by themselves .
- **Exo 36:18** (✗) [set_aside: physical_only] *target: couple*
  > Exo 36:18 And he made fifty clasps of bronze to couple the tent together that it might be a single whole .
- **Exo 39:4** (✗) [set_aside: physical_only] *target: attaching*
  > Exo 39:4 They made for the ephod attaching shoulder pieces , joined to it at its two edges .
- **Psa 122:3** (✗) [set_aside: spatial_only] *target: bound firmly*
  > Psa 122:3 Jerusalem — built as a city that is bound firmly together ,
- **Eze 1:9** (✗) [set_aside: physical_only] *target: touched*
  > Eze 1:9 their wings touched one another . Each one of them went straight forward , without turning as they went .
- **Eze 1:11** (✗) [set_aside: physical_only] *target: touched*
  > Eze 1:11 Such were their faces . And their wings were spread out above . Each creature had two wings, each of which touched the wing of another, while two covered their bodies .
- **Dan 11:6** (✗) [set_aside: no_inner_being] *target: alliance*
  > Dan 11:6 After some years they shall make an alliance , and the daughter of the king of the south shall come to the king of the north to make an agreement . But she shall not retain the strength of her arm , and he and his arm shall not endure , but she shall be given up , and her attendants , he who fathered her, and he who supported her in those times .
- **Dan 11:23** (✗) [set_aside: no_inner_being] *target: alliance*
  > Dan 11:23 And from the time that an alliance is made with him he shall act deceitfully , and he shall become strong with a small people .

### `H2267` — 4/4 classified · 2 anchor verse(s)

**Group `7569-001`** (2 verses — anchors: Psa 58:5)

- **Psa 58:5** 🔵 (✓) *target: enchanter*
  > Psa 58:5 so that it does not hear the voice of charmers or of the cunning enchanter .
- **Deu 18:11** (✓) *target: charmer*
  > Deu 18:11 or a charmer or a medium or a necromancer or one who inquires of the dead ,

**Group `7569-002`** (2 verses — anchors: Isa 47:9)

- **Isa 47:9** 🔵 (✓) *target: enchantments*
  > Isa 47:9 These two things shall come to you in a moment , in one day ; the loss of children and widowhood shall come upon you in full measure , in spite of your many sorceries and the great power of your enchantments .
- **Isa 47:12** (✓) *target: enchantments*
  > Isa 47:12 Stand fast in your enchantments and your many sorceries , with which you have labored from your youth ; perhaps you may be able to succeed ; perhaps you may inspire terror .

### `H2270` — 11/11 classified · 4 anchor verse(s)

**Group `7566-001`** (2 verses — anchors: Psa 119:63)

- **Psa 119:63** 🔵 (✓) *target: companion*
  > Psa 119:63 I am a companion of all who fear you, of those who keep your precepts .
- **Judg 20:11** (✓) *target: united*
  > Judg 20:11 So all the men of Israel gathered against the city , united as one man .

**Group `7566-002`** (3 verses — anchors: Isa 1:23)

- **Isa 1:23** 🔵 (✓) *target: companions*
  > Isa 1:23 Your princes are rebels and companions of thieves . Everyone loves a bribe and runs after gifts . They do not bring justice to the fatherless , and the widow’s cause does not come to them .
- **Pro 28:24** (✓) *target: companion*
  > Pro 28:24 Whoever robs his father or his mother and says , “That is no transgression ,” is a companion to a man who destroys .
- **Isa 44:11** (✓) *target: companions*
  > Isa 44:11 Behold , all his companions shall be put to shame , and the craftsmen are only human . Let them all assemble , let them stand forth . They shall be terrified ; they shall be put to shame together .

**Group `7566-003`** (1 verse — anchors: Ecc 4:10)

- **Ecc 4:10** 🔵 (✓) *target: fellow*
  > Ecc 4:10 For if they fall , one will lift up his fellow . But woe to him who is alone when he falls and has not another to lift him up!

**Group `7566-004`** (1 verse — anchors: Eze 37:19)

- **Eze 37:19** 🔵 (✓) *target: associated*
  > Eze 37:19 say to them, Thus says the Lord God : Behold , I am about to take the stick of Joseph ( that is in the hand of Ephraim ) and the tribes of Israel associated with him. And I will join with it the stick of Judah , and make them one stick , that they may be one in my hand .

**Group `SET-ASIDE`** (4 verses)

- **Psa 45:7** (✗) [set_aside: wrong_face] *target: companions*
  > Psa 45:7 you have loved righteousness and hated wickedness . Therefore God , your God , has anointed you with the oil of gladness beyond your companions ;
- **Song 1:7** (✗) [set_aside: wrong_face] *target: companions*
  > Song 1:7 Tell me, you whom my soul loves , where you pasture your flock , where you make it lie down at noon ; for why should I be like one who veils herself beside the flocks of your companions ?
- **Song 8:13** (✗) [set_aside: wrong_face] *target: companions*
  > Song 8:13 O you who dwell in the gardens , with companions listening for your voice ; let me hear it .
- **Eze 37:16** (✗) [set_aside: no_inner_being] *target: with him*
  > Eze 37:16 “ Son of man , take a stick and write on it, ‘ For Judah , and the people of Israel associated with him ’; then take another stick and write on it, ‘ For Joseph (the stick of Ephraim ) and all the house of Israel associated with him .’

### `H2271` — 1/1 classified · 0 anchor verse(s)

**Group `SET-ASIDE`** (1 verse)

- **Job 41:6** (✗) [set_aside: no_inner_being] *target: traders*
  > Job 41:6 Will traders bargain over him? Will they divide him up among the merchants ?

### `H2272` — 1/1 classified · 1 anchor verse(s)

**Group `7573-001`** (1 verse — anchors: Jer 13:23)

- **Jer 13:23** 🔵 (✓) *target: spots*
  > Jer 13:23 Can the Ethiopian change his skin or the leopard his spots ? Then also you can do good who are accustomed to do evil .

### `H2274` — 1/1 classified · 1 anchor verse(s)

**Group `7574-001`** (1 verse — anchors: Job 34:8)

- **Job 34:8** 🔵 (✓) *target: company*
  > Job 34:8 who travels in company with evildoers and walks with wicked men ?

### `H2278` — 1/1 classified · 1 anchor verse(s)

**Group `7576-001`** (1 verse — anchors: Mal 2:14)

- **Mal 2:14** 🔵 (✓) *target: is your companion*
  > Mal 2:14 But you say , “ Why does he not?” Because the Lord was witness between you and the wife of your youth , to whom you have been faithless , though she is your companion and your wife by covenant .

### `H2279` — 3/3 classified · 0 anchor verse(s)

**Group `SET-ASIDE`** (3 verses)

- **Exo 26:4** (✗) [set_aside: physical_only] *target: set*
  > Exo 26:4 And you shall make loops of blue on the edge of the outermost curtain in the first set . Likewise you shall make loops on the edge of the outermost curtain in the second set .
- **Exo 26:10** (✗) [set_aside: physical_only] *target: set*
  > Exo 26:10 You shall make fifty loops on the edge of the curtain that is outermost in one set , and fifty loops on the edge of the curtain that is outermost in the second set .
- **Exo 36:17** (✗) [set_aside: physical_only] *target: connecting*
  > Exo 36:17 And he made fifty loops on the edge of the outermost curtain of the one set , and fifty loops on the edge of the other connecting curtain .

### `H4225` — 7/7 classified · 0 anchor verse(s)

**Group `SET-ASIDE`** (7 verses)

- **Exo 26:4** (✗) [set_aside: physical_only] *target: set*
  > Exo 26:4 And you shall make loops of blue on the edge of the outermost curtain in the first set . Likewise you shall make loops on the edge of the outermost curtain in the second set .
- **Exo 26:5** (✗) [set_aside: physical_only] *target: set*
  > Exo 26:5 Fifty loops you shall make on the one curtain , and fifty loops you shall make on the edge of the curtain that is in the second set ; the loops shall be opposite one another .
- **Exo 28:27** (✗) [set_aside: physical_only] *target: seam*
  > Exo 28:27 And you shall make two rings of gold , and attach them in front to the lower part of the two shoulder pieces of the ephod , at its seam above the skillfully woven band of the ephod .
- **Exo 36:11** (✗) [set_aside: physical_only] *target: set*
  > Exo 36:11 He made loops of blue on the edge of the outermost curtain of the first set . Likewise he made them on the edge of the outermost curtain of the second set .
- **Exo 36:12** (✗) [set_aside: physical_only] *target: set*
  > Exo 36:12 He made fifty loops on the one curtain , and he made fifty loops on the edge of the curtain that was in the second set . The loops were opposite one another .
- **Exo 36:17** (✗) [set_aside: physical_only] *target: set*
  > Exo 36:17 And he made fifty loops on the edge of the outermost curtain of the one set , and fifty loops on the edge of the other connecting curtain .
- **Exo 39:20** (✗) [set_aside: physical_only] *target: seam*
  > Exo 39:20 And they made two rings of gold , and attached them in front to the lower part of the two shoulder pieces of the ephod , at its seam above the skillfully woven band of the ephod .

### `H4226` — 2/2 classified · 0 anchor verse(s)

**Group `SET-ASIDE`** (2 verses)

- **1Ch 22:3** (✗) [set_aside: physical_only] *target: clamps*
  > 1Ch 22:3 David also provided great quantities of iron for nails for the doors of the gates and for clamps , as well as bronze in quantities beyond weighing ,
- **2Ch 34:11** (✗) [set_aside: physical_only] *target: binders*
  > 2Ch 34:11 They gave it to the carpenters and the builders to buy quarried stone , and timber for binders and beams for the buildings that the kings of Judah had let go to ruin .

### `G2842` — 14/17 classified · 3 anchor verse(s)

**Group `873-001`** (8 verses — anchors: Phili 3:10, 1Jo 1:3)

- **Phili 3:10** 🔵 (✓) *target: share*
  > Phili 3:10 that I may know him and the power of his resurrection , and may share his sufferings , becoming like him in his death ,
- **1Jo 1:3** 🔵 (✓) *target: fellowship*
  > 1Jo 1:3 that which we have seen and heard we proclaim also to you , so that you too may have fellowship with us ; and indeed our fellowship is with the Father and with his Son Jesus Christ .
- **1Cor 1:9** (✓) *target: fellowship*
  > 1Cor 1:9 God is faithful , by whom you were called into the fellowship of his Son , Jesus Christ our Lord .
- **1Cor 10:16** (✓) *target: participation in*
  > 1Cor 10:16 The cup of blessing that we bless , is it not a participation in the blood of Christ ? The bread that we break , is it not a participation in the body of Christ ?
- **2Cor 13:14** (✓) *target: fellowship*
  > 2Cor 13:14 The grace of the Lord Jesus Christ and the love of God and the fellowship of the Holy Spirit be with you all .
- **Phili 2:1** (✓) *target: participation*
  > Phili 2:1 So if there is any encouragement in Christ , any comfort from love , any participation in the Spirit , any affection and sympathy ,
- **1Jo 1:6** (✓) *target: fellowship*
  > 1Jo 1:6 If we say we have fellowship with him while we walk in darkness , we lie and do not practice the truth .
- **1Jo 1:7** (✓) *target: fellowship*
  > 1Jo 1:7 But if we walk in the light , as he is in the light , we have fellowship with one another , and the blood of Jesus his Son cleanses us from all sin .

**Group `873-002`** (6 verses — anchors: 2Cor 6:14)

- **2Cor 6:14** 🔵 (✓) *target: fellowship*
  > 2Cor 6:14 Do not be unequally yoked with unbelievers . For what partnership has righteousness with lawlessness ? Or what fellowship has light with darkness ?
- **Act 2:42** (✓) *target: fellowship*
  > Act 2:42 And they devoted themselves to the apostles ’ teaching and the fellowship , to the breaking of bread and the prayers .
- **2Cor 8:4** (✓) *target: taking part*
  > 2Cor 8:4 begging us earnestly for the favor of taking part in the relief of the saints —
- **Gal 2:9** (✓) *target: fellowship*
  > Gal 2:9 and when James and Cephas and John , who seemed to be pillars , perceived the grace that was given to me , they gave the right hand of fellowship to Barnabas and me , that we should go to the Gentiles and they to the circumcised .
- **Phili 1:5** (✓) *target: partnership*
  > Phili 1:5 because of your partnership in the gospel from the first day until now .
- **Phile 6** (✓) *target: sharing*
  > Phile 6 and I pray that the sharing of your faith may become effective for the full knowledge of every good thing that is in us for the sake of Christ .

**Group `UNCLASSIFIED`** (3 verses)

- **Rom 15:26** (—) *target: contribution*
  > Rom 15:26 For Macedonia and Achaia have been pleased to make some contribution for the poor among the saints at Jerusalem .
- **2Cor 9:13** (—) *target: contribution*
  > 2Cor 9:13 By their approval of this service , they will glorify God because of your submission that comes from your confession of the gospel of Christ , and the generosity of your contribution for them and for all others,
- **Heb 13:16** (—) *target: share*
  > Heb 13:16 Do not neglect to do good and to share what you have, for such sacrifices are pleasing to God .

### `G2844` — 8/10 classified · 2 anchor verse(s)

**Group `5367-001`** (5 verses — anchors: 2Pe 1:4)

- **2Pe 1:4** 🔵 (✓) *target: partakers*
  > 2Pe 1:4 by which he has granted to us his precious and very great promises , so that through them you may become partakers of the divine nature , having escaped from the corruption that is in the world because of sinful desire .
- **1Cor 10:18** (✓) *target: participants*
  > 1Cor 10:18 Consider the people of Israel : are not those who eat the sacrifices participants in the altar ?
- **1Cor 10:20** (✓) *target: participants*
  > 1Cor 10:20 No , I imply that what pagans sacrifice they offer to demons and not to God . I do not want you to be participants with demons .
- **2Cor 1:7** (✓) *target: share*
  > 2Cor 1:7 Our hope for you is unshaken , for we know that as you share in our sufferings , you will also share in our comfort .
- **1Pe 5:1** (✓) *target: partaker*
  > 1Pe 5:1 So I exhort the elders among you , as a fellow elder and a witness of the sufferings of Christ , as well as a partaker in the glory that is going to be revealed :

**Group `5367-002`** (3 verses — anchors: Mat 23:30)

- **Mat 23:30** 🔵 (✓) *target: taken part*
  > Mat 23:30 saying , ‘ If we had lived in the days of our fathers , we would not have taken part with them in shedding the blood of the prophets .’
- **Phile 17** (✓) *target: partner*
  > Phile 17 So if you consider me your partner , receive him as you would receive me .
- **Heb 10:33** (✓) *target: partners*
  > Heb 10:33 sometimes being publicly exposed to reproach and affliction , and sometimes being partners with those so treated .

**Group `UNCLASSIFIED`** (2 verses)

- **Luk 5:10** (—) *target: partners*
  > Luk 5:10 and so also were James and John , sons of Zebedee , who were partners with Simon . And Jesus said to Simon , “Do not be afraid ; from now on you will be catching men .”
- **2Cor 8:23** (—) *target: partner*
  > 2Cor 8:23 As for Titus , he is my partner and fellow worker for your benefit. And as for our brothers , they are messengers of the churches , the glory of Christ .

---

## K. Legacy-VC Terms — UNVERIFIED UNDER v3 CONTRACTS

**13 term(s)** in this registry carry classification rows from pre-v3 work.

> **Analytical instruction (per vc-corrective-strategy v2 §4):** these classifications are facts on the ground. The VC programme has not re-classified them under v3 contracts. If a finding depends *materially* on a verse classification, group description, or anchor designation from this section, emit an `ANALYSIS_VC_UNVERIFIED_MATERIAL` flag specifying the source term(s), verses, the alternative scenario, and the predicted change to the finding.

| strongs | gloss | vc_status | verses | groups | vc_rows |
|---|---|---|---:|---:|---:|
| `H2250` | wound | `to_revise` | 6 | 2 | 6 |
| `H2266` | to unite | `to_revise` | 25 | 4 | 25 |
| `H2267` | spell | `to_revise` | 4 | 2 | 4 |
| `H2270` | companion | `to_revise` | 11 | 4 | 11 |
| `H2271` | associate | `to_revise` | 1 | 0 | 1 |
| `H2272` | spot | `to_revise` | 1 | 1 | 1 |
| `H2274` | company | `to_revise` | 1 | 1 | 1 |
| `H2278` | consort | `to_revise` | 1 | 1 | 1 |
| `H2279` | set | `to_revise` | 3 | 0 | 3 |
| `H4225` | joining | `to_revise` | 7 | 0 | 7 |
| `H4226` | clamp | `to_revise` | 2 | 0 | 2 |
| `G2842` | participation | `to_revise` | 17 | 2 | 14 |
| `G2844` | participant | `to_revise` | 10 | 2 | 8 |

---

## L. Stage 2b Foundational Input — Observation Question Catalogue

**Generic questions: 158** across 11 sections. The section grouping IS the Stage 2b chapter structure — Stage 2b works through the catalogue section-by-section, producing answers grouped by section.

### Section summary (generic)

| Section | n questions |
|---|---:|
| Section 1 — Generic (gap addition R067 obslog v3) | 3 |
| Section 1 — Generic (gap addition R067) | 2 |
| Section 1 — Word Characteristic Summary | 20 |
| Section 2 — Generic (gap addition R067) | 2 |
| Section 2 — Word Impact Description | 21 |
| Section 3 — Annotated Verse Evidence | 44 |
| Section 3 — Generic (gap addition R067) | 2 |
| Section 4 — Generic (gap addition R067) | 1 |
| Section 4 — Original Language Vocabulary | 36 |
| Section 5 — Connections and Research Pointers | 26 |
| Section 5 — Generic (gap addition R067) | 1 |

### Generic questions (JSON, grouped by section)

Format: JSON. Structure: as-is from `wa_obs_question_catalogue`. Apply to every word.

```json
{
  "total": 158,
  "section_count": 11,
  "sections": {
    "Section 1 — Generic (gap addition R067 obslog v3)": [
      {
        "obs_id": 221,
        "question_code": "GAP-N-001",
        "section": "Section 1 — Generic (gap addition R067 obslog v3)",
        "source_word": "goodness",
        "source_registry_no": 67,
        "question_text": "For registries where verse context groups carry affective inner-being states (gladness, well-being, shalom-condition) that do not fit Moral Character, Cognition, or Volition, what dimension should be assigned? The current 10-dimension vocabulary may require an Experiential/Affective category for these groups.",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 222,
        "question_code": "GAP-N-002",
        "section": "Section 1 — Generic (gap addition R067 obslog v3)",
        "source_word": "goodness",
        "source_registry_no": 67,
        "question_text": "For verse context groups that name inner affective well-being states (glad of heart, shalom-condition, prospering inwardly) that are not primarily moral assessments, cognitive evaluations, or volitional acts, should the dimension be Emotion — Positive or Vitality / Existence? The two dimensions need clearer boundary criteria for these borderline cases.",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 223,
        "question_code": "GAP-N-003",
        "section": "Section 1 — Generic (gap addition R067 obslog v3)",
        "source_word": "goodness",
        "source_registry_no": 67,
        "question_text": "For verse context groups where God's inner-being engagement is a creative-constitutive evaluative act (declaring creation good, establishing ontological goodness) rather than a relational disposition toward humanity, should Dimension 11 (Divine-Human Correspondence) apply, or should the dimension review introduce a distinct label for this ontological-creative register?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      }
    ],
    "Section 1 — Generic (gap addition R067)": [
      {
        "obs_id": 207,
        "question_code": "GAP-S1-001",
        "section": "Section 1 — Generic (gap addition R067)",
        "source_word": "goodness",
        "source_registry_no": 67,
        "question_text": "Where the word has multiple distinct semantic modes, does the verse evidence reveal a unified inner logic that holds the modes together — or are they genuinely independent phenomena?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 208,
        "question_code": "GAP-S1-002",
        "section": "Section 1 — Generic (gap addition R067)",
        "source_word": "goodness",
        "source_registry_no": 67,
        "question_text": "Does the word carry a structural negative or absence form — and if so, does the negative form engage the same inner-being faculty as the positive?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      }
    ],
    "Section 1 — Word Characteristic Summary": [
      {
        "obs_id": 1,
        "question_code": "Q001",
        "section": "Section 1 — Word Characteristic Summary",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What is the structural disposition of the word — where does it originate?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 2,
        "question_code": "Q002",
        "section": "Section 1 — Word Characteristic Summary",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What determines whether the word is extended or withheld?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 3,
        "question_code": "Q003",
        "section": "Section 1 — Word Characteristic Summary",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What are the distinct modes of operation of the word in the inner being?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 4,
        "question_code": "Q004",
        "section": "Section 1 — Word Characteristic Summary",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What does the word produce in the inner being of the recipient?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 5,
        "question_code": "Q005",
        "section": "Section 1 — Word Characteristic Summary",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What does the word produce in the relational position of the recipient toward another?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 6,
        "question_code": "Q006",
        "section": "Section 1 — Word Characteristic Summary",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What does the word reveal about the disposition of God toward the human being?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 7,
        "question_code": "Q007",
        "section": "Section 1 — Word Characteristic Summary",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What does the word reveal about the basis on which God's disposition toward a person is established?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 8,
        "question_code": "Q008",
        "section": "Section 1 — Word Characteristic Summary",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "Where, somatically or relationally, does the word locate the reality of its operation in the giver and in the recipient?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 9,
        "question_code": "Q009",
        "section": "Section 1 — Word Characteristic Summary",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "Does the word describe a one-time act or an ongoing condition — and how are these distinguished?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 10,
        "question_code": "Q010",
        "section": "Section 1 — Word Characteristic Summary",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What spatial or directional language is used to describe the ongoing condition the word produces?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 11,
        "question_code": "Q011",
        "section": "Section 1 — Word Characteristic Summary",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "Does the word produce enabling capacity in the inner being — and if so, what kind?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 12,
        "question_code": "Q012",
        "section": "Section 1 — Word Characteristic Summary",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What character quality does the word produce in the inner being?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 13,
        "question_code": "Q013",
        "section": "Section 1 — Word Characteristic Summary",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "How does the word express itself in relation to others?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 14,
        "question_code": "Q014",
        "section": "Section 1 — Word Characteristic Summary",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What inner condition or orientation is identified as the ground of genuine expression of the word?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 15,
        "question_code": "Q015",
        "section": "Section 1 — Word Characteristic Summary",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "Is there a discernible sequence or movement in the way the word operates through the inner person?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 16,
        "question_code": "Q016",
        "section": "Section 1 — Word Characteristic Summary",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What direction of movement does the word follow within and through the inner person?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 17,
        "question_code": "Q017",
        "section": "Section 1 — Word Characteristic Summary",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What does the word identify as its originating source?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 18,
        "question_code": "Q018",
        "section": "Section 1 — Word Characteristic Summary",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What does the word reveal about the origin of the human capacity to seek it?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 19,
        "question_code": "Q019",
        "section": "Section 1 — Word Characteristic Summary",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "Does the word share an etymological root with another inner-being characteristic — and if so, what is that characteristic?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 20,
        "question_code": "Q020",
        "section": "Section 1 — Word Characteristic Summary",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What does the word produce as a natural inner response in the one who receives it?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      }
    ],
    "Section 2 — Generic (gap addition R067)": [
      {
        "obs_id": 209,
        "question_code": "GAP-S2-001",
        "section": "Section 2 — Generic (gap addition R067)",
        "source_word": "goodness",
        "source_registry_no": 67,
        "question_text": "Where the word has both a positive (presence) and negative (absence/not-word) register, what does the negative register reveal about the inner-being mechanisms of the positive?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 210,
        "question_code": "GAP-S2-002",
        "section": "Section 2 — Generic (gap addition R067)",
        "source_word": "goodness",
        "source_registry_no": 67,
        "question_text": "Does the verse evidence distinguish between the inner quality of goodness and the external assessment of conduct as good — and what is the relationship between them?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      }
    ],
    "Section 2 — Word Impact Description": [
      {
        "obs_id": 21,
        "question_code": "Q021",
        "section": "Section 2 — Word Impact Description",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What inner-being logic or orientation functions as the structural opposite of the word?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 22,
        "question_code": "Q022",
        "section": "Section 2 — Word Impact Description",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What effect does the logic of merit have on the inner being's capacity to receive the word?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 23,
        "question_code": "Q023",
        "section": "Section 2 — Word Impact Description",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What effect does the logic of merit have on the inner being's capacity to extend the word to others?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 24,
        "question_code": "Q024",
        "section": "Section 2 — Word Impact Description",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What is the inner-being condition of the person who has received the word but failed to recognise it?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 25,
        "question_code": "Q025",
        "section": "Section 2 — Word Impact Description",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What inner-being experience cultivates the capacity to extend the word to others?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 26,
        "question_code": "Q026",
        "section": "Section 2 — Word Impact Description",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What inner-being posture does the act of earnest appeal express?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 27,
        "question_code": "Q027",
        "section": "Section 2 — Word Impact Description",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What somatic forms does the inner act of seeking the word take?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 28,
        "question_code": "Q028",
        "section": "Section 2 — Word Impact Description",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What inner-being orientation closes off the reception of the word?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 29,
        "question_code": "Q029",
        "section": "Section 2 — Word Impact Description",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What relational orientation toward others diminishes the operation of the word?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 30,
        "question_code": "Q030",
        "section": "Section 2 — Word Impact Description",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What is the relationship between the word and conditions of weakness in the inner being?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 31,
        "question_code": "Q031",
        "section": "Section 2 — Word Impact Description",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What kind of inner-being transformation does the word produce — does it change the condition or the person's orientation to the condition?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 32,
        "question_code": "Q032",
        "section": "Section 2 — Word Impact Description",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What is the first inner-being response to receiving the word unexpectedly?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 33,
        "question_code": "Q033",
        "section": "Section 2 — Word Impact Description",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What is the sequence of inner-being states as the word takes hold in the person?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 34,
        "question_code": "Q034",
        "section": "Section 2 — Word Impact Description",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "In the eschatological context, what is the first inner-being response to the full outpouring of the word?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 35,
        "question_code": "Q035",
        "section": "Section 2 — Word Impact Description",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What is the relationship between mourning and the full reception of the word in the inner being?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 36,
        "question_code": "Q036",
        "section": "Section 2 — Word Impact Description",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What quality of inner-being stability does the word produce?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 37,
        "question_code": "Q037",
        "section": "Section 2 — Word Impact Description",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What orientation does the stability produced by the word carry?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 38,
        "question_code": "Q038",
        "section": "Section 2 — Word Impact Description",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What capacity toward others does the word produce in the inner being of the one who has received it?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 39,
        "question_code": "Q039",
        "section": "Section 2 — Word Impact Description",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What is the inner-being source of the capacity to extend the word to others — is it discipline or transformation?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 40,
        "question_code": "Q040",
        "section": "Section 2 — Word Impact Description",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "How does the word relate to genuine human effort — does it displace it, supplement it, or reconstitute it?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 41,
        "question_code": "Q041",
        "section": "Section 2 — Word Impact Description",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What does the word reveal about the inner-being condition of the person who does not receive it?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      }
    ],
    "Section 3 — Annotated Verse Evidence": [
      {
        "obs_id": 42,
        "question_code": "Q042",
        "section": "Section 3 — Annotated Verse Evidence",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What does the word's primary verse reveal about its essential character?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 43,
        "question_code": "Q043",
        "section": "Section 3 — Annotated Verse Evidence",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What does the primary verse identify as the relationship between the human version and the divine version of the word?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 44,
        "question_code": "Q044",
        "section": "Section 3 — Annotated Verse Evidence",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What does the primary verse identify as the primary subject of the word — who exercises it?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 45,
        "question_code": "Q045",
        "section": "Section 3 — Annotated Verse Evidence",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "Does the primary verse name more than one function or dimension of the word — and if so, what is the relationship between them?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 46,
        "question_code": "Q046",
        "section": "Section 3 — Annotated Verse Evidence",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What does the primary verse reveal about the breadth of those toward whom the word operates?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 47,
        "question_code": "Q047",
        "section": "Section 3 — Annotated Verse Evidence",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What does the verse evidence reveal about the direction of the word's operation?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 48,
        "question_code": "Q048",
        "section": "Section 3 — Annotated Verse Evidence",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What does the verse evidence reveal about the word's relationship to suffering or affliction?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 49,
        "question_code": "Q049",
        "section": "Section 3 — Annotated Verse Evidence",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What does the verse evidence reveal about the word's relationship to moral failure or guilt?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 50,
        "question_code": "Q050",
        "section": "Section 3 — Annotated Verse Evidence",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What does the verse evidence reveal about the word's relationship to covenantal relationship?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 51,
        "question_code": "Q051",
        "section": "Section 3 — Annotated Verse Evidence",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What reason does a key verse give for the extension of the word — in the recipient's actions, or in the character of the one who gives it?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 52,
        "question_code": "Q052",
        "section": "Section 3 — Annotated Verse Evidence",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "Where does a key verse locate the reality of the word — in a specific faculty, organ, or location of the giver?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 53,
        "question_code": "Q053",
        "section": "Section 3 — Annotated Verse Evidence",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What practical outcome does a key verse show the word producing for the recipient?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 54,
        "question_code": "Q054",
        "section": "Section 3 — Annotated Verse Evidence",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What inner state does a key verse identify as the first response to receiving the word?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 55,
        "question_code": "Q055",
        "section": "Section 3 — Annotated Verse Evidence",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What comes first in a key verse — the establishment of the relationship or standing the word confers, or the commission or responsibility that follows from it?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 56,
        "question_code": "Q056",
        "section": "Section 3 — Annotated Verse Evidence",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What does a key verse identify as the concrete content of what the word gives?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 57,
        "question_code": "Q057",
        "section": "Section 3 — Annotated Verse Evidence",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What spatial or directional language does a key verse use for the reality of the word's operation?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 58,
        "question_code": "Q058",
        "section": "Section 3 — Annotated Verse Evidence",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "Does any verse distinguish between the means of entry into the word and the condition the word produces?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 59,
        "question_code": "Q059",
        "section": "Section 3 — Annotated Verse Evidence",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "Does any verse describe the present condition produced by the word as carrying a forward orientation?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 60,
        "question_code": "Q060",
        "section": "Section 3 — Annotated Verse Evidence",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What does a key verse identify as the ground of the speaker's or recipient's identity — achievement, reception, or something else?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 61,
        "question_code": "Q061",
        "section": "Section 3 — Annotated Verse Evidence",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "How does a key verse handle the co-presence of genuine human effort and prior divine initiative?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 62,
        "question_code": "Q062",
        "section": "Section 3 — Annotated Verse Evidence",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "In what form does a key verse present the word — and what does that form enable?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 63,
        "question_code": "Q063",
        "section": "Section 3 — Annotated Verse Evidence",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What effect does the word in communicative form produce in those who receive it?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 64,
        "question_code": "Q064",
        "section": "Section 3 — Annotated Verse Evidence",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "Does a key verse describe the word's work as directed toward the present only, or toward a future state?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 65,
        "question_code": "Q065",
        "section": "Section 3 — Annotated Verse Evidence",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "Does any verse distinguish between a performed version and a genuine version of the word?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 66,
        "question_code": "Q066",
        "section": "Section 3 — Annotated Verse Evidence",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What inner orientation does a key verse identify as the source of the genuine quality?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 67,
        "question_code": "Q067",
        "section": "Section 3 — Annotated Verse Evidence",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What is the sequence of somatic and verbal response in a key verse — which comes first?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 68,
        "question_code": "Q068",
        "section": "Section 3 — Annotated Verse Evidence",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What does a recipient's response in a key verse reveal about their inner experience of receiving the word?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 69,
        "question_code": "Q069",
        "section": "Section 3 — Annotated Verse Evidence",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What structural condition in a key verse establishes the recipient as having no basis for the word they receive?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 70,
        "question_code": "Q070",
        "section": "Section 3 — Annotated Verse Evidence",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "In a key verse, does the word operate within or across existing relational, covenantal, or social boundaries?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 71,
        "question_code": "Q071",
        "section": "Section 3 — Annotated Verse Evidence",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What is the logical structure of a key argument about the word — and what is its premise and conclusion?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 72,
        "question_code": "Q072",
        "section": "Section 3 — Annotated Verse Evidence",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What inner-being state does the argument structure in a key verse produce in the recipient?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 73,
        "question_code": "Q073",
        "section": "Section 3 — Annotated Verse Evidence",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What is the relationship between the divine act and the human act in a key verse — illustrative or causal?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 74,
        "question_code": "Q074",
        "section": "Section 3 — Annotated Verse Evidence",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "Where does a key verse locate the inner quality from which the word's outward act flows?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 75,
        "question_code": "Q075",
        "section": "Section 3 — Annotated Verse Evidence",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What does a verse about the withdrawal or absence of the word reveal about the word's role?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 76,
        "question_code": "Q076",
        "section": "Section 3 — Annotated Verse Evidence",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What does a verse about the word in extremity reveal about its depth of operation?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 77,
        "question_code": "Q077",
        "section": "Section 3 — Annotated Verse Evidence",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What does a verse about the word in the judicial or accountability context reveal about its function?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 78,
        "question_code": "Q078",
        "section": "Section 3 — Annotated Verse Evidence",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What does a verse about the word in the supplication context reveal about what the inner person knows about itself?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 79,
        "question_code": "Q079",
        "section": "Section 3 — Annotated Verse Evidence",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What does a verse about the word in the worship or liturgical context reveal about the word's function in ordered relationship with God?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 80,
        "question_code": "Q080",
        "section": "Section 3 — Annotated Verse Evidence",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What does a verse about the word at the level of covenantal promise reveal about its scope and duration?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 81,
        "question_code": "Q081",
        "section": "Section 3 — Annotated Verse Evidence",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What does a verse about the word in the context of moral collapse reveal about the word's place in the structure of the inner life?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 82,
        "question_code": "Q082",
        "section": "Section 3 — Annotated Verse Evidence",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What does a verse about the word in the context of formation or sanctification reveal about how the word shapes the person over time?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 83,
        "question_code": "Q083",
        "section": "Section 3 — Annotated Verse Evidence",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What does a verse about the word in the context of community or fellowship reveal about the word's social dimension?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 84,
        "question_code": "Q084",
        "section": "Section 3 — Annotated Verse Evidence",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What does a verse about the word in the context of eschatology or final things reveal about the word's ultimate trajectory?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 85,
        "question_code": "Q085",
        "section": "Section 3 — Annotated Verse Evidence",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What does a verse about the word's physical or somatic expression reveal about the inner-outer relationship in the word's operation?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      }
    ],
    "Section 3 — Generic (gap addition R067)": [
      {
        "obs_id": 211,
        "question_code": "GAP-S3-001",
        "section": "Section 3 — Generic (gap addition R067)",
        "source_word": "goodness",
        "source_registry_no": 67,
        "question_text": "Where a registry contains multiple anchor verses across multiple groups, is there a primary or controlling anchor — and how is it identified?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 212,
        "question_code": "GAP-S3-002",
        "section": "Section 3 — Generic (gap addition R067)",
        "source_word": "goodness",
        "source_registry_no": 67,
        "question_text": "Does the comparative or evaluative mode of the word (where the word functions as a ranking operator rather than naming a characteristic) constitute a distinct analytical case requiring separate treatment?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      }
    ],
    "Section 4 — Generic (gap addition R067)": [
      {
        "obs_id": 213,
        "question_code": "GAP-S4-001",
        "section": "Section 4 — Generic (gap addition R067)",
        "source_word": "goodness",
        "source_registry_no": 67,
        "question_text": "Where the programme has distributed a root family across multiple registries, what does that distribution reveal about the programme's analytical framework, and does the distribution reflect genuine semantic distinctions or is it a programme boundary decision requiring Session D review?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      }
    ],
    "Section 4 — Original Language Vocabulary": [
      {
        "obs_id": 86,
        "question_code": "Q086",
        "section": "Section 4 — Original Language Vocabulary",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What is the total number of terms in this registry, and how are they distributed between Hebrew and Greek?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 87,
        "question_code": "Q087",
        "section": "Section 4 — Original Language Vocabulary",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What is the sharing ratio — what proportion of terms are shared with adjacent word studies?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 88,
        "question_code": "Q088",
        "section": "Section 4 — Original Language Vocabulary",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What is the primary Hebrew term, and what does its root meaning reveal about the word's essential character?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 89,
        "question_code": "Q089",
        "section": "Section 4 — Original Language Vocabulary",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What is the primary Greek term, and what does its range of use reveal?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 90,
        "question_code": "Q090",
        "section": "Section 4 — Original Language Vocabulary",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "Does the vocabulary distinguish between the word as an inner disposition and the word as an outward act — and how?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 91,
        "question_code": "Q091",
        "section": "Section 4 — Original Language Vocabulary",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "Does the vocabulary include a term for the word as a settled character quality?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 92,
        "question_code": "Q092",
        "section": "Section 4 — Original Language Vocabulary",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "Does the vocabulary include a term for the one who habitually exercises the word — a person-type term?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 93,
        "question_code": "Q093",
        "section": "Section 4 — Original Language Vocabulary",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "Does the vocabulary include a term for the word's absence or structural opposite?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 94,
        "question_code": "Q094",
        "section": "Section 4 — Original Language Vocabulary",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What does the relationship between the root meaning and the primary sense reveal about the word's conceptual origin?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 95,
        "question_code": "Q095",
        "section": "Section 4 — Original Language Vocabulary",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "Does the vocabulary include terms that name the word as something received passively and terms that name it as something actively exercised?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 96,
        "question_code": "Q096",
        "section": "Section 4 — Original Language Vocabulary",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "Does any term in the vocabulary carry both the sense of the word in its human expression and its divine expression?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 97,
        "question_code": "Q097",
        "section": "Section 4 — Original Language Vocabulary",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What does the LXX use of the vocabulary reveal about the continuity or development of the word across the Testaments?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 98,
        "question_code": "Q098",
        "section": "Section 4 — Original Language Vocabulary",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "Is there a named failure-mode term in the vocabulary — a term for the person who has received the word but withholds it from others?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 99,
        "question_code": "Q099",
        "section": "Section 4 — Original Language Vocabulary",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "Does the vocabulary include a term newly coined in the NT period for this word — and if so, what does the coinage reveal?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 100,
        "question_code": "Q100",
        "section": "Section 4 — Original Language Vocabulary",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What does the verbal form of the primary term reveal about the word's mode of operation?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 101,
        "question_code": "Q101",
        "section": "Section 4 — Original Language Vocabulary",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "Does the vocabulary include a spatial or architectural term — a place or structure associated with the word?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 102,
        "question_code": "Q102",
        "section": "Section 4 — Original Language Vocabulary",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What does the semantic range of the primary term reveal about the breadth of the word's operation?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 103,
        "question_code": "Q103",
        "section": "Section 4 — Original Language Vocabulary",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "Does any term carry a somatic or physiological dimension — naming an inner organ or physical site as the word's location?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 104,
        "question_code": "Q104",
        "section": "Section 4 — Original Language Vocabulary",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What does the grammatical range of the primary term (noun, verb, adjective) reveal about how the word is conceptualised — as object, action, or quality?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 105,
        "question_code": "Q105",
        "section": "Section 4 — Original Language Vocabulary",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "Does the vocabulary include a supplication term — a term for the act of seeking the word from another?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 106,
        "question_code": "Q106",
        "section": "Section 4 — Original Language Vocabulary",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What does the supplication term reveal about the inner posture required to seek the word?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 107,
        "question_code": "Q107",
        "section": "Section 4 — Original Language Vocabulary",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "Does the vocabulary include a term for the mechanism by which the word is administered or conveyed?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 108,
        "question_code": "Q108",
        "section": "Section 4 — Original Language Vocabulary",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What does the atonement or propitiation vocabulary (if present) reveal about the structural conditions under which the word operates?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 109,
        "question_code": "Q109",
        "section": "Section 4 — Original Language Vocabulary",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "Does any term reveal a classical-to-NT directional reversal — a term whose direction of operation changes between its classical use and its NT use?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 110,
        "question_code": "Q110",
        "section": "Section 4 — Original Language Vocabulary",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What does the vocabulary reveal about whether the word operates primarily within or across relational boundaries?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 111,
        "question_code": "Q111",
        "section": "Section 4 — Original Language Vocabulary",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What does the vocabulary reveal about the word's relationship to covenant — is it bounded by covenant or can it extend beyond?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 112,
        "question_code": "Q112",
        "section": "Section 4 — Original Language Vocabulary",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "Does any term in the vocabulary name the word as a divine possession — something that belongs to God and is located with him?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 113,
        "question_code": "Q113",
        "section": "Section 4 — Original Language Vocabulary",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What does the root architecture of the vocabulary reveal about the word's conceptual relationship to adjacent characteristics?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 114,
        "question_code": "Q114",
        "section": "Section 4 — Original Language Vocabulary",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "Does the vocabulary include compound terms — and if so, what do the compounds reveal?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 115,
        "question_code": "Q115",
        "section": "Section 4 — Original Language Vocabulary",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What does the vocabulary reveal about the word's temporal character — is it punctiliar, durative, or both?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 116,
        "question_code": "Q116",
        "section": "Section 4 — Original Language Vocabulary",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "Does the vocabulary reveal whether the word operates as a judicial category, a relational one, or both?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 117,
        "question_code": "Q117",
        "section": "Section 4 — Original Language Vocabulary",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What does the most intensive or plural form of the vocabulary term reveal?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 118,
        "question_code": "Q118",
        "section": "Section 4 — Original Language Vocabulary",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "Does the vocabulary include terms that name the word's expression in speech?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 119,
        "question_code": "Q119",
        "section": "Section 4 — Original Language Vocabulary",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "Does the vocabulary include terms whose etymology connects to the body — and if so, to which part?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 120,
        "question_code": "Q120",
        "section": "Section 4 — Original Language Vocabulary",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What does the full vocabulary arc reveal about the word's complete semantic range — from its most intimate to its most structural expression?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 121,
        "question_code": "Q121",
        "section": "Section 4 — Original Language Vocabulary",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "Does the vocabulary include a term that names the word's operation at the intersection of the human and divine — a term that holds both simultaneously?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      }
    ],
    "Section 5 — Connections and Research Pointers": [
      {
        "obs_id": 122,
        "question_code": "Q122",
        "section": "Section 5 — Connections and Research Pointers",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What is the strongest co-occurrence connection for this word — which adjacent characteristic appears most frequently in the same verses — and what does the co-occurrence pattern reveal?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 123,
        "question_code": "Q123",
        "section": "Section 5 — Connections and Research Pointers",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "Does any verse indicate that this word and its most closely connected adjacent characteristic operate simultaneously in the same inner-being moment — and what would that simultaneity imply?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 124,
        "question_code": "Q124",
        "section": "Section 5 — Connections and Research Pointers",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What are the three highest vocabulary-sharing registries for this word — and what does the pattern of sharing reveal about the word's structural position in the programme?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 125,
        "question_code": "Q125",
        "section": "Section 5 — Connections and Research Pointers",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "Does the vocabulary overlap with any adjacent characteristic extend to root-level architecture — a shared root rather than only shared individual terms?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 126,
        "question_code": "Q126",
        "section": "Section 5 — Connections and Research Pointers",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "How many of this word's confirmed analytical dimensions are shared with another cluster or characteristic — and is there any cluster that shares all confirmed dimensions?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 127,
        "question_code": "Q127",
        "section": "Section 5 — Connections and Research Pointers",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "Does any single verse make an explicit structural relationship between this word and an adjacent characteristic — naming the connection rather than merely exemplifying it?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 128,
        "question_code": "Q128",
        "section": "Section 5 — Connections and Research Pointers",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What is the co-occurrence count between this word and the characteristic with which it shares the most anchor verses — and what does that shared anchoring reveal?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 129,
        "question_code": "Q129",
        "section": "Section 5 — Connections and Research Pointers",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "Where this word and an adjacent characteristic share a dominant directionality (such as both being primarily divine-to-human), what does the shared directionality reveal about their structural relationship?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 130,
        "question_code": "Q130",
        "section": "Section 5 — Connections and Research Pointers",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What is the relationship between this word and human will in the verse evidence — does the word displace, bypass, or reconstitute the will?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 131,
        "question_code": "Q131",
        "section": "Section 5 — Connections and Research Pointers",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "How does the study describe the relationship between this word and calling — is calling a consequence, an expression, or a distinct phenomenon?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 132,
        "question_code": "Q132",
        "section": "Section 5 — Connections and Research Pointers",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What inner-being posture connects this word and listening — and is that posture described as a precondition or an expression of the word?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 133,
        "question_code": "Q133",
        "section": "Section 5 — Connections and Research Pointers",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "How does the study distinguish this word from faith — and what is their structural relationship?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 134,
        "question_code": "Q134",
        "section": "Section 5 — Connections and Research Pointers",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What is the described sequence from the word to peace — and what comes between them?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 135,
        "question_code": "Q135",
        "section": "Section 5 — Connections and Research Pointers",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What is the vocabulary overlap and co-occurrence count between this word and guilt?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 136,
        "question_code": "Q136",
        "section": "Section 5 — Connections and Research Pointers",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What is the relationship between this word and mourning — does mourning precede, follow, or accompany the word?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 137,
        "question_code": "Q137",
        "section": "Section 5 — Connections and Research Pointers",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "Does the study present this word and hope as two separate phenomena or as aspects of a single inner-being posture?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 138,
        "question_code": "Q138",
        "section": "Section 5 — Connections and Research Pointers",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "Does any verse function as a primary anchor in both this word's study and another word's study — and what does that dual membership reveal about their relationship?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 139,
        "question_code": "Q139",
        "section": "Section 5 — Connections and Research Pointers",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "Does any verse anchor both this word and another word — and what shared inner-being posture does that dual anchoring reveal?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 140,
        "question_code": "Q140",
        "section": "Section 5 — Connections and Research Pointers",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "Does any verse present adjacent qualities as aspects of a unified inner-being posture — and if so, what is their common source?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 141,
        "question_code": "Q141",
        "section": "Section 5 — Connections and Research Pointers",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What functional overlap does the verse evidence suggest between this word and wisdom?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 142,
        "question_code": "Q142",
        "section": "Section 5 — Connections and Research Pointers",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "Does the word operate only in relation to moral conditions (guilt) or also in relation to conditions of incapacity — and what is the evidence?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 143,
        "question_code": "Q143",
        "section": "Section 5 — Connections and Research Pointers",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What is the co-occurrence count between this word and goodness — and in what literary context does the pairing appear?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 144,
        "question_code": "Q144",
        "section": "Section 5 — Connections and Research Pointers",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "What is the co-occurrence count between this word and anointing, and between this word and blessing?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 145,
        "question_code": "Q145",
        "section": "Section 5 — Connections and Research Pointers",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "Is the connection between this word and forgiveness established through contextual inference or through the lexical form of the term itself?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 146,
        "question_code": "Q146",
        "section": "Section 5 — Connections and Research Pointers",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "Does the verse evidence in this study point toward a connection with repentance — and is that connection sufficiently examined or deferred?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      },
      {
        "obs_id": 147,
        "question_code": "Q147",
        "section": "Section 5 — Connections and Research Pointers",
        "source_word": "Grace",
        "source_registry_no": 68,
        "question_text": "Does a recurring posture appear across the word-seeking scenes in the study — and is its relationship to an adjacent characteristic examined or deferred?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      }
    ],
    "Section 5 — Generic (gap addition R067)": [
      {
        "obs_id": 214,
        "question_code": "GAP-S5-001",
        "section": "Section 5 — Generic (gap addition R067)",
        "source_word": "goodness",
        "source_registry_no": 67,
        "question_text": "Where a registry's word functions in more than one dimension (both as a character attribute and as a comparative/evaluative operator), does the co-occurrence and correlation data reveal different connection patterns for different modes of the word?",
        "pattern_type": null,
        "scope": "universal",
        "status": "active"
      }
    ]
  }
}
```

### Registry-specific questions for 062 fellowship

_None._ No questions in `wa_obs_question_catalogue` are sourced from registry 62 (fellowship).

---

## N. Open Session B Items — must resolve this session

**No open items.** This is either a first analytical session for the registry, or all prior open items have been resolved.

---

## M. Readiness Verification

- **Generated at:** `2026-04-28T06:24:53Z`
- **Schema version:** `3.17.0`
- **OWNER term md_versions present:** `[1]`

**Stage 1 quick checks:**

- Registry status fields populated: ✓
- OWNER term inventory non-empty: ✓
- All OWNER terms have at least 1 verse: ✓
- Researcher fields preserved: absent — researcher narrative not yet written

**Notes / concerns:**
- session_b_status='Verse Context Reset' — investigate whether this is current or stale post-VCB-13.

---

*End of readiness output v3 — wa-062-fellowship.*