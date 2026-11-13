"""collection_phrases_step4_2491_v1_20261113.py -- escalation #2491, plan v3 step 4 (phrases).

Researcher, 2026-11-13: 'Yes, step 4'. Rule of the researcher (#2491 v9/v11): a phrase is one concept, and the concept is placed in one collection;
it is not attached to the collections of each of its words. The phrase rule of #2437 (attach_phrases) put 3,134 phrase links into several collections;
here the 490 phrase surfaces that sat in two or more collections, the 34 whose only collection was dissolved, and the clear cases among the 106
study phrases in none were read by meaning, one by one, and each was given the one collection of its concept (PLACE) or, where it is a generic
phrase (set up, went up, come upon, lift up, to do) and not a behaviour or an inner-being state, was regrouped to other (OTHER). The lists are the ruling;
every ruling is inferential (B:4), none is made by a script rule. Phrases in exactly one collection are not touched. Phrases not listed stay as they are.
PLACE: the phrase keeps (or gets, as tier phrase) its link in the named collection and every other member link of the surface is set deleted.
OTHER: group other (group state corrected, reason kept) and every member link set deleted.
Then surface_term.collection_state and ib_node.collection_id (the exactly-one rule). Nothing is physically deleted. Stops and rolls back unless predicted
equals actual, every placed phrase is in exactly its one collection, and nothing except the regrouped phrases loses its collection. Idempotent.
    python -m iba.app.migration.collection_phrases_step4_2491_v1_20261113 [--db PATH] [--dry-run]   (from the project root)
"""
import argparse
import collections
import pathlib
import sqlite3
import sys

ROOT = next(p for p in pathlib.Path(__file__).resolve().parents if (p / "iba" / "app").is_dir())
sys.path.insert(0, str(ROOT))
from iba.app.lib import observationrecord as orec  # noqa: E402

DEFAULT_DB = pathlib.Path(r"C:\Bible_study_projects\iba\app\db\iba.db")
RUN_ID = "DEVMODE-2491-PHRASES-STEP4-20261113"
WHO = "devmode-2491"
MEMBER = ("core", "synonym", "opposite", "gathered", "phrase")
SRC = "researcher 2026-11-13 (#2491): step 4"

