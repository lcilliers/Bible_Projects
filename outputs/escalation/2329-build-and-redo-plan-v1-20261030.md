# 2329: build and redo plan for the new observation structure (2026-10-30)

Researcher, chat 2026-10-30 (verbatim): 'proceed with redoing all 39 verses to this new level. measure the time each verse takes and ensure that the configs include pointers for the different nuances.'

The structure is `outputs/escalation/2329-observation-structure-worked-example-v3-20261030.md` (the researcher's rulings are quoted at its head). This plan is what a Developer Mode session builds first, and what the standard-mode session then runs. The redo cannot run today: Record enforces the old structure (`reading.observation_rules`, RS-08: every part on one observation, a link and a party observation per verse), and it would refuse observations written one per item. Config first, then the code that reads it (`governance.rules_must_be_config_driven`).

## 1. Developer Mode session: build, tested on a copy (B:97)

Start: a fresh session, `/developer-mode` as the first thing typed, then `do 2329 build v3`.

1. **Config.**
   - The nine items of spec 4.2 as observation items: for each its key, the observation kind it is written as, whether it is written only where the verse shows it, whether it may be shared across characteristics, and the bases allowed (stated, read).
   - Remove `before`, `after` and the typed party (`acts`, `acted_on`) from `reading.observation_parts` and from `reading.observation_rules`; RS-08 restated for the new structure.
   - The rules on what the code now checks: every surface with role characteristic has the observations of its applicable items; qualifiers and shared observations carry nodes on every characteristic they cover; a read observation names its grounds; no observation restates the verse text.
   - **The nuance pointer table** (section 3).
2. **Code** (`iba/app/lib/reading.py`, `iba/app/lib/observationrecord.py` and their handlers): the sheet and Record work on observations written one per item, with shared observations applied by nodes; the check enforces the config of step 1; the existing observations are checked and accepted, modified or soft deleted as before (RS-04), including the triplicated statement, link and party observations of the 39 verses.
3. **Timing.** The scope JSON records, per verse, when its sheet was put in hand and when it was recorded, and the redo is run one verse per sheet (`-Count 1`), so that the time per verse comes from the app and not from run ids.
4. **Docs.** Spec v6 (section 4.2 restated, the nuance pointers), USER-GUIDE, BUILD.md entry, tests on a copy, `Config Validate` clean.

Points the builder meets that need a decision from the researcher before they are built (B:44): whether each item has its own observation kind or the existing kinds are kept; what becomes of the `parts` column on the existing observations; how the mode of an operation (done, foreseen, commanded, negated, reported) is recorded. Each goes to the researcher as a decision with its options, not answered inline.

## 2. Standard-mode session: the redo of the 39 verses

- Take the named snapshot first (`dbsnapshot --named`).
- For each of the 39 verses: `Reopen`, `Observe -Count 1`, fill, `Record`. Judg 13:6 first, as in the worked example. Each verse is read outward from the verse (RG-01): every surface with role characteristic, every applicable item, the read relations marked read with their grounds, the discovery flags for what the passage must give.
- After the first three verses I compare them with the worked example. If they differ in structure, I stop and report.
- Time per verse from the JSON, in a table with the number of observations written, kept and soft deleted, and the characteristics found per verse.
- After the 39: the quote check against the ESV text (as run today on 223 segments), the read-back of the observations against their verses (RG-20), and a claims test from the observations alone (the five claims of `outputs/escalation/2329-readback-and-claims-test-v1-20261030.md` rebuilt, plus any track the new observations show).

## 3. The nuance pointers

The researcher asks that the configs point to the different nuances, so that the reading and the check know where each is recorded. One row per nuance: the nuance, the item it falls under, the observation kind and basis, the rule it comes from, and a verse that shows it. The rules already exist as `cfg_method_rule` rows; the pointer table links them to the structure. Nuances found so far:

| Nuance | Item and form | Rule | Verse |
|---|---|---|---|
| a negated act is a refusal; the negator is a qualifier | 3 polarity; qualifier node on the negator | RG-07 | Judg 13:6, Jos 9:14 |
| a qualifier shared across characteristics | 2 role; one observation, nodes on each | RG-04 | Judg 13:6 ('very', 'not') |
| a T-coded word takes the role characteristic because the verse makes it carry the track | 2 role by the verse, never by the cluster | RG-03 | Judg 13:6 (appearance) |
| a refrained act with something hidden behind it | read observation with grounds | RG-11 | Judg 13:6 |
| a relation between characteristics in one verse (one conditions another) | read link, nodes on each characteristic, discovery flag | RW-08, RG-15 | Judg 13:6 |
| a source of a state against an enablement to act | separate observations | RG-13 | to find |
| a figure or simile: the tenor, not the vehicle | operation of the tenor | RG-25, RG-02 | to find |
| a tagged word working adverbially | qualifier in that occurrence | RG-24 | to find |
| an idiom or multi-word span whose surface hides the word | meaning item, surface rule | RG-08, `lexical.span_surface` | Jos 9:14 ('counsel' as 'ask at the mouth') |
| a reading that is open in more than one way | one observation per reading, basis read | RW-08, RG-08 | to find |
| the speaker and the audience of reported speech | party item | RG-02 | Gen 43:7, Judg 13:6 |
| the mode of an operation: done, foreseen, commanded, negated, reported | to be decided (section 1) | to be decided | Gen 32:17, Deu 4:32, Gen 43:7, Jos 9:14 |
| a homonym or data error | flag, not fixed in the reading | RG-16 | to find |
| a literary pattern with no inner-being content | open question, not an observation | RG-12 | to find |
| a structural fact the verse does not explain | kept, not dropped | spec 4.2 | to find |

Each nuance met in the redo that has no row gets a row in the same session, with the verse that showed it, so the table grows from the verses and not from a list made beforehand.

## 4. What is not decided or known

- The cost: observations per verse (Judg 13:6 is 23 in the worked example) and the time per verse are unmeasured; the redo of the 39 gives the first figures.
- Whether the new structure surfaces the significance of a verse when I read it; Judg 13:6 showed it in the researcher's reading, not in my five observations.
