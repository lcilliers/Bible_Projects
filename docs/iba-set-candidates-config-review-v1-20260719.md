# Set-Candidates module — config rules review (v1, 2026-07-19)

> Source of truth: live `iba/app/db/iba.db` (the `cfg_*` config store), queried 2026-07-19.
> The CSV exports in `iba/app/config/` are dated 2026-07-18 and are **stale** — they still show only the `new-word` work package. The DB below is current.
>
> Module in focus: [`iba/app/ps/Set-Candidates.ps1`](../iba/app/ps/Set-Candidates.ps1). It is a thin, config-driven runner — it hardcodes nothing about the steps; it reads the sequence from `cfg_step` and runs each via `python -m iba.app.run set-candidates --step <step>`.

---

## 1. What the module is (from config)

**`cfg_work_package`**

| name | ps_script | runs_over |
|---|---|---|
| set-candidates | iba/app/ps/Set-Candidates.ps1 | **book** |

**`cfg_step`** — the two steps, in order:

| ord | step | handler | scope | does |
|---|---|---|---|---|
| 0 | `candidate.seed` | `iba.app.handlers.candidate:seed` | **global** | refresh `candidate_seed` over `lemma_inventory` (independent net + registry-direct + config); recompute `registry_match` (the double control) |
| 1 | `candidate.set` | `iba.app.handlers.candidate:set` | **book** | stamp `span_candidate` on the book's spans whose base-strong is a candidate |

