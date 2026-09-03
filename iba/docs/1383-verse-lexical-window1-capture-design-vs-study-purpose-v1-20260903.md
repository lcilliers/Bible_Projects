# Verse-lexical Window 1 — what must be captured, checked against the study's actual purpose

**Filename:** 1383-verse-lexical-window1-capture-design-vs-study-purpose-v1-20260903.md
**Escalation:** #1383
**The question this answers, verbatim (researcher):** the lexical result is building blocks for
the study's main question — how does the inner being work, what does it consist of, what does it
do, as reflected by scripture. How must the result be captured; what must be captured; is anything
missing to sensibly dig in at every level.
**Method:** not assumed — checked against the LIVE Window 2 mechanism (`hib`/`phenomenon`/
`operation`/`operation_party`, and their governing `cfg_method_rule` rows), since that is the actual
place the study's central questions get answered today. Window 1's job is only sensible in relation
to what Window 2 actually needs from it.

---

## 1. Window 1 already IS the building block, today — the alignment is real, not aspirational

`phenomenon.set`'s own live governing rule (`hib-first-traversal`) instructs: "read every verse
that HIB appears in against **its own `verse_lexical` row (full range, not the story or the printed
gloss)**." This is not a future intention — it is the CURRENT operating rule for the study's Window
2 analysis. Window 1's whole reason for existing is already load-bearing, live, not something
#1383 is proposing into existence.

Checked directly, item by item, whether what Window 1 already plans to capture supplies what Window
2's own rules say they need:

| What Window 2 needs (from its own live `cfg_method_rule` rows) | Window 1 checklist item that supplies it |
|---|---|
| Who is acting/undergoing/speaking/named (`hib.set/presumptive-candidate`) | Entity-linking / subject-of-record; pronoun resolution |
| A pronoun/party genuinely ambiguous, every live reading enumerated (`hib.set/referent-crux-resolution`) | Pronoun test's own `unresolved` discipline — already built for exactly this handoff |
| Process = state, or movement (come/go/impact/emerge/become) (`operation.set/four-parts`) | Chain/sequencing; verb triggered-by/impacts |
| Source vs. target of an operation, kept distinct from mere enablement (`operation.set/source-vs-enablement`) | Noun — relational/addressee classification; entity-linking |
| Full lexical weight of the governing word, this exact context (`phenomenon.set/full-lexical-weight-in-description`) | `resolved_sense` (T1-3 baseline) — **see §5, a real open question found here, not assumed sound** |

**This alignment is good.** The concern isn't that Window 1 is capturing the wrong things — it's
that what it captures isn't yet *connected*, structurally, to where Window 2 would use it.

## 2. Self-correction: HIB candidacy is not "which words are inner-being content"

