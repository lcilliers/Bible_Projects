# #2486 End-to-end trial: plan v1 (2026-11-13)

Status: plan for the researcher's approval (B:17). Nothing is built or changed. Basis: `outputs/escalation/2486-claim-objectives-and-definition-draft-v2-20261113.md`. Area confirmed by the researcher (2026-11-13, "Yes, that area"): movement II of the four-movement story (#2345), the will and purpose part, on the collections intend, plot, choose and desire.

## Purpose

Take a few claims through every layer to find out whether the ideas in draft v2 hold, before any rule, config row or schema is written: the observation and claim border, the four levels, a claim that names a skeleton key instead of a chapter number, and the evidence link in both directions.

## Material (read-only count, `iba/app/db/iba.db`)

46 current claims name observations whose live nodes sit in the four collections; 94 current claims reach them through their verses. The trial uses six, chosen for their range of levels and for bridging:

| Claim | Said in brief | Collections its observations reach |
|---|---|---|
| C-367 | The heart is where thoughts and plans come from | thought, intend, plot |
| C-338 | The choice is the chooser's own | desire, quarrel, choose |
| C-362 | What the heart devises on its own can be a rival worship, a false report or a god | thought, intend, plot |
| C-364 | A purpose can be set ahead and held; kept and directed by God | thought, intend, heart, loyalty |
| C-359 | Looking ahead weighs ability and cost, plans under uncertainty | desire, wise, choose, teach, intend |
| C-370 | A path from a thought arising to the deed | honor, thought, intend, plot |

The researcher may swap any claim.

## Steps (each on a copy, in the researcher's reading)

1. **Copy.** A copy of `iba.db` by `iba/app/lib/dbsnapshot.copy_db` and a named snapshot as the rollback point (rule B:97). Everything below is written to the copy only; the live database and files are not touched.
2. **Per claim, back direction.** List the claim's sources, the observations on those verses and their nodes with surface, role and collection. Mark, with the researcher: which observations and nodes the claim uses, which it does not, and which observations say more than the verse says (past the border). Record the border cases; nothing is rewritten in this trial except on the copy.
3. **Per claim, level and claim wording.** Name its level (surface, interaction between words, across behaviours, meta) and test it against the draft's tests (what the verse says about how the inner being works; one point; founded).
4. **Skeleton index (minimal, on the copy).** From movement II of #2345 and the domains of `_analytics/surfaces/exports/documents/inner-being-story-fit-v2-20261101.md` (Will and action; Knowing and thinking), make the few entries these claims need: a stable key, a title and a parent. Each claim names one entry; where a bridging claim fits two, that is recorded as a finding.
5. **Forward direction.** For each claim, the block that tells it today (`narrative_claim_telling`) and where that block would sit under its skeleton key.
6. **Findings, for the researcher.** What the border, the levels and the skeleton key need to be stored (columns, a table, a view), where the evidence link breaks, what a chapter built from the skeleton would look like, and any rule that needs wording or amending (B:127, B:129).

## What it does not do

No rule, `cfg_*` row, migration or document change; no change to claims, observations, nodes or the narrative in the live database; no assignment of the other 288 claims; no decision on chapter numbers.

## Output

One findings file under `outputs/escalation/` with the six claims worked through, and the copy kept until the researcher closes the trial. The build of the design that follows is a separate step after the researcher decides.
