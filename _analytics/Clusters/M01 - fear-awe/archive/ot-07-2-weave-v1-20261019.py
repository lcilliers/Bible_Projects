"""OT-07.2 weave (#2160): 10.12 v13 -> v14, Ch 11 v36 -> v37, Ch 2 v26 -> v27, 10.10 v31 -> v32.

Researcher, chat 2026-10-19 (verbatim): "#2168 approved: amend rule 73 and its guide with the three
points. Then weave OT-07.2 as proposed in v2 section 4." Proposal: section 4 of
ot-07-2-fe85-lam4-reading-v2-20261019.md. Each edit replaces an exact block; the script stops if a
block is not found exactly once. Old versions are moved to archive/.
"""
import pathlib
import shutil
import sys

sys.stdout.reconfigure(encoding="utf-8")
D = pathlib.Path(__file__).resolve().parents[3] / "_analytics/essay/spirit_soul_body/inner-being-narrative"


def edit(old_name, new_name, pairs):
    src = D / old_name
    text = src.read_text(encoding="utf-8")
    for old, new in pairs:
        n = text.count(old)
        if n != 1:
            sys.exit(f"{old_name}: block found {n} times: {old[:70]!r}")
        text = text.replace(old, new)
    (D / new_name).write_text(text, encoding="utf-8")
    shutil.move(str(src), str(D / "archive" / old_name))
    print(f"{old_name} -> {new_name}")


# ── 10.12 Fear: new section after "Fear that comes upon a person" ─────────────────────────────
F_OLD = """Chapter 2 carries the same verse as the approach of death.

## What fear does
"""
F_NEW = """Chapter 2 carries the same verse as the approach of death.

## Fear in the body

Fear is not only felt. It is seen, and the verses see it first in the hands.
- **The hands fall when the report comes.** The people's hands fall helpless at the report (Jeremiah 6:24, above). The same is said of an enemy king: "The king of Babylon heard the report of them, and his hands fell helpless; anguish seized him, pain as of a woman in labor" (Jeremiah 50:43).
- **The hands go with the heart.** "Therefore all hands will be feeble, and every human heart will melt. They will be dismayed: pangs and agony will seize them; they will be in anguish like a woman in labor. They will look aghast at one another; their faces will be aflame" (Isaiah 13:7–8). Ezekiel names the inner and the outer in one breath: "Every heart will melt, and all hands will be feeble; every spirit will faint, and all knees will be weak as water" (Ezekiel 21:7). "All hands are feeble, and all knees turn to water" (7:17).
- **The body takes up the posture of labour.** "Why then do I see every man with his hands on his stomach like a woman in labor? Why has every face turned pale?" (Jeremiah 30:6).
- **Fear is aimed at the hands.** Nehemiah's enemies "all wanted to frighten us, thinking, 'Their hands will drop from the work, and it will not be done.' But now, O God, strengthen my hands" (Nehemiah 6:9). God speaks to the same place: "Fear not, O Zion; let not your hands grow weak" (Zephaniah 3:16).
- **And the answer is given to the hands.** "Strengthen the weak hands, and make firm the feeble knees" (Isaiah 35:3). "Therefore lift your drooping hands and strengthen your weak knees" (Hebrews 12:12). Eliphaz says to Job, "you have instructed many, and you have strengthened the weak hands" (Job 4:3).

The Hebrew verb behind much of this anguish is *ḥûl*, "to twist, writhe". It is the writhing of a woman in labour, and the heart's anguish: "My heart is in anguish within me" (Psalm 55:4). In Lamentations it is said of hands. The ESV reads, "For the chastisement of the daughter of my people has been greater than the punishment of Sodom, which was overthrown in a moment, and no hands were wrung for her" (Lamentations 4:6). The Hebrew says that hands did not writhe in her or on her. I read two things the words allow: no one's hands writhed in grief over Sodom, or no human hand worked her fall, which came "in a moment". The English chooses the first. Either way the writhing of hands is the body's anguish, and the root carries it; "wrung" is the translator's word for it. Chapter 11 sets out the root's other faces.

The English can also hide the body. When Ish-bosheth heard that Abner had died, "his courage failed, and all Israel was dismayed" (2 Samuel 4:1). The Hebrew says his hands dropped.

I read the hands as the place where the verses let fear be seen: the work stops, the grip goes, the arms take the posture of pain. In these verses what weakens the hands is something heard: a report, news that is coming, a threat meant to frighten. What strengthens them is a word ("Fear not"), another person, or God asked to do it. Chapter 7 follows the body.

## What fear does
"""
edit("10-12-fear-v13-20261018.md", "10-12-fear-v14-20261019.md", [(F_OLD, F_NEW)])

