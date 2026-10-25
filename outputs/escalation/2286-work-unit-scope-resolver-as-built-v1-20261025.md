# #2286 prototype step 1: the work unit (0.C scope) as built

Date: 2026-10-25. Escalation #2286. Read from the live code and config. No code or data was changed.

## 1. Answer

The code is built. One scope request, whatever it is defined from, comes out as a JSON collection
of verses.

| part | where | registered |
|---|---|---|
| scope resolver, logic | `iba/app/lib/versescope.py` | cfg_utility `handlers_versescope`; cfg_step `verse-scope / verse_scope.resolve` (active) |
| run.py handler | `iba/app/handlers/versescope.py` | as above |
| PS entry | `iba/app/ps/Verse-Scope.ps1` | cfg_utility `Verse-Scope.ps1` |
| settings | `verse_scope.output_dir` = `outputs/verse-scope`; `verse_scope.max_verses` = 2500; `verse_scope.max_seconds` = 30 | cfg_setting, module verse_scope |
| design | `outputs/escalation/2228-scope-resolver-design-v1-20261022.md` (approved 2026-10-22, #2228) | |

On disk there are two outputs: `outputs/verse-scope/anger-bosom-20261022.json` and
`outputs/verse-scope/ot108-3-item-20261023.json`.

## 2. What it does

- **Defined from:** a cluster, a cluster subgroup, a strand, a word (word_registry), a Strong's code,
  verse references, a narrative chapter or one of its blocks, a claim, an observation, a thread item
  (OT-nn.n), a whole thread (its open items), or a request file holding any of these as lists.
- **Combining:** the selectors are joined as a union. `-OnlyStrong` then keeps only the verses that hold one
  of the given codes.
- **Strong's codes:** a bare code stands for all of its lettered derivatives that occur
  (cfg_behaviour_rule bare-strong-decomposed-to-derivatives, #2233).
- **Output:** each verse comes with its id, OSIS reference and the routes that brought it in. Anything
  that could not be resolved is listed with its reason. The JSON also holds the request, each selector
  with its Strong's codes and their senses, and the counts.
- **Guards:** a result over 2,500 verses is held until it is run again with `-Reviewed "<the review>"`.
  A request still running after 30 seconds is refused. Clusters over the guard (from the setting's own
  note): M72 (3,972), M47 (2,841), M65 (2,568).
- **Writes:** only the JSON file. It reads the tables and writes none.

Example from the live output `anger-bosom-20261022.json`: the request was cluster M02 Anger & Wrath
with only H3708A (vexation). Cluster M02 resolved to 681 verses through 66 Strong's codes. The filter
dropped 659 of them and left 22. The first verse is Deu 32:19, routed by cluster M02 via H3708A.

## 3. Where it sits in the analytic cycle

The resolver is used in two places:

1. **On its own:** `Verse-Scope.ps1`, which gives only the verse collection.
2. **Inside a reading:** `Reading.ps1 -Step Open` (`iba/app/ps/Reading.ps1`, header lines 12 to 15).
   Open takes the same selectors plus `-Label`, `-Escalation` (the anchoring item), `-Home` (a home
   cluster) and `-Objective`. It resolves the scope, keeps its verses, collates the scope and writes
   the pre-gap JSON to `outputs/reading/<label>/`.

So in the code as built, the work unit that starts a cycle is more than the verse JSON. It is the
verse collection plus a label, an objective, a home cluster and an anchoring escalation.

## 4. Points for the prototype

These are facts from the code. What they mean for a reliable work unit is still open and is the
researcher's question for this step.

- **a.** The resolver answers "which verses does this selector stand for". It does not judge whether
  those verses make a sound work unit: whether they hang together, whether they serve the objective,
  or whether they are the right size. The only limits are the size and time guards. (Inferential: that
  this is a gap is my reading, not a recorded ruling.)
- **b.** A chapter, block or claim scope gives only the verses it cites. Bringing in neighbouring
  verses is left to a judgement made outside the tool (`versescope.py` lines 17 and 18, "#2228 tool 6").
- **c.** A cluster scope is wide. M02 alone gave 681 verses, and three clusters are over the 2,500 guard.
- **d.** The strand selector reads table `reading_strand`, but the strand steps are retired (#2228 D-a).
  This is related to #2264 (stage strand-reading still live though its steps are retired).
- **e.** One open item touches this tool: #2235 (on hold), "Key words of a scope and a reverse surface
  lookup".

## 5. 0.C rules in config with no code behind them

Three rules say how a scope is set (phase 0.C), but nothing in the code carries them out. I checked
this by searching `iba/app` (`*.py`, with archive left out) for each rule's name or setting key; none
was found.

| rule | what it asks at 0.C | code |
|---|---|---|
| RM-03 / RO8 no-whole-cluster, cfg_setting `reading.whole_cluster_reading_start` (#2268 R2) | a scope on a cluster starts from an overview of its subgroups and how its verses spread, and the scope is cut from that | none: no code reads the setting |
| B:94 study_method.strand-pull-scans-glosses-across-codes | before a scope is set, the glosses of its theme are scanned across all M and T codes | none found |
| RG-19 trial-first | a few verses are read and checked before the whole scope | none found |

So the tool that turns a request into verses is built. The steps that decide what the request
should be are written as rules but are not built. Today they would have to be done by hand in the
session.

