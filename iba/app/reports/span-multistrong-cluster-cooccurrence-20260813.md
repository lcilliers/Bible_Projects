# Multi-strong spans → cluster co-occurrence: a new lens on cross-cluster association

> Ad hoc, outside-structured-operations investigation, per researcher idea 2026-08-13: *"extract
> from span (or the lexicals) all the spans with multi strongs, then map this to the clusters of
> each strong — this should create a new perspective on the associations of the strongs in
> different clusters."* Read-only — no DB writes. `iba.db` = `iba/app/db/iba.db`.

## 1. The data

`verse_lexical` (deleted=0, 540,563 live rows) carries one row per (span, Strong's code) —
370,741 `role='content'` (real lexical content) + 169,822 `role='function'` (bound grammatical
morphemes: prepositions, articles, pronominal suffixes). A **span** is one surface word/phrase
unit; most map to exactly one content Strong's code, but **31,653 spans carry 2 or more distinct
content-role Strong's codes** — compound Hebrew constructs, construct chains ("heart of X"),
idioms rendered as one English surface form from two Hebrew lexemes, etc. Those are the "multi
strongs" the idea points at.

## 2. A methodological trap, caught before reporting it

**First pass, naive:** for each multi-strong span, take the union of every content strong's
cluster tag(s) and count all pairs. Top result: **M03 (Grief) ↔ M27 (Evil): 28**, M29 (Desire) ↔
M30 (Obedience): 12, M04 (Joy) ↔ M08 (Pride): 7 — looked like a real finding.

**It wasn't, mostly.** `cluster_strong` allows a single Strong's code to carry more than one
cluster tag (e.g. `H7451I` "distress: evil" is tagged both **M03 and M27** — see the M10b/M10c
review's homonym-risk notes). The naive count doesn't distinguish "two *different* Strong's codes
in this span, one M03 one M27" from "one dual-tagged Strong's code, alone in the span, trivially
producing the pair M03×M27 against itself." Checking: `H7451I → {M03, M27}` and every one of the
"M03↔M27" example spans turned out to be a single occurrence of `H7451I` plus an untagged function
word (`H0853` "[Obj.]", `H0413` "to[wards]"). Same story for `H0014` "be willing" (tagged both
**M29 and M30**) driving the whole M29↔M30 result. **Fixed**: cross-cluster pairs now only counted
when they come from **two distinct Strong's codes** in the same span, each contributing its own
cluster tag(s). Under the fix, M03↔M27, M29↔M30, and M04↔M08 all but disappear — they were an
artifact of the tagging scheme, not a textual association. Recorded here so the mistake doesn't
get re-made if this is re-run.

## 3. Corrected same-cluster cohesion — two *different* words, same span, same cluster

| cluster | doublets |
| --- | --- |
| T2 | 7,429 |
| T3 | 357 |
| **M05 Love** | **8** |
| M15 Wisdom, M25 Life, M03 Grief | 4 each |
| M36 Service | 2 |
| M06, M02, M10, M04, M01, M42, M29, M28 | 1 each |

T2/T3 dominate as expected (generic vocabulary compounds readily). Among the M-clusters, real
emphatic/idiomatic doublets are rare but genuine — e.g.:

- **M03 (Grief), Isa 38:3 / 2Ki 20:3 / Judg 21:2 / Jer 48:32** — "wept" = `H1058` (to weep) +
  `H1065` (weeping), the same root doubled for emphasis ("wept bitterly").
- **M05 (Love), Deu 10:17 / Pro 6:35 / Mal 2:9 / Deu 28:50** — "partial"/"accept"/"respect" all
  render the *same* idiom: `H5375Q` "to lift: kindness" + `H6440N` "face: kindness" — "to lift the
  face" = show favour/partiality. One idiom, four English surface forms, correctly recognised as
  the same M05 doublet each time.
- **M25 (Life)** — `H2416E`+`H2421` ("life"+"to live"), `H2421`+`H5315H` ("to live"+"soul: life") —
  the expected cognate-doubling pattern for a "life" theme.

## 4. Corrected cross-cluster pairs (excluding T2/T3/FLAG)

| pair | spans | reading |
| --- | --- | --- |
| **M15 Wisdom ↔ M47 Constitution** | **19** | by far the strongest genuine M–M pairing |
| M25 Life ↔ M47, M23 Strength ↔ M47 | 5 each | |
| M24 Weakness ↔ M47, M28 Envy ↔ M47 | 4 each | |
| M21 Prayer ↔ M33 Peace | 4 | |
| M03 Grief ↔ M47 | 3 | |
| M26 Righteousness ↔ M30 Obedience | 3 | |
| everything else | 1–2 | long tail, plausible but too thin to lean on individually |

**M47 (Constitution: heart/soul/spirit/mind/flesh/conscience) is the hub** — it pairs with more
other clusters than anything else does, at low-but-consistent counts. That tracks with how Hebrew/
Greek actually predicates an inner quality: "heart of X" / "X of soul" construct chains bind
*whatever quality is in view* to one of the seats. M47 isn't a themed cluster competing with the
others so much as the grammatical anchor several of them attach to — worth remembering when reading
M47's own membership list; a lot of it will legitimately co-occur with everything.

**Concrete reads on the two most interesting non-M47 pairs:**

- **M15 ↔ M47** — 1Ki 2:44 "You know in your own **heart**" (`H3045` to know [M15] + `H3824` heart
  [M47]); Job 1:8 / Job 2:3 / 2Sa 18:3 "**considered**"/"**care**" (`H7760K` to set/consider [M15] +
  `H3820A` heart [M47]); Exo 36:1 "every **craftsman** ... wise of **heart**" (`H2450` wise [M15] +
  `H3820A` heart [M47]). Wisdom in this corpus is disproportionately *heart*-wisdom, not
  head/mind-wisdom — a real textural observation, not obvious in advance.
- **M21 (Prayer) ↔ M33 (Peace)** — 1Sa 25:5, 1Sa 17:22, 1Sa 30:21 "**greet(ed)**", 1Ch 18:10
  "**ask about his health**": all four are the same Hebrew idiom, `H7592` "to ask" [M21] + `H7965`
  "peace/well-being" [M33] — *sha'al + shalom*, "ask [of] peace" = "greet". A clean idiom the
  M21/M33 split doesn't currently represent as one unit — it's two clusters' vocabulary standing in
  for one speech-act.
- **M26 (Righteousness) ↔ M30 (Obedience)** — Num 3:38, 2Ki 11:6, 2Ki 11:7 "**guard(ing)**": `H8104`
  "to keep/guard" [M30] + `H4931` "charge" [M26] — *shamar mishmeret*, "keep the charge/duty",
  the standard idiom for faithful cultic/military service.

## 5. Honest scale check

31,653 multi-content-strong spans exist; after removing the dual-tag artifact, the real M–M
cross-cluster signal tops out at **19** spans for the single strongest pair and is single digits
for everything else. This is **texture, not statistics** — real, checkable, individually-readable
associations (every pair above was verified against actual verse text, not inferred from counts
alone), but not yet a large enough sample to encode as a rule or use to justify a cluster merge/
split on its own. What it *is* good for: a reading list. If you want to pursue this, the concrete
next step is reading the M15↔M47 spans (heart-wisdom) and the idiom pairs (M21↔M33, M26↔M30) in
full to see whether they reveal something the current cluster/characteristic model doesn't capture
— that's a researcher judgement call, not one this pass can make for you.

## 6. Follow-up question (researcher, same day): is M47 (Constitution) structurally like T3?

*"It looks like Constitution is not a cluster by itself, but in essence is a 'qualifier' in various
other clusters — is Constitution something similar to T3 (but not T3 itself)?"*

Tested directly rather than answered from impression. For every cluster: its own size (distinct
strongs), how often two of its *own* members double up in one span (§3's cohesion metric), how many
*different other* clusters it pairs with, and its total cross-cluster span count.

| cluster | size | own-doublets | distinct partners | total cross-pair spans | partners ÷ size |
| --- | --- | --- | --- | --- | --- |
| T2 | 1,961 | 7,429 | 49 | 7,923 | 0.025 |
| T3 | 764 | 357 | 45 | 3,737 | 0.059 |
| M24 | 167 | 0 | 10 | 276 | 0.060 |
| M23 | 166 | 0 | 14 | 307 | 0.084 |
| M15 | 152 | 4 | 11 | 647 | 0.072 |
| **M47** | **37** | **0** | **19** | **426** | **0.51** |
| (all other M-clusters) | 18–151 | 0–8 | 1–14 | 3–307 | 0.02–0.18 |

**Confirmed, and more pronounced than the hypothesis:** M47 is the smallest kind of cluster (37
members — comparable to M25's 30 or M29's 40) but has **more distinct cross-cluster partners (19)
than any other M-cluster**, including ones 4–5× its size (M23 at 166 members manages only 14
partners; M24 at 167 manages 10). Its **own-doublet count is zero** — no two M47 words (heart+soul,
spirit+flesh, etc.) were found paired with each other in this corpus at all — meaning M47 shows no
self-reinforcing thematic cohesion the way M05 (Love, 8 doublets), M15 (Wisdom, 4), M25 (Life, 4),
and M03 (Grief, 4) do. And on a **per-member basis**, M47 connects to other clusters at **8–20×**
the rate of T2 or T3 themselves (0.51 vs 0.025/0.059) — M47 is structurally *more* hub-like than
the two categories explicitly defined as "not tied to one cluster."

**So: yes, but not literally T3 — a different half of the same phenomenon.** T3's own definition
already says it: *"a strong considered as a human operation/movement, not tied to one inner-being
cluster; context may pair the operation with a specific cluster."* T3 is the **verb** side of that —
generic actions that other clusters' themes get enacted *through*. M47 is the **noun** side — the
seats/faculties (heart, soul, spirit, mind, flesh, conscience) that other clusters' qualities get
*predicated of*, via the construct-chain idiom this report keeps surfacing ("wise of **heart**",
"bitter of **soul**", "strong of **heart**", every §4 M47 example). Both are cross-cutting carrier
categories rather than standalone content-themes at the same level as Fear/Anger/Love — they just
carry different parts of speech.

**Where this leaves an open question, not a conclusion:** T2/T3 exist precisely to hold vocabulary
that *isn't* inner-being-specific. M47 is the opposite case — its vocabulary (heart/soul/spirit/
mind/flesh/conscience) is arguably the single most central naming of the inner being the whole
programme studies, which is a real reason it might belong as its own top-level category rather
than being folded into a T-style utility bucket. Whether that argues for restructuring M47 (a new
T-style "seats/faculties" category, structurally parallel to T3 but for nouns) or for leaving it
exactly as it is *because* of that centrality is a call this data can inform but not make — flagging
it as an open item, not resolving it here.

## 7. Not yet done

This was run as a one-off script, not built into `report.cluster` or any other registered app
step — no code change, no `BUILD.md` entry, nothing persisted to the app itself. If this lens
turns out to be worth returning to regularly (e.g. re-run after every cluster-relocation phase to
see how the co-occurrence picture shifts), it's a candidate for a proper `report.*` step later —
flagging that as a possible follow-up, not doing it now.
