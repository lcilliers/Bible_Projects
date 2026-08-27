# Instructions: writing an inner-being narrative from a book's passage debates

**Filename:** WA-inner-being-narrative-guidance-v1-2026-07-28.md
**Date timestamp:** 2026-07-28
**Why this document exists.** Two narratives were written from Daniel's sixteen passage debates on
2026-07-28 (`WA-dan-inner-being-narrative-v1`, thread-based, and `-v2`, organized around three
questions the researcher dictated directly in chat). Both stood undocumented anywhere but that
chat transcript. When a third, consolidated narrative (`-v3`) was written by summarizing the
second attempt's own scope, the summary silently narrowed it: the researcher's actual words —
"what goes on in the inner being is strongly influenced, to the extent of transfer, not only
suggested from the outside, and other humans" — describe transfer into a person from three kinds
of source (a non-human being, another human, or the surrounding physical world), but the written
narrative's own framing sentence said only "one person's inner state... into another's" — human
to human alone. The error had actually been present since the second narrative's own first draft;
it simply wasn't caught until a third piece summarized it and the researcher checked the summary
against the original words. This is exactly the failure this whole session's other work was built
to close for the passage-debate method itself (BUILD.md §27-33): a rule that exists only in a chat
transcript, applied once from memory, drifts on the next retelling. This document exists so the
same doesn't happen to narrative-writing.

**Status.** This guidance governs any inner-being narrative written from this point forward
(`-v2` onward, in Daniel's case — both were corrected in place, per the researcher's direct
instruction, once the gap was found). It does not retroactively apply to `-v1`, which was written
under a different, earlier brief (`WA-instruction-daniel-inner-being-narrative-v1-2026-07-28.md`)
that never mentioned a three-channel framework at all — `-v1`'s own scope is not in error, it is
simply answering a different, narrower question than `-v2`/`-v3` were asked to.

---

## 1. What this governs, and what it doesn't

The hard constraints for *what a narrative may claim* — nothing invented beyond what the source
debates state, imply, or pointedly withhold; open threads stay open; contradictions stand; no
forced unity; general-reader language; no self-reference to the method or its internal vocabulary
— are set by `WA-instruction-daniel-inner-being-narrative-v1-2026-07-28.md` and are not restated
here. This document adds one further, specific requirement, born from a specific found gap: any
narrative organized around the question of how an inner state is affected, produced, or reached
must explicitly cover all three channels a state can be reached through, not silently narrow to
the most familiar one.

## 2. The three channels (the researcher's own definition, spelled out)

When a narrative addresses how something in a person's inner life is influenced, transferred into
them, evidenced, suppressed, or produced, it must consider all three of the following as distinct,
not treat one as standing in for the others:

1. **Non-human ↔ human.** God, angels, watchers, an unnamed "voice from heaven," a sent hand,
   a spirit — any non-human being acting on, moving into, or being sought by a human's interior.
   Example already on record: God moving the eunuch's own disposition toward Daniel (Dan 1:9,
   genuinely ambiguous but recorded as a live reading); Gabriel's touch restoring Daniel's strength
   and speech (Dan 10:10/16/18-19).
2. **Human ↔ human.** One person's stated or inferred interior producing, shaping, or landing
   inside another's — not merely one person setting an example the other reasons about, but cases
   where the text shows something closer to direct effect. Example already on record: Darius's
   grief for Daniel personally, preceding and shaping his eventual theological conviction, rather
   than following from it (Dan 6:14-26).
3. **Physical world ↔ human.** The surrounding physical world's ordinary causation acting on a
   person's interior or body, or — the direction most easily missed — a person's interior state
   determining what the physical world is shown doing to them. Example already on record: fire
   failing to burn and lions failing to harm the three/Daniel, tied explicitly by the text to what
   they held onto, not merely to an intervention laid on top of normal causation (Dan 3:27, 6:23);
   Nebuchadnezzar's own body carrying out an interior judgment as literal physical transformation
   (Dan 4:33).

**The specific failure to guard against.** A narrative's own opening framing statement is not
suffient evidence that all three were considered — the found error was exactly a framing statement
naming only one channel while the body's actual examples, on inspection, still leaned toward two
of the three and never named the third as its own category at all. Naming the channels in an
intro paragraph is necessary but not sufficient; §3 exists because of that gap specifically.

## 3. Required structure: the Scope self-check

Any narrative governed by this document must close with a section titled exactly `## Scope
self-check`, containing one entry per channel, in this form:

```
## Scope self-check

- **Non-human ↔ human:** <!-- one concrete example, with its verse reference and source debate,
  actually used in the body above -->
- **Human ↔ human:** <!-- same -->
- **Physical world ↔ human:** <!-- same -->
```

Each entry must point to a specific example that genuinely appears in the body text above it — not
be written to satisfy the section in isolation. This is a structural forcing-function, not a
content-quality guarantee: it catches a channel being silently dropped entirely (the actual failure
that occurred), the same way the passage-debate scaffold's Action-type label catches an operation
being recorded with no label, not whether the label is the *right* one. Whether the three examples
chosen are the *best* the source material offers remains a judgment call for whoever writes the
narrative — this document does not, and cannot, mechanize that.

## 4. What can and cannot be automatically checked

`report.book_narrative_validate` (registered alongside this document, `BUILD.md` §34) checks,
mechanically, against a given narrative file:
- that this guidance document itself resolves to a real file on disk (same pattern as
  `method.passage_read_guidance_path`'s check in `passagedebatereport.py`);
- that a `## Scope self-check` section exists in the file;
- that it contains all three required labeled entries, each with non-empty content following the
  label (i.e. the placeholder was actually filled in, not left as `<!-- fill in -->`).

This is a **presence check, not a semantic one** — the same honest limit `passage.validate` and
every other quality-check in this app operates under ("read-only findings, not a gate"). It cannot
confirm the three cited examples are accurate, well-chosen, or actually appear in the body text
above; it can only confirm the section exists and isn't empty. Confirming the citations are real
and load-bearing remains something only an actual read — by the researcher, or by whoever drafts
the narrative checking their own work — can do. Mechanizing that further would mean semantically
parsing prose for argument quality, which is exactly the kind of interpretive judgment this whole
project's method documents (`WA-passage-read-guidance`, `lib/passagedebatereport.py`'s own
docstring) have consistently and deliberately left to the AI/researcher, not to code.
