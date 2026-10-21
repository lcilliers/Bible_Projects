"""claude_md_rules_to_config_v1_20261021.py -- escalation #2181 (option B of the #2179 review;
element of the IBA app reset, #2177): the rules CLAUDE.md held with no cfg_* home are moved into
config before CLAUDE.md is cut to a short entry file.

Researcher, 2026-10-21, verbatim: "There should be no instance of the same rule in multiple
documents." The control map (cfg_control_home, #2180) puts every rule in cfg_behaviour_rule and
makes CLAUDE.md pointers only. The pre-cut CLAUDE.md is kept as history at
archive/docs/claude-md-history-to-20261021.md (read only deliberately); the statement-by-statement
mapping of where each of its rules now lives is
outputs/escalation/2181-claude-md-content-homes-v1-20261021.md.

Builds:
  - cfg_behaviour_class 'study_method' (how study work -- strands, reading, weaving, the
    narrative -- is done), so the start routine can scope it (#2185).
  - 13 cfg_behaviour_rule rows: 1 filing (authoritative source), 12 study_method. Each rule's
    source carries the researcher's ruling and the escalation it came from, as CLAUDE.md held it.
  - cfg_setting governance.study_status: the study hold of 2026-10-19 (state, read at start).
  - cfg_behaviour_rule 74: matching threads before every unit pull is added to the text.
  - cfg_behaviour_rule enforced_by texts that said a rule was "delivered by CLAUDE.md": restated
    as delivered by the start routine (Start-Iba prints every active rule; the compliance file).

Every cfg_* write goes through configmaint.apply_logged(). Idempotent. One transaction.

Usage:
    python iba/app/migration/claude_md_rules_to_config_v1_20261021.py [--db PATH] [--dry-run]
"""
import argparse
import datetime
import pathlib
import sqlite3
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from iba.app.handlers.configmaint import apply_logged  # noqa: E402

DEFAULT_DB = r"C:\Bible_study_projects\iba\app\db\iba.db"
RUN_ID = "DEVMODE-2181-CLAUDE-MD-RULES-20261021"
NOW = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
MOVED = "Moved from CLAUDE.md 2026-10-21 (escalation #2181)."
DELIVERY = ("Context-delivered: printed in full at session start (Start-Iba.ps1) and restated in "
            "the session compliance file (rule 81).")

CLASS = ("study_method", None,
         "How study work is done: strands, verse reading, weaving, the inner-being narrative and "
         "its chapters. Distinct from llm_output (epistemic trust in generated content) and from "
         "development. Added 2026-10-21, escalation #2181, when CLAUDE.md's study rules moved to "
         "config.")

