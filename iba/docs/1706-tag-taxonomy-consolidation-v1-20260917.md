# `ib_observation.tag` — consolidated inventory, consolidation check, registration proposal

**Continues #1706.** Per researcher instruction, 2026-09-17: *"throughout the preparation we
signposted tags to be included - start with ensuring those tags are in configs and they make
sense... pay special attention to tags that essentially means the same thing, and consolidate
them. tags are really important because it is a key differentiator for the follow up stages."*

**Checked live first:** `ib_observation.tag` is `NOT NULL`, `cfg_column.use` says "stage-specific
enum, cfg_enum-governed" — but `cfg_enum` has **zero** registered groups for it, for any stage
(only `ib_observation.stage` and `ib_observation.window` exist), and the table has **0 live rows**.
Every value below was signposted across design docs but never actually registered. This is not
new — flagged already at #1706 v17 (§3.1 of the Phase C build-scoping doc) — this doc is the
promised full follow-through: gather every signposted value, check for overlap, propose the
registration.

---

## 1. Full inventory, by stage — grounded, not invented

### `reading` (process c) — real, exercised 8-value taxonomy
Data-derived from the M10 prototype run (#1691 §5, 394 observations across 15 families):

| tag | count | meaning (from the reading-stage rules, checklist §2) |
|---|---|---|
| `instance-meaning` | 145 | a positive per-occurrence reading (rule 5) |
| `verse-grouping` | 110 | similar verses grouped, each occurrence still individually accounted for (rule 4) |
| `difference-inference` | 39 | a difference or specific inference, kept as its own observation (rule 7) |
| `surface-gloss-divergence` | 32 | `span.surface` vs `stepGloss` divergence explored (rule 8) |
| `no-human-context` | 23 | a homonym/name with no meaningful context, earmarked, not forced (rule 11) |
| `cross-family` | 20 | a cross-family/cluster pointer, deferred to synergy (rule 12, cross-cutting rule 5a) |
| `data-error` | 17 | a data-quality issue found while reading, flagged separately (rule 13) |
| `alternative-meaning` | 8 | more than one candidate reading where the data supports it (rule 6) |

This 8-value set is real and already exercised — propose registering it as-is for `reading`.

### `answer` (process d) — no real taxonomy yet, direction confirmed
Every prototype row currently carries the placeholder `'slant'`. Researcher's own words, #1691 §5
(2026-09-13): *"this is exactly what it should be — the question answer raises a flag that needs
follow up."* Confirmed axis: fold the two currently-separate flag arrays into `tag` values —
`needs_adjacent_verse_context` (4 occurrences in the prototype) and `cross_family_or_cluster_flags`
(15 occurrences) — plus whatever ordinary "answered cleanly" case needs its own value once real
non-flagged answers are tagged too (not just flags). **Exact value names not chosen** — this doc
proposes them in §3.

### `synthesis` (process e) — too few rows to generalize
Only 5 prototype rows, all uniformly `'synthesis'`. #1691 §5 explicitly parks this ("worth the
researcher's own eye once more synthesis rounds accumulate") — not proposing values here; flagged
as a known future gap, not urgent.

### `subgroup` (process b's promoted observations) — zero candidates on record
When a `placement_note` carries a genuine observation (not just a bookkeeping placement reason),
it's promoted to its own `ib_observation` row, `stage='subgroup'` (#1691 §9 item 8). No tag value
has ever been proposed for these rows. **Cannot be drafted responsibly yet** — the promotion
mechanism itself (telling "just a reason" from "also an observation" apart) is still undesigned
(#1693 §2, carried at #1706 v17 §3.4/§3.5) — a tag taxonomy for a mechanism that doesn't exist yet
would be guessing. Flagged as a dependent gap, not proposed here.

### `verse_meaning` (Phase C, this build) — zero candidates on record
Same situation as `subgroup` — a new stage with no exercised data yet. Unlike `subgroup`, its
design IS closed (#1711), so a first draft is reasonable here (§3).

### Cross-cutting, not stage-specific
- **`unresolved-not-guessed` (working name only, not chosen as a literal value)** — the "genuinely
  couldn't resolve from available data" principle, confirmed 2026-09-16 as governing *every*
  `ib_observation`-writing stage (checklist §0 item 6), explicitly modeled on `data-error`/
  `no-human-context` "already work[ing]" — but neither of those is actually registered either (see
  header). **Open question this raises, not previously asked:** is this its own new tag value, or
  is `no-human-context` already exactly this principle for the one case it currently covers
  (homonyms), needing only a sibling value for non-homonym cases? See §2.2.

---

## 2. Consolidation check — RESOLVED, researcher, verbatim, 2026-09-17

### 2.1 `cross-family`/`cross_family_or_cluster_flags` → consolidated as `cross-cluster-significance`
*"consolidate into 1 tag to flag cross_cluster_sginificance; each ib_node reference 1 cluster. a
cross cluster tag would expect multiple rows for the same observation with a seq entry to link the
nodes together."* **Closed** — one tag, one observation, multiple `ib_node` rows (one per
referenced cluster), `seq` linking them together. This also directly answers #1692's own open item
3 (whether `ib_node.cluster_code` can independently name a *different* cluster than the
observation's home) — **yes, confirmed**, exactly the mechanism this tag needs. Normalized to
hyphen-case per §2.3 below and the apparent typo corrected: **`cross-cluster-significance`** —
flagging the normalization explicitly since the researcher's own text was
`cross_cluster_sginificance`, in case that changes the intended spelling/wording.

### 2.2 `no-human-context` vs. "could not resolve" — RESOLVED, two distinct tags, not one
*"a tag saying 'could not resolve' means reading of the verse could not get a clear result, but
there are some signal that it should be able with further analysis to resolve. however
'no-human-context' is a definitive tag which is an indicator that the verse likely have no IB
significance."* **Closed** — these are different in kind, not degree:
- **`no-human-context`** — a *definitive, resolved* conclusion: this verse/occurrence likely has no
  inner-being significance at all. Not a failure to resolve — a real finding.
- **`could-not-resolve`** (working name, hyphen-case, not yet confirmed as the literal string) — a
  *provisional, unresolved* state: the reading could not reach a clear result this pass, but a
  signal exists that further analysis could resolve it. Given its "revisit later" character, this
  looks like it belongs under cross-cutting rule 5a's "flagged now, resolved in a later pass"
  pattern (like `needs_adjacent_verse_context`) — not decided here, flagged for confirmation in §5.

### 2.3 Naming convention — RESOLVED
*"hyphen case is acceptable - but be consistent throughout the project."* Adopted throughout this
doc: `cross-cluster-significance`, `could-not-resolve`. Scoping this as "consistent across
`ib_observation`'s enum-governed columns going forward," not a retroactive rename of unrelated,
already-registered snake_case values elsewhere (e.g. `ib_observation.stage`'s own `verse_meaning`
value) — flagging that one visible tension for awareness, not proposing to touch it unless you want
it included.

### 2.4 Checked, NOT redundant (due diligence, no merge proposed)
- `difference-inference` vs. `alternative-meaning` — distinct: the first is an inferred distinction
  arising from comparing occurrences (rule 7), the second is multiple candidate readings for one
  instance where the data supports more than one (rule 6). Kept separate.
- `verse-grouping` vs. `instance-meaning` — distinct: grouping is a presentation/organization
  signal (rule 4), instance-meaning is the substantive reading itself (rule 5). Kept separate.

---

## 3. Registration proposal — CORRECTED, my per-stage grouping was wrong

Researcher, verbatim, 2026-09-17: *"be careful to not fragment tags on the basis of stage, the
majority of tags could apply through all the stages. `ib_observation` is one set [of] data records
that is populated in various stages, but each stage works with all the related observations, not
just with the specific stage. I would not make the grouping for observation tags the stage, but the
observation. observation will have several sub groups of enums e.g. tag, stage, window,
meaning_source, status. looking at the current items in [§]3 it seems that you have your wires
crossed."*

**Correction accepted.** My §3 draft in the prior version of this doc proposed one `cfg_enum` group
per *stage* (`ib_observation.tag.reading`, `.answer`, etc.) — wrong. The grouping axis is the
*column*, not the stage: `ib_observation` is one unified record set, and most tags (as `2.1`/`2.2`
just confirmed — `cross-cluster-significance`, `could-not-resolve`, `data-error`, `no-human-context`
have no reason to be reading-only) can legitimately apply at more than one stage. One flat group per
enum-governed column, matching `stage`/`window`'s own already-correct pattern:

| Column | `cfg_enum` group | Status |
|---|---|---|
| `stage` | `ib_observation.stage` | Already correctly registered (5 values) |
| `window` | `ib_observation.window` | Already correctly registered (4 values) |
| `tag` | `ib_observation.tag` | **Not registered at all — this doc's main proposal** |
| `meaning_source` | `ib_observation.meaning_source` | **Also not registered** — found checking this correction (see below) |
| `status` | `ib_observation.status` | **Also not registered**, despite real prototype data existing |

**Two more columns found with the same untapped-registration problem, checking `cfg_column` against
this same principle:**
- **`meaning_source`** — `cfg_column.use` currently reads *"reading stage only"*, which looks like
  the identical mistake this doc just got corrected on: `verse_meaning` (Phase C) *also* reads the
  same 3 meaning sources per its own design (#1706 §4A, the "complementary, not redundant" rule) —
  there's no reason `meaning_source` would be reading-exclusive. Flagging the `use` text itself as
  likely stale, not just the missing `cfg_enum` group — proposing to correct it to something
  scope-neutral (e.g. "which of the 3 meaning sources this observation drew from — any
  meaning-reading stage, not reading-only") rather than leave a second wrong stage-scoping claim
  standing right next to the one just fixed.
- **`status`** — `cfg_column.use` already has real prototype data (*"resolved (56),
  needs-corroboration (15), open (8), silent (2)"*), correctly framed with no stage restriction —
  but, like `tag`, was never actually turned into a registered `cfg_enum` group.

**Proposed `ib_observation.tag` values (one flat group, all stages share it):**
`instance-meaning`, `verse-grouping`, `difference-inference`, `surface-gloss-divergence`,
`no-human-context`, `cross-cluster-significance`, `data-error`, `alternative-meaning`,
`could-not-resolve` — the 8 real/exercised values plus the newly-confirmed consolidation and the
newly-distinguished "provisional, not definitive" tag. **Still open, not yet drafted:** the
answer-stage's plain "nothing flagged" baseline (every row needs a tag; a flag is the exception),
and any `verse_meaning`-specific additions once real data exists — not proposing to invent either
blind.

**Proposed `ib_observation.status` values:** `resolved`, `needs-corroboration`, `open`, `silent` —
straight from the already-recorded prototype counts, hyphen-cased per §2.3.

**Proposed `ib_observation.meaning_source` values:** not drafted here — I don't have the same kind
of grounded inventory for this column that `tag`/`status` have (no prototype-data breakdown on
record). Flagging as the next small gather-and-register task, not guessing at values now.

---

## 4. `needs_adjacent_verse_context` — content requirement, per researcher instruction 2026-09-17

Researcher, verbatim: *"this flag should have clear instructions to ensure the observation text
captures the reason for the flag - what is outstanding that need a cross check. This applies
through all the observation stages."* **Decided, recording directly, not a new judgment call:**
whenever this tag/flag is raised, at ANY stage that can raise it, `obs_text` must state explicitly
what's outstanding and what the follow-up cross-check needs to establish — never a bare flag with
no explanation. This refines cross-cutting rule 5a (flags deferred to a later run) with a content
requirement 5a didn't previously state. Added to the governing-rules checklist directly as new rule
5b, since it's a clear instruction, not a design choice needing a decision.

## 5. Resolved, researcher, verbatim, 2026-09-17

### 5.1 — `cross-cluster-significance` spelling, CONFIRMED
Normalization accepted as proposed.

### 5.2 — `could-not-resolve`, CONFIRMED
Working name accepted as the literal value.

### 5.3 — the `answer`-stage baseline isn't just an `answer`-stage problem — stage naming itself needs to be explicit
*"answer as a label almost imply this is the only place where the catalogue applies, it is not,
because verse-reading include answers also as well as 'reading'. maybe the stages must be explicit:
verse-reading; char-reading; char-answers; char-synergy."* **Real point, not just a tag-naming
nit**: `verse_meaning` also answers catalogue questions (T1.1/T7.1) — so a bare `answer` stage tag
baseline would misleadingly suggest catalogue-answering only happens at the `answer` stage. This
reopens, with a sharper reason this time, the naming question #1692 §item 5 already flagged and
left unresolved (*"whether stage/source_stage's actual DB values should be renamed... `answer`→
`observation`, `synthesis`→`synergy`"*) — a different proposed mapping this time
(`verse-reading`/`char-reading`/`char-answers`/`char-synergy`), not the same one repeated.

**Proposed `ib_observation.stage` rename** (table is still 0 rows — free to rename, no migration
cost):

| Current value | Proposed | Grain |
|---|---|---|
| `verse_meaning` | `verse-reading` | per-cluster, pre-subgroup — reads + answers T1.1/T7.1 in one pass |
| `subgroup` | *(not addressed in your instruction — keeping as-is unless you want it in the same scheme, e.g. `char-subgroup`)* | subgroup formation |
| `reading` | `char-reading` | per-family, post-subgroup |
| `answer` | `char-answers` | per-family, post-subgroup, catalogue Q&A |
| `synthesis` | `char-synergy` | cross-cluster |

**Needs your confirmation:** does `subgroup` join this naming scheme too (e.g. `char-subgroup`), or
stay as `subgroup` since it isn't a meaning-reading stage at all? Flagging rather than guessing —
and noting for completeness this also finally answers #1692's long-open item 5, in this session's
own vocabulary rather than the earlier `observation`/`synergy` one.

**Consequence for the `answer`-baseline tag question**: parked until the stage rename is
confirmed, since the value's own name will likely want to echo whichever stage label it lands
under (e.g. a `char-answers`-scoped "nothing flagged" baseline).

### `meaning_source` — RESOLVED, real data exists (M10 prototype), not undrafted after all
*"meaning source refers to the three meaning tables - if the observation pulls the data from a
specific meaning table it needs to be referenced. (this was done in M10 prototype)."* Confirmed
live: the M10 prototype already carries a real exemplar
(`1682-cluster-reading-process-spec-v1-20260911.md` line 187): `"meaning_source":
"strong_meaning_tree"`. The three source tables/columns, checked against the live schema:
`strong_meaning_tree` (its own table), `strong_lexicon.lsj`, `strong_lexicon.mounce` (two columns
of one table, not two tables). Proposed `ib_observation.meaning_source` values: `strong_meaning_tree`,
`strong_lexicon.lsj`, `strong_lexicon.mounce` — kept as literal schema references, not
hyphen-cased, since these name actual tables/columns rather than descriptive categories (flagging
this as a deliberate exception to §2.3's hyphen-case rule, not an oversight).

**One open question this raises, not addressed by the M10 exemplar**: the "read all 3 sources as
complementary, never pick-one-drop-the-rest" rule (confirmed governing `verse_meaning` too, per
#1706 §4A) means a single observation could legitimately draw on more than one source at once. Does
`meaning_source` then need to carry multiple values (e.g. all sources that contributed), or does it
record only the most load-bearing one even when others were read? The M10 exemplar shows a single
value; whether that's "only one source ever mattered per observation in practice" or "the field was
never asked to carry more than one" isn't distinguishable from one example.

### 5.4 (doc's own item 4) — go-ahead to register, PROGRESSIVELY
*"you can register the configs that is sorted out. that helps if we do it progressively because it
will allow us to spot more anomalies."* Registering now, this session, everything with no open
question left: the 9 `ib_observation.tag` values (§3, including the two just confirmed), the 4
`ib_observation.status` values, the 3 `ib_observation.meaning_source` values just resolved above,
and the `tag`/`meaning_source` `cfg_column.use` text corrections. **Held back, on purpose:** the
`answer`-stage baseline tag (blocked on §5.3's stage-rename confirmation) and the `stage` rename
itself (needs your subgroup answer first).
