# `cfg_quality_check` — per-row review of all `enforced_by IS NULL` rows

**Date:** 2026-08-30 · **Escalation:** #1128 (per-table cfg review), this doc answers the
researcher's direct follow-up on that item: *"I don't see the results of you evaluating that all
the configs that is set to be excluded from validation (quality check null) should in fact be
null. why are they excluded?"*

**Method.** The mechanism itself was already confirmed live in an earlier pass:
`_required_quality_checks()`/`_check_quality_attestations()` (`iba/app/handlers/operations.py`
lines 213-241) query exactly `WHERE step=? AND required=1 AND active=1 AND enforced_by IS NULL`
and require a human-written `quality_checks: {check_key: "<reasoning>"}` entry for each, wired
into `hib_set`, `phenomenon_set`, `operation_set`, `closing_set`. That confirms the *gate* fires.
It does **not** by itself confirm each of the 16 individual rows genuinely belongs on the
human-attestation side rather than a mechanical one — that per-row question is what this doc
answers, checked against the real handler code and real schema, not inferred from the
`test_kind`/question text alone.

There are 16 rows: 3 `existence`, 4 `non_existence`, 9 `reasonableness`.

## Verdict summary

| check_key | step | test_kind | Verdict |
| --- | --- | --- | --- |
| `linkage-genuinely-registered` | closing.set | existence | **Correctly excluded, but mislabeled** — see below |
| `validation-finding-corrected-not-just-logged` | closing.set | existence | **GAP** — currently unverifiable even in principle (no revision tracking) |
| `warrant-is-specific` | phenomenon.set | existence | Correctly excluded |
| `insufficiency-genuinely-absent` | closing.set | non_existence | Correctly excluded |
| `not-already-excluded` | hib.set | non_existence | **GAP** — mechanically checkable today, not implemented |
| `source-target-not-invented` | operation.set | non_existence | Correctly excluded |
| `not-a-literary-pattern` | phenomenon.set | non_existence | Correctly excluded |
| `emergent-question-not-resolvable-now` | closing.set | reasonableness | Correctly excluded |
| `is-genuinely-human` | hib.set | reasonableness | Correctly excluded, weaker relative than flagged rows — see note |
| `verse-actually-supports-it` | hib.set | reasonableness | Correctly excluded |
| `observation-uses-full-lexical-range` | operation.set | reasonableness | Correctly excluded |
| `phenomenon-actually-underlies-it` | operation.set | reasonableness | Correctly excluded |
| `boundary-not-arbitrary` | passage.build | reasonableness | Correctly excluded |
| `description-uses-full-lexical-range` | phenomenon.set | reasonableness | Correctly excluded |
| `genuinely-inner-being` | phenomenon.set | reasonableness | **GAP — revised 2026-08-30, see below** |
| `hib-still-warranted` | phenomenon.set | reasonableness | Correctly excluded |

**Revised 2026-08-30** (researcher follow-up, caught a real error in the first pass): 13 of 16
hold up. **3 are real findings** — the first pass had wrongly cleared `genuinely-inner-being`
as "no gap" on the same basis as the other reasonableness checks (no DB column to test against).
That basis is necessary but not sufficient: absence of a mechanical check does not mean the human/
AI attestor has anything live to judge against. `genuinely-inner-being` fails that second, deeper
test where the others don't — see below.

## The 9 `reasonableness` rows

All nine ask whether a piece of free text is a *genuine* semantic/interpretive fit to the
Hebrew/Greek source (a real HIB vs. a personified place; a description that draws on the word's
full lexical range vs. a generic label; a boundary judgement that would survive independent
re-reading). None of these has a corresponding structured DB column or registry to check against
— verifying them requires actually reading the verse's lexical row and judging fit, which is
exactly the class of thing this project's method treats as irreducibly human (per the interaction
protocol on genuine judgement calls vs. standards violations). Checked each against its handler's
write path (`hib_set`, `phenomenon_set`, `operation_set`, `closing_set`) — none does or could
substitute a query for this, on the *mechanical-check* axis.

**But "no mechanical check possible" is not the same test as "correctly excluded," and the first
pass wrongly conflated them for one row** (`genuinely-inner-being` — see its own entry below,
corrected after researcher challenge). The real second test: does the attestor — human or Claude —
have a live, authoritative *definition* of the term the question turns on, or only the question's
own free-standing paraphrase? Re-checked all 9 against that:

- `verse-actually-supports-it`, `observation-uses-full-lexical-range`,
  `description-uses-full-lexical-range`, `phenomenon-actually-underlies-it`, `boundary-not-
  arbitrary`, `emergent-question-not-resolvable-now`, `hib-still-warranted` — all turn on
  something already concretely in front of the reader at the moment of the call: the verse's own
  lexical row, the word's own `meaning_tree` entry, the operation's own already-written fields, the
  passage's own `feasibility_note`. Nothing external needs defining. **Genuinely self-contained —
  no gap.**
