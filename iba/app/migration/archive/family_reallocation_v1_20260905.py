"""family_reallocation_v1_20260905.py — ONE-OFF. Researcher-directed rebuild of the M-cluster
taxonomy from the heuristic family-grouping exercise (2026-09-05, same session as escalation
#1006's cluster-subgroup review). Full method and evidence trail:
`_analytics/clusters/m01-m47-family-grouping-iteration-v1-20260905.md` and the three CSVs beside
it (`m01-m47-strong-family-v1/v2/v3-20260905.csv`).

**What this does and why.** The family-grouping pass (an ordered, first-match-wins regex ruleset
applied to every M01-M47 strong's `stepGloss`, reused from `_apply_ib_char_family_grouping_v1_
20260711.py`'s own technique) classified 2,971 strongs into 78 evidence-checked families, each
quantified against the live corpus. Comparing each family back to its members' ORIGINAL M-cluster
tags showed most families concentrate heavily in one parent M-code — confirming the old numbering
mostly still fits, just too coarsely named — while several old clusters have genuinely split into
multiple distinct families (M05 "Love" -> kindness-gentleness-friendship / grace-mercy-compassion
/ love-devotion / encouragement-edification; M10 "Sin" -> three ways; M15 "Wisdom" -> four ways;
etc.). Researcher's own framing: *"it feels wrong to abandon the existing clusters... keep the
existing cluster numbers, but extend it to the full 80 or so... reallocations, reset the naming
[are OK to] fit the representative terms."*

**The rule applied** (confirmed with the researcher before building): for every old M-code with
more than one family claiming it as their dominant parent, the LARGEST family (by member count)
keeps the number and the cluster's `short_name`/`description` are reset to match it; every other
sibling family gets a brand-new code, continuing sequentially from M48. A family with no genuine
dominant parent (spread thinly across many old clusters) also gets a new code. Result: 41 families
keep an existing M-code (renamed), 37 get new codes M48-M84 — 78 total, up from 47.

**7 old M-codes are left completely untouched**: M10b, M10c, M17, M27, M29, M31, M32 — none of the
78 families has any of these as its dominant parent (their prior membership dissolved into other
families or into T2/T7/T8/unassigned). Deliberately NOT touched here — M10b/M10c specifically are
the same known-anomalous legacy artefact the M10bc cluster review (`iba/app/reports/m10bc-cluster-
review-20260813.md`) already flagged as an open question for the researcher; folding that decision
into this migration was avoided on purpose, per `feedback_dont_bake_design_judgment_calls_into_
code_fixes` — a separate, explicit decision, not a side effect of this one.

**Write mechanics, per strong, per family membership** (never a blind bulk overwrite):
  - member's current cluster_code == its family's dominant parent, family WON that code
      -> no write; the existing row is already correct, and the cluster's rename covers it.
  - member's current cluster_code == its family's dominant parent, family LOST that code
      -> that row is now WRONG (the code now names a different family) -- soft-deleted, and a
         fresh row inserted under the family's own new code.
  - member's current cluster_code != its family's dominant parent (a minority member whose own
    cluster's mode isn't this family) -> its existing tag is untouched (a different, still-valid
    fact) and a NEW row is added under the family's resolved code -- additive, never a removal.
  - the 47 T2/T7/T8 reclassifications (place/person names, body parts, divine/idol references,
    generic human-relational terms -- read individually, not guessed) get an additive
    `cluster_strong` row under the existing T2/T7/T8 codes, skipped if already present.
  - the 331 residual UNASSIGNED strongs get no write at all -- left exactly as they were, per the
    researcher's own instruction ("the remaining for now can be unassigned").

Idempotent: checks the live `cluster` table for M48 before doing anything (a no-op if this has
already run).

    python -m iba.app.migration.family_reallocation_v1_20260905
"""

from __future__ import annotations

import csv
import datetime
import re
import sqlite3
import sys
from collections import Counter, defaultdict

from ..lib.cfg import DB_PATH

CSV_PATH = "_analytics/clusters/m01-m47-strong-family-v3-20260905.csv"