PLACE_LINES = """
performing: appear righteous
evildoer: done wickedly; done wickedness; own wickedness; wicked man; wicked men; wicked one; wicked person; wicked schemes; wicked woman; wicked women; doing evil; done evil; evil a; evil deeds; evil devices; evil man; evil men; evil person; evil purpose; me with evil purpose; more evil; speak evil; speaking evil; speaks evil against; do ill; till unrighteousness; vile person
righteous: practicing righteousness; righteous deeds; righteous judgment; righteous man; righteous one; righteous person; righteous persons; righteous person’s; righteous acts; righteous triumphs; good deed; good deeds; good man; good person
honor: dishonorable use; high esteem; high honor; high honors; honorable use; put them to shame; put to shame; more noble; most noble; noble things; open shame
anger: became angry; became enraged; became furious; become angry; burn hot; burned hot; anger is roused
unclean: became filthy; became unclean; become corrupt; become unclean; becomes unclean; defile himself; defiled themselves; take uncleanness
cleanse: become clean; purified himself; purify themselves; purify yourself; purify yourselves; made clean; made clear; purge out
believe: faith in; faith with; good faith; little faith
faithless: broken faith; broke faith
loyalty: faithful ones; remained steadfast; show faithfulness; steadfast love
thank: gave thanks; give thanks; give thanks to; give you thanks; given thanks; gives thanks
choose: has determined
condemn: have judged; judgment is; judgment on; pass judgment; passing judgment; enter into judgment; executing judgment; execute judgment; held guilty; incur guilt; guilt deserving; guilt of theirs
destruction: being destroyed; blotted out; tearing down; wasting away; wipe away; beaten down; desolate one; desolate places; devoted to destruction; dreadful end; tore down; utter ruin; working destruction; laying waste
bless: call her blessed; call him blessed; called blessed; called her blessed; called me blessed
abase: humble estate; humble mind; humble yourselves; humbled himself; humbled yourself; bowed down; brings low; brought low; humiliated her; laid low; might humble
live: come to life; live on; live peaceably; lives on; live quietly; remained alive
mighty: grew strong; grow strong; one stronger; stronger than; became strong; become strong; give strength; gives strength; made strong; mightier than; mighty strength; mighty work; more powerful; strong enough; valiant man; full vigor
watch: keep watch; keeping watch; keeps watch; kept watch; keep awake; stay awake; lie awake; wake up
upright: more upright; stand upright; upright is; upright man; made straight; make straight
kill: put him to death; put them to death; put to death; put you to death
guard: watch over; watched over; watches over; watching over; keep guard; whoever guards
rich: became poor; became rich; becomes poor; makes rich
wise: can discern; can feel; discerning men; deal wisely; dealt wisely; wise dealing; act wisely; learn prudence; sound wisdom; good sense
mute: fell silent; finished speaking; without meaning; keep silence; keep silent; kept silence; kept quiet; remained silent; stopped speaking
gladden: glad news; glad songs; rejoice together; made glad
godly: godly one; godly ones; show godliness
trust: leaning on; leans to; rest yourselves
sing: sing praise; sing praises; sing your praise; sing aloud
delight: take pleasure; takes pleasure; took pleasure; take delight; took delight; altogether joyful; delight in; great delight; great joy; joyful cry; joyous song; shout of joy; sing for joy; take joy; found favor; favored man; good will; wonderful things
combat: attacked him; might attack
lament: bitter tears; mourning aloud; groaning together; exceedingly sorry
witness: bear witness; bears witness; false testimony; false witness
submission: became obedient; become obedient; became subject
snatch: caught hold; lays hold
aloud: cry aloud; crying aloud; shout aloud; shouts aloud; raise shouts
desire: eager longing; yearn for; earnestly desire; heart’s desire; sinful desire; willing to; defiling passion; lustful talk
faint: fell helpless; sinks down; weak person; weak women; become discouraged; become weak; grown feeble; still weak
firm: firm covenant; stand firm; made firm; make firm
tenderhearted: gracious will; is gracious; find compassion; tender care; tender heart
tribulation: great distress; greatly distressed; hard pressed; pressed hard; suffered affliction; bring trouble; causes trouble; out of trouble
endure: heavy burdens; rested heavily; endure suffering; enduring evil; added burden; crushing burden
covered: hides himself; secret things; secret places; cover yourself; hides itself; seen exposed; without hiding
commend: high praise; high praises; offer praises; offered praises; give approval; give you praise; spoke well
hope: hoped for; hopes for; false hope
reverence: in awe; stood in awe; awesome things; fearful awe; reverent fear; kneel down; spiritual worship
heart: inner parts; inward parts; take heart; whole being
turn: perverse things; crooked ways
build: built up
know: made known; sound knowledge; be unaware; not recognized; can interpret; can read
quarrel: given us peace; given you peace; making peace; contended sharply
thought: minds on; setting your mind; gives thought; once regarded; mind on
partial: partial to; show partiality; showing favoritism
trial: produces character; proven worth; tested by his praise
counsel: take counsel; took counsel
blaspheme: utter blasphemies; uttered blasphemy
abominable: accursed ones
forgive: atoned for; forgiveness of sins; obtain mercy; propitiation for
care: attend to; take care
hear: attention to; kept hearing; paid attention; whoever heeds; you obey
shatter: broken down
rebel: not obey
sin: committed an offense; committed iniquity; done amiss; done wrong; no offense
sloth: complacent ones
pride: become proud; dealt proudly; lofty pride; proudly defied; puffed up; puffs up; arrogant people
scoff: deeply despised; suffer derision; with contempt; spoken against; speak against; speaks against; regard lightly
deceive: devious person
plot: devising evil; evil intent; evil plan; evil plot; malicious intent
folly: driven mad; foolish ones; foolish person; foolish women; foolish talk; outrageous fools; out of your mind
dry: dries up; parched ground
empty: empty nothings
govern: exercise authority
forsake: forsake them
backsliding: fall away; falling away; wickedly departed
greed: free from love of money; greedy for dishonest gain; shameful gain; not a lover of money; selfish ambition
share: freely given
offer: freely offered
skill: gained mastery; great ability; skilled in working
majesty: give glory; glorious presence; radiant appearance
teach: give instruction
rescued: give deliverance; brought safely
save: give salvation; restored me to life; working salvation; restored to life
warn: give warning
amazement: greatly amazed; marvelous works; wondrous things
love: greatly loved; one beloved; loathe my; loving kindness
innocent: guilty man; without blemish
jealous: had a grudge
dedicate: hallowed be; made holy; pure devotion; set apart
self-control: hold back; one’s regret; under control
justify: judged right
impartial: just measure; only justice
forget: let him remind
astray: led astray
continual: long continue; without ceasing
search: look for; looking for; earnestly seeks
earnest: earnest care
compel: insist on
intend: made plans
confess: made confession
magnify: might enlarge
hard: more severe
supplication: appealed to; can intercede; humble plea; makes petition; must plead; offer prayer; plea for mercy
pain: cause grief; must suffer; suffer harm; suffer want; share in suffering; bitter grief
labor: painful toil; take pains; working hard
lawless: outside the law
whoring: played the whore
wait: quietly wait
still: kept still
distinction: sees anything different
promise: sure oath; vowed willingly
real: speak sincerely
sober: sober judgment
stumble: took offense
strengthen: strong support
call: will invite; summoned him
disease: desperately sick; sick man
cruel: become cruel; cruel man; ruthless men
fear: free from anxieties; make them afraid; less anxious
die: yielded up
oppress: put in subjection
"""
OTHER = """laid it up; laid them down; lay aside; set down; mounts up; to do; more handsome; well disposed; breathes out; bringing up; bring up; brought up; can do; chased away;
cleaned out; come upon; far off; fell down; full measure; lift them up; lift up; lifted up; lifting up; lifts up; made long; prevented me; requiring decision; seek shelter; seems right;
sending away; set aside; set up; shown herself; spoke to; successfully accomplished; surpassing worth; taken shelter; therefore consider; treasured up; wake yourself; was priced; went up;
laid up; said nothing; say anything; say to; talked about; good things; grew up; grows up; grew warm; grew worse; grew fat; grown fat; full grown; better off; ever before; within you; seems good;
seemed good; could carry; binding on; tied up; more sure; life to; fixed provision; good purpose; legal right; outside his control"""
PLACE = {}
for line in PLACE_LINES.strip().splitlines():
    col, phrases = line.split(":", 1)
    for p in phrases.split(";"):
        p = p.strip()
        if p:
            if p in PLACE:
                raise SystemExit("phrase ruled twice: %s (%s, %s)" % (p, PLACE[p], col))
            PLACE[p] = col.strip()