Note the scopes: `candidate.seed` is **global** (re-assesses the whole lemma inventory every run, book-independent); `candidate.set` is **book** (only stamps the given book's spans).

---

## 2. Failure rules — `cfg_on_fail`

| step | condition | path | message |
|---|---|---|---|
| `candidate.seed` | no-inventory | **report-stop** | lemma_inventory is empty — run the seed migration first |
| `candidate.set` | no-spans | **report-stop** | the book has no spans — build its words first |

(Downstream, `passage.build`/no-candidates → report-stop "run set-candidates first" — that's the Build-Passages package, shown for context.)

`on_fail` enum: `report-continue` · `pause-continue` · `report-stop` · `self-heal`.

---

## 3. Write permissions — `cfg_write_grant`

The only tables each writer is allowed to touch:

| writer | table_name |
|---|---|
| `candidate.seed` | `lemma_inventory` |
| `candidate.seed` | `candidate_seed` |
| `candidate.set` | `span_candidate` |
| `migration` | `lemma_inventory` |
| `migration` | `candidate_seed` |
| `migration` | `word_strong` |

So `candidate.seed` may write the seed assessment and (re)touch the inventory; `candidate.set` may write **only** the span stamp. The one-time `import_seed` migration populates `lemma_inventory` + `candidate_seed` + `word_strong`.

---

## 4. Settings the module reads — `cfg_setting`

Only one setting is candidate-specific:

| key | value | use |
|---|---|---|
| `candidate.lemma_base_pattern` | `^([HG]\d+)([A-Z]?)$` | capture group 1 = base Strong's (sub-letters stripped) = the lemma key. **The seed and the stamp both key on this.** |

Adjacent settings that shape what is *eligible* to be a candidate (used at discovery, carried through):

| key | value | use |
|---|---|---|
| `discovery.particle_pattern` | `^[HG]9\d{3}$` | grammar-particle codes; excluded from discovery, flagged on a span |
| `discovery.follow_related` | false | relatedNos is root-family noise; not followed |
| `language.greek_prefix` | `G` | a strong starting `G` is Greek, else Hebrew |

---

## 5. Enums the module uses — `cfg_enum`

| enum | values |
|---|---|
| `candidate_decision` | candidate · rejected · undecided |
| `candidate_source` | registry-direct · curated-synonym · ib-judgement · read-emergent |

`candidate_seed.decision` is constrained to `candidate_decision`. The four `candidate_source` values name the intended seeding layers — see the gap in §7.

---

## 6. The tables it writes — grain + columns (`cfg_table` / `cfg_column`)

### `lemma_inventory` — the independent substrate
Grain: *one row per corpus lemma (base Strong's) — the INDEPENDENT substrate the seed net runs over.*
Use: imported from the old study, **NOT derived from the registry**, so the seed is a real completeness control.

| column | use | source / filled_by |
|---|---|---|
| lemma_key (pk-ish) | base Strong's, sub-letters stripped | import:lemma-inventory |
| gloss | English gloss — **the meaning the net matches on** | import:lemma-inventory |
| language | Hebrew/Greek | derived:lemma_key |
| source / created_at / deleted | provenance / soft-delete | migration |

### `candidate_seed` — the over-inclusive Axis-A assessment
Grain: *one row per assessed lemma.* Use: L4b seed decision (potential, not definite); the lexical stage is the real test. `registry_match` NULL on a candidate = a candidate **missing** a registry word (the double control).

| column | use | filled_by |
|---|---|---|
| lemma_key | the assessed lemma | — |
| decision | candidate \| rejected \| undecided | candidate.seed |
| layer | which layer decided it | candidate.seed |
| registry_match | registry word covering this lemma, or NULL | candidate.seed |
| tag | IB label carried onto the stamp | candidate.seed |
| assessed_at | when assessed | candidate.seed |

### `span_candidate` — the L4b stamp
Grain: *one row per CANDIDATE span (existence = candidate) — the L4b stamp over the L4a span.*

| column | use | source / filled_by |
|---|---|---|
| span_id | the L4a span stamped | — |
| lemma_key | base Strong's of the span (denormalised) | derived:span.strong_variant |
| candidate_tag | IB label from the seed | candidate_seed.tag |
| seed_source | which seed layer | candidate.set |
| set_at | when stamped | candidate.set |

---

## 7. ⚠ The gap — what config does NOT yet govern

The plumbing is fully config-driven (sequence, scope, on-fail, write-grants, keys, enums). **What is missing is the config that decides *which lemmas become candidates* — the actual seeding rule.** Specifically:

1. **No decision rule in config.** `candidate_seed.decision` (candidate/rejected/undecided) is `filled_by: candidate.seed`, but there is **no `cfg_setting` or table that defines how the handler decides**. The "independent net + registry-direct + config" described in the step's `does` has no `config` rows behind the word "config" — the logic lives entirely in the Python handler, unreviewed.
2. **No layer definition.** `candidate_source` enum lists four layers (registry-direct · curated-synonym · ib-judgement · read-emergent) and `candidate_seed.layer` records which fired — but **no config enumerates what each layer matches on**. There is no curated-synonym list, no ib-judgement rule set, no read-emergent feed in the config store.
3. **No function-word / noise exclusion for seeding.** `discovery.particle_pattern` excludes `H9xxx` particles at *discovery*, but there is **no config rule filtering the seed net itself**. This is the concrete cause of the known defect (memory `project_iba_candidate_seeding_registry_direct_noise`): registry-direct-only seeding pulls in function-word noise that then distorts char-continuity passage generation downstream.
4. **No gloss-match rule.** `lemma_inventory.gloss` is described as "the meaning the net matches on", but **no config defines the match** (exact/substring/threshold, stop-words, which registry field).

**Net:** the module's *orchestration* is properly config-governed; the module's *judgement* (the seeding decision) is not. That judgement is the part flagged as rushed, and it is exactly what needs config rules before a re-run.

---

## 7A. What logic the handler ACTUALLY uses (code-read 2026-07-19)

Read of [`iba/app/handlers/candidate.py`](../iba/app/handlers/candidate.py) + [`iba/app/migration/import_seed.py`](../iba/app/migration/import_seed.py).

**Span judgement (`candidate.set`)** — there is no span-level judgement. A span is stamped iff its
base-Strong's is in `candidate_seed` with `decision='candidate'`. No context, frequency, or per-verse test.

**Seedlist (`candidate_seed`) inputs** — three, only one active:
- **registry-direct** — *any* inventory lemma whose base-Strong's is carried by *any* registry word's
  `word_strong` list. **2447 of 2805 candidates (87%).**
- **frozen migration** (`import_seed.py`) — ib-judgement 202, read-emergent 156, copied once from old-study flag files.
- **`cfg_candidate_rule`** (synonym/accept/reject) — the dedicated module config — **0 rows. Contributes nothing.**

**The fault (confirmed by data).** registry-direct keys on `word_strong` = the raw STEP word-search hits,
which include incidental high-frequency helpers. Top candidate lemmas by corpus span-frequency:

| lemma | spans | layer | tag | admitted because it co-occurs in STEP hits for registry word… |
|---|---|---|---|---|
| H5921 | 5774 | registry-direct | "upon" (preposition) | **reasoning** |
| H1961 | 3561 | registry-direct | "to be" | endurance / being |
| H3117 | 2233 | registry-direct | "day" | longing |
| H3027 | 1619 | registry-direct | "hand" | consecration / power / … |
| H0559 | 5309 | read-emergent | "to say" (’amar) | promoted whole-lemma from a single-verse read |

None are the anchor sense of the matched word — they are co-occurring noise. The rule never asks
"is this Strong's the word's OWNER/anchor?", so every generic verb and preposition rides in, and
char-continuity then chains on them so passages never break. **This is the registry-direct noise defect.**

**Three-part root cause (all in the seeding logic, not the span stamp or the PS runner):**
1. registry-direct is too crude — `word_strong` membership instead of anchor/owner ownership.
2. no stop-lemma / function-word screen and no frequency ceiling anywhere.
3. `cfg_candidate_rule` (the reject layer) is empty.

**Passages, for parity:** passage rules live as loose `cfg_setting` keys (`passage.default_rule`,
`passage.cross_chapter`, `passage.min_shared_strongs`, `passage.review_over`) — there is **no dedicated
`cfg_passage_rule` table**. The two modules are inconsistent (candidates: dedicated-but-empty table;
passages: scattered settings). Neither is the populated, module-dedicated ruleset expected.

## 7B. FIX APPLIED (2026-07-19)

**Change** — [`iba/app/handlers/candidate.py`](../iba/app/handlers/candidate.py) `seed()`: the
`word_strong`-coverage block that *created* candidates was removed. Registry coverage is now the
**double-control only** — it sets `registry_match` on already-independent candidates and never
confers candidacy (the explicitly-rejected "LORD→lust" co-occurrence route per
`wa-characteristic-role-lexical-cycle-authoritative-v1-20260708.md` §4/§11). Candidacy is
meaning-based only: migrated independent net (gloss/synonym `char_matched` + `ib_candidate`) +
read-emergent + editable `cfg_candidate_rule` (config seed `iba/app/config/candidate.json`).

**Re-run** — `import_seed` reset `candidate_seed`; fixed `candidate.seed` re-run; all 66 books
re-stamped (`candidate.set`) and re-passaged (`passage.build`).

**Result**

| metric | before | after |
|---|---|---|
| candidates | 2805 | **1732** (1353 registry-direct gloss, 202 ib-judgement, 177 read-emergent, 74 reject) |
| function words as candidates | H5921 upon, H1961 to-be, H3117 day, H3027 hand… | **none** |
| passages | runaway chains on "upon"/"to be" | **18,571**; 15,027 single-verse, 2,953 of 2–3, 25 over 10 (max 26) |
| needs_review passages | — | 25 |

**Config parity, both modules:** candidates = `cfg_candidate_rule` (editable meaning-net) + the
independent seed; passages = `cfg_setting` `passage.*` keys (`default_rule=char-continuity`,
`min_shared_strongs=1`, `cross_chapter=false`, `review_over=10`). No new tables added
(scalar rules belong in `cfg_setting` by app design; list-inputs in `cfg_candidate_rule`).

**Residual, by design:** top remaining candidates are generic verbs (asah/bo/halak/amar/raah/shuv)
from the read-emergent layer — meaning-based, intentionally over-inclusive, tested at the lexical
(Axis B role) stage; they no longer over-chain passages.

## 8. Suggested review questions (for you)

- Should the seeding decision be expressible as config rows (e.g. a `cfg_candidate_rule` table: per-layer matcher, source field, threshold, exclusion pattern), so it is reviewable and adjustable without code?
- What is the correct **function-word / stop-lemma exclusion** for the seed net, and should it be a `cfg_setting` pattern like `discovery.particle_pattern`?
- For the **curated-synonym** and **ib-judgement** layers — where does that list live, and should it be config or a data table?
- Confirm `candidate.seed` being **global** (re-runs the whole inventory each book) is intended, vs. incremental.
