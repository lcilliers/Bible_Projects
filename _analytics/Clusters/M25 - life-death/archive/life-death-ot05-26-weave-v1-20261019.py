"""OT-05.26 weave (#2160): Ch 2 v25 -> v26, 13.1 v29 -> v30, Ch 11 v35 -> v36.

Researcher, chat 2026-10-19 (verbatim): "regarding OT-05.26 proceed with the weave." The proposal is
section 3 of life-death-ot05-26-body-raised-r0-v1-20261019.md. Each edit replaces an exact block of
the current file; the script stops if a block is not found exactly once. Old versions are moved to
archive/.
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


# ── Ch 2 ──────────────────────────────────────────────────────────────────────────────────────
CH2_OPEN_OLD = """- A few verses earlier, of other lords: "They are dead, they will not live; they are shades, they will not arise" (26:14).
- "After two days he will revive us; on the third day he will raise us up, that we may live before him" (Hosea 6:2).

Paul ties the raising of the body to the Spirit already living within: "If the Spirit of him who raised Jesus from the dead dwells in you, he who raised Christ Jesus from the dead will also give life to your mortal bodies through his Spirit who dwells in you" (Romans 8:11). The resurrection reaches the inner being before it reaches the body. God "has caused us to be born again to a living hope through the resurrection of Jesus Christ from the dead" (1 Peter 1:3). Chapter 14 follows that.
"""
CH2_OPEN_NEW = """- A few verses earlier, of other lords: "They are dead, they will not live; they are shades, they will not arise" (26:14).

Paul ties the raising of the body to the Spirit already living within: "If the Spirit of him who raised Jesus from the dead dwells in you, he who raised Christ Jesus from the dead will also give life to your mortal bodies through his Spirit who dwells in you" (Romans 8:11). The body's raising is still to come. But Paul also speaks of believers as raised already: they were "raised with him through faith in the powerful working of God" (Colossians 2:12), and God "raised us up with him and seated us with him in the heavenly places" (Ephesians 2:6). He draws from it at once where the mind is to be: "If then you have been raised with Christ, seek the things that are above, where Christ is, seated at the right hand of God. Set your minds on things that are above, not on things that are on earth" (Colossians 3:1–2). He prays that they may know "the immeasurable greatness of his power toward us who believe", the power "that he worked in Christ when he raised him from the dead" (Ephesians 1:19–20). Peter says the same of new birth. God "has caused us to be born again to a living hope through the resurrection of Jesus Christ from the dead" (1 Peter 1:3), "not of perishable seed but of imperishable" (1:23), "so that your faith and hope are in God" (1:21). Chapter 14 follows that.

### Believed, questioned, denied

