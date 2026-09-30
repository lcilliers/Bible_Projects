# mti_terms dedup (OT-DBR-009) — status & options — 2026-06-01

**Type:** status note (read-only investigation) · supersedes the migration-number assumption in `mti-terms-dedup-design-v1-20260420.md`.

## 1. The "M32" correction

The 2026-04-20 dedup design listed **"Migration number (tentative) M32"**. That number was **never used for the dedup**:

- `engine/migrate.py` **M32 = "Reference-as-Database POC: wa_vocab_set + wa_vocab_member"** (line 1090); M33–M35 = more reference-as-DB work; M36–M39 = other things.
- The only trace of the dedup in `migrate.py` is a comment (line 922): *"M32 mti_terms dedup is separate Change Plan (R)"* — i.e. it was deferred out of the M29/30/31 batch and **never picked up.**

**Conclusion: the dedup migration was designed (draft, 2026-04-20) but displaced and never implemented.** It has no migration number and no code. "Full M32" was a mislabel on my part — apologies. The work is an **unbuilt draft awaiting approval.**

## 2. Current duplication state (live DB, 2026-06-01)

| Metric | Value |
|---|---:|
| `mti_terms` rows | 7,581 |
| distinct Strong's | 3,965 |
| extra (duplicate) rows | 3,616 |
| strongs with >1 row | 1,780 |
| **strongs with >1 *LIVE* (delete_flagged=0) row** | **55** |

So **~3,561 of the 3,616 dup rows are already `delete_flagged=1` (inert)** — they don't affect live queries. The genuine active problem is the **55 strongs that have more than one *live* row** (ambiguous: which row is canonical for joins).

## 3. Important: this session created/exposed many of the 55

The 55 live-dup strongs include the **suffering family** (G3958 *paschō*, G3804, G3077, G2552/3, G3805, G4777, G3663), the **`qol` "voice" family** (H6963A/B/H/I/J/K/L), and the **`amal`/`atsav` toil family** (H5998, H6001B, H6031A, H6033, H6039, H6087B, H6089B, H6090B, H6092). These are exactly the **wrongly-deleted terms we rescued this session**: each had 2+ rows (e.g. G3958 = id 4032 reg163 + id 5932 reg115, both formerly `delete_flagged=1`). The span-rescue → FLAG → cluster-apply un-deleted **all rows of each strongs** and routed them to the same cluster, so a term that was a *fully-deleted dup* became a *live dup*. So a large chunk of the 55 is a direct, expected side-effect of the rescue — and cleaning them is the natural finish.

Full 55: G2552, G2553, G3077, G3663, G3804, G3805, G3806, G3844, G3958, G4777, G4862, H0197H, H0197I, H0206G, H1180, H2256C, H2258A, H2258B, H2259, H2260, H2470A, H2470B, H2470H, H2603B, H4245A, H4245B, H4251, H4714I, H4714J, H4865, H4941K, H5796, H5798G, H5808, H5822, H5998, H6001B, H6031A, H6033, H6039, H6087B, H6089B, H6090B, H6092, H6697G, H6944I, H6946H, H6963A, H6963B, H6963H, H6963I, H6963J, H6963K, H6963L, H7067G.

## 4. The draft design and why it can't be run as-is

The 2026-04-20 design is a **hard-delete migration** (Phase 4 = `DELETE ~3,616 rows`, point of no return) and:

- **DRAFT, awaiting approval** — §9 Q1–Q7 (incl. "approve the hard-delete?") never answered.
- **Its FK-repoint list is stale.** It lists 4 child tables (`mti_term_flags`, `mti_term_cross_refs`, `verse_context_group`, `verse_context`). Since 2026-04-20 the M49 work added **`mti_term_subgroup` (1,196 refs) and `vcg_term` (5,091 refs)** that also point at `mti_terms.id`. Running the old repoint would **orphan ~6,287 references.**

## 5. Options

**4a — full dedup migration (the draft, done properly).** Consolidate all 7,581 → 3,965. Requires: assign a real migration number, **refresh the FK list for the current schema** (add `mti_term_subgroup` + `vcg_term`), fresh backup, dry-run on a DB copy, answer §9, and **researcher sign-off before the hard-delete**. Thorough but a multi-step migration with an irreversible step.

**4b — scoped, reversible fix of the 55 live-dups (recommended now).** For each of the 55 strongs: pick the canonical live row (Rule A: OWNER `extracted` + registry FK, tie-break MIN(id)), **repoint its FK references** (incl. `mti_term_subgroup` + `vcg_term`) to the canonical, then **soft-delete** (not hard-delete) the redundant live rows. Clears the live ambiguity (and the dups this session created), **fully reversible**, no point-of-no-return. Leaves the ~3,561 inert deleted-dups for a future full migration if ever wanted.

## 6. Recommendation

**4b now.** It resolves the only part that actually interferes with analysis (the 55 live-dups, most of them from this session's rescue), is reversible, and avoids running a stale unapproved hard-delete migration. The full 7,581→3,965 consolidation (4a) stays a separately-scheduled, properly-approved migration — not a cleanup-session action.
