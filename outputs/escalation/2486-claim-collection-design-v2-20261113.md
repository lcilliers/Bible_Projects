# #2486 Re-evaluate each claim against its observations and nodes: design v2 (2026-11-13)

Status: design for the researcher's decision. Nothing built or changed. Replaces v1 (`outputs/escalation/archive/2486-claim-collection-design-v1-20261113.md`).

Researcher, verbatim (2026-11-13): "this is not just a problem of making links that is missing - it is about re-evaluating each of the 294 claims into the observations and identify claims which is simply not supported by their observations. This is not about adding every observation and node for a verse to a claim, because there can be a variety of claims pointing the the same verse or group of verses, but only referencing certain observations and nodes. observations and nodes that are not used or applied in the claim does not belong to claim."

## What this changes

The task is a reading of each claim, with the researcher, not a migration. A claim is linked to the observations it actually uses, and to the nodes of those it applies. Its collections then follow from those nodes by query (the collection is on the node, B:130); no collection is stored on the claim. A verse shared by several claims gives each claim only its own observations and nodes.

## Measured (read-only, `iba/app/db/iba.db`)

- 393 claims; 66 already have observation sources (87 rows, none on a withdrawn observation).
- 294 claims with verse sources only: their verses carry a median of 17 live observations per claim (max 126), so no verse-based rule can choose between them.
- 38 claims reach no observation; 12 of those are withdrawn.
- 0 live nodes have disposition `claim` (635 `told`, 6 `data`, 5 `held`, 67,760 none). No node yet says which claim uses it.

## What already exists (B:3, B:123)

- `narrative_claim_source.observation_id`: the claim-to-observation link (source kind `observation`).
- The reading process, `iba/app/ps/Reading.ps1` (Synergy, Apply, Check at the claims gate), which already requires every current claim on the scope to rest on a finding, and disposes each node of the reading as `claim`, `held`, `data`, `context` or `withdrawn`, with the carrying claim in `disposition_note`.

## Proposed way

Claim by claim, in the reading with the researcher, per scope (a chapter or collection), never in one pass (B:127):
1. Present the claim, its verses and the observations on them; Claude names the observations and nodes the claim uses and the ones it does not.
2. The researcher confirms or corrects. Each claim ends in one of:
   - **Supported**: observation sources set to the ones used, nodes disposed `claim` with the claim named.
   - **Partly supported**: sources set for the part supported; the claim is restated (verdict Restated or Corrected) or held.
   - **Not supported**: claim held or withdrawn with its reason (the register's own actions).
   - **Needs an observation**: the verses show what the claim says but no observation does; a new observation is written by the reading.
3. The change goes through the register and reading tools, with the change log.

## Decisions needed (B:44, B:105)

1. **Level of the link.** Observation level only (`narrative_claim_source.observation_id`, which exists), or also node level, since the researcher wants only the nodes the claim applies. Recommend node level through the existing node `disposition` `claim` plus its note naming the claim, which needs no new table. Option: a new `node_id` on `narrative_claim_source` (a schema change, `cfg_column` rows, migration) so a claim can be asked for its nodes directly; a node used by two claims fits only this option, because `disposition_note` names one carrier. Which?
2. **Order of the 294.** Recommend by collection (the unit of study, B:127): claims grouped by the collections their verses reach, so each reading serves one collection. Alternative: by chapter (`main_chapter_id`).
3. **Claims that are not supported.** Recommend the researcher decides each one in the reading (held or withdrawn with a reason), none automatically.
4. **The 4 claims and 82 live nodes with observations but no collection** are completed under the node rules (#2484 closed; to be taken up in the first reading that meets them).
5. **No migration of links in bulk.** The 66 existing observation-source claims are re-checked in the same reading as the 294, since the same test applies to them.

## Not built until decided

On approval, Claude proposes the first scope (one collection) with its claims, observations and nodes for the researcher to read.
