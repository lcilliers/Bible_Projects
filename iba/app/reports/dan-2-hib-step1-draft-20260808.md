# Dan 2 — Step 1 HIB draft (for review before writing to DB)

**Date:** 2026-08-08. **Scope:** `hib.set -Book Dan` payload covering Daniel 2 (verses 1-32, 34-49
— Dan.2.33 has no `verse` row at all; confirmed by-design per `governance.verse_gap_by_design`,
not a gap to fill).

**Method followed:** `debate-analytic-process-digest-20260805.md` Step 1 — read every verse from
the lexical (`verse_lexical`/`span`), not the English gloss; every human mentioned is a presumptive
candidate; collectives stay collective; referential/implied HIBs are named, not skipped; genuine
referent cruxes are enumerated with textual grounds, not silently resolved to the obvious English
reading.

**Why this file exists rather than a direct write:** `hib.set` is scope=`book` — the payload must
reconcile against *every* existing live `hib` row for Dan (currently 14, from the Dan 1 and Dan 8
runs), not just Dan 2's new ones. A wrong grouping/collective decision here becomes permanent,
reconciled DB content, and several of the calls below are genuinely interpretive, not mechanically
resolvable from the DB/lexical alone. Per project protocol, judgement calls go in a filed review,
not a silent default.

---

## Judgment calls needing a decision (JC1-JC6)

**JC1 — "the wise men of Babylon" as ONE collective HIB, not four/five.** Dan 2 names the summoned
professional class several ways: "the magicians, the enchanters, the sorcerers, and the Chaldeans"
(v2), "any magician or enchanter or Chaldean" (v10), "wise men, enchanters, magicians, or
astrologers" (v27), and "the wise men of Babylon" as the standing collective term from v12 on. The
whole group is threatened together (v5), sought together (v13), destroyed together (v12-13), and
Daniel is later made "chief prefect over **all** the wise men of Babylon" (v48) — the narrative
treats them as one body throughout. **Recommendation (adopted below): ONE `named_collection` HIB,
"the wise men of Babylon,"** spanning every verse where any of these titles appears, with the
professional-title variation noted as description of the same collective, not separate HIBs. This
parallels Dan 8's "the four kingdoms" (id 27) — one collective HIB despite naming distinct
constituents. **Open to override** — the alternative is genuinely defensible (treat "the Chaldeans"
in vv4-11 as a narrower, distinct sub-collective from "the wise men of Babylon").

**JC2 — v36 "we will tell the king its interpretation."** Lexically confirmed 1st-person **plural**
(`H0560 AVqi1cp`) — not a majestic/idiomatic singular. Live readings: (a) Daniel + his three
companions (who prayed jointly for the mystery, vv17-18, 23) — **adopted below**; (b) Daniel +
God, the actual revealer; (c) a formal/idiomatic Aramaic plural with no real second party. Adopting
(a) on the strength of vv18/23 already establishing the four as a joint party in this same episode;
(b) and (c) are on record as live alternatives, not asserted.

**JC3 — v13 "they sought Daniel and his companions, to kill them."** Lexically confirmed plain 3mp
(`H1156 AVqp3mp`), no named antecedent in this verse. Arioch — later identified (v14) as "the
captain of the king's guard, who had gone out to kill the wise men of Babylon" — is the natural
real-world referent, but v13 itself does not name him. **Adopted below: a one-verse
`implicit_collection` HIB, "the king's executioners"** (Step 1's own rule: name a referential HIB,
never assert an inferred identity as settled fact). Alternative: fold Dan.2.13 directly into
Arioch's own verse list as an anticipatory reference — rejected here because it would assert an
identity the verse doesn't itself state, but flagged as a live alternative.

**JC4 — generic/gnomic mentions excluded from HIB tracking.** v21 "the wise... those who have
understanding" (inside Daniel's doxology, a gnomic class, not a narratively present party) and v38
"the children of man" (inside Daniel's description of the king's God-given dominion, a totalizing
rhetorical category, not a discrete tracked party). **Adopted: excluded from the HIB register.**
Flagged because both are genuine human-noun mentions a stricter reading of the presumptive-candidate
rule could argue for including.