Before checking the live rules, my working assumption was that #1378's own named gap ("no
mechanism marks which words in a verse are inner-being-related") meant Window 1 needed a new
per-code relevance FLAG. **Checked against `hib.set/presumptive-candidate` directly: wrong.** HIB
candidacy is about named/implicit *parties* in the text ("every human mentioned... anyone who acts,
undergoes an act, thinks, speaks, refrains from acting, or is simply named as present"), not about
tagging which lexical items carry inner-being *content*. Window 1's existing entity-linking and
pronoun-resolution items already supply exactly that raw material (who's present, who the pronouns
resolve to). **No new flag needed on this specific point** — recorded here so the earlier framing
doesn't quietly stand as if it were still the live read.

## 3. The real structural gap: no link from Window 2's record back to a specific Window 1 finding

Checked live: `phenomenon.textual_warrant` and `operation.observation_text`/`description_text` are
plain `TEXT` columns. `operation_party` links structurally to `hib_id` when a party IS a HIB, but
has no equivalent link to `span`/`verse_lexical`/`verse_lexical_note` at all. **So even though the
governing rule says "read against verse_lexical's full range," nothing in the schema records WHICH
verse_lexical row (which code, which finding) actually warranted a given phenomenon or operation —
the warrant is restated in prose, not pointed at.** This is the actual gap "how must the result be
captured" is asking about: Window 1 producing rich per-code findings only serves as *building
blocks* if Window 2's own records can point back at them, not just describe the same thing again in
free text. Recommendation, not decided here: `verse_lexical_note` (once built) should be
FK-referenceable from `phenomenon`/`operation`, at minimum an optional pointer alongside the
existing free-text field (matching the precedent already set by `operation_party.hib_id` — a real
structural link added alongside, not instead of, its own free-text `detail`).

## 4. Completeness — borrow the mechanism Window 2 already proved, don't reinvent one

`phenomenon.set/control-total` already solves, for Window 2, exactly the completeness problem this
session's drift-mitigation plan solved for Window 1 independently: "every HIB crossed with every
verse it appears in... equals the exact number of phenomena-register entries... known in advance,
not dependent on trusting the pass to remember." **Window 1's own mechanical-layer completeness
guarantee (§2 of the drift-mitigation plan) should be described in these same terms** — every code
in a passage × every mechanical check = a known, checkable total, not just "run every check and
trust it happened." Same pattern, not a new invention — worth stating explicitly so the two windows
share one completeness discipline, not two accidentally-different ones.

## 5. Something genuinely missing, found while checking this — not fixed here, flagged

`lib/lexical.py` is written to resolve `resolved_sense` from `strong_meaning_parsed` (a narrowed,
context-appropriate sense), **falling back to the flat `stepGloss` dump only when no parsed-sense
match is found** (confirmed live in the code, line ~177). Checked against every code pulled across
this whole validation run (all 5 passages, 19 verses, ~140 codes): **every single `resolved_sense`
value was the flat `stepGloss:` fallback form — not one narrowed sense was observed.** This may be
coincidence in a 19-verse sample, or it may mean the parsed-sense match is failing far more often
than intended, live, at scale. Directly relevant to "what must be captured": `resolved_sense` is
supposed to BE the word-sense-disambiguation Window 2's `full-lexical-weight-in-description` rule
depends on — if it's silently falling back to the unresolved full gloss everywhere, Window 1 hasn't
actually been doing that job. **Not investigated further here** (out of this document's own scope,
and worth its own focused check rather than a guess) — flagged plainly as a real open thread, not
buried in a footnote.

## 6. #1443 (recurring verse-structure findings) — resolved by direct precedent, not left open

`phenomenon.set/not-literary-pattern` already answers this, for Window 2: "A genuine literary/
structural/genre observation is not a phenomenon — log it once as an emergent question (Step 7)
instead, never built into the phenomena register." **Recommend the same disposition for Window
1**: merism/chiasm/antithetic-parallelism/paired-image findings are not a `verse_lexical_note`
`note_type` — they go into an analogous lightweight "emergent question" log, the same shape Window
2 already uses, not forced into the per-code structured record. This is a recommendation for your
confirmation, not applied — but it is grounded in existing, live, working precedent, not invented
fresh.

## 7. Answers to the three questions, stated plainly

- **How must the result be captured?** Structurally linked to Window 2's own records (§3), using
  the same completeness discipline Window 2 already proved works (§4) — not a richer free-text
  description, a real FK.
- **What must be captured?** What Window 1 already plans to capture (chain, connective, entity-
  link, relational/severity noun classification, pronoun resolution, related words) already maps
  onto what Window 2's live rules need (§1) — the content list itself is sound. The one addition
  this check surfaced is the link (§3), not new checklist items. Literary/structural findings
  explicitly do NOT belong in this record (§6, by precedent).
- **Is anything missing?** Two real things, both named here for the first time with evidence: the
  FK link (§3), and the `resolved_sense` fallback question (§5) — worth checking before this is
  treated as build-ready, since it bears on whether Window 1's baseline output is actually doing
  its own stated job.

## 8. Open items for your decision — nothing here applied unilaterally

1. Add the `verse_lexical_note` → `phenomenon`/`operation` FK link now (schema-design stage,
   before any table is built) — or leave it for a later increment once Window 2 integration is
   actually being built?
2. Confirm #1443's disposition (structural findings → emergent-question log, by precedent) —
   or is there a reason Window 1 should diverge from Window 2's own pattern here?
3. `resolved_sense` fallback rate — worth a dedicated live check before build, or fold into the
   Layer-1 mechanical-facts work already proposed in the drift-mitigation plan?