# family -> (short_name, description). short_name is a readable title from the family slug;
# description restates the family's own matching scope in one line, for anyone reading `cluster`
# directly without cross-referencing the CSV/analysis doc.
FAMILY_META = {
 'inner-seat-heart-soul-spirit': ('Inner Seat', 'The heart/soul/spirit/inward parts as the seat of inner life'),
 'trust-refuge-security': ('Trust & Refuge', 'Trust, reliance, refuge, security, taking shelter'),
 'hope-waiting': ('Hope & Waiting', 'Hope, waiting, expectation'),
 'fear-of-god-awe': ('Fear & Awe', 'Fear, dread, terror, awe, reverence, panic, shuddering'),
 'worship-prostration-service': ('Worship & Service', 'Worship, prostration, bowing, ministering, service'),
 'praise-extol-sing': ('Praise & Song', 'Praise, extolling, exalting, singing, making music'),
 'thanksgiving': ('Thanksgiving', 'Giving thanks'),
 'blessing-benediction': ('Blessing', 'Blessing, benediction'),
 'joy-gladness': ('Joy & Gladness', 'Joy, gladness, rejoicing, exultation, laughter, delight'),
 'faith-faithfulness-truth': ('Faith & Faithfulness', 'Faith, belief, faithfulness, being true, godliness'),
 'love-devotion': ('Love & Devotion', 'Love, devotion, cleaving to, affection'),
 'grace-mercy-compassion': ('Grace & Mercy', 'Grace, mercy, compassion, pity, favor'),
 'desire-longing-appetite': ('Desire & Longing', 'Desire, craving, longing, thirst, hunger, appetite, zeal'),
 'prayer-petition-crying-out': ('Prayer & Petition', 'Prayer, petition, crying out, pleading, supplication'),
 'being-heard-listening': ('Being Heard', 'Hearing, listening, being heard, being answered'),
 'knowing-understanding': ('Knowing & Understanding', 'Knowing, understanding, discerning, considering, meditating'),
 'wisdom-folly-teaching': ('Wisdom & Folly', 'Wisdom, folly, teaching, instruction, counsel, discipline'),
 'sloth-diligence-industry': ('Sloth & Diligence', 'Slothfulness, laziness, diligence, industriousness'),
 'wealth-poverty-riches': ('Wealth & Riches', 'Wealth, riches, prosperity, treasure, abundance'),
 'memory-remembrance': ('Memory (act)', 'Remembering, forgetting, calling to mind'),
 'speech-mouth-tongue': ('Speech & Tongue', 'Speaking, the mouth/tongue/lips, declaring, telling'),
 'walk-way-conduct': ('Walk & Conduct', 'Walking, one’s way/path, conduct, journeying, straying'),
 'keeping-guarding-vigilance': ('Keeping & Guarding', 'Keeping, guarding, watching, vigilance'),
 'torah-obedience-word': ('Torah & Obedience', 'Obeying commands/statutes/law/decree'),
 'righteousness-integrity': ('Righteousness & Integrity', 'Righteousness, uprightness, blamelessness, integrity, justice'),
 'sin-guilt-iniquity': ('Sin & Guilt', 'Sin, iniquity, transgression, guilt, trespass'),
 'shame-confusion': ('Shame & Confusion', 'Shame, confusion, disgrace, reproach, dishonor'),
 'confession-forgiveness': ('Confession & Forgiveness', 'Confession, forgiveness, pardon, atonement'),
 'rebellion-stubbornness': ('Rebellion & Stubbornness', 'Rebellion, stubbornness, refusal, rejection, forsaking'),
 'wickedness-ungodliness': ('Wickedness', 'Wickedness, ungodliness, vileness'),
 'malice-enmity-persecution': ('Malice & Enmity', 'Hatred, enmity, persecution, contempt, hostility, scorn'),
 'pride-arrogance-scoffing': ('Pride & Arrogance', 'Pride, arrogance, haughtiness, boasting, scoffing, self-exaltation'),
 'deceit-falsehood': ('Deceit & Falsehood', 'Deceit, lying, falsehood, cunning, treachery, hypocrisy'),
 'anger-wrath-vexation': ('Anger & Wrath', 'Anger, wrath, rage, indignation, quarreling, vexation'),
 'violence-cruelty': ('Violence & Cruelty', 'Violence, cruelty, destruction, killing, wounding'),
 'humility-lowliness-contrition': ('Humility & Lowliness', 'Humility, lowliness, meekness, contrition, being needy/poor'),
 'rest-stillness-peace': ('Rest & Peace', 'Rest, stillness, quiet, peace, calm'),
 'strength-courage-steadfastness': ('Strength & Courage', 'Strength, courage, might, power, steadfastness'),
 'faint-despair-languishing': ('Faintness & Despair', 'Fainting, languishing, despair, distress, weariness, toil'),
 'grief-lament-sorrow': ('Grief & Lament', 'Grief, mourning, weeping, lament, sorrow, wailing, torment'),
 'turning-repentance': ('Turning & Repentance', 'Turning, returning, repenting'),
 'restoration-revival-satisfaction': ('Restoration & Revival', 'Restoring, reviving, healing, satisfying, delivering'),
 'seeking-inquiring': ('Seeking & Inquiring', 'Seeking, inquiring, searching'),
 'lifting-bearing': ('Lifting & Bearing', 'Lifting, bearing, carrying, sustaining'),
 'will-resolve-vow-intent': ('Will & Resolve', 'Resolve, purpose, intent, determination, vowing, choosing'),
 'being-searched-tested-by-god': ('Being Tested', 'Being searched, tried, tested, proven, examined'),
 'entrustment-committing': ('Entrustment', 'Entrusting, committing, casting one’s way upon another'),
 'life-death-vitality': ('Life & Death', 'Life, death, dying, vitality, perishing'),
 'light-darkness-inner': ('Light & Darkness', 'Light, darkness, gloom, shadow (inner sense)'),
 'authority-dominion-rule': ('Authority & Dominion', 'Authority, dominion, kingship, rule, reigning, lordship'),
 'kindness-gentleness-friendship': ('Kindness & Friendship', 'Kindness, gentleness, friendship, hospitality, tenderness, doing good'),
 'encouragement-edification': ('Encouragement', 'Encouraging, building up'),
 'sickness-weakness-infirmity': ('Sickness & Weakness', 'Illness, sickness, disease, weakness, blindness, infirmity'),
 'corruption-perversion-immorality': ('Corruption & Perversion', 'Adultery, corruption, perversion, unfaithfulness'),
 'reasoning-judgment-interpretation': ('Reasoning & Interpretation', 'Reasoning, discussing, deciding, interpreting, advising'),
 'purity-holiness-sanctification': ('Purity & Holiness', 'Purity, purification, sanctification, holiness'),
 'judgment-condemnation-justice': ('Judgment & Condemnation', 'Judging, condemning, justifying, avenging, vengeance'),
 'envy-greed-excess': ('Envy & Greed', 'Envy, greed, lust, fornication, self-indulgence'),
 'astonishment-wonder-marvel': ('Astonishment & Wonder', 'Astonishment, marveling, wonder'),
 'dishonor-mutilation-disgrace': ('Dishonor & Disgrace', 'Dishonor, mutilation, filth, reviling, disgrace'),
 'disobedience-hardness-lawlessness': ('Disobedience & Lawlessness', 'Disobedience, hardening, lawlessness, insubordination'),
 'patience-endurance-perseverance': ('Patience & Perseverance', 'Patience, perseverance, enduring'),
 'stumbling-trial-temptation': ('Stumbling & Trial', 'Stumbling, trial, temptation, enticement'),
 'slavery-bondage-burden': ('Slavery & Bondage', 'Slavery, bondage, enslaving, burden'),
 'salvation-ransom-propitiation': ('Salvation & Ransom', 'Salvation, ransom, propitiation, redeeming'),
 'gift-favor-goodwill': ('Gift & Favor', 'Gift, favor, goodwill, goodness'),
 'remembrance-reminder-report': ('Reminder & Report', 'Reminding, news, tidings, report'),
 'prophecy-vision-interpretation': ('Prophecy & Vision', 'Prophesying, prophecy, interpretation, insight, sign'),
 'outcry-roaring-shouting': ('Outcry & Shouting', 'Outcry, roaring, shouting, moaning'),
 'covenant-fellowship-unity': ('Covenant & Fellowship', 'Covenant, brotherhood, fellowship, sharing, unity'),
 'renewal-transformation-change': ('Renewal & Transformation', 'Renewal, transformation, change, regeneration'),
 'self-control-sobriety-zeal': ('Self-Control & Zeal', 'Self-control, sobriety, fervency, eagerness'),
 'doubt-discouragement-worry': ('Doubt & Discouragement', 'Anxiety, discouragement, perplexity, doubt, worry'),
 'firstborn-foreknowledge': ('Firstborn & Foreknowledge', 'Firstborn status, foreknowledge, predetermination'),
 'destruction-ruin-devastation': ('Destruction & Ruin', 'Destruction, ruin, devastation, crime, error'),
 'truth-sincerity-certainty': ('Truth & Sincerity', 'Straightness, sincerity, certainty, confirmation'),
 'madness-recklessness-insanity': ('Madness & Recklessness', 'Madness, insanity, recklessness'),
 'fasting-piety-intercession': ('Fasting & Piety', 'Fasting, piety, intercession, asking, begging'),
 'glory-honor-splendor': ('Glory & Splendor', 'Glory, honor, splendor, greatness, adornment'),
 'release-relinquish-reconcile': ('Release & Reconciliation', 'Leaving, releasing, being reconciled'),
}


