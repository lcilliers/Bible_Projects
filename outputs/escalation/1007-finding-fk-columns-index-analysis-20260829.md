# `finding`'s verse_context_id / mti_term_id / characteristic_id — index analysis

Investigated before touching anything, per your observation that these should be indexes rather
than direct columns. All three checked against live data; findings below, none applied yet.

## `verse_context_id` — your "index already exists" is right, but it's currently broken

`verse_context` (bible_research.db) is indeed the legacy, now-secondary table (`verse_record_id` +
`mti_term_id` per verse) — `iba.db`'s own `verse` table is the canonical one going forward. The
index you're thinking of is `finding_verse_link` (`finding_id`, `verse_record_id`, `reference`,
`role`) — it already exists, structurally correct, but:

- **Only 3,659 of the 435,193 VERSE-level findings have a `finding_verse_link` row at all** —
  everything else relies solely on the direct `verse_context_id` column, which is what we'd be
  dropping.
- **`finding_verse_link.verse_record_id` doesn't reliably point anywhere.** It resolves into
  `wa_verse_records.id` for only 73/3,659 rows (2%), and into `iba.verse.id` for 40/3,659 — and I
  checked those 40: they're coincidental id collisions, not real matches (e.g. `finding_verse_link.
  reference='Lev 11:26'` matched against an `iba.verse` row whose own reference is `'Hos 14:6'`).
  The numeric id in this column is effectively unreliable/junk for most rows.
- **A clean, verified path DOES exist**, just not through that broken column:
  `finding.verse_context_id → verse_context.verse_record_id → wa_verse_records.id`
  (100% resolves) `→ wa_verse_records.verse_id` (93% populated, 230,045/247,046) `→ iba.verse.id`.

**Plan, pending your go-ahead:** backfill `finding_verse_link` for all 435,193 VERSE-level findings
via that verified chain, into a **new** column (not the existing broken `verse_record_id` — reusing
it would inherit its unreliability) holding the resolved `iba.verse.id` directly. Only then drop
`finding.verse_context_id`. The 6.93% of `wa_verse_records` rows with no `verse_id` yet (~17,000)
would leave that many `finding` rows unbackfillable for now — same "don't drop what can't be
replaced yet" logic as the `wa_finding_catalogue_links` 743 rows earlier today.

## `mti_term_id` — 99.98% redundant with `verse_context`, confirmed

`verse_context.mti_term_id` matches `finding.mti_term_id` for all but 96 of 435,193 VERSE-level
findings (0.02%) — your read is correct, this is genuinely derivable via `verse_context_id`, not an
independent fact. Those 96 mismatches are worth a look before dropping (real disagreement, not
migration noise — same "check before you drop" discipline as above), but don't change the overall
picture.

**No existing finding→term index table** (unlike verse, nothing already plays this role).
`iba.db` does have a canonical term table (`strong`), bridgeable via `mti_terms.strongs_number`.
**Open question for you:** does the resolved `iba.strong.id` belong as a second new column on the
*same* `finding_verse_link` row (a VERSE-level finding's term is, after all, the term active in
that same verse occurrence) — or a separate link table? I'd lean toward the same row (one place to
look up both "which verse, which term" for a finding), but it's your data model.

## `characteristic_id` — genuinely different situation, added today

No existing index — because this column didn't exist before today (§203, the `cluster_finding`
migration). More importantly: **`iba.db` has no `characteristic` table at all** — only `cluster`/
`cluster_strong` exist there; the characteristic-level model hasn't migrated to IBA yet. So there's
no canonical IBA-side id to remap this into the way verse/term have. Options: (a) leave it as a
plain column for now, since there's nowhere else for it to live yet, or (b) build a
`bible_research`-local link table anyway, for shape-consistency with the other two, even without an
IBA-side id behind it yet. Your call — this one isn't a "the index already exists" case at all.

## Not yet done

Nothing has been changed. All three need a decision from you (verse/term have a clear target and
just need the backfill-then-drop sequencing agreed; characteristic doesn't have a target yet at
all) before I write any migration for this.
