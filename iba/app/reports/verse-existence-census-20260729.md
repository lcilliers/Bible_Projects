# Verse-existence census — full extent of the term-discovery gating gap — 2026-07-29

Follow-on to [`SESSION-LOG-20260729-joel-1-parked-verse-discoverability-assumption.md`](../../logs/SESSION-LOG-20260729-joel-1-parked-verse-discoverability-assumption.md),
which established the mechanism (a `verse` row exists in `iba.db` iff at least one Strong's
number in that verse is a seed strong of some already-onboarded IB study word — see that log for
the config/code trace). This report answers the researcher's next question, in two parts:
**(a)** how many verses across the whole Bible are missing this way, and **(b)** for a sample of
the missing verses per book, is there real inner-being content being silently excluded, or is the
exclusion benign (the verse genuinely has none)?

**Method:** a read-only crawl of the local STEP server (`ESV_th`), one request per chapter (1189
requests total, ~36s), walking `nextChapter.osisKeyId` to find book boundaries. Each response's
plain verse text was diffed against every `osisId` currently in `iba.db`'s `verse` table (29,037
rows, `deleted=0`). No writes to `iba.db`. Raw per-book results (including the full text of every
missing verse) are saved alongside this report:
[`verse-existence-census-20260729.json`](verse-existence-census-20260729.json). Parser validated
against the already-confirmed Joel gap (73 canonical verses, 2 missing — 1:15 and 2:4 — matched
exactly) before running the full crawl. Five single-chapter books (Obad, Phlm, Jude, 2John, 3John)
needed a reference-format correction (STEP resolves `Book.1` to verse 1, not chapter 1, for
one-chapter books; fixed by requesting the bare book name) and were re-run individually.

