# #2307 Prior capture: verses the reading index does not reach (v1)

**Date:** 2026-10-26 · **Escalation:** #2307, raised from #2305 · **Found in:** the M10 capture, Developer Mode session of 2026-10-26.

## 1. What was found

The capture takes its unit from `reading_ref`, the lines of a document that name a verse. The recorder refuses a finding
that no indexed line answers (`iba/app/lib/priorcapture.py`, check(), the "a finding comes from a line" test). Two kinds
of verse mention are not in that index, so the observations they carry cannot be recorded.

**A. Verses given only in a provenance line.** The 1682 process documents give each observation as a bullet followed by
an italic line, for example `*[strong=G1777 · verse=Matt.5.22 · ...]*`. The index reads `Matt 5:22`, not the dotted
form `Matt.5.22`. A bullet whose own text names no verse is not an indexed line, though the document makes an observation
about a verse.

| Document (M10) | Observation bullets | Indexed lines | Bullets with a dotted provenance verse and no indexed line | Status |
|---|--:|--:|--:|---|
| `_analytics/Clusters/1682-test-m10-process-c-C_adultery-v2-20260911.md` | 35 | 18 | 13 (lines 45, 48, 54, 63, 66, 78, 83, 89, 92, 95, 98, 101, 129) | recorded, 18 observations |
| `_analytics/Clusters/1682-test-m10-process-c-H_guilt-v1-20260911.md` | 49 | 14 | 33 (lines 20, 23, 26, 29, 32, 35, 38, 41, 47, 50, 53, 56, 59, 62, 65, 71, 74, 77, 80, 83, 86, 92, 95, 101, 104, 107, 110, 113, 116, 119, 124, 130, 171) | held, not recorded |
| `_analytics/Clusters/1682-test-m10-process-c-J_unfaithfulness-v2-20260911.md` | 27 | 24 | 2 (lines 46, 60) | recorded, 24 observations |
| `_analytics/Clusters/1682-test-m10-process-c-SUNDRY-v1-20260911.md` | 18 | 6 | 2 (lines 18, 33) | recorded, 6 observations |

**B. A mention the parser did not take.** `_analytics/Clusters/m10-family-synthesis-L_defilement-20260911.md` line 16 reads
"one verse, Ps 12:8:" (H2149, vileness is exalted among the children of man). The index holds no reference for it, so the
document has 0 lines and its one finding is not recorded. The document is left unrecorded: marking it `nothing to capture`
would be wrong.

## 2. Why it matters

A document's `capture_status` of `captured` stops a second Prepare ("already captured"). The three recorded process
documents cannot take their unreached bullets without a reset of that status. Recording the held document as it stands
would take 14 of its 49 observations and lock the rest out.

## 3. Options

1. **Extend the index parser** to read the dotted form and the trailing-colon form, rebuild the index
   (`iba/app/ps/Reading-Index.ps1 -Step Build`), reset `capture_status` on the three recorded documents, and run a second
   pass on each that adds only the unreached bullets; the held document is then recorded whole.
2. **Let Prepare add the lines**: Prepare reads the provenance lines itself and lists each such bullet as a line with the
   provenance verses; the recorder's line check is widened to the Prepare list. The index stays as it is.
3. **Accept the gap**: record the held document for its 14 indexed lines and list the unreached bullets here as not
   captured. 33 of that document's 49 observations stay out of `ib_observation`.

Recommended: option 2. It fixes the unit at the point where the capture takes it, and leaves the index (used by other
tools) unchanged.

## 4. Effect on the work in hand

The capture continues on documents whose verses are written in their text (family syntheses, readings, ledgers). M47 is
measured per document before recording: bullets with a provenance verse on no indexed line. The held and unrecorded
documents wait for the decision.