The raising of the dead is not only told. It is met, and the verses show how people met it.
- **Denied.** Luke notes that "the Sadducees say that there is no resurrection, nor angel, nor spirit" (Acts 23:8). They brought Jesus a woman who had been married to seven brothers: "In the resurrection, therefore, of the seven, whose wife will she be?" (Matthew 22:28). He named the cause of their error: "You are wrong, because you know neither the Scriptures nor the power of God" (22:29). He answered from God's own words to Moses, "I am the God of Abraham, and the God of Isaac, and the God of Jacob" (Mark 12:26), and Luke adds, "Now he is not God of the dead, but of the living, for all live to him" (Luke 20:38).
- **Questioned, and understood later.** Coming down the mountain, the disciples "kept the matter to themselves, questioning what this rising from the dead might mean" (Mark 9:10). At the empty tomb, "as yet they did not understand the Scripture, that he must rise from the dead" (John 20:9). The understanding came afterwards. "When therefore he was raised from the dead, his disciples remembered that he had said this, and they believed the Scripture and the word that Jesus had spoken" (John 2:22). "Then he opened their minds to understand the Scriptures" (Luke 24:45). Paul still writes, "Remember Jesus Christ, risen from the dead" (2 Timothy 2:8).
- **Known, and believed.** Martha knew the teaching: "I know that he will rise again in the resurrection on the last day" (John 11:24). Jesus turned it to himself, "I am the resurrection and the life", and asked her, "Do you believe this?" She answered, "Yes, Lord; I believe that you are the Christ, the Son of God, who is coming into the world" (11:25–27).
- **Mocked, put off, thought incredible.** At Athens, "when they heard of the resurrection of the dead, some mocked. But others said, 'We will hear you again about this'" (Acts 17:32). Paul asks, "Why is it thought incredible by any of you that God raises the dead?" (Acts 26:8). He says he is on trial "with respect to the hope and the resurrection of the dead" (23:6).
- **Faith resting on it.** Paul puts the question to believers: "how can some of you say that there is no resurrection of the dead?" (1 Corinthians 15:12). He lets everything rest on it: "if Christ has not been raised, your faith is futile and you are still in your sins" (15:17); "If in Christ we have hope in this life only, we are of all people most to be pitied" (15:19). Teaching that "the resurrection has already happened" is "upsetting the faith of some" (2 Timothy 2:18).
- **Feared.** The chief priests had the tomb sealed, "lest his disciples go and steal him away and tell the people, 'He has risen from the dead'" (Matthew 27:64). When Herod heard of Jesus he said, "John, whom I beheaded, has been raised" (Mark 6:16), and "he was perplexed" (Luke 9:7). I read Herod's word as his conscience speaking, because it names the beheading.
- **A sign that moves people.** When John asked from prison, "Are you the one who is to come, or shall we look for another?", part of the answer was that "the dead are raised up" (Matthew 11:3, 5). After Lazarus was raised, "the chief priests made plans to put Lazarus to death as well, because on account of him many of the Jews were going away and believing in Jesus" (John 12:10–11).
"""

CH2_PSYCH_OLD = """Said of a person, the same word does carry blame: "The natural person does not accept the things of the Spirit of God" (1 Corinthians 2:14)."""
CH2_PSYCH_NEW = """Said of a person, the same word does carry blame: "The natural person does not accept the things of the Spirit of God" (1 Corinthians 2:14). James uses it of a wisdom that "is earthly, unspiritual, demonic" (James 3:15), and Jude of "worldly people, devoid of the Spirit" (Jude 19)."""

CH2_FIRST_OLD = """"But in fact Christ has been raised from the dead, the firstfruits of those who have fallen asleep" (1 Corinthians 15:20). "For as in Adam all die"""
CH2_FIRST_NEW = """"But in fact Christ has been raised from the dead, the firstfruits of those who have fallen asleep" (1 Corinthians 15:20). "For as by a man came death, by a man has come also the resurrection of the dead" (15:21). "For as in Adam all die"""

CH2_HOS_OLD = """"I shall ransom them from the power of Sheol; I shall redeem them from Death. O Death, where are your plagues? O Sheol, where is your sting?" (Hosea 13:14)."""
CH2_HOS_NEW = """"I shall ransom them from the power of Sheol; I shall redeem them from Death. O Death, where are your plagues? O Sheol, where is your sting? Compassion is hidden from my eyes" (Hosea 13:14)."""

CH2_CHANGED_OLD = """John says how much is still hidden: "what we will be has not yet appeared; but we know that when he appears we shall be like him, because we shall see him as he is" (1 John 3:2).
"""
CH2_CHANGED_NEW = """John says how much is still hidden: "what we will be has not yet appeared; but we know that when he appears we shall be like him, because we shall see him as he is" (1 John 3:2).

The word for the imperishable is not kept for the body. Paul blesses "all who love our Lord Jesus Christ with love incorruptible" (Ephesians 6:24). Peter speaks of new birth "not of perishable seed but of imperishable" (1 Peter 1:23), of "an inheritance that is imperishable, undefiled, and unfading" (1:4), and of "the imperishable beauty of a gentle and quiet spirit" (3:4). Chapter 11 sets the word beside its other uses. The immortality that "this mortal body must put on" (1 Corinthians 15:53) is said of God as his own: he "alone has immortality" (1 Timothy 6:16; 13.1).
"""

CH2_WAIT_OLD = """The raised body is waited for, and the waiting is felt within. "We ourselves, who have the firstfruits of the Spirit, groan inwardly as we wait eagerly for adoption as sons, the redemption of our bodies" (Romans 8:23)."""
CH2_WAIT_NEW = """The raised body is waited for, and the waiting is felt within. Paul sets the creation's waiting first. "For the creation waits with eager longing for the revealing of the sons of God", because "the creation itself will be set free from its bondage to corruption", and "the whole creation has been groaning together in the pains of childbirth until now" (Romans 8:19, 21–22). Then: "we ourselves, who have the firstfruits of the Spirit, groan inwardly as we wait eagerly for adoption as sons, the redemption of our bodies" (8:23)."""