**JC5 — "the second kingdom" / "the third kingdom" / "the fourth kingdom" as `unnamed_collection`
HIBs**, representing the human rulers/peoples of each future kingdom in Nebuchadnezzar's image-
vision (v39 second and third; vv40-44 fourth/divided). This directly parallels the already-committed
Dan 8 pattern ("the four kingdoms," id 27; "the first king," id 26; "the bold-faced king," id 28) —
treating a prophetic kingdom/ruler as a trackable (unnamed) HIB. **Recommendation: adopt**, for
internal consistency with the precedent already in the DB. The kingdom "set up" by God in v44 (the
eternal kingdom) is **not** modeled as a HIB — it's explicitly God's own action/possession, not a
human dynasty in the same sense.

**JC6 — applied principle: a speaker counts as "present" through their own continuous quoted
speech**, even in sub-verses whose content is about a third party (e.g., Nebuchadnezzar present
throughout his own speech vv4-9 even where addressing the Chaldeans; Daniel present throughout his
own speech vv27-45 even while describing the kingdoms of the vision, not himself). This is why
Daniel's Dan 2 span below runs almost continuously from v13 to v49. Grounded in Step 1's own "speaks"
criterion, but it's a sweeping consequence worth confirming rather than assuming.

---

## Full draft register (Dan, whole book — repeats every existing row + Dan 2 additions)

### Unchanged (Dan 1 / Dan 8, no Dan 2 content) — repeated as-is, no note needed
Belshazzar(23) · the kings of Media and Persia(24) · the king of Greece(25) · the first king(26) ·
the four kingdoms(27) · the bold-faced king(28) · the people who are the saints(29) ·
Ashpenaz(50) · the youths(51) · Melzar (the steward)(55)

### Changed — same identity, Dan 2 verses added (reconciliation note: "extends Dan 1 coverage with
this HIB's Dan 2 appearances; same identity, not a correction")

| Label | id | Dan 2 verses added |
|---|---|---|
| Daniel | 47 | 13-32, 34-49 (all of 13-49 except missing v33 — JC6) |
| Nebuchadnezzar | 48 | 1-12, 14-16, 23-31, 34, 36-38, 41, 43, 45-49 |
| Hananiah | 52 | 13, 17, 18, 23, 49 |
| Mishael | 53 | 13, 17, 18, 23, 49 |
| Azariah | 54 | 13, 17, 18, 23, 49 |

### New

| Label | kind | verses | note |
|---|---|---|---|
| Arioch | named_individual | 14, 15, 24, 25 | captain of the king's guard |
| the wise men of Babylon | named_collection | 2,3,4,5,6,7,8,9,10,11,12,13,14,18,24,27,48 | JC1 |
| the king's executioners | implicit_collection | 13 | JC3 |
| the second kingdom | unnamed_collection | 39 | JC5 |
| the third kingdom | unnamed_collection | 39 | JC5 |
| the fourth kingdom | unnamed_collection | 40,41,42,43,44 | JC5 |

**Referent option on record for the wise men of Babylon / v4-11 "the Chaldeans":** reading adopted
= same collective as "the wise men of Babylon," textual grounds = v12-13's retrospective unification
("all the wise men of Babylon be destroyed" ties directly back to the group just addressed);
rejected alternative = "the Chaldeans" as a standing sub-collective distinct from the professional
class as a whole, textual grounds = v2's coordinated list treats "Chaldeans" as one class among four
named ones.

---

## Next step

If JC1-JC6 stand as adopted above, I'll write the full `hib.set` payload (with per-item
`quality_checks` attestations) to `iba/app/staging/operations/dan-2-hib.set.json` and rerun
`Debate-Run.ps1 -Book Dan -Chapters 2`. Flag any of JC1-JC6 you want resolved differently and I'll
adjust before writing.