Caveat on precision: the crawl's parsed total (31,086 canonical verses) is close to but not
identical to the commonly-cited standard count (~31,102) — a ~0.05% discrepancy, almost certainly
from a small number of translation notes/combined-verse edge cases in the HTML parse, not a
systematic error (it reproduced the Joel case exactly and the grand total's "present" count
matches `iba.db`'s actual row count exactly — 29,037 both ways). Fine for the purpose here
(sizing and sampling the gap); would want re-verification before using individual per-book counts
for a precise remediation budget.

---

## (a) Full extent — every book

**Grand total: 2,049 of 31,086 canonical verses (6.59%) have no `verse` row in `iba.db`.**
That's roughly two-thirds of the researcher's ~10% estimate — real, but smaller than guessed, and
**very unevenly distributed** rather than a flat background rate.

| book | total | missing | pct |
|---|---:|---:|---:|
| 1Chr | 942 | 416 | 44.2% |
| Ezra | 280 | 113 | 40.4% |
| Neh | 406 | 126 | 31.0% |
| Josh | 658 | 149 | 22.6% |
| Num | 1288 | 224 | 17.4% |
| Phlm | 25 | 4 | 16.0% |
| Song | 117 | 15 | 12.8% |
| Gen | 1533 | 121 | 7.9% |
| 2John | 13 | 1 | 7.7% |
| Exod | 1213 | 92 | 7.6% |
| Matt | 1067 | 77 | 7.2% |
| Ruth | 85 | 6 | 7.1% |
| Luke | 1149 | 72 | 6.3% |
| Mark | 673 | 40 | 5.9% |
| 2Sam | 695 | 38 | 5.5% |
| Acts | 1003 | 53 | 5.3% |
| Obad | 21 | 1 | 4.8% |
| Dan | 357 | 16 | 4.5% |
| 1Kgs | 816 | 35 | 4.3% |
| 2Chr | 822 | 33 | 4.0% |
| Rev | 404 | 15 | 3.7% |
| 2Tim | 83 | 3 | 3.6% |
| Lev | 859 | 31 | 3.6% |
| Esth | 167 | 6 | 3.6% |
| Amos | 146 | 5 | 3.4% |
| John | 878 | 30 | 3.4% |
| Gal | 149 | 5 | 3.4% |
| Lam | 154 | 5 | 3.2% |
| Judg | 618 | 20 | 3.2% |
| 1Sam | 810 | 26 | 3.2% |
| Ezek | 1273 | 36 | 2.8% |
| 1Cor | 437 | 12 | 2.7% |
| Joel | 73 | 2 | 2.7% |
| Job | 1070 | 29 | 2.7% |
| 1Tim | 113 | 3 | 2.7% |
| Hag | 38 | 1 | 2.6% |
| Prov | 915 | 23 | 2.5% |
| Deut | 959 | 22 | 2.3% |
| Ps | 2461 | 53 | 2.2% |
| Nah | 47 | 1 | 2.1% |
| Col | 95 | 2 | 2.1% |
| Isa | 1292 | 26 | 2.0% |
| Phil | 104 | 2 | 1.9% |
| Mic | 105 | 2 | 1.9% |
| 1Pet | 105 | 2 | 1.9% |
| 1John | 105 | 2 | 1.9% |
| Zech | 211 | 4 | 1.9% |
| Rom | 432 | 8 | 1.9% |
| Mal | 55 | 1 | 1.8% |
| Jer | 1364 | 21 | 1.5% |
| 2Kgs | 719 | 11 | 1.5% |
| Hos | 197 | 3 | 1.5% |
| 1Thess | 89 | 1 | 1.1% |
| 2Cor | 257 | 2 | 0.8% |
| Heb | 303 | 2 | 0.7% |
| Eccl | 222 | 0 | 0.0% |
| Jonah | 48 | 0 | 0.0% |
| Hab | 56 | 0 | 0.0% |
| Zeph | 53 | 0 | 0.0% |
| Eph | 155 | 0 | 0.0% |
| 2Thess | 47 | 0 | 0.0% |
| Titus | 46 | 0 | 0.0% |
| Jas | 108 | 0 | 0.0% |
| 2Pet | 61 | 0 | 0.0% |
| 3John | 15 | 0 | 0.0% |
| Jude | 25 | 0 | 0.0% |

**The gap is concentrated, not uniform.** The five worst books (1 Chronicles, Ezra, Nehemiah,
Joshua, Numbers) account for 1,028 of the 2,049 missing verses — over half the entire Bible-wide
gap — and every one of them is exactly the genre the term-driven model would predict is thin on
IB vocabulary: genealogies, censuses, land-allotment lists, temple-building inventories. 12 books
(mostly short epistles + the minor prophets with least narrative) have **zero** gap at all —
consistent with those already having had thorough per-word coverage. Everything else sits in a
1–8% band.

---

## (b) Sample read — is the exclusion actually benign?

For every book with at least one missing verse, up to 5 verses were sampled (evenly spread across
its missing list) and read in full. Full samples for all 55 affected books are in the JSON; the
pattern below is representative of the whole set, not cherry-picked from it.

### The aggregate story holds for the bulk of the raw count
The overwhelming majority of sampled misses across the five worst offenders — and scattered
elsewhere — are exactly what the researcher's model predicts: genuinely inert for an inner-being
study.

- **Genealogies/name lists:** `1Chr.1.1`, `1Chr.4.8`, `1Chr.7.18`, `Gen.36.27`, `Ezra.2.28`,
  `Ezra.2.60`, `Ezra.10.43`, `Ruth.4.18-4.22`, `Matt.1.3`, `Luke.3.30`, `Neh.10.8`, `2Chr.21.2`.
- **Census/troop/livestock counts:** `1Chr.12.35`, `Num.26.12`, `Num.31.38`, `Neh.7.38`.
- **Building/temple/tabernacle measurements:** `Exod.27.15`, `Exod.36.32`, `Ezek.40.31`,
  `Ezek.42.9`, `Ezek.48.34`, `1Kgs.6.34`, `2Chr.3.6`.
- **Place-name lists / geography / itineraries:** `Josh.13.31`, `Josh.15.56`, `Josh.19.35`,
  `Neh.11.29`, `1Sam.14.5`, `2Sam.24.8`, `Acts.28.12`, `1Kgs.7.46`, `2Chr.8.5`, `2Chr.11.10`.
- **Ritual/procedural mechanics:** `Lev.1.6`, `Lev.8.20` (butchering steps of an offering).
- **Greeting rosters:** `2Tim.4.12`, `2Tim.4.19`, `1Pet.5.13`, `Phlm.1.24`.

This is genuinely reassuring at the aggregate level — it explains *why* 1Chr/Ezra/Neh/Josh/Num
dominate the missing-verse count, and confirms the term-driven build isn't randomly gutting
narrative content; it's specifically the list-heavy genre pockets that go dark.

### But the exclusion is not risk-free — a real minority carries substantive IB content
Scattered through the same sample, a non-trivial number of misses are not inert at all — they are
emotionally, relationally, or morally loaded verses that a study of the inner being would plausibly
want, missing for the same structural reason (no onboarded word happened to hit them):

- **`Job.30.19`** — "God has cast me into the mire, and I have become like dust and ashes." Raw
  humiliation/suffering lament.
- **`Ps.91.6`** — "nor the pestilence that stalks in darkness, nor the destruction that wastes at
  noonday." Psalm 91 is the psalm of dread/refuge/trust — this is dread-imagery from inside it,
  directly on-topic for [[project_iba_book_by_book_debate_phase]]'s later work if a Psalms
  fear-cluster pass ever revisits it.
- **`Lam.3.2`, `Lam.3.12`, `Lam.3.49`** — three of five samples from Lamentations, all from the
  single most personal lament chapter in the OT ("he has driven and brought me into darkness";
  "he bent his bow and set me as a target for his arrow"; "my eyes will flow without ceasing").
  This is the strongest single warning sign in the sample: it isn't one stray verse, it's a
  *cluster* — suggesting some passages of concentrated inner-being content can still fall entirely
  outside onboarded vocabulary, not just isolated one-offs in list-heavy books.
- **`Isa.14.15`** — "you are brought down to Sheol, to the far reaches of the pit" — the pride/fall
  oracle against Babylon's king.
- **`Deut.4.4`** — "you who held fast to the Lord your God are all alive today" — covenant
  loyalty/devotion ("held fast" = cleave-type relational language).
- **`Prov.1.12`** — "like Sheol let us swallow them alive" — the wicked's own scheming speech,
  squarely inside a passage about enticement and violent intent.
- **`Rom.13.12`** — "let us cast off the works of darkness and put on the armor of light" — moral
  transformation metaphor.
- **`1Pet.4.9`** — "Show hospitality to one another without grumbling" — "grumbling" is itself an
  inner-disposition word.
- **`1Tim.1.6`** — "swerving from these, have wandered away into vain discussion" — heart/mind
  drift.
- **`John.1.11`** — "he came to his own, and his own people did not receive him" — the Gospel's
  rejection/reception theme in miniature.

### Net read
The researcher's assumption is **directionally correct and quantitatively dominant** — most of
the 2,049 missing verses really are inert (names, numbers, measurements, itineraries), and that's
exactly why the worst-affected books are the ones with the least narrative/poetic content. But the
sample shows the exclusion is **not uniformly safe**: a meaningful minority — concentrated more in
poetic/lament/wisdom material (Lamentations 3 above all, but also Job, Psalms, Proverbs) than in
narrative or legal material — carries content the study would likely want, and is currently
invisible not because the verse was read and judged silent, but purely because of which English
headwords happened to get onboarded first. This is the same distinction the original session log
named: a verse being IB-silent as a *result* of applying the method is fine; a verse being
IB-silent because it never *reached* the method is a gap.

**Not yet decided:** remediation route. This report only sizes and characterizes the gap, per the
researcher's instruction to discover the full extent before choosing how to handle it.
