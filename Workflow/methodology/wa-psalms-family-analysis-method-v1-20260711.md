# Method — analysing a single family base-source JSON (in isolation)

> Every base source is described **in isolation**. Read ONLY your one assigned JSON file (plus this method). Do **not** read other base sources, the DB, or any other file. Describe **strictly within the scope of that one file** — nothing from outside it.

## The assignment
Describe **in depth how the base-source data describes the inner workings of the inner being (IB)**. Consider **all** the data and **all** aspects. Do **not** silently ignore data — every meaning and every instance must be accounted for, every dimension considered. **Only** the source data: do not invent or import findings the file does not support. **Highlight where meaning could not be derived.**

## Hard rules
1. **Every finding must be back-trackable and cited** as `reference · span_id · Dnnn(label)` (e.g. `Psa 78:18 · span 283050 · D105 bearer`). No claim without a citation into the file.
2. **Discovery notes (D114) are source** (the original reader's read) — you may cite them, labelled as D114.
3. **No invention.** If the file does not say it, do not write it. Prefer "unread / not derivable from this source" over a guess.

## Data-integrity screen — do this FIRST, before reading meaning
Report what the file can and cannot bear:
- **D112 (coupling) / D116 (locus) field-swap:** if D116 "locus" holds a prose phrase and D112 "coupling" holds an `internal:`/`external:` code, they are **transposed** — read them corrected and **list which instances** are swapped. (Correct order = D116 a code, D112 a phrase.)
- **Self-loop "edges" are not real links:** any edge with `item_type:"flag"` + `resolution:"inferred"` whose `to_span` equals the span's own id is a self-loop, **not** a network edge. Only `pair` edges (`resolution:"span"`) linking to a **different** span are genuine — use only these for the network.
- **`seat`(D104)/`manner`(D108) = "none":** count how many instances leave these unfilled.
- **Absent dimensions:** note which of D109 intensity, D110 specifier, D111 effect, D113 prohibition are absent across all instances.
- **Cluster NULL / `T2`:** note instances whose `cluster.code` is null or T2 (the term-cluster cannot type them).

## Coherence check
State whether the **family label matches its data**: do the meanings/senses/clusters form one coherent inner-being movement, or has the keyword grouping fused unrelated movements? If fused, name the distinct movements (with counts + citations). This is a first-class finding.

## What to describe (all aspects, grounded per instance)
Work through the dimensions as the IB's anatomy and motion, always cited:
- **sense (D101) / type (D102):** what the word is and whether action/status/state/disposition/affect/faculty/volition/cognition.
- **seat (D104):** where in the interior (heart, soul, spirit/ruach, eye, …) — or unstated.
- **bearer (D105):** whose inner being (must be the human IB; note if a person/group, and if `inferred`).
- **source (D103) / operation (D106) / target (D107) / manner (D108):** what moves it, what it does, toward what, how.
- **coupling (D112) / locus (D116):** what it is bound to; where it sits (internal/external) — corrected for swaps.
- **role (D115):** characteristic / qualifier / standalone.
- **the network:** the genuine `pair` edges only (from→to span, on which dimension) — describe what links to what; note if sparse or one-directional.
- **the interior anatomy the data actually names:** assemble only the filled seats/sources/couplings.

## Output
- Write the analysis to **`verse-analysis/psalms/_family-analyses/wa-family-analysis-<slug>-20260711.md`** where `<slug>` is the family (from the file's `meta.scope.family`; for the outliers file use `OUTLIERS`).
- Suggested sections: **0. Data-integrity screen · 1. Coherence (does the label fit) · 2…n. The movements/operations evidenced (cited) · The network · The interior anatomy named · What could not be derived · Summary.**
- British spelling. Terse, evidence-dense, no padding.
- Your chat return = one line only (e.g. "Filed wa-family-analysis-<slug>-20260711.md — N meanings/M instances; <one-clause headline>."). The analysis lives in the file, not the chat.
