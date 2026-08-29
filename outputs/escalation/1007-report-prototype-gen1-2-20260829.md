# Report prototype — Gen 1:2 (real data, not a mockup)

Built to react to, per your instruction — this is what "verse text + findings + lexical" for one
real, ordinary verse actually looks like with the current data. Two things came out of building
it that matter more than the layout question itself; both are flagged inline below.

---

## Gen 1:2

> The earth was without form and void, and darkness was over the face of the deep. And the Spirit
> of God was hovering over the face of the waters.

### Findings linked to this verse (16 total — all of them, not a sample)

| id | provenance | text |
|---|---|---|
| 179332 | l2_mechanical | impure, unclean; lewd; foul; evil |
| 179333 | l2_mechanical | QUALITY |
| 179334 | l2_mechanical | n/a (noun) |
| 179335 | l2_mechanical | located here |
| 179336 | l2_mechanical | pneuma(M25) |
| 214389 | l2_mechanical | wind, breath, things which are commonly perceived as having no material substance |
| 214390 | l2_mechanical | STATUS |
| 214391 | l2_mechanical | n/a (noun) |
| 214392 | l2_mechanical | located here |
| 214393 | l2_mechanical | akathartos(M10c) |
| 472014 | l2_meaning | In Mar 7:25, akathartos ("unclean") carries the sense "unclean", functioning as a quality, in Greek adjective form, located in the spirit, engaging the perception faculty, combining with pneuma(M25). |
| 483437 | l2_meaning | In Mar 7:25, pneuma ("spirit/breath: breath") carries the sense "spirit/breath: spirit", functioning as a status, in Greek noun form, located in the spirit, engaging the perception faculty, combining with akathartos(M10c). |
| 1006211 | l2_meaning | In Mar 7:25, akathartos ("unclean") carries the sense "unclean", as a quality, in Greek adjective form, located in the spirit, borne by other, operating by had (G2192), acting on spirit (spiritual-being), [cause: UNRESOLVED], combining with pneuma "spirit/breath: breath" — co-seated. |
| 1006212 | l2_meaning | In Mar 7:25, pneuma ("spirit/breath: breath") carries the sense "spirit", as a status, in Greek noun form, located in the spirit, borne by other, engaging the cognition, perception faculty, operating by had (G2192), acting on unclean, [cause: UNRESOLVED], combining with akathartos "unclean" — partner. |
| 1038998 | l2_meaning | In Mar 7:25, akathartos ("unclean") carries the sense "unclean", as a quality, in Greek adjective form, located in the spirit, borne by other, operating by had (G2192), describing spirit, acting on spirit (spiritual-being), in order to feet, [cause: UNRESOLVED], combining with pneuma "spirit/breath: breath" — co-seated. |
| 1038999 | l2_meaning | In Mar 7:25, pneuma ("spirit/breath: breath") carries the sense "spirit", as a status, in Greek noun form, located in the spirit, borne by other, engaging the affect, cognition, perception, volition faculty, operating by had (G2192), acting on unclean, in order to feet, [cause: UNRESOLVED], combining with akathartos "unclean" — partner. |

### `report.verse_lexical` reading for this verse

| # | surface | reading |
|---|---|---|
| 3 | void | H0922 [content]: void — emptiness, void, waste + H9002 [function]: and |
| 4 | darkness | H2822 [content]: darkness — darkness, obscurity; secret place + H9002 [function]: and |
| 8 | Spirit | H7307G [content]: spirit — wind, breath, mind, spirit... *(full entry is a genuine paragraph, ~900 characters, omitted here — see the real §206 Gen 1:1-5 output already sent you)* |
| 9 | God | H0430G [content]: God — *(full entry ~1,900 characters — the divine-name catalogue alone)* |

---

## Two things this surfaced

**1. The density question you asked about is real and severe.** One ordinary verse: 16 findings
(most one-line fragments) + a lexical reading where 2 of 14 codes alone run to ~2,800 characters
combined. Multiply by a passage of any length and a naive "show everything" report is unreadable —
your instinct was right.

**2. Something bigger, found while building this — not a density problem, a correctness one.**
**Every one of the 6 `l2_meaning` findings above is about Mark 7:25** ("unclean spirit," Greek
πνεῦμα ἀκάθαρτον) — **not Gen 1:2** (Hebrew, an entirely different verse, different Testament,
different language, no Greek word could occur here at all). Checked at scale, not just this one
verse: **93% of a random 300-row sample of `l2_meaning` findings cite a different verse in their
own text than the verse they're structurally linked to.** This isn't new corruption from today's
migration — `finding.verse_context_id` (the source I read from) already carried this mismatch;
today's work faithfully carried it forward into `finding_verse_index`, unnoticed until building
this exact prototype exposed it. It also directly bears on #1041's still-open question: if the
"verse" a finding is linked to often isn't the verse its own content is about, showing verse text
next to finding text can be actively misleading, not just verbose.

**Not yet investigated:** why this mismatch exists at this scale — a real question for you, likely
tied to how `verse_context`/XREF term-sharing worked, before the report design goes further.
