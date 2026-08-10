# SESSION LOG — 2026-08-10 — verse-restatement-by-Strong's report designed, built, and formalised; `healing` added to the registry; two real cross-cutting bugs found and fixed

Long session, several threads chained off one design conversation. Grouped by thread, in the order
they happened.

## 1. New report design: verse restatement for a single Strong's reference

Started from an inline-preview request (blessing's linked spans in Eph 1:3), iterated through four
rounds of the researcher's own answers to open design questions:

1. **Scope** — not one example verse per Strong's, but every verse the exact code occurs in
   (whole Bible). This is what made volume the live question for the rest of the thread.
2. **Inline annotation** — `**surface** [strong: senses]`, verse text otherwise untouched.
3. **Senses** — exact `strong_variant` match only, never a sibling/base-collapsed fallback.
4. **Collisions never silently dropped** — a real bug, not a hypothetical: G2128 (8 verses, no
   repeated word-forms) never tested the substitution method's safety. G2127 (40 verses) broke it
   on the first real try — `text.count("bless")` matched inside `"blessing"` (a different span,
   different Strong's) in 1Cor 10:16. Fixed with a word-boundary regex, verified against every row
   in both test verses. Two more real shapes found building G2127: combined-tag spans (STEP tags
   two Strong's on one rendering unit) and empty-surface spans (no independent English text) —
   both given explicit, non-silent handling rather than smoothed over.

**Volume check, before committing to the design**: regenerated `verse-lexical-by-registry-
20260810.md` (whole-Bible rescope of the 2026-08-09 NT-only version — found live that
`verse_lexical` now covers all 66 books, not just NT+6 OT books as assumed). 196,144 (registry
word, verse) pairs total; per-word range 0–10,128. Recommended on-demand-by-single-Strong's as the
only workable scope (matches `report.verse_lexical`'s own existing on-demand-by-range precedent) —
confirmed by the two preview samples: G2128 = 8 verses, G2127 = 40, both trivially readable.

**Formalised into the app** (researcher: "formalise this report into the app... ensure there is a
ps module... update the user guide"): new `report.strong_verse` — `lib/strongversereport.py`,
`handlers/reports.py:strong_verse_report`, `ps/StrongVerse-Report.ps1 -Word <word> -Strong
<strong>`, `USER-GUIDE.md` §12f. Filed directly into `word_registry/<word>/` **in code** this time
— both bugs from this same fix from earlier in the day (`report.word_registry_span`,
`report.registry`) still write flat and need a manual refile every run; this one doesn't.

Needed **9 separate `cfg_*` proposals** (`cfg_work_package`, `cfg_step`, `cfg_report`, 2×
`cfg_report_section`, 2× `cfg_on_fail`, `cfg_setting`, `cfg_utility`) — `configmaint.propose` is
one row per call. Researcher: "you can approve all 9 escalations to complete the work" — explicit,
in-session authorisation for this specific batch, not a standing policy. Answered all 9, applied
all 9, verified each row by direct query. **Then actually ran it** (`-Word blessing -Strong
G2127`) and found a real bug on the very first live run: an intro blank-line separator was being
eaten by an over-broad empty-string filter. Fixed, regenerated, re-verified against both preview
samples' exact content (40 verses, 8 senses, the combined-tag label, the empty-surface aside, the
correctly-isolated `bless`/`blessing` — all matched).

## 2. `strong.count` root-caused as dictionary-wide, not verse-scoped — fixed in the live report

Testing G2128 surfaced a real discrepancy: the researcher expected 52 verses (reading "STEP total
count: 52" off `blessing-strong-span-v1-20260809.md`); the real, twice-confirmed figure (local DB
+ live `call3_strong`) is 8. Traced live: called `call2_getInfo` for the same code under 9
different `{version}` values, including two Hebrew-only modules that can't sensibly answer for a
Greek code — identical `count` every time, proving the field is fixed Strong's-dictionary
reference data, not scoped to any Bible text this app holds.

**Fixed** in `lib/wordregistryspanreport.py`: the line now leads with the real, local
`verse_lexical` occurrence/verse count, with the dictionary number kept alongside but explicitly
relabelled. Verified against `blessing` (G2128: 8/8 matches live STEP exactly; G2127: 42 rows/40
verses, both cross-checked independently).

## 3. `report.registry` — missing listing + a second CSV, both approval-gated, both applied

Researcher: `Registry-Report.ps1` had no plain per-word listing and (thought it had) no CSV.
Checked rather than assumed: **(1)** confirmed real — the two existing sections are both INNER
JOINs through `word_strong`, so a zero-link word (`blindness`) never appeared as a named row
anywhere. **(2)** not correct — `word_registry.csv` already existed and refreshes every run
(confirmed via archive timestamps). Added a `listing` section (1 `cfg_report_section` proposal),
approved and applied, verified live (`blindness` now appears, row count matches exactly).
Researcher, re-reading: "you still did not get it... both word-registry table and registry table"
— the CSV side needed the same split. Added `registry.csv` (1 `cfg_report_csv_table` proposal),
approved and applied, verified live (178 rows, `blindness` present with `strong_count=0`).

**Follow-on defect found later, not fixed this session**: running `configmaint.validate` as a
sanity check after the `report.strong_verse` work surfaced a real, pre-existing coherence error —
`cfg_report_csv_table (report.registry).table_name 'registry'` isn't a real table, just an
invented output name (every other row in that table names an actual table). Flagged, not silently
patched — the proper fix is a SQL `VIEW`, schema work with its own migration, out of scope for a
single `configmaint.propose` row.

## 4. Environment fix — absolute paths, not relative

Researcher: commands kept not running "in the context of the terminal." Root cause: every
`iba/app/ps/*.ps1` script already `Set-Location`s to the repo root internally — the only thing
that ever needed the *terminal's* cwd to be right was the initial `.\Script.ps1` invocation itself.
Proved live: invoked a script by full path from `C:\`, worked with no `cd` first. Fix: give full
absolute paths in every command from here on (adopted for the rest of the session), plus added
`.vscode/settings.json` (`terminal.integrated.cwd`) so new VS Code terminals default to the repo
root too.

## 5. Cross-registry overlap — quantified, then explained mechanically

Researcher noticed `word_registry` is the ONLY table matching `%registry%` in the schema (verified
live) — no separate entity enforces cross-word integrity; the one automated check
(`_possible_duplicates`) only escalates at 100% Strong's overlap, and even then only warns. Built
`strongs-shared-across-registry-words-20260810.md` (880 codes shared across 2+ words, full list +
distribution). Walked through a concrete example (kindness/compassion/devotion/faith via H2617A)
to separate WORD-level verse overlap (any strong) from the SAME-CODE overlap (invariant regardless
of which pairing frames it) — a real distinction the first answer had blurred, corrected on
follow-up. Root-caused the overlap mechanism itself: `handlers/raw.py:discover()` populates
`word_strong` purely from `call1_meanings(ctx.word)` — STEP's own English-word reverse-lookup, no
cross-registry dedup, `discovery.follow_related` explicitly off. Confirmed live: three separate
STEP calls (kindness/mercy/compassion) each independently returned `H2617A` — not a shared cache,
genuinely independent hits on STEP's own lexicon data.

## 6. Healing-domain word check, both languages

Researcher supplied 21 Hebrew + 19 Greek healing/health-domain roots (transliteration/count/gloss)
to check against the registry. Matched each to `strong.stepTransliteration`, disambiguated
homonyms by gloss, checked `word_strong` linkage. Result: **no registry word named "healing" or
"health" exists at all**; 11/21 Hebrew hits were incidental (swept in by unrelated English words);
Greek was mixed — `salvation` is a real, deliberately-registered word, so `sōzō`/`sōtēria`/
`diasōzō` landed there on-topic, but the core ἰάομαι "to heal" family had zero coverage anywhere.
4 Greek words given (`hugiazō`/`hugieia`/`iatreia`/`iatēs`) don't exist in Strong's numbering at
all — confirmed by transliteration AND gloss search, consistent with the researcher's own `0x`
counts (classical/LXX-only, no NT occurrence). `healing-words-in-study-check-20260810.md`.

## 7. `healing` added to the registry (id 184) + 44 curated `word_strong` links

Researcher: "add healing to the word-registry index and add all the missing hebrew and greek words
to it... create the cross registry items for the strong already in other registries also."
Deliberately NOT the normal `New-Word.ps1` chain (its `raw.discover` step would have used STEP's
own uncontrolled search for "healing," not the researcher's curated list) — ran `registry.create`
standalone (confirmed safe: chaining is a PS-script loop convention, not automatic), answered its
approval, stopped. `word_strong` writes went through the already-granted `migration` writer, new
one-off `migration/add_healing_word_strong_20260810.py` — 44 codes (17 genuinely new, 27
cross-registry). Caught and fixed a real categorisation error in my own first draft before
applying (`H2418`/`H2425` mismarked as cross-linked; a direct query showed neither had any prior
link). Two items from the source list deliberately not fully included, flagged rather than
guessed (the other 10 `H5414` sub-forms; `G4990`/`G4992`). Verified live: `word_strong` count = 44,
regenerated `healing`'s own strong-span report, all 44 render with real data.

## 8. Full meaning-table audit — 8 real gaps found and backfilled, which surfaced a second bug

Researcher: "take these new strongs into all the meaning tables and generate the lexicals for it
also." Audited all 44 codes across `strong`/`span`/`verse_lexical`/`strong_meaning_parsed` —
confirmed the lexical layer (whole-Bible build) already covers all 44 (two apparent zero-span
cases were combined-tag spans, not gaps; `G7534` genuinely has 0 live verse occurrences, confirmed
via `call3_strong`). Real gap: 8 sub-lettered codes (`H7965G`–`L`, `H2492A`, `H5414P`) had never
had their own `strong_meaning_tree`/`strong_meaning_parsed` row — only the shared base existed.
`raw.detail_one` is a no-op for all 8 (`strong` row already exists from the bulk import). Reused
`fix_strong_meaning_tree_collapse.py`'s own mechanism in a new one-off,
`migration/backfill_healing_exact_variant_meaning_20260810.py`, deliberately going beyond that
script's "genuine collapse only" policy on direct instruction. Applied, self-verified 0 remaining.

**Checking the result surfaced a second, independent, pre-existing bug** in
`wordregistryspanreport.py` itself (there since it was built, 2026-08-09) — its senses lookup
queried `strong_meaning_parsed` by `lemma_key` using the full sub-lettered code, which can never
match (lemma_key is always the base) — every sub-lettered code silently fell through to base
fallback regardless of whether its own exact row existed. Confirmed live: `healing`'s 8 newly-
backfilled codes still showed the fallback message immediately after being fixed — proof the query
was structurally incapable of finding them. **Fixed** (`lemma_key=?` → `strong_variant=?`).
Checked the blast radius across three words, not just `healing`: `blessing` unaffected (byte-
identical regeneration, no sub-lettered cases there); `fear` showed a real, previously-hidden
improvement unrelated to today's backfill — `H1481C`/`H8175C` used to render two unrelated senses
interleaved from a genuine 2026-07-26 homonym-collapse fix that this bug had been silently hiding
ever since; `H3372G`/`H3372H` (a genuine remaining gap, not backfilled by anything) still
correctly show the fallback message, proving the fix isn't over-corrected.

## Explicitly not included in this commit

- `iba/app/verse-analysis/word_registry/Cursing/cursing-strong-span-v1-20260810.md` — a
  `WordRegistrySpan-Report.ps1 -Word Cursing` run this session did not execute.
- `iba/app/verse-analysis/word_registry/Renewal/wa-109-renewal-in-inner-being-v1_0-20260810.md` +
  `wa-obslog-renewal-synergise-v1-20260810.md` — same shape as the `Fear`/`blessing` synthesis
  pairs excluded from the 2026-08-09 log: the researcher's own separate synthesis work product,
  not anything this session produced.
- `iba/app/reports/registry-v4-20260810.md` — a third `report.registry` regeneration, byte-size-
  identical to `v2`/`v3`; this session ran the tool twice (producing `v2`, `v3`), not a third time.
- `iba/app/verse-analysis/.obsidian/workspace.json` — editor state, not repo content (same
  standing exclusion as every prior session log).

## Files touched (this commit)

**New (code):** `iba/app/lib/strongversereport.py`, `iba/app/handlers/reports.py`
(`strong_verse_report`), `iba/app/ps/StrongVerse-Report.ps1`,
`iba/app/migration/add_healing_word_strong_20260810.py`,
`iba/app/migration/backfill_healing_exact_variant_meaning_20260810.py`.

**Modified (code):** `iba/app/lib/wordregistryspanreport.py` (§88's count-field fix + §93's
`strong_variant` fix), `iba/app/lib/registryreport.py` (`listing` section + CSV `row_filter`),
`iba/app/handlers/reports.py` (import + handler), `iba/app/USER-GUIDE.md` (§12f + cross-refs),
`iba/app/BUILD.md` (§88–§93).

**Config (DB), all via `configmaint.propose`, all approved and applied:** `cfg_report_section`
insert (`report.registry` listing), `cfg_report_csv_table` insert (`report.registry` → `registry`
csv), 9 rows for `report.strong_verse` (`cfg_work_package`/`cfg_step`/`cfg_report`/2×
`cfg_report_section`/2×`cfg_on_fail`/`cfg_setting`/`cfg_utility`).

**Data (DB), via sanctioned writers, not raw SQL:** `word_registry` +1 (`healing`, id 184, via
`registry.create`), `word_strong` +44 (via the `migration` writer), `strong_meaning_tree` +66 rows
/ `strong_meaning_parsed` fully rebuilt (via `lexicon.parse`).

**Reports/artefacts generated this session:** `iba/app/reports/{eph-1-3-verse-lexical-stream-
sample,g2128-verse-lexical-by-strong-sample,g2127-verse-lexical-by-strong-sample,verse-lexical-by-
registry,healing-words-in-study-check,strongs-shared-across-registry-words}-20260810.md`, plus
`iba/app/reports/registry-v{1,2,3}...` and their archived predecessors, `CONFIG-REPORT-v68`
through `v78` + archive, `iba/app/verse-analysis/word_registry/{blessing,healing,Fear}/` report
regenerations described above.

## Next

Nothing queued by the researcher beyond re-running the `fear` synergy report themselves (their own
action, not this session's). Open, not resolved: the `cfg_report_csv_table.table_name='registry'`
coherence gap (§3 above — needs a schema-level `VIEW`), and the two `na.tan`/`sōtēria` items
deliberately left out of `healing`'s Strong's list if the researcher wants them reconsidered.