# class, rule_key, rule_text, source
RULES = [
    ("filing", "authoritative-source-only",
     "C:\\Bible_study_projects is the only authoritative source for the project. Every other copy "
     "is ignored by default: G:\\My Drive\\Bible_study_projects (an old copy, to be archived), "
     "G:\\My Drive\\Claude_Research (a working folder for other platforms; what duplicates this "
     "project or Zotero is to be archived), and study documents in %USERPROFILE%\\Zotero\\storage, "
     "Documents, Desktop and elsewhere on G:\\My Drive. A file from those places is used only when "
     "the researcher names it; even then Claude says it is outside the authoritative source and "
     "brings it into the project, with the researcher's approval, before relying on it.",
     "Researcher decision 2026-09-28 (CLAUDE.md banner); inventory "
     "research/investigations/file-location-inventory-*. " + MOVED),
    ("study_method", "fan-out-progressive-strands",
     "Analysis is fan-out / progressive-stream, not cluster by cluster: no cluster reading is "
     "started as such. The inner being is a web of interrelated activity; a strand is one strand of "
     "that web, with no start and no finish, taken in turn and explored; the fan-out follows as the "
     "picture develops; a strand may be diverted, and a 'distraction' may deserve a deeper look; all "
     "strands merge into one whole. Open items are parked focus areas. Cluster codes are anchor "
     "points, not goals. Capture is focused: nodes and observations are written per topic or "
     "strand as that strand is explored, with no generic whole-scope task and no backfill of "
     "earlier work. The ib_node principle (verse, surface, strong, subgroup = association, question "
     "= stream) is the central linkage.",
     "Researcher 2026-09-30 (#1899, #1900): 'Clusters were originally designed to allow for "
     "creating batches of similar words to be analysed. however the study of M02 and M20 shows that "
     "progressive stream analysis will provide better result without doing a large portion of "
     "unnecessary cluster based findings.' " + MOVED),
    ("study_method", "prose-only-on-instruction",
     "Prose is the researcher's: it is built up by the researcher as each area of focus develops. "
     "Claude writes no prose (the DB prose store, or a narrative chapter file) without a specific "
     "instruction. The inner-being narrative's chapter files are drafts written on the researcher's "
     "specific instruction; they are files, not the DB prose store.",
     "Researcher 2026-09-30 (CLAUDE.md fan-out banner). " + MOVED),
    ("study_method", "narrative-reset-and-weave-record",
     "The narrative is Inner Being in Operation, in chapter files under "
     "_analytics/essay/spirit_soul_body/inner-being-narrative/, written to the style guide "
     "(narrative.inner_being_style_guide_path). The original adjusts to the new, not the reverse; "
     "each unfounded claim is checked and restated; each later stream of work adds to it. Each "
     "strand updates the chapter files it touches (version bump, prior version archived) and records "
     "the weave in the narrative claim register in the same pass "
     "(Narrative-Register.ps1 -Action Record -File <the weave's update JSON> -By Claude). A "
     "chapter's purpose is read in narrative_chapter before material is placed in it (rule 78). The "
     "researcher's own pictures (e.g. 'umbrella') are not narrative terms: the verses' own phrases "
     "are used.",
     "Researcher 2026-09-30 (#1912, #1913, #1916): 'to original must adjust to the new, not visa "
     "versa'; 'new theme is the inner being in operation described through the voice of the "
     "bible'; 'each unfounded claim must be checked and restated'; 'Each next stream of work will "
     "add further updates to the narrative.' Register in iba.db #2110 (2026-10-13); chapter table "
     "#2155 (2026-10-18); pictures #1937 (2026-10-02). " + MOVED),
    ("study_method", "narrative-chapter-text-rules",
     "In the chapter text: unchecked original material stays in marked Held sections; quote wording "
     "is checked against the ESV text in iba.db verse; science chapters come later; the Holy Spirit "
     "study is separate, except that for 13.1 (the divine) the Spirit is part of it -- a verse about "
     "the Spirit's own acts is placed in 13.1, not set aside; Jesus is part of the divine and gets "
     "attention in Ch 13 -- his own acts get their 13.1 face, and Ch 10 keeps the human side.",
     "Researcher 2026-09-30; 2026-10-08 (#1986): 'for the purpose of 13.1 (the divine) the Holy "
     "Spirit or Spirit is part of it, and should not be left untouched'; 2026-10-15 (#2148): 'also "
     "note that Jesus is part of divinity and need attention in Ch 13.' " + MOVED),
    ("study_method", "weave-not-fit",
     "A new item is woven into the narrative, knowing there is more to come; it is never fitted to "
     "where it supports the current narrative. Every observation from a strand gets a recorded "
     "placement; 'does not fit' is never one -- it means the narrative's structure must change. Each "
     "strand re-reads the sections it touches, and they adjust to it. Ch 10 is designed to grow. A "
     "strand is woven by activity and never given a file or chapter of its own, except that a key "
     "characteristic gets its full account as its own Ch 10 sub-chapter (as 10.12 Fear, 10.13 "
     "Anger, 10.14 Humility, 10.15 Pride), with its angles also woven into the chapters they belong "
     "to, in context. Method: _analytics/essay/spirit_soul_body/"
     "wa-essay-narrative-weave-method-and-ch10-structure-*.",
     "Researcher 2026-09-30 (#1918): 'Adding additional items is not a process of where does the "
     "new item support the current narrative - this is the wrong way around - it must be wove the "
     "new item into the narrative - knowing there is more to come.' #1920 (2026-10-01); #1961 "
     "(2026-10-04): 'encapsulate the full finding of fear ... into a separate Ch10 sub chapter.' "
     + MOVED),
    ("study_method", "change-of-character-recorded",
     "How the meaning or application of the same word or concept changes in different circumstances "
     "is a key discovery and is built upon, never set aside. Every strand records each word's or "
     "concept's faces, the circumstances that differ, and why. A word's meaning is never taken from "
     "its cluster tag, since a tag shows one face only. Ch 11 section 4 ('What changes the "
     "character') is the cross-cutting account every strand adds to; the ledger is "
     "_analytics/cross-cluster-web/origin-of-thought/origin-of-thought-change-of-character-*.",
     "Researcher 2026-10-01 (#1919): 'One of the key discoveries in the study is how the meaning or "
     "application of the same concept / word changes in different circumstances ... This should not "
     "be lost ... It must be built upon, not be set aside.' " + MOVED),
    ("study_method", "weaving-carries-meaning",
     "Weaving applies the appropriate parts of the ledger work into other sections with "
     "interpretation; it is not a list of quotes or a mechanical mix and match. Rule 69 forbids "
     "joining verses into patterns no verse states; it does not forbid saying what a verse means in "
     "its own setting -- that interpretation is required. A phenomenon gets one coherent account "
     "answering what Scripture says it is, its forms from the words themselves, and why they differ. "
     "Other sections carry only the parts that belong to their activity, rewritten as prose with "
     "chosen verses, pointing back to the account; full verse lists stay in the ledger. A verse that "
     "says nothing about the inner being or the word stays in the data. Readings beyond what a verse "
     "states are marked 'I read'.",
     "Researcher 2026-10-01 (#1930): 'We lost meaning and interpretation, it is starting to just "
     "become a list of quotes'; 'weaving means applying into other sections appropriate parts - it "
     "does not say you must ignore all the work that was done and listed in the ledger.' " + MOVED),
    ("study_method", "narration-probes-not-restates",
     "Narration is done from the perspective of the inner being's workings: restating a verse is not "
     "narration. Each item is thought about with probing questions -- compare; why different; what "
     "lies behind it; whether the relationships make a difference -- and figurative speech is "
     "explored, not restated. Each verse is read in its whole passage, with no reading framework laid "
     "over it; the account grows from the readings. A gap often sits in the neighbouring verses of a "
     "marked verse, so the whole passage is read.",
     "Researcher 2026-10-09 (M18/M25): 'the narration must be done from the perspective of the inner "
     "being workings - merely restating the verse is not a proper narration ... it is especially "
     "important to not just restate figurative speach but explore it.' 2026-10-07 (#1978): 'maybe I "
     "must leave you alone to do your thing, and then work with the outcome.' " + MOVED),
    ("study_method", "no-unnecessary-holding",
     "Items are not held unnecessarily: verses or items that bear on the work in hand are read while "
     "the strand is busy with them, and accumulating outstanding items are completed, not parked "
     "behind another step.",
     "Researcher 2026-10-09: 'OT-95 just read these verses while you are busy with it, don't hold "
     "things unnecessarily. OT-15 why are you holding this? ... complete all these accumulating "
     "outstanding items'. " + MOVED),
    ("study_method", "strand-checks-its-m47-verses",
     "For each strand as it is taken up, its M47 (inner seat) verses are checked for dropped "
     "placements, by word and not by citation (a narrative citation is verse-level, not word "
     "coverage), as was done for M64 (#1989). The record is on OT-09.",
     "Researcher 2026-10-08, closing #1979: 'I will tackle them as we move through the clusters.' "
     "#1987: 'assuming the verse is already in the narrative and therefore should be ignored, is "
     "wrong.' " + MOVED),
    ("study_method", "strand-pull-scans-glosses-across-codes",
     "Before a theme is read, the glosses are scanned across all cluster codes, M and T alike: words "
     "for the theme may sit in T-codes that no strand ever pulled (e.g. the dead/die words, G3498 "
     "nekros and 16 others, found only when the researcher asked).",
     "OT-02 (#2003), 2026-10-14: the researcher asked whether 'spiritual death', 'dead to sin', "
     "'causes of death' were covered; they were not. " + MOVED),
    ("study_method", "verse-sets-only-through-raw-layer",
     "A strand's verse sets come only through the app's raw layer (New-Word, strong.reconcile), "
     "never through an inline STEP call.",
     "#2163 (2026-10-18): the step-0 STEP check of #2162 was outside the app and is superseded. "
     + MOVED),
]

