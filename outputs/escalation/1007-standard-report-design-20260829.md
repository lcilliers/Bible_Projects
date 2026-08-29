# Escalation #1007 — standard report design (findings × verse × question × strong)

## 1. Entry points / filters — all optional, compoundable, AND across dimensions

| filter | accepts | matches |
|---|---|---|
| `-Verse` | single ref, comma/semicolon-delimited list, or range — e.g. `"Heb 4:1-6; Heb 4:7; Hebr 4:5, Rom 2:5"` | `finding_verse_index.verse_id` (any listed/ranged verse — OR within this filter) |
| `-Cluster` | a cluster code or comma-delimited list, e.g. `"M06"` or `"M06,M08"` | `finding.cluster_code` |
| `-Strong` | a Strong's number or comma-delimited list, e.g. `"H0157,G0026"` | `finding.strong_number` |
| `-Question` | a catalogue question code or comma-delimited list, e.g. `"T1.2.1"` | `finding_question_link.question_id` (joined via `wa_obs_question_catalogue.question_code`) |

Any omitted filter is ignored entirely (no clause added, not "match nothing" or "match null").
Combining filters ANDs across dimensions — `-Cluster M06 -Strong H0157` returns only findings that
satisfy both. Within one filter's comma-list, matching is OR (`-Verse` accepting several
references means "any of these").

**`-Verse` parsing reuses the reference resolver built for §205** (`extract_references`/
`resolve_references`, the same book-crosswalk verified against `iba.verse` by canonical position)
— extended to also parse a `chapter:verse-verse` range (`Heb 4:1-6` → 6 individual verses) and
tolerate the same messy input real citations already come in (mixed `;`/`,` delimiters, a
misspelled book like `Hebr` — the crosswalk already has multiple variant spellings per book from
`book_code_variants` plus full names, so a stray misspelling either resolves via an existing
variant or is reported as unrecognised, not silently dropped).

## 2. Filter summary (required — you asked for this explicitly)

Every report opens with a plain statement of what was actually run: each filter's raw input,
what it resolved to (e.g. `-Verse "Heb 4:1-6"` → 6 verses, `Heb 4:1`–`Heb 4:6`, all resolved; or
naming anything that DIDN'T resolve, e.g. an unrecognised book or a Strong's number not in
`iba.strong`), and the total match count before listing results — so a zero-result report is
never silently indistinguishable from "filters were ignored."

## 3. Output shape — my recommendation, since you flagged both as open

**Grouped by finding, not one flat row per finding×verse×question combination.** A finding can
carry several verses and several questions; a flat join would multiply rows in a way that reads as
more results than there really are. One block per matched finding, listing all its own matched
verses/questions/strong-meaning underneath it.

**Ordering — my recommendation:** canonical Scripture order (book/chapter/verse of the finding's
*first* linked verse), falling back to `finding.id` for CLUSTER/GLOBAL-level findings with no verse
at all. Reasoning: a researcher reviewing findings naturally thinks "where in Scripture am I,"
not "which cluster/id came first" — Scripture order is the one ordering that stays meaningful
regardless of which filters were actually applied (verse-scoped, cluster-scoped, or unfiltered).
If a `-Cluster` filter is the ONLY one given (no `-Verse`), grouping under a cluster heading first,
then Scripture order within it, is the natural secondary shape — happy to adjust if you see it
differently once you see real output.

**Per-finding block contents:**
```
Finding #<id> (<cluster_code>, <level>)
  <finding_value text>
  Verse(s): <ref> — "<verse text>"  [one line per linked verse]
  Question(s): <question_code> — "<question_text>"  [one line per linked question]
  Strong: <strongNumber> <accentedUnicode> (<transliteration>) — "<gloss>"
```

## 4. Strong's meaning shape — my recommendation, since you flagged this as open too

Two real shapes exist in the data, checked directly (example: G0026/ἀγάπη):

- **Short (my recommended default):** `strong.accentedUnicode` + `stepTransliteration` +
  `stepGloss` — one line: `ἀγάπη (agapē) — "love"`. Enough to place the term without derailing a
  report whose subject is the FINDING, not the lexicon entry.
- **Full (available via a `-Detailed` switch, not the default):** the structured outline from
  `strong_meaning_parsed` (Hebrew, BDB-style — e.g. `1) to love / 1a) (Qal) / 1a3) human love for
  or to God...`) or `strong_lsj_parsed` (Greek, LSJ-style — `I. love / I.2 love, brotherly love,
  charity`). This is a genuine multi-line dictionary entry per term, not a one-liner — right for a
  dedicated word-study pull, wrong as the default in a report about findings.

My reasoning for defaulting to Short: the report's subject is findings-in-context, not lexicon
research — the full entry is one flag away if a specific result needs deeper inspection, rather
than every result carrying a paragraph of lexicon data by default.

## 5. Not yet built

This is the design, per your instruction to work through report design before code. Confirm (or
correct) the two open points — ordering and strong-shape — and the `-Question` matching key
(`question_code` like `T1.2.1`, or the raw numeric `obs_id`?), and I'll build it as a registered
IBA report step (its own `cfg_report`/`cfg_step` entry, output path governed the same way every
other report here is), not a standalone script.