OTHER_SET = {p.strip() for p in OTHER.replace("\n", " ").split(";") if p.strip()}
both = set(PLACE) & OTHER_SET
if both:
    raise SystemExit("phrase in both lists: %s" % sorted(both))


class Stop(Exception):
    pass


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=str(DEFAULT_DB))
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    conn = sqlite3.connect(a.db)
    conn.row_factory = sqlite3.Row
    q = lambda s, *p: conn.execute(s, p).fetchall()
    one = lambda s, *p: conn.execute(s, p).fetchone()[0]
    cname = {r["name"]: r["id"] for r in q("SELECT id, name FROM collection WHERE deleted=0 AND status IN ('indicative','confirmed')")}
    cid_name = {v: k for k, v in cname.items()}
    missing = sorted({c for c in PLACE.values() if c not in cname})
    if missing:
        raise Stop("collections not found: %s" % missing)
    rows_by_text = collections.defaultdict(list)
    text_of = {}
    for r in q("SELECT id, surface, surface_group FROM surface_term WHERE deleted=0"):
        rows_by_text[r["surface"]].append(r)
        text_of[r["id"]] = r["surface"]
    absent = sorted(p for p in list(PLACE) + sorted(OTHER_SET) if p not in rows_by_text)
    links_of = collections.defaultdict(list)
    for r in q("SELECT l.* FROM collection_link l JOIN collection c ON c.id=l.collection_id WHERE l.deleted=0 AND c.deleted=0 AND c.status IN ('indicative','confirmed') "
               "AND l.tier IN (%s)" % ",".join("?" * len(MEMBER)), *MEMBER):
        links_of[r["term_id"]].append(r)

    actions = []   # ("add", col, term, reason) | ("drop", link id, reason)
    regroup = []   # (term id, surface, group before, reason)
    regroup_ids = set()
    for p, kc in PLACE.items():
        k = cname[kc]
        for r in rows_by_text.get(p, []):
            ls = links_of.get(r["id"], [])
            if not any(l["collection_id"] == k for l in ls):
                actions.append(("add", k, r["id"], "the phrase %s is one concept, placed in %s (step 4, by meaning)" % (p, kc)))
            for l in ls:
                if l["collection_id"] != k:
                    actions.append(("drop", l["id"], "the phrase %s sits once, in %s (step 4, by meaning)" % (p, kc)))
    why_o = "a generic phrase (a motion, placing or plain-action phrase), not a behaviour or an inner-being state (researcher 2026-11-13, #2491 step 4)"
    for p in sorted(OTHER_SET):
        for r in rows_by_text.get(p, []):
            regroup_ids.add(r["id"])
            for l in links_of.get(r["id"], []):
                actions.append(("drop", l["id"], "the phrase %s is regrouped to other: %s" % (p, why_o)))
            if r["surface_group"] != "other":
                regroup.append((r["id"], p, r["surface_group"], why_o))

    def covered_set():
        own = {r[0] for r in q("SELECT DISTINCT l.term_id FROM collection_link l JOIN collection c ON c.id=l.collection_id WHERE l.deleted=0 AND c.deleted=0 "
                               "AND c.status IN ('indicative','confirmed') AND l.tier IN (%s)" % ",".join("?" * len(MEMBER)), *MEMBER)}
        out = set(own)
        for r in q("SELECT id, base_id FROM surface_term WHERE deleted=0"):
            if r["id"] in own or (r["base_id"] and r["base_id"] in own):
                out.add(r["id"])
        return out
    covered_before = covered_set()
    kinds = collections.Counter(a_[0] for a_ in actions)
    live_before = one("SELECT count(*) FROM collection_link WHERE deleted=0")
    pred = dict(actions=dict(kinds), regrouped=len(regroup), live_links_after=live_before + kinds["add"] - kinds["drop"])
    print("predicted:", pred, "| phrases placed:", len(PLACE), "| regrouped list:", len(OTHER_SET), "| not found as a surface:", absent)
    if not actions and not regroup:
        print("nothing to do (already applied)")
        return 0
    regrouped_before = one("SELECT count(*) FROM surface_event WHERE run_id=? AND action='set_group'", RUN_ID)
    conn.execute("SAVEPOINT w")
    try:
        now_sql = "strftime('%Y-%m-%dT%H:%M:%SZ','now')"
        touched = set()

        def ev(subject, sid, action, before, after, reason, field=None):
            conn.execute("INSERT INTO surface_event (subject_kind, subject_id, action, field, value_before, value_after, by, reason, run_id, created_by) "
                         "VALUES (?,?,?,?,?,?,?,?,?,?)", (subject, sid, action, field, before, after, "Claude", "%s (%s)" % (reason, SRC), RUN_ID, WHO))
        for act in actions:
            if act[0] == "add":
                _, col, t, reason = act
                nl = conn.execute("INSERT INTO collection_link (collection_id, term_id, tier, superseded_by_id, shared, reason, run_id, created_by) VALUES (?,?,'phrase',NULL,0,?,?,?)",
                                  (col, t, reason, RUN_ID, WHO)).lastrowid
                ev("collection_link", nl, "add", None, cid_name.get(col), reason, "collection_id"); touched.add(t)
            else:
                _, old, reason = act
                oc, t = conn.execute("SELECT collection_id, term_id FROM collection_link WHERE id=?", (old,)).fetchone()
                conn.execute("UPDATE collection_link SET deleted=1, updated_at=" + now_sql + ", run_id=? WHERE id=?", (RUN_ID, old))
                ev("collection_link", old, "remove", cid_name.get(oc), None, reason, "collection_id"); touched.add(t)
        for tid, p, before, why in regroup:
            conn.execute("UPDATE surface_term SET surface_group='other', group_state='corrected', group_judged_by='Claude (researcher direction, #2491)', group_reason=?, "
                         "updated_at=" + now_sql + ", run_id=? WHERE id=?", (why, RUN_ID, tid))
            conn.execute("INSERT INTO surface_event (subject_kind, subject_id, action, field, value_before, value_after, by, reason, run_id, created_by) VALUES "
                         "('surface_term',?,'set_group','surface_group',?,'other','Claude',?,?,?)", (tid, before, why + " (" + SRC + ")", RUN_ID, WHO))
            touched.add(tid)
        for t in touched:
            ls = q("SELECT l.collection_id, l.tier FROM collection_link l JOIN collection c ON c.id=l.collection_id WHERE l.term_id=? AND l.deleted=0 AND c.status IN ('indicative','confirmed')", t)
            strong = {r["collection_id"] for r in ls if r["tier"] in ("core", "synonym", "opposite")}
            if not ls:
                st = "untouched" if one("SELECT count(*) FROM surface_term WHERE id=? AND collection_state IS NOT NULL", t) else None
            elif len(strong) > 1:
                st = "shared"
            elif any(r["tier"] in MEMBER for r in ls):
                st = "placed"
            else:
                st = "listed_only"
            conn.execute("UPDATE surface_term SET collection_state=? WHERE id=? AND COALESCE(collection_state,'~')<>COALESCE(?,'~')", (st, t, st))
        cols_now = collections.defaultdict(set)
        for r in q("SELECT l.term_id, l.collection_id FROM collection_link l JOIN collection c ON c.id=l.collection_id WHERE l.deleted=0 AND c.deleted=0 "
                   "AND c.status IN ('indicative','confirmed') AND l.tier IN (%s)" % ",".join("?" * len(MEMBER)), *MEMBER):
            cols_now[r[0]].add(r[1])
        by_surface = collections.defaultdict(list)
        for r in q("SELECT id, surface, base_id FROM surface_term WHERE deleted=0"):
            by_surface[r["surface"]].append((r["id"], r["base_id"]))

        def carry(s):
            o = set()
            for sid, b in by_surface.get(s, []):
                o |= cols_now.get(sid, set()) | (cols_now.get(b, set()) if b else set())
            return o
        surf_touched = {text_of[t] for t in touched if t in text_of}
        changed_nodes = 0
        for n in q("SELECT id, observation_id, collection_id, lower(trim(surface)) AS s FROM ib_node WHERE deleted=0 AND surface IS NOT NULL AND trim(surface)<>''"):
            if n["s"] in surf_touched:
                cs = carry(n["s"])
                new = next(iter(cs)) if len(cs) == 1 else None
                if new != n["collection_id"]:
                    orec.log(conn, n["observation_id"], n["id"], "collection_id", n["collection_id"], new,
                             "each phrase is one concept in one collection (researcher 2026-11-13, #2491 step 4); the node carries the one collection of its surface, or none where it has none or several", None, RUN_ID, "Claude")
                    conn.execute("UPDATE ib_node SET collection_id=? WHERE id=?", (new, n["id"])); changed_nodes += 1
        got = dict(regrouped=one("SELECT count(*) FROM surface_event WHERE run_id=? AND action='set_group'", RUN_ID) - regrouped_before,
                   live_links_after=one("SELECT count(*) FROM collection_link WHERE deleted=0"))
        print("actual:   ", got, "| nodes whose collection changed:", changed_nodes)
        bad = [k for k in ("regrouped", "live_links_after") if got[k] != pred[k]]
        stranded = one("SELECT count(*) FROM collection_link l JOIN collection c ON c.id=l.collection_id WHERE l.deleted=0 AND c.status IN ('merged','retired') AND l.tier IN (%s)" % ",".join("?" * len(MEMBER)), *MEMBER)
        lost = sorted(text_of[t] for t in covered_before - covered_set() if t in text_of and t not in regroup_ids)
        notone = sorted(p for p in PLACE if rows_by_text.get(p) and any(len(cols_now.get(r["id"], set())) != 1 for r in rows_by_text[p]))
        print("member links on a merged or retired collection:", stranded, "| surfaces losing coverage (not regrouped):", len(lost), lost[:40],
              "| placed phrases not in exactly one collection:", len(notone), notone[:20])
        if bad or stranded or lost or notone:
            raise Stop("actual differs from predicted (%s), links stranded, coverage lost or a placed phrase not in one collection: rolled back" % bad)
        if a.dry_run:
            conn.execute("ROLLBACK TO w"); print("dry run: rolled back")
        else:
            conn.execute("RELEASE w"); conn.commit(); print("committed")
    except Exception:
        conn.execute("ROLLBACK TO w"); conn.commit(); raise
    return 0


if __name__ == "__main__":
    sys.exit(main())