CH2_WAIT2_OLD = """so that what is mortal may be swallowed up by life" (5:4). Sections 10.1 and 10.6 follow the groaning and the longing.
"""
CH2_WAIT2_NEW = """so that what is mortal may be swallowed up by life" (5:4). Sections 10.1 and 10.6 follow the groaning and the longing.

The hope is given as a reason for how a person lives now. Jesus tells a host to invite those who cannot repay: "and you will be blessed, because they cannot repay you. For you will be repaid at the resurrection of the just" (Luke 14:14). Some who were tortured refused release, "so that they might rise again to a better life" (Hebrews 11:35). Athletes exercise self-control "to receive a perishable wreath, but we an imperishable" (1 Corinthians 9:25). God gives eternal life "to those who by patience in well-doing seek for glory and honor and immortality" (Romans 2:7). Paul ends his chapter on the resurrection with the present: "Therefore, my beloved brothers, be steadfast, immovable, always abounding in the work of the Lord, knowing that in the Lord your labor is not in vain" (1 Corinthians 15:58).
"""

CH2_SECOND_OLD = """"The one who conquers will not be hurt by the second death" (Revelation 2:11)."""
CH2_SECOND_NEW = """"The one who conquers will not be hurt by the second death" (Revelation 2:11). "Blessed and holy is the one who shares in the first resurrection! Over such the second death has no power" (20:6)."""

edit("02-life-breath-and-death-v25-20261014.md", "02-life-breath-and-death-v26-20261019.md", [
    (CH2_OPEN_OLD, CH2_OPEN_NEW), (CH2_PSYCH_OLD, CH2_PSYCH_NEW), (CH2_FIRST_OLD, CH2_FIRST_NEW),
    (CH2_HOS_OLD, CH2_HOS_NEW), (CH2_CHANGED_OLD, CH2_CHANGED_NEW), (CH2_WAIT_OLD, CH2_WAIT_NEW),
    (CH2_WAIT2_OLD, CH2_WAIT2_NEW), (CH2_SECOND_OLD, CH2_SECOND_NEW)])

# ── 13.1 ──────────────────────────────────────────────────────────────────────────────────────
D131_INTRO_OLD = "It now also holds what the verses on humbling say of his own lowering, and what the verses on pride say of his majesty."
D131_INTRO_NEW = "It now also holds what the verses on humbling say of his own lowering, what the verses on pride say of his majesty, and what the verses on the resurrection say of his immortality."
D131_SEC_OLD = """What this means for the one who humbles himself is in 10.14.

---
"""
D131_SEC_NEW = """What this means for the one who humbles himself is in 10.14.

## Immortal

Paul's praise names God as the one whose life has no end: "To the King of the ages, immortal, invisible, the only God, be honor and glory forever and ever. Amen" (1 Timothy 1:17). He is the one "who alone has immortality, who dwells in unapproachable light, whom no one has ever seen or can see" (6:16). The same word is what "this mortal body must put on" (1 Corinthians 15:53; Chapter 2, *Changed*).
- **He raises the dead.** Paul learned to rely "not on ourselves but on God who raises the dead" (2 Corinthians 1:9).
- **By his Spirit.** "If the Spirit of him who raised Jesus from the dead dwells in you, he who raised Christ Jesus from the dead will also give life to your mortal bodies through his Spirit who dwells in you" (Romans 8:11).
- **In the Son.** "I am the resurrection and the life" (John 11:25). "I died, and behold I am alive forevermore, and I have the keys of Death and Hades" (Revelation 1:18).
- **It is his pledge of judgment.** "He has fixed a day on which he will judge the world in righteousness by a man whom he has appointed; and of this he has given assurance to all by raising him from the dead" (Acts 17:31).

---
"""
edit("13-01-divine-v29-20261018.md", "13-01-divine-v30-20261019.md",
     [(D131_INTRO_OLD, D131_INTRO_NEW), (D131_SEC_OLD, D131_SEC_NEW)])

# ── Ch 11 ─────────────────────────────────────────────────────────────────────────────────────
C11_OLD = """(10.6 *Precious*.)
"""
C11_NEW = """(10.6 *Precious*.)
- **Imperishable.** The Greek *aphthartos* and its noun name what the dead are raised: "the dead will be raised imperishable" (1 Corinthians 15:52). The same words name love, "love incorruptible" (Ephesians 6:24), the seed of new birth (1 Peter 1:23), an inheritance (1:4), "the imperishable beauty of a gentle and quiet spirit" (3:4), the wreath that self-control runs for (1 Corinthians 9:25), and God himself, "immortal, invisible" (1 Timothy 1:17). (Chapter 2, *Changed*; 13.1, *Immortal*.)
"""
edit("11-other-sides-of-the-inner-being-v35-20261015.md", "11-other-sides-of-the-inner-being-v36-20261019.md",
     [(C11_OLD, C11_NEW)])
