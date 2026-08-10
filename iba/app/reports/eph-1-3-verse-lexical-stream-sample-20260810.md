# Eph 1:3 — lexical-stream sample (new report design, for inspection)

> One-off preview, not yet a built report. Requested: a new report type to sit alongside each
> word-registry report (e.g. `blessing-strong-span-v1-20260809.md`) that, for a verse the
> registry's linked Strong's occur in, shows the **verse text with only the linked-Strong's
> word(s) swapped for their lexicon meaning** — every other word in the verse stays as ordinary
> text. Not a full-verse interlinear stream (that was v1/v2, superseded — this instruction: "only
> the span for the strongs that is included in the related word, not all the other spans").
>
> Gloss source: `strong_meaning_parsed`, `sort=0`/`row_type='description'` row (the general
> definition) per matched Strong's — same source as the prior revision, per the earlier
> instruction to use `strong_meaning_parsed`, not `strong.stepGloss`.

## 1. Which spans in this verse are in scope

Registry: **blessing** (`word_registry.id=158`). Linked Strong's (`word_strong`, 20 total):
G1757, G2036, G2127, G2128, G2129, G3106, G3107, G3108, G5485, G5486, G5487, G6050, G8231, H0833,
H0835, H1288, H1289, H1293, H1926, H3190.

`span` for `Eph.1.3` has 18 spans total; only **3** carry a `strong_variant` in that linked set —
every other span (God, and, Father, our, Lord, Jesus, Christ ×2, us, in ×3, with, every,
spiritual, heavenly places) is left untouched:

| pos | surface | strong | in linked set? |
| --- | --- | --- | --- |
| 0 | Blessed | G2128 | **yes** |
| 8 | blessed | G2127 | **yes** |
| 15 | blessing | G2129 | **yes** |
| (all other 15 positions) | — | — | no — unchanged in the rendering below |

## 2. Actual verse text (ESV, as stored, for reference)

> Blessed be the God and Father of our Lord Jesus Christ, who has blessed us in Christ with every
> spiritual blessing in the heavenly places,

## 3. Rendered — only the linked-Strong's words replaced/annotated

> **Blessed** [G2128: worthy of being praised, blessed, or commendedpraiseworthy] be the God and
> Father of our Lord Jesus Christ, who has **blessed** [G2127: to praise, give thanks to, speak
> well of, extol; ( passive ) to be blessed, receive blessing; in some contexts, to give a
> blessing is to act kindly and impart benefits to the one being blessed] us in Christ with every
> spiritual **blessing** [G2129: glibness, fluency of speech ; praise and blessing] in the
> heavenly places,

Built by locating each matched span's `surface` text at its position in the original verse
string (matches taken left-to-right, non-overlapping) and substituting `**surface** [strong:
gloss]` at that exact span — everything else in the string is untouched byte-for-byte.

## 4. Detail for the 3 matched spans only

| pos | surface | strong | morph | `strong_meaning_parsed` (sort=0, general definition) |
| --- | --- | --- | --- | --- |
| 0 | Blessed | G2128 | A-NSM | worthy of being praised, blessed, or commendedpraiseworthy |
| 8 | blessed | G2127 | V-AAP-NSM | to praise, give thanks to, speak well of, extol; ( passive ) to be blessed, receive blessing; in some contexts, to give a blessing is to act kindly and impart benefits to the one being blessed |
| 15 | blessing | G2129 | N-DSF | glibness, fluency of speech ; praise and blessing |

## Open questions still standing before this becomes a built, per-word report

1. **Scope of "alongside each word report"** — one such file per verse the registry's linked
   Strong's occur in (this would mean ~one file per verse across `blessing`'s 20 Strong's ×
   however many verses each occurs in), or one file per registry with every verse listed inside
   it (matching the existing `-strong-span-` report's per-registry shape)?
2. **Inline annotation form** — `**surface** [strong: gloss]` as shown, vs. a footnote-style
   marker with the gloss listed separately below the verse, vs. replacing the surface word
   outright rather than annotating alongside it?
3. **Multiple senses** — §3 uses only the `sort=0` general definition per matched word (same as
   the detail table). Full sense breakdown (all `strong_meaning_parsed` rows) would be far longer
   inline — keep it out of the inline rendering and reserve it for the detail section, as here?
4. **Collision handling** — this verse's 3 matches are single, non-overlapping surface words with
   no repeats of the exact-case string elsewhere in the verse, so plain substring matching was
   safe. A verse where the same word-form both is and isn't a linked-Strong's occurrence (e.g. two
   different Greek words both surfacing as "blessed") would need position-based matching off
   `span.position`/offsets, not surface-text search — worth building that way from the start
   rather than patching it in later.

No code changes made yet — this is a data preview only, built directly against
`span`/`strong_meaning_parsed`/`word_strong` for Eph 1:3, to get your read before this becomes a
real report tool.
