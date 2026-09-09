# Layer 1 / Layer 2 — six-point column map

- **filename:** 1607-layer1-layer2-six-point-column-map-v1-20260909.md
- **date:** 2026-09-09
- **escalation:** #1607
- **template** (session log `Logs/SESSION-LOG-20260909-layer1-role-design-and-tcode-completeness-sweep.md`,
  confirmed by the researcher this session): for every live `verse_lexical` (Layer 1) and
  `verse_lexical_note` (Layer 2) column —
  1. **Definition** — roughly what it is
  2. **Source** — where it comes from
  3. **Soundness** — validity of source
  4. **Config-currency** — does `cfg_column.use`/`cfg_method_rule` still say this accurately
  5. **Recorded-value** — what values the column should have, and why
  6. **Layer-2-consumption** — why/how Layer 2 will use the values
- **Scope note:** this map states the **target design** (post-redesign, per #1605's role/status/
  pairing/party_kind decisions this session), checked against **live current data**, not a
  description of the pre-redesign behaviour — `cfg_column.use` and code still describe the old
  model everywhere (see each column's Config-currency point); nothing here has been applied to the
  DB. Genuinely open decisions are called out inline and collected in §3.
- **Not in scope:** `passage.genre`/`passage.lexical_complete_at` (CA-11/CA-12) are a related, still-
  open gap but belong to `passage`, not `verse_lexical`/`verse_lexical_note` — not repeated here.
- **Still pending from the prior turn, unrelated to this map's own findings:** `H3477H`'s disposition
  (Book of Jashar, T2+T3 live) — not yet answered.

---

## 1. Layer 1 — `verse_lexical` (544,572 live rows, 29,754 verses)

### `id`
1. Surrogate PK. 2. Auto-increment. 3. Structural, sound. 4. Accurate. 5. Unique per row, no gaps
expected. 6. Not read by Layer 2 directly — join key only.

### `span_id`
1. Which span this reading is for. 2. `span.id`. 3. Sound — 0/544,572 rows reference a missing/
deleted span, corpus-wide. 4. Accurate. 5. Every row has a live span. 6. Layer 2 joins through it to
get `span.surface`/`span.position`/sibling ordinals for `pairing`.

### `verse_id`
1. Denormalized from span, for query-without-joining-through-span. 2. `span.verse_id`, copied at
build time. 3. Sound — 0/544,572 mismatches vs. `span.verse_id`, corpus-wide join. 4. Accurate.
5. Matches its own span, always. 6. Layer 2's primary scoping key — every note/finding is filtered by
verse (or passage-block) via this column.

### `code_ordinal`
1. Position of this code within the span's space-joined `strong_variant`, 0-based. 2. Computed at
build time from `strong_variant`'s own token order. 3. Sound — 0 duplicate `(span_id, code_ordinal)`
pairs live, corpus-wide. 4. Accurate. 5. Contiguous 0..N-1 per span, no gaps expected (not directly
re-verified this round). 6. Layer 2's `pairing` (§ below) and `target_verse_lexical_id` resolution
both need this to identify "the other codes in this span."

### `strong`
1. The single code this row resolves. 2. One token of `span.strong_variant`. 3. Sound — 0/544,572
NULL, confirmed against the purpose text's own stated expectation ("should not occur in practice").
4. Accurate. 5. Always a real Strong's code string. 6. Layer 2's entry point into `cluster_strong`
(for `role`), `strong_meaning_parsed` (for `resolved_sense`), and every other strong-keyed table.

### `morph_code`
1. This code's own morph slice (space-split from `span.morph_code`). 2. `span.morph_code`, split at
build time. 3. **Not fully sound** — 1,082/544,572 (0.2%) NULL, unexplained by the purpose text.
Researcher decision this session (§9.1 of #1605): **stays exactly as-is, populated for every code, no
M-code restriction** — settles the scoping question, but not the 1,082-NULL gap itself (CA-1, still
open — silently defaults `classify_role`'s Greek branch to `content` for these rows today; whether
that silent default survives `role`'s redesign depends on how `role`'s build handles a NULL morph
slice, not decided here). 4. Accurate as far as it goes; says nothing about the NULL case.
5. Should be non-NULL for every code (per its own purpose's implicit claim); 1,082 rows aren't.
6. Layer 2 reads it for stem/voice context on `resolved_sense`, and (once built) for `pairing`'s
same-span binding.

### `role` — the central redesign
1. **Redefined, researcher instruction verbatim, 2026-09-09:** the **complete set** of live
`cluster_strong.cluster_code` values the strong belongs to — not a scalar, not a translated category
label, everything found. Multiple memberships are not an error; a **NULL set (no cluster membership
at all) IS an error**, must be surfaced, never silently defaulted.
2. Source: `cluster_strong WHERE strong=<this row's strong> AND deleted=0`, read at build time — the
same table `is_negator`/`party_kind` already draw from, generalized to the whole cluster taxonomy
(M01-M80ish, T2-T15, FLAG) rather than the T4/T5/T7/T8/T9 subset those two use.
3. Soundness — checked live, corpus-wide, this session: **107 distinct strongs (108,163 live rows)
have zero live `cluster_strong` row at all** — the exact NULL-set-is-an-error case the redesign names.
100% of those rows are currently `role='function'` under the old model (Greek prepositions/
conjunctions — `G0575` "away from" 606 rows, `G1519` "toward" 1,603 rows, etc.) — real, frequent
words, not edge cases. This is escalation #1606's own leg-3 finding (109 zero-cluster strongs, 107 of
which are these). **Also checked: 96 strongs carry 2+ live cluster_codes** — resolved this session
(#1605 §§0/10, §5 of the same doc): 59 by-design (T7-T14 referent-identity axis), 7 M+FLAG (a review
marker, not a second classification), 37 were T2-vs-M real conflicts, **now all individually
reconciled** (§5.1/§5.0 of #1605, confirmed live). A further 13 M+T3/T2+T3 combos surfaced scanning
the whole live table (not just the 96); researcher verdict this session: **M+T3 is normal, accept
as-is** (12 of 13); `H3477H` (T2+T3) still open.
4. **Not current** — live `cfg_column.use` still describes the pre-redesign content/function model
verbatim ("'content' (independent lexical item) or 'function' (grammatical formative...)"). Per
§1.0's own disposition: not rewritten yet, deliberately — recorded as a `cfg_method_rule` first, then
`cfg_column.use` and the code together, same unit of work, once storage shape is settled (point 5).
5. **Storage shape — still open, not decided.** Candidates on record: a denormalized comma/JSON list
(same shape already used ad hoc to check the 96 multi-code strongs) with an explicit
error/incompleteness marker for the NULL-set case (a flag column, or NULL itself being read as the
error signal rather than "checked, has none" — ambiguous today, needs a real answer). Not proposed
here.
6. Layer 2's primary signal for what kind of word this is: single-M → likely characteristic;
multi-M → weigh both senses in context; M+T → read together as a tight connection (T7-T14
specifically: source/target/affected-party of the verse's movement — the fact `verb_argument` is
supposed to consume, see §2); pure T → treatment depends which T-code. Per `cluster-allocation-is-
preliminary-triggers-reach-back` (#1605 §1.3, live-registered as a proposed `cfg_method_rule`, not
yet applied): a mismatch between allocation and verse-context is not an error to reconcile, it's a
trigger to pull the strong's full meaning data for that occurrence.
**Build-currency note:** since `role` isn't built yet, this doesn't apply to it directly, but it will
inherit the same staleness risk documented under `is_negator`/`party_kind` below — every
`cluster_strong` change needs a rebuild to reach `verse_lexical`.

### `status`
1. **Redefined, researcher instruction verbatim (§8.2/8.5 of the prior 1592-1595 doc, restated in
#1605 §3):** meaning-data readiness, not resolution-outcome — `Meaning Ready` / `Meaning to be
pulled` / `Meaning not applicable` (T2). 2. Not yet built. **Open, unresolved from the prior session:
"ready against which table(s)?"** — candidates checked live (#1592-1595 doc §8.3): `strong.stepGloss`,
`strong_sense.head`, `strong_meaning_parsed.gloss` — same source-table question `resolved_sense` (next
column) needed answered, and it now has been for `resolved_sense` specifically
(`strong_meaning_parsed.gloss`); whether `status`'s own readiness check reads the *same* table or a
different one is **still not confirmed**. 3. N/A pending 2. 4. Live `cfg_column.use` describes the
OLD `'resolved'`/`'unregistered'` model — accurate for that model, not for the redesign.
5. Three-valued per the redefinition; exact boundary condition not set. 6. Layer 2 would use this as
a fast pre-filter (don't bother pulling meaning for a T2 word; know upfront whether a real gap exists
before reading `resolved_sense`).
**Open decision carried forward, needs your call:** which table backs "meaning is available"?

### `resolved_sense`
1. Stem/voice-selected sense text, scoped to **M-code words only** (settled #1527/#1575 — not every
code, unlike the pre-#1575 model). 2. **Settled, researcher instruction verbatim, 2026-09-08:**
`strong_meaning_parsed.gloss`, capped **100 characters**. 3. Checked live against 3 M-code strongs
with zero exact-variant rows (the hard case) — base-fallback lookup (`resolve_code()`, unchanged
algorithm) catches all 3 correctly. Sound, for the mechanism; **currently 0/544,572 populated**
because it isn't built yet (correctly NULL under the still-live #1575 code, which stopped writing
this column for every word pending the M-code-only rescope). 4. **Not current** — live
`cfg_column.use` still describes the pre-#1575 all-codes model (CA-3, "the documentation itself is now
false"). 5. A joined, sorted, 100-char-capped gloss string, M-code rows only, NULL for everything
else. **Open, not decided:** truncation boundary — hard cut at exactly 100 chars (two live samples cut
mid-word: `"...to u"`, `"...to spe"`), or cut at the last complete `;`-clause at-or-under 100 (cleaner,
variable length)? 6. Layer 2's primary "what does this word mean" text for characteristic-tagged
words specifically — the qualifier/function population (T-coded) deliberately gets no
`resolved_sense`, relying on `role`'s cluster membership + reach-back instead.
**Open decision carried forward, needs your call:** truncation boundary.

### `ambiguity_note` → `pairing`
1. **Redefined, researcher instruction verbatim:** renamed from "flag a sibling/base-fallback meaning
ambiguity" to "show the morph-based binding of this code to other codes in the same verse." **Scope
confirmed, researcher instruction: same-span only** (not cross-span). 2. Would draw on `code_ordinal`
grouping within `span_id` — the same underlying fact `gloss_consistent_in_verse`'s multi-ordinal-span
check already uses. 3. The underlying same-span grouping is sound (0 structural issues, checked under
`code_ordinal`/`span_id` above). 4. Live `cfg_column.use` describes the old ambiguity-flag purpose —
stale the moment `pairing` is built (not yet). 5. **Open, not decided — format.** Three candidates
costed against real spans (2Cor.6.6 span 534082, Jer.23.12 spans 534253/534248): **(1) sibling
ordinals** — cheapest, comma-list of `code_ordinal`s, arguably adds nothing a reader couldn't get by
querying the span; **(2) sibling code+role list** — still cheap (one join), self-contained, e.g.
`"G0054 (content)"`; **(3) interpreted binding** — richest, closest to "binding" in the original
wording, but needs a new prefix/suffix morph-code attachment lexicon that doesn't exist yet (real
build, not a join). 6. Layer 2 reads this to know which codes in a compound span/idiom belong
together before interpreting any one of them alone.
**Open decision carried forward, needs your call:** format 1/2/3/other.

### `created_at`
1. Row creation timestamp. 2. Mechanical, `datetime('now')` at insert. 3. Sound. 4. Accurate.
5. ISO-8601 UTC, always. 6. Not read by Layer 2 analytically; provenance/audit only.

### `deleted`
1. Version-aware soft-delete — a rewritten `(span_id, code_ordinal)` inserts a fresh row, flips the
superseded row's `deleted` to 1. 2. Mechanical, set by the write path. 3. Sound. 4. Accurate.
5. 0 or 1; 430,888/975,460 all-time rows currently 1 (44% churn, from multiple full-corpus rebuild
waves — not a defect, scale context only). 6. Layer 2 always filters `deleted=0`; never reads deleted
rows except for history/audit tooling.

### `position`
1. `span.position`, denormalized. 2. `span.position`, copied at build time. 3. Sound — 0/544,572
mismatches vs. `span.position`, corpus-wide, full check (not sampled). 4. Accurate. 5. Matches its
span's position always. 6. Layer 2 uses it for verse-order sequencing without a join.

### `surface`
1. **Invariant restated, not redesigned, researcher instruction verbatim:** never blank, must be the
single aligned English word for *this specific code*. 2. `span.surface`, denormalized. 3. **Not
sound — already-escalated defect (#1591, 192 rows, 0.035%)**, cross-referenced not re-litigated here:
59 rows blank outright, plus confirmed misalignment cases (Deut.7.18 pos.2, 1Thess.1.1 pos.17).
4. Accurate as a purpose statement; doesn't itself claim the invariant always holds. 5. Should be
never-blank per the restated invariant; isn't, for 192 rows. 6. Layer 2's literal-text anchor for
every finding that needs to quote or point at "the actual word" — the 192-row defect directly
undermines that for affected rows.
**Gated, not part of this map's open-decisions list:** #1591 stays gated pending your approval of the
repair method already on record there.

### `language`
1. `strong.language`, denormalized. 2. Copied at build time. 3. Sound — 559 NULL, exactly matching
`status='unregistered'` (no strong row → no language to copy) — internally consistent. 4. Accurate.
5. `'Hebrew'`/`'Greek'`/`'Aramaic'`, or NULL only for the 559 unregistered rows. 6. Layer 2's
Hebrew/Greek branch selector for every language-specific rule (`narrative_morph`, `classify_role`'s
two different tag schemes, etc.).

### `testament`
1. `'OT'` if `cfg_book_order.ordinal`<=38 else `'NT'`. 2. Pure ordinal derivation from the verse's
book, no reference-table join needed beyond `cfg_book_order`. 3. Sound — 0/544,572 NULL, corpus-wide,
independent of whether the code itself resolved. 4. Accurate. 5. Always `'OT'` or `'NT'`, no NULL
case. 6. Layer 2 uses it for testament-scoped rules/questions from the catalogue.

### `is_negator`
1. 1 if this strong is a negator, else NULL (never 0 — NULL means "not in the T5 lexicon").
2. **`cluster_strong WHERE cluster_code='T5' AND deleted=0`** (11 live strongs as of today, up from 7
before this session's T2-resweep). 3. Sound as a mechanism; **current live values are stale** —
checked this round: none of today's 4 new T5 additions (G3366, G3768, H0336, H1077 — 151 live
`verse_lexical` rows between them) show `is_negator=1` yet, because no rebuild has run since they were
added. Not a data error, a **build-currency gap** — worth naming as its own operational dependency:
every `cluster_strong` change needs a rebuild to reach Layer 1. 4. **Not current** — live
`cfg_column.use` names `cfg_lexical_code_class WHERE class='negator'`, a table confirmed dead code
(never read anywhere) — CA-5, small fix, no judgement needed. 5. 1 or NULL, per point 1; treat as
preliminary per `cluster-allocation-is-preliminary-triggers-reach-back` (#1605 §1.3). 6. Layer 2's
fast negation-detection trigger, same shape as `party_kind` for divine-detection.

### `narrative_morph`
1. Hebrew-only flag: `wayyiqtol` (TAM='w') or `az_imperfect_opening` (TAM='i' + sibling H0227). 2.
Parsed from `morph_code`'s own TAM slot at a fixed position. 3. Sound for Hebrew — 0 non-NULL Greek
rows, matches its own stated scope exactly. 4. Accurate for what it currently does. 5. One of the two
named values, or NULL; Hebrew-only by design (Greek's TVM tagging has no equivalent single-slot
convention). 6. Layer 2 uses it to detect Hebrew narrative-sequence markers.
**Open decision carried forward, needs your steer, not answered yet:** what should the Greek
equivalent capture? (Greek's own narrative-sequencing signal is more the aorist/imperfect/
historical-present distinction in context than a single morph-code flag — no mechanism proposed
without more direction on what signal you want captured.)

### `gloss_consistent_in_verse`
1. **Redefined, researcher instruction verbatim:** for a multi-ordinal span (>1 live code sharing one
span/surface — 118,906/378,094 live spans, 31.4%, confirmed live), this should read as the gloss for
the **combined** sense of every code in that span, not evaluated per-code as it is today. 2. Would
draw on the same span/code_ordinal grouping as `pairing`. 3. The underlying grouping is sound (same
basis as `pairing`, verified above). 4. **Not current at all** — the live column is structurally dead
post-#1575 (its formula depends on `resolved_sense`, now permanently NULL, so ">1 distinct value"
can never fire); 106,658/544,572 (19.6%) still carry a stale pre-#1575 `0`. This is escalation #1596,
directly superseded by this redefinition, not a second fix. 5. Combined-sense-consistency read per
multi-ordinal span, once built. 6. Layer 2 would use it to know whether a compound span's combined
gloss is stable/trustworthy before relying on it.

### `party_kind`
1. `'divine'`/`'human'`/`'non_human'` — set only when the code is itself a name in the referent-
identity axis. 2. **`cluster_strong WHERE cluster_code IN ('T4','T7','T8','T9') AND deleted=0`**
(T4=adversarial→non_human, T7=divine, T8=human, T9=angelic→non_human; 78 live strongs total as of
today, up from 63 before this session's T7/T9 additions). 3. Sound as a mechanism; **same
build-currency gap as `is_negator`** — checked live, 11 of today's 15 new T4/T7/T9 members show
`party_kind` still NULL on their existing `verse_lexical` rows (one, H0410J, already shows it set on
all 4 of its rows — pre-existing from an earlier pass, not from today's addition). A rebuild is owed
before this column reflects today's cluster work. 4. **Not current** — live `cfg_column.use` drops
`party_adversarial`/T4 from its own source list (the same under-count `is_negator` doesn't have, since
`is_negator` only ever needed T5) — CA-6, small fix, no judgement needed. 5. One of the three named
values or NULL; T4/T9 both collapse to `non_human` (a deliberate coarse grain, see point 6).
6. **Confirmed this session, researcher instruction verbatim:** kept deliberately alongside `role`
despite the overlap — `role`'s complete cluster_code list (once built) *could* answer "is this word
T7 (divine)?", but `party_kind` exists as a fast, purpose-built trigger specifically so the catalogue's
divine-impact-on-characteristic questions surface immediately, without Layer 2 having to parse the
full `role` list every time. The T4-vs-T9 collapse is fine under this framing — `party_kind`'s job is
"flag divine fast," not "give the full referent-identity picture"; `role` carries the fine distinction
when it's actually needed. **§5.2, closed.**

### `updated_at`
1. Timestamp of the row's last real content correction (post-insert). 2. Set by
`write_readings_for_span` on a correction, mechanically. 3. Sound as far as it's used — 113,684/
544,572 (20.9%) currently non-NULL, consistent with "only rows corrected since the #1520
identity-stable-write redesign get it." 4. **Missing entirely — CA-7, no `cfg_column` row at all**,
a direct `governance.table_columns` violation (20/21 live columns registered, this one isn't). Small
fix, no judgement needed — behaviour already documented in code and the #1527 genealogy doc.
5. **Open, needs your confirmation of scope** — you called it "required" this session; two readings
still unresolved: required as in *every future correction sets it* (already true, mechanically), or
required as in *every row carries a non-NULL value*, which would mean stamping it on INSERT too (a
real behaviour change, not just a registration). 6. Not currently consumed by Layer 2 directly —
would become a recency/trust signal ("has this reading been corrected since first written") if built
out further.
**Open decision carried forward, needs your call:** INSERT-stamping scope.

---

## 2. Layer 2 — `verse_lexical_note` (173 live rows)

### `id`
1. PK. 2. Auto-increment. 3. Sound. 4. Accurate. 5. Unique. 6. Join key only.

### `verse_lexical_id`
1. The code-row this note is about. 2. FK, set at write time. 3. Sound — 0/173 orphaned references,
every note resolves to a live `verse_lexical` row. 4. Accurate. 5. Always a live FK. 6. Layer 2's
anchor — every note is "about" exactly one Layer 1 code-row.

### `verse_id`
1. Denormalized, matches `phenomenon`'s own precedent. 2. Copied from the parent `verse_lexical_id`'s
own `verse_id` at write time. 3. Sound — 0/173 mismatches, corpus-wide join, not sampled. 4. Accurate.
5. Always matches its own `verse_lexical_id`'s verse. 6. Query-without-joining-through-verse_lexical
scoping for Layer 2 reads.

### `passage_id`
1. Denormalized, matches `phenomenon`'s own precedent (original design). 2. Would be set from an
active passage-scoped enrichment run. 3. **Not sound in current practice** — 0/173 live rows carry a
non-NULL value; every live Layer 2 write happens in the verse-scoped mode #1451 made the default.
4. **Stale** — `cfg_column.use` describes a mode the pipeline no longer runs in at all; #1451 itself
named this as an open item ("needs a decision: drop it, or repurpose it"), not decided since.
5. Currently always NULL; target value undetermined pending the drop-or-repurpose call. 6. N/A while
undecided.
**Open decision carried forward, needs your call (CA-8):** drop the column, or repurpose it for
something real.

### `note_type`
1. What kind of Layer 2 finding this is. 2. `cfg_enum note_type`. 3. **Under-registered** — live
`cfg_enum` carries 15 values; `cfg_column.use`'s own doc-string lists only 13, **missing
`verb_argument` and `compound_unit`** entirely. 6 of the 15 (`#1589`) have zero operational
definition anywhere (separate open item, not repeated here). 4. **Stale**, the enum doc-string itself
is incomplete, independent of #1589's deeper "no definition" issue. 5. One of the 15 live values;
`verb_argument` has exactly 1 live example ever written (see §2a below) — functionally unsupported
despite being a real enum member. 6. Layer 2's dispatch key — which downstream logic/validation a
note goes through.
**Open decision carried forward:** register `verb_argument`/`compound_unit` in the doc-string (small,
no judgement) — separately, #1589's 6-undefined-values gap needs its own resolution, not decided here.

### `resolution_status`
1. Whether/how this note resolved. 2. `cfg_enum resolution_status`. 3. Structurally sound — every
live value is a real enum member; one value, `not_supported_this_language`, has **0/173 occurrences
ever** — exists, never exercised (CA-9, low priority — worth a deliberate test, e.g. a Hebrew-only
rule run against a Greek verse, to confirm the path writes correctly when it should). 4. Accurate.
5. One of 5 live values. 6. Layer 2's own confidence/completeness signal per finding.

### `target_verse_lexical_id`
1. **Doc says:** "same-verse OR cross-verse (within the loaded passage-block) resolution target
(pronoun/noun/entity-link)." **Live use contradicts this** — the one `verb_argument` example uses it
as the **agent/trigger** of a movement (Laban, in "Laban gave Leah"), not a pronoun/entity-link
resolution target at all. 2. Set at write time by the enriching LLM call, per note_type's own logic
(where logic exists — see §2a, none exists for `verb_argument`). 3. Sound for its documented uses
(21/173 rows use it, 0 unresolved/orphaned); **undocumented for `verb_argument`'s actual use**.
4. **Stale/incomplete** — needs the agent/trigger use case added to its own purpose text, not just
pronoun/entity-link. 5. A live `verse_lexical.id`, or NULL if unresolved. 6. Layer 2 (and, once built,
Window 2 synthesis) reads this to resolve what a pronoun/entity/trigger actually points at.

### `related_verse_lexical_ids`
1. **Doc says:** "structural_pattern/recurrence_role_shift rows only." **Live use contradicts this
too** — the same `verb_argument` example uses it for the **recipient/impact** of the movement (Leah),
a third, undocumented use. 2. Set at write time, JSON array. 3. Sound for its documented uses (1/173
rows, valid); undocumented for `verb_argument`. 4. **Stale/incomplete**, same shape as
`target_verse_lexical_id` above. 5. JSON array of live `verse_lexical.id`s. 6. Same as above — Layer 2/
Window 2's recipient/impact resolution, once `verb_argument` is actually wired up (§2a).

### `value_text`
1. The finding itself, free text. 2. Written directly by the enriching LLM call. 3. Sound — 0/173
NULL, 100% populated. 4. Accurate. 5. Free text, content shape varies by `note_type` (deliberately not
typed yet). 6. Layer 2's/Window 2's primary readable output per finding.

### `evidence_text`
1. What in the verse's own data supports the finding (morph marker, related-word pull, etc.).
2. Meant to be written alongside `value_text` at the same write time. 3. **Not sound at all — 0/173
rows have ANY value, universally, across every note_type, every resolution_status, without exception**
— the single largest concrete defect in this whole map (CA-10). Practice has informally folded
evidence into `value_text` instead (sample: a `related_word` note's `value_text` reads "Genuine
same-concept family: rich/enrich (H6223/H6238)" — the Strong's codes ARE the evidence, just not in
the column built to hold it). 4. Accurate as a purpose statement; says nothing about the 0%
population. 5. Should be non-NULL whenever a finding claims grounding; isn't, ever. 6. **This is the
one column Window 2 synthesis needs to audit any Window-1 finding's grounding at all** — right now
there is no way to check any of the 173 live findings' evidence without it.
**Open decision carried forward, needs your call:** enforce as a required field (write-time gate), or
formally merge into `value_text` since practice already does that.

### `created_at` / `deleted`
Mechanical, same convention as Layer 1. `deleted`: 0/173 (nothing superseded yet — thin, early-stage
sample, not a defect).

### §2a — `verb_argument`, consolidated (per your instruction: resolves in the same process as this map)

**What it's for:** capturing the source/target of a verse's movement — exactly what the T7-T14
referent-identity axis (§ `role`, §1 above) was built to feed. **The one live example works**
(note id 346, Gen, `H5414G` "gave": `target_verse_lexical_id`=agent/trigger, Laban;
`related_verse_lexical_ids`=recipient/impact, Leah; `value_text` spells both roles in prose).

**Confirmed unsupported, not just underused:**
1. **No trigger logic anywhere** — `lexicalenrich.py`'s `_note_problems` has dedicated checks for
   `chain`/`idiom`/`structural_pattern`/`recurrence_role_shift`/`cross_lemma_shared_gloss`; none for
   `verb_argument`. Nothing tells the pipeline "this T3 operation-verb should get one attempted."
2. **Field docs contradict live use** — `target_verse_lexical_id`/`related_verse_lexical_ids`, above.
3. **Missing from `note_type`'s own doc-string** (13 vs. 15 live enum values), above.
4. **No connection to T7-T14 in code anywhere** — the mechanism points at another `verse_lexical` row
   generically; nothing checks or leverages whether that row's own `cluster_strong` tag is a real
   party/place/object/natural-world referent, which is exactly the link that would make this session's
   T-code tagging work pay off for Layer 2.

**Proposed scope for a real fix (not decided/built):** correct the two field docs; add
`verb_argument`/`compound_unit` to `note_type`'s doc-string; decide the trigger condition (which T3
verbs get one attempted, and how that interacts with `role`'s complete cluster-set once built); wire
it to check the T7-T14 tag on the resolved target. Folds into the same open-decisions register as the
rest of this map (§3) rather than a separate track, per your instruction.

---

## 3. Open decisions register — consolidated from this map

| # | Item | Column | Needs |
|---|---|---|---|
| D1 | `role` storage shape — denormalized list format + NULL-set error marker | `verse_lexical.role` | Researcher decision |
| D2 | `status`'s "meaning is available" — which table backs the readiness check | `verse_lexical.status` | Researcher decision |
| D3 | `resolved_sense` truncation boundary — hard 100-char cut vs. clause-boundary cut | `verse_lexical.resolved_sense` | Researcher decision |
| D4 | `pairing` format — sibling-ordinals (1) / sibling-code+role (2) / interpreted-binding (3) / other | `verse_lexical.ambiguity_note`→`pairing` | Researcher decision |
| D5 | `narrative_morph` Greek signal — what should it capture | `verse_lexical.narrative_morph` | Researcher steer, no proposal yet |
| D6 | `updated_at` "required" scope — every correction (already true) vs. every row incl. INSERT | `verse_lexical.updated_at` | Researcher decision |
| D7 | `passage_id` — drop or repurpose | `verse_lexical_note.passage_id` | Researcher decision |
| D8 | `evidence_text` — enforce as required, or merge into `value_text` | `verse_lexical_note.evidence_text` | Researcher decision |
| D9 | `verb_argument` — trigger condition + T7-T14 wiring, once field docs are fixed | `verse_lexical_note.note_type`/`target_verse_lexical_id`/`related_verse_lexical_ids` | Researcher decision (scope), then build |
| D10 | `H3477H` disposition — T3-only vs. other, now that "Jashar" (not "upright") is confirmed | `cluster_strong` (T2+T3 live) | Researcher decision (carried from prior turn, still open) |

**Small, no-judgement config-currency fixes surfaced by this map** (buildable via
`Config-Maintenance.ps1 -Step Propose`, same batch #1605 §6 already scoped): CA-3 (`resolved_sense`
doc), CA-5 (`is_negator` doc), CA-6 (`party_kind` doc), CA-7 (`updated_at` registration), plus
`note_type`'s doc-string (missing 2 enum values) and `target_verse_lexical_id`/
`related_verse_lexical_ids`'s doc text (verb_argument use undocumented) from this map.

**Operational fact, not a decision:** `is_negator`/`party_kind` (and `role`, once built) are
build-time snapshots of `cluster_strong` — every cluster reallocation (today's T2-resweep included)
needs a `verse_lexical` rebuild before Layer 1 reflects it. 15 strongs, 316 live rows, are currently
stale from today's own T4/T5/T7/T9 additions.

Nothing in this document has been applied to the DB or to `cfg_column`/`cfg_method_rule`. Per the
standing rule against deciding judgement calls unilaterally, every D-item above is for your
disposition.