- `is-genuinely-human` (hib.set) — its question explicitly invokes "as Step 1 defines it." Unlike
  `genuinely-inner-being`, there IS live text defining this nearby: `cfg_method_rule` carries
  `non-human-scope` ("HIB = Human Inner Being. A non-human being can NEVER itself be registered as
  a HIB, by definition...", `source_doc='WA-passage-read-guidance-v1.5 step 2 notes b, d'`) and
  `presumptive-candidate` for `hib.set`. The definition text itself is real and present in the same
  config family the researcher already uses for rules — weaker than an ideal (nothing in
  `cfg_quality_check` formally links check_key → rule_key, so the connection is "sits in the same
  table family, findable by a competent reader," not a resolvable pointer) but materially better
  than `genuinely-inner-being`, which has no equivalent row at all for `phenomenon.set`.
  **Correctly excluded, but the same class of pointer weakness applies here at a lesser degree —
  worth folding into any fix for `genuinely-inner-being` rather than reopening separately.**

**8 of 9 correctly excluded outright; 1 (`genuinely-inner-being`) is corrected below to GAP.**

## The 4 `non_existence` rows

- **`insufficiency-genuinely-absent`** (closing.set) — asks whether a claimed data gap is real
  vs. substituted from memory/external knowledge. This is a claim about what source the *human*
  consulted, not a DB state — nothing in `passage_insufficiency` or `verse_lexical` can distinguish
  "genuinely checked and found absent" from "assumed absent." **Correctly excluded.**
- **`source-target-not-invented`** (operation.set) — asks whether the named parties in an
  operation are actually in the verse text. No party/entity registry exists to cross-check against;
  this is a direct-textual-reading judgement. **Correctly excluded.**
- **`not-a-literary-pattern`** (phenomenon.set) — distinguishing a genuine per-verse phenomenon
  from a book-wide literary pattern smuggled in as one is a scope/genre judgement with no
  structural marker in `phenomenon` to test. **Correctly excluded.**
- **`not-already-excluded`** (hib.set) — **GAP.** The question is: has this exact referent already
  been recorded as out-of-scope (e.g. explicitly set aside), and is this entry silently
  reintroducing it? The schema already carries the answer: `operation.decision` has a live
  `'set_aside'` value (`operations.py:885`), reachable via `phenomenon.hib_id`. Read `hib_set()`
  in full (`operations.py:397-516`): its book-wide identity lookup (`all_by_label`, lines 461-472)
  joins `hib` → `verse_hib`/`hib_referent_option` only — it never joins through
  `phenomenon`/`operation` and never looks at `decision`. So a HIB label that was previously
  reviewed and explicitly set aside is **not** cross-checked against a new payload proposing the
  same label again; only the human attestation catches it. The referential half of this ("has it
  been recorded as set-aside") is queryable today with no schema change; the interpretive half
  ("silently reintroducing... without new textual grounds") would remain a genuine judgement call.
  This is a *partial* gap: worth a mechanical floor-check (flag, not block, when a proposed label
  matches one with a live `set_aside` operation elsewhere in the book), not a full replacement for
  the attestation.

## The 3 `existence` rows

- **`warrant-is-specific`** (phenomenon.set) — asks whether `textual_warrant` names an actual
  verb/clause vs. restating `description`. Comparing two free-text fields for "vague restatement"
  is a linguistic judgement, not a query. **Correctly excluded.**
- **`linkage-genuinely-registered`** (closing.set) — **mislabeled, not a gap.** Read `closing_set`
  in full (`operations.py:1276-1301`): `_find_operation_id`/`_find_phenomenon_id`
  (`operations.py:1202-1227`) already resolve every `from_verse`/`to_verse` to a live,
  non-deleted `operation` row (via a live `phenomenon`) *before* the quality-check attestation is
  ever evaluated — if either side fails to resolve, `closing_set` returns `fail("unresolved-
  reference", ...)` and nothing is written. So the literal claim in the question — "do both sides
  reference already-registered phenomena/operations" — is mechanically guaranteed for every row
  that reaches the attestation stage; it is not actually gated by human attestation at all, despite
  `enforced_by` being NULL. What the check is *actually* doing useful work on is the question's
  second half — "not licence to narrate a pattern across the whole passage as if it were a
  linkage" — which is a genuine judgement about whether the connection is real, not just that the
  IDs exist. That half has no DB-checkable counterpart. **Net: correctly excluded from mechanical
  enforcement, but the `test_kind=existence` label is misleading** — it should read
  `reasonableness` (or the question text should be split so the existence half is visibly already
  covered by the write path, leaving only the judgement half under this check_key). No behaviour
  gap, but a labeling/documentation inaccuracy worth correcting so a future reader doesn't assume
  (as I did on first pass) that this row is unenforced.
- **`validation-finding-corrected-not-just-logged`** (closing.set) — **GAP, different shape from
  the others.** `closing_set` (`operations.py:1370-1396`) reads `passage_validation_note.corrected`
  straight off the payload (`corrected = 1 if item.get("corrected") else 0`, line 1384) and writes
  it verbatim — nothing checks that a `corrected=1` claim is actually backed by a real subsequent
  change. I checked whether this could be verified mechanically today: `phenomenon` and `operation`
  (`PRAGMA table_info`, both tables) have `created_at` but **no `updated_at`/revision timestamp at
  all**, and there is no revision/history table for either (`escalation_history` is the escalation
  system's own audit trail, unrelated to passage content — confirmed by name search across
  `sqlite_master`). So unlike `not-already-excluded` above, this isn't a queryable check sitting
  unused in the current schema — the schema itself doesn't yet track phenomenon/operation edits at
  all, so there is no way, today, to mechanically distinguish "genuinely corrected" from "boolean
  flipped." This is a real, correctly-diagnosed reliance on attestation for now, but it rests on a
  missing capability (change tracking on `phenomenon`/`operation`), not a deliberate design
  choice — worth the researcher's attention as a possible future schema addition, not a quick
  code fix.

## `genuinely-inner-being` (phenomenon.set) — GAP, corrected 2026-08-30

Researcher's challenge (verbatim): *"you say that there is no reason to check that this rule is
applied. And, I also do not see anywhere what would actually be checked, how is inner-being
defined... that is something I specifically asked that the configs should include specific
portions of the prose which defines this, and the prose is the authoritative source for it. So I
assume that the module does not check if a phenomenon is inner being relevant, and would not know
how to do it."* Correct on all counts, verified live:

- `cfg_quality_check`'s schema has no column that could carry or point to a definition
  (`id/step/check_key/question/test_kind/required/enforced_by/ordinal/active`) — the question
  text ("a state, disposition, or characteristic of the HIB's inner life") is a free-standing
  paraphrase, not a citation.
- The authoritative definition already exists, exactly where the researcher asked for it:
  `cfg_prose_concept.inner_being_definition` (`chapter=1`, `section_hint='Defining Inner Being /
  This Inner-Being Programme sections'`, added 2026-08-18 per escalation #714, explicitly
  recorded as *"this pointer to the prose is now the canonical reference, not a restated rule
  text"* superseding the old `wa_rule_registry GR-PROG-002`).
  It is **never read by any code** — grepped the whole app (`iba/app/**/*.py`) for
  `cfg_prose_concept` and `inner_being_definition`; zero hits outside the migration that created
  the row. Not surfaced in `phenomenon_set()`, not referenced by `cfg_quality_check`, not
  referenced by any `cfg_method_rule` row for `phenomenon.set` (checked every row for that step:
  `phase-separation`, `hidden-behind-act`, `warrant-required`, `not-literary-pattern`,
  `control-total`, `silence-is-a-finding`, `hib-first-traversal`, `hib-still-warranted`,
  `full-lexical-weight-in-description` — none defines "inner being").

**Net: the module does not check whether a phenomenon is inner-being-relevant in any sense — not
mechanically (expected; a semantic reading call, same as the other 8 reasonableness checks) and
not by ensuring the call is even made against the live authoritative definition (not expected —
the definition row exists for exactly this purpose and is orphaned).** This is a real,
correctable config-completeness gap, distinct from — and worse than — the "no mechanical check"
finding that correctly clears the other 8 reasonableness rows.

## Recommendation

Three items worth an escalation (folded into #1235), each narrower than "re-open the whole
`cfg_quality_check` table":

0. **(Priority — the researcher-caught error)** Wire `genuinely-inner-being` to
   `cfg_prose_concept.inner_being_definition`: at minimum, surface the definition's text/section
   to whoever performs the attestation at the point `phenomenon_set()` requires it (so the
   judgement is made against the canonical Chapter 1 definition, not free recall of the question's
   own paraphrase). The same weaker-form gap applies to `is-genuinely-human`'s "as Step 1 defines
   it" (real text exists in `cfg_method_rule.non-human-scope`/`presumptive-candidate`, but nothing
   formally links check_key → rule_key either) — worth the same fix, not a separate escalation.

1. Add a floor-level mechanical check to `hib_set()` for `not-already-excluded`: when an incoming
   HIB label matches one that has a live `operation.decision='set_aside'` elsewhere in the book,
   surface it (as a `problems`-list flag alongside the existing reconciliation problems, not a
   silent block) so the human attestation is checking a flagged case, not blind free recall.
2. Correct `linkage-genuinely-registered`'s `test_kind` from `existence` to `reasonableness` (a
   `cfg_quality_check` config-content fix via `configmaint.propose`, since the referential half is
   already provably enforced elsewhere and the row's label currently overstates what it's gating).

`validation-finding-corrected-not-just-logged` is flagged for awareness (no schema exists yet to
act on) rather than proposed as an immediate fix — extending `phenomenon`/`operation` with change
tracking is a design decision, not a standards violation to just correct.