STATUS_KEY = "governance.study_status"
STATUS_VALUE = (
    "ON HOLD since 2026-10-19. Researcher, verbatim: 'you have officially been put on hold until I "
    "have the enthusiasm and the will power to re-open the study.' No study work (readings, weaves, "
    "strands, audits) is started, continued or proposed until the researcher re-opens it. Reason "
    "and state at hold: escalation #2172 (readings did not reliably reach the narrative and the "
    "claims register; no control enforces completeness); #2171 (M07/M53) trial and batch 1 read, "
    "nothing woven.")
STATUS_USE = ("Whether the study is active or on hold, and why. Read at session start (module "
              "governance). Changed only on the researcher's instruction. Moved from the CLAUDE.md "
              "banner 2026-10-21 (escalation #2181).")

R74_ADD = (" Before every unit pull of a strand, the threads that bear on it are matched "
           "(Escalation.ps1 -Action Match -Cluster .. -Strong .. -Verse ..; -For nnnn records the "
           "match); held items and researcher questions are raised as threads at every ledger "
           "approval (Escalation.ps1 -Action Raise -Type thread).")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=DEFAULT_DB)
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    conn = sqlite3.connect(a.db)
    if a.dry_run:
        print(f"DRY RUN -- would add class {CLASS[0]}, {len(RULES)} rules, {STATUS_KEY}")
        return 0
    n = 0
    one = lambda sql, p=(): conn.execute(sql, p).fetchone()  # noqa: E731
    with conn:
        if not one("SELECT 1 FROM cfg_behaviour_class WHERE class=?", (CLASS[0],)):
            apply_logged(conn, RUN_ID, "cfg_behaviour_class", "insert", {}, {
                "class": CLASS[0], "authoritative_doc": CLASS[1], "description": CLASS[2],
                "added_at": NOW, "inactive": 0}); n += 1
        for cls, key, text, src in RULES:
            if not one("SELECT 1 FROM cfg_behaviour_rule WHERE class=? AND rule_key=?", (cls, key)):
                apply_logged(conn, RUN_ID, "cfg_behaviour_rule", "insert", {}, {
                    "class": cls, "rule_key": key, "rule_text": text, "source": src,
                    "enforced_by": DELIVERY, "added_at": NOW, "active": 1,
                    "enforcement_status": "context_delivered"}); n += 1
        if not one("SELECT 1 FROM cfg_setting WHERE key=?", (STATUS_KEY,)):
            import json
            apply_logged(conn, RUN_ID, "cfg_setting", "insert", {}, {
                "key": STATUS_KEY, "value": json.dumps(STATUS_VALUE), "use": STATUS_USE,
                "module": "governance", "inactive": 0}); n += 1
        r74 = one("SELECT rule_text FROM cfg_behaviour_rule WHERE id=74")
        if r74 and "Before every unit pull" not in r74[0]:
            apply_logged(conn, RUN_ID, "cfg_behaviour_rule", "update", {"id": 74},
                         {"rule_text": r74[0] + R74_ADD}); n += 1
        for rid, eb in conn.execute("SELECT id, enforced_by FROM cfg_behaviour_rule WHERE active=1 "
                                    "AND enforced_by LIKE '%CLAUDE.md%'").fetchall():
            new = (eb.rstrip() + " [2026-10-21, #2181: CLAUDE.md no longer carries rule text; "
                   "delivery is the start routine -- Start-Iba.ps1 prints every active rule, "
                   "restated in the compliance file (rule 81).]")
            if "#2181: CLAUDE.md no longer" not in eb:
                apply_logged(conn, RUN_ID, "cfg_behaviour_rule", "update", {"id": rid},
                             {"enforced_by": new}); n += 1
    print(f"{n} audited cfg_* write(s) (run {RUN_ID})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