def main() -> int:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    already = conn.execute("SELECT 1 FROM cluster WHERE cluster_code='M48'").fetchone()
    if already:
        print("family_reallocation_v1_20260905: no-op — M48 already exists, already applied.")
        return 0

    rows = list(csv.DictReader(open(CSV_PATH, encoding="utf-8")))
    by_family: dict[str, list[dict]] = defaultdict(list)
    for r in rows:
        by_family[r["family"]].append(r)

    real_families = {f: m for f, m in by_family.items()
                     if f not in ("UNASSIGNED", "T2-generic-nonIB", "T7-divine", "T8-human-relational")}

    dominant_of: dict[str, str] = {}
    for fam, members in real_families.items():
        dominant_of[fam] = Counter(m["cluster"] for m in members).most_common(1)[0][0]

    by_dominant: dict[str, list[str]] = defaultdict(list)
    for fam, dom in dominant_of.items():
        by_dominant[dom].append(fam)

    final_code: dict[str, str] = {}
    winners: dict[str, str] = {}   # old_code -> winning family
    report: list[str] = []
    next_new = 48
    for code in sorted(by_dominant):
        fams_sorted = sorted(by_dominant[code], key=lambda f: -len(real_families[f]))
        winner = fams_sorted[0]
        final_code[winner] = code
        winners[code] = winner
        for loser in fams_sorted[1:]:
            newcode = f"M{next_new}"
            final_code[loser] = newcode
            next_new += 1

    # ── 1. Rename the 41 winner clusters ──────────────────────────────────────────────────
    for code, fam in winners.items():
        short, desc = FAMILY_META[fam]
        conn.execute("UPDATE cluster SET short_name=?, description=? WHERE cluster_code=?",
                    (short, desc, code))
    report.append(f"{len(winners)} existing clusters renamed to their winning family")

    # ── 2. Insert the 37 new clusters ─────────────────────────────────────────────────────
    new_codes = {f: c for f, c in final_code.items() if f not in winners.values()}
    for fam, code in new_codes.items():
        short, desc = FAMILY_META[fam]
        conn.execute(
            "INSERT INTO cluster (cluster_code, short_name, description, gloss, deleted) "
            "VALUES (?,?,?,NULL,0)", (code, short, desc))
    report.append(f"{len(new_codes)} new clusters inserted ({min(new_codes.values())}-{max(new_codes.values())})")

    # ── 3. Per-member writes ──────────────────────────────────────────────────────────────
    inserted = 0
    corrected = 0
    unchanged = 0
    for fam, members in real_families.items():
        code = final_code[fam]
        dom = dominant_of[fam]
        is_winner = winners.get(dom) == fam
        for m in members:
            strong = m["strong"]
            if m["cluster"] == dom:
                if is_winner:
                    unchanged += 1
                    continue
                # this family lost the shared old code -- its row there is now wrong
                conn.execute(
                    "UPDATE cluster_strong SET deleted=1 WHERE strong=? AND cluster_code=? AND deleted=0",
                    (strong, dom))
                corrected += 1
            exists = conn.execute(
                "SELECT 1 FROM cluster_strong WHERE strong=? AND cluster_code=? AND deleted=0",
                (strong, code)).fetchone()
            if not exists:
                conn.execute(
                    "INSERT INTO cluster_strong (strong, cluster_code, source, created_at, deleted, "
                    "confidence, operation, review_flag, rationale) "
                    "VALUES (?,?,?,?,0,'heuristic',0,0,?)",
                    (strong, code, "heuristic-family-grouping-v1-20260905",
                     now, f"family={fam}"))
                inserted += 1
    report.append(f"member rows: {unchanged} already correct, {corrected} corrected "
                 f"(stale tag removed), {inserted} new tags inserted")

    # ── 4. T2/T7/T8 reclassification (47 items, read individually — see the analysis doc) ──
    T_RECLASS = {
        'G2960': 'T7',
        'G1493': 'T2', 'G1494': 'T2', 'G1495': 'T2', 'G1496': 'T2', 'G1497': 'T2', 'G2712': 'T2',
        'H0457': 'T2', 'H1544': 'T2', 'H5566': 'T2', 'H6091': 'T2', 'H6456': 'T2', 'H6459': 'T2',
        'H4809G': 'T2', 'H4809H': 'T2', 'H7293': 'T2', 'H3477H': 'T2', 'H3027W': 'T2', 'H7218K': 'T2',
        'G1065': 'T2', 'G4007': 'T2', 'H0061': 'T2', 'G5600': 'T2', 'G4229': 'T2', 'H6640': 'T2',
        'G1888': 'T2', 'G1764': 'T2', 'G3873': 'T2', 'G3918': 'T2', 'G4840': 'T2', 'G4894': 'T2',
        'G2192': 'T2', 'G5607': 'T2', 'H6105A': 'T2', 'G1832': 'T2', 'H6819': 'T2',
        'H2256M': 'T2', 'H3499B': 'T2', 'H4340': 'T2', 'H5688': 'T2', 'H6616': 'T2', 'H6957A': 'T2',
        'H8615A': 'T2', 'G0080': 'T8', 'H0252': 'T8', 'H2416B': 'T8', 'H2416D': 'T8',
    }
    t_inserted = 0
    for strong, code in T_RECLASS.items():
        exists = conn.execute(
            "SELECT 1 FROM cluster_strong WHERE strong=? AND cluster_code=? AND deleted=0",
            (strong, code)).fetchone()
        if not exists:
            conn.execute(
                "INSERT INTO cluster_strong (strong, cluster_code, source, created_at, deleted, "
                "confidence, operation, review_flag, rationale) "
                "VALUES (?,?,?,?,0,'heuristic',0,0,?)",
                (strong, code, "heuristic-family-grouping-v1-20260905", now,
                 "no inner-being significance -- place/person name, body part, divine/idol "
                 "reference, or generic human-relational term"))
            t_inserted += 1
    report.append(f"T2/T7/T8 reclassification: {t_inserted} rows inserted "
                 f"({len(T_RECLASS)} identified, {len(T_RECLASS)-t_inserted} already present)")

    conn.commit()
    conn.close()

    print("family_reallocation_v1_20260905:")
    for line in report:
        print(f"  - {line}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