# ── Ch 11 §4: the ḥûl bullet, and a compassion case under "What changes the character" ───────
C11_OLD = """(Chapter 2, *Changed*; 13.1, *Immortal*.)
"""
C11_NEW = """(Chapter 2, *Changed*; 13.1, *Immortal*.)
- **Writhing.** The Hebrew *ḥûl*, "to twist, writhe", is a woman in labour ("Writhe and groan, O daughter of Zion, like a woman in labor", Micah 4:10), the earth before God ("tremble before him, all the earth!", Psalm 96:9), and the heart in anguish (Psalm 55:4). It is also the daughters of Shiloh who come out "to dance in the dances" (Judges 21:21), "a whirling tempest" (Jeremiah 23:19), and patient waiting: "Be still before the Lord and wait patiently for him" (Psalm 37:7). Struck people can be without it: "You have struck them down, but they felt no anguish" (Jeremiah 5:3). One twisting is pain, trembling, birth, the dance and waiting (10.12, *Fear in the body*).
"""
C11_OLD2 = """- **Distress turns people both ways.** In distress Manasseh "humbled himself greatly" (2 Chronicles 33:12), and Ahaz "became yet more faithless" (28:22). The texts set the cases side by side without saying why."""
C11_NEW2 = """- **Distress turns people both ways.** In distress Manasseh "humbled himself greatly" (2 Chronicles 33:12), and Ahaz "became yet more faithless" (28:22). The texts set the cases side by side without saying why. Under siege, "The hands of compassionate women have boiled their own children" (Lamentations 4:10; 10.10)."""
edit("11-other-sides-of-the-inner-being-v36-20261019.md", "11-other-sides-of-the-inner-being-v37-20261019.md",
     [(C11_OLD, C11_NEW), (C11_OLD2, C11_NEW2)])

# ── Ch 2 Life weighed: Lam 4:9 ─────────────────────────────────────────────────────────────────
L_OLD = """And before God, "no one living is righteous before you" (Psalm 143:2). Chapter 12 follows this.
"""
L_NEW = """And before God, "no one living is righteous before you" (Psalm 143:2). Chapter 12 follows this.

A death can be weighed against a death. In the siege of Jerusalem, "Happier were the victims of the sword than the victims of hunger, who wasted away, pierced by lack of the fruits of the field" (Lamentations 4:9). The verse before says what the wasting was: "their skin has shriveled on their bones; it has become as dry as wood" (4:8). The same lament sets Zion's long punishment above Sodom's, "which was overthrown in a moment" (4:6). The quick death is called the happier one. The lingering is what makes it worse.
"""
edit("02-life-breath-and-death-v26-20261019.md", "02-life-breath-and-death-v27-20261019.md", [(L_OLD, L_NEW)])

# ── 10.10 Friends, company and care: Lam 4:10 ─────────────────────────────────────────────────
R_OLD = """The animals are set above the people. And the worker thirsts among what he makes for another"""
R_NEW = """The animals are set above the people. The same lament goes further: "The hands of compassionate women have boiled their own children; they became their food during the destruction of the daughter of my people" (Lamentations 4:10). The women are called compassionate, and the verse names when it happened: "during the destruction". I read the siege as what turned the hands of compassion. The verse does not explain it, and I do not try to. And the worker thirsts among what he makes for another"""
edit("10-10-relating-to-others-v31-20261018.md", "10-10-relating-to-others-v32-20261019.md", [(R_OLD, R_NEW)])
