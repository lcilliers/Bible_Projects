# What T1-T3 completeness actually changes — two real spans, Dan 8:1

Source: `iba/app/verse-analysis/Daniel/dan-8-1-27-verse-span-meaning.md`, verbatim rows. Same
underlying DB data both times — nothing added that isn't already in `span`/`strong`/
`strong_meaning_parsed`. The only thing that changes is whether the extract *uses* what it already
fetched.

## Example 1 — a verb where morph is fetched but never applied (T3)

**Span:** position 6, surface `appeared`, `strong = H7200G`, `morph_code = HVNp3ms`.

**Today's row, verbatim:**

> stepGloss: to see: see <br> meaning_tree (base H7200 fallback): to see, look at, inspect,
> perceive, consider; (Qal); to see; to see, perceive; to see, have vision; to look at, see,
> regard, look after, see after, learn about, observe, watch, look upon, look out, find out; to
> see, observe, consider, look at, give attention to, discern, distinguish; to look at, gaze at;
> to provide, choose; (Niphal); to appear, present oneself; to be seen; to be visible; (Pual) to
> be seen; (Hiphil); to cause to see, show; to cause to look intently at, behold, cause to gaze
> at; (Hophal); to be caused to see, be shown; to be exhibited to; (Hithpael) to look at each
> other, face

That's the entire verb's paradigm across six stems (Qal/Niphal/Pual/Hiphil/Hophal/Hithpael) dumped
as one undifferentiated string. `morph_code` (`HVNp3ms` — **H**ebrew **V**erb, **N**iphal,
**p**articiple, **3ms**) was fetched (it's the 4th column) and never used to pick the one
applicable stem. A reader has to visually scan the whole blob, find the `(Niphal)` marker inside
it, and extract the ~13 words that actually apply — for every single occurrence of this verb, and
there are three more in this same chapter (Dan 8:1 row 11, 8:2 rows 0/2/9).

**What the T1-T3 record would hold instead** (mechanical: `strong_meaning_tree`'s own text already
segments by stem — `(Qal)...(Niphal)...(Pual)...` — this is a parse against morph, not a judgment):

> **H7200G, Niphal participle (3ms):** to appear, present oneself; to be seen; to be visible.

Same source data. The difference is that "which sense applies to *this* occurrence" — a fact
`morph_code` already settles — is now stated, not left for every reader to re-derive by hand, every
time, from a six-stem paragraph.

## Example 2 — a compound span presented as two unrelated entries (T1)

**Span:** position 3, surface `King`, `strong_variant = "H4428G H9009"`, `morph_code = "HNcmsa
HTd"` (noun + definite-article prefix — one grammatical unit, not two words).

**Today's row, verbatim:**

> **H4428G**: stepGloss: king <br> meaning_tree (base H4428 fallback): king; Aramaic equivalent:
> me.lekh... <br> **H9009**: stepGloss: [the] <br> meaning_tree (variant H9009): Prefix hé
> article: "the" for a subject, not object

Two bulleted dictionary entries, exactly as unconnected as the `G1722 G0505` ("genuine") case
looked at earlier this session — a reader has to notice on their own that `H9009` isn't a separate
word at all, it's the definite article riding on `H4428G`, and that together they mean "the king,"
not "king" + a fragment about grammatical subjects.

**What the T1-T3 record would hold instead:**

> **the king** (H4428G + definite article H9009) — royal-power/reign sense, definite.

## The pattern

Both fixes are the same shape: the extract already fetches everything needed (`morph_code`,
`strong_variant`'s component codes, the stem-segmented `strong_meaning_tree` text) — it just never
closes the loop between what it fetched and what it renders. Nothing here required a judgment call;
both are grammar facts already sitting in the row. This is what "the routine delivers a complete
T1-T3 record" concretely means: not new data, not interpretation — using the data it already pulls.
