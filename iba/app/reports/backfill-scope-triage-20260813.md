# Bringing backfill into scope: what the 3 examples actually showed, and a triage framework

> Ad hoc, outside-structured-operations investigation, follow-on from the multi-strong span
> exercise, 2026-08-13. Read-only except where noted. `iba.db` = `iba/app/db/iba.db`.

Your read of the 3 examples: 4 different actions needed. Checked each against the DB and the
actual pipeline code (`iba/app/lib/strongreconcile.py`) rather than reasoning about it from memory.

## 1. Circumcision — confirmed, genuine gap

`G4061` (circumcision, 40), `G0203` (uncircumcision, 34), `G4059` (to circumcise, 52), `G0564`
(uncircumcised, 33) — all four `origin='backfill'`, **zero cluster tag, zero `word_registry`
entry**. Not a partial gap — this concept has no foothold in the study at all right now despite
being a substantive covenant/purity concept, not an incidental modifier. This is the one of the
four that's unambiguous: it needs full term onboarding (`New-Word.ps1 -Word circumcision -Source
"..."`), the same pipeline any of the 214 words goes through, not a cluster-tag shortcut.

## 2. The STEP/Gal 5:6 claim — checked, and it isn't a data-integrity issue

Called the actual endpoint the app's pipeline uses (`Step.call3_strong`, the governed
`rest/search/masterSearch/strong=...` route — the same one `raw.py:verses_one()` calls when
promoting a code) live against G0203: **17 verses returned, `Gal.5.6` is among them.** The raw
per-verse STEP tagging already in our DB (`verse.preview`'s reverse-interlinear HTML) also tags
`strong='G0203'` at "uncircumcision" in that verse — both our own data and the live concordance
search agree.

What's actually inconsistent is a *different* STEP surface: `Step.call2_getInfo` (the vocab/
dictionary lookup — `rest/module/getInfo/...`) returns a `mediumDef` prose entry that only cites
**two** illustrative references ("Rom. 4:10", "Rom. 4:9") as *examples in the dictionary gloss*,
not a verse list at all — that's almost certainly what looked like "Gal 5:6 missing." Recorded
here so it isn't re-investigated as a bug: **the pipeline's own source of truth for a Strong's
code's verses is `call3_strong`, and it's correct.** If a manual STEP-website check produced a
different impression, it was likely the dictionary-entry page, not the concordance search.

## 3. G0240 "one another" → M44 — real rule gap, not yet resolvable through the standard path

Read `strongreconcile.reconcile()` end to end rather than guessing at the mechanism. The actual
rule (`_word_optional_clusters`, `cfg_setting cluster.assign.word_optional_clusters` = `["T2",
"T3"]`, researcher correction 2026-08-12):

- A backfill code classified into **T2 only** → tagged, never promoted to `word` origin. Stays
  backfill forever, by design.
- A backfill code classified into **T3** (even T3-only) → promoted straight through, **no
  `word_strong` link required** — "T3 is inherently not word-specific" (your own words, quoted in
  the code comment).
- A backfill code classified into **any real M-cluster or FLAG** → requires a `word_strong` link
  (i.e. correlation to an actually-registered word) before it's allowed to promote. No link →
  `reconcile()` returns `exception: no-word` and **refuses**, leaving the code exactly as-is.

Your read of G0240 is exactly this case: thematically it's M44 (Relational Disposition — a
reciprocal pronoun, "one another"), but it doesn't naturally correlate to any single registered
word the way a content noun/verb does — it rides along with whatever verb is in view (love one
another, forgive one another, serve one another...), which is structurally the T3 pattern, not
the M-cluster pattern. Tag it M44 today and the pipeline will simply refuse to promote it; it'll
sit as a classified-but-inert exception in `cluster.validate`'s backlog indefinitely.

**This is a genuine open policy question, not something to resolve unilaterally.** Three live
options, all mechanically simple once chosen:

- **(a) Widen `word_optional_clusters`** to include M44 specifically (or a small, named set of
  clusters that are reciprocal/relational-marker-shaped by nature) — narrow, precedented (mirrors
  exactly how T3 already got this treatment), but sets a pattern other clusters may later ask for
  too.
- **(b) Give it a word_strong link deliberately** — if M44 already has a natural "home word" (e.g.
  if "one another"/reciprocity is meant to ride under an existing registered relational word),
  add the link by hand rather than changing the rule. Needs checking whether such a word already
  exists in scope for M44.
- **(c) Leave M44-bound reciprocal markers as classified-but-backfill** (tagged for the
  co-occurrence/reading value, never promoted) — accepts they stay second-class data forever,
  simplest but means M44's own coverage picture is permanently incomplete for this class of word.

## 4. G0166 "eternal" → T2 — not actually an open question, just an action

You reclassified this away from my earlier speculative M25 read, and the DB backs you up: T2
already holds `H5769G` "forever: enduring" and `G0165H` "an age: eternity" — both time/duration
qualifiers, both already correctly `does not denote inner being → T2 (F2)`. G0166 is the same
semantic class (a duration-adjective, not the "life" it modifies). This one just needs the tag —
no policy question attached, unlike #3.

## 5. What the 3-examples-4-actions result actually means: a triage taxonomy

Every backfill content strong that gets looked at from here needs one question answered before
any action: **what kind of gap is this?**

| type | signature | action | mechanical consequence |
| --- | --- | --- | --- |
| **1. Missing term** | a substantive concept with no `word_registry` entry at all, not just no cluster tag (circumcision) | `New-Word.ps1` — full onboarding | brings in the whole Strong's family, goes through the normal word-study pipeline |
| **2. Plain T2 qualifier** | generic modifier/quality word, no inner-being content of its own, usually with existing T2 precedent to match against (eternal) | direct `cluster_strong` tag, `cluster_code='T2'` | tag only — **never promotes** to `word` origin (reconcile's own rule) |
| **3. Plain T3 operation** | generic verb/action, not tied to one theme | direct `cluster_strong` tag, `cluster_code='T3'` | tag **and automatic promotion** — no word link needed, but does trigger a real STEP verse-fetch cascade, unlike type 2 |
| **4. M-cluster-thematic, word-independent** | genuinely fits a specific M-cluster's theme, but rides along with other words rather than being its own content word (one another) | **policy decision first** (§3's three options), then act | blocked by `reconcile()` until the policy question is settled — don't tag-and-walk-away, it'll just sit as a silent exception |

Types 2 and 3 are mechanical once identified — same shape as the T2/T3 relocation work already
done this session. Types 1 and 4 both need a judgement call before any DB write: type 1 asks "is
this substantive enough to deserve its own word study", type 4 asks "should the promotion rule's
scope widen, or does this word-class just stay backfill forever." Recommend triaging into these
four buckets *before* batching any actual relocation work, the same way the M10b/M10c and T2/T3
phases separated "clear, act now" from "judgement call, ask first."

## 6. Not yet done

No DB writes this pass — purely diagnostic. §3's policy question is the one item needing your
decision before backfill-clustering work can proceed at any real volume; §1 (circumcision) can
start independently whenever you want it onboarded.
