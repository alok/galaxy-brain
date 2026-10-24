Probably not. The number that matters is 140 channels for 8 people, about 17 per person. A daily AI summary of all of them becomes a 141st channel, and it's the longest one. It also gives the hardest part of the job to the party least able to do it. The person posting an announcement usually knows it matters when they post it. The summarizer has to guess afterward, from one line buried in a day of chatter.

**What I'd do instead (about 75% confident this is the right fix):**

1. **Fix it on the sending side.** Create one #announcements channel where only a few people can post (or there's a strict norm), with notifications on for everyone. Keep it low-traffic so people actually read it. Add one rule: if something needs action from a specific person, @mention them. Being in the right channel doesn't count. This takes 10 minutes to set up and costs nothing to undo.
2. **Cut the channel count.** Use Slack's analytics to archive every channel with no messages in the last 30 days. I'd bet most of the 140 are dead or nearly dead, and you end up with 15 to 25. Archiving is reversible, so be aggressive.
3. **At 8 people, a short weekly written update or a 15-minute sync** catches whatever the first two miss, and it's cheaper than any bot.

**The check that decides it:** collect the last 5 to 10 announcements people actually missed. For each one, ask two things: did the sender know it was important when they posted it, and where did they post it?

- If most were known to be important and posted in a niche channel, the sending-side fix above solves it. No bot needed.
- If most only turned out to matter later (a decision 40 messages deep in a thread, or a casual "oh, we're moving the launch" in #random), then automated extraction has a real job. Even then, build or buy something narrow: a daily list of *decisions and action items*, not a summary of everything. Check Slack's own AI add-on before building, since it already does channel recaps.

**Why not the obvious version:**

- **The summary grows with channel count, not with importance.** You'd be compressing noise and hoping the signal survives.
- **It weakens accountability.** Once a bot exists, people stop reading channels, senders stop flagging things ("the bot will pick it up"), and a miss becomes "the summary didn't mention it." The failure is the same, but nobody owns it.
- **It costs engineering time** at a company where that's your scarcest resource, and it solves a problem that a posting rule and an archive pass probably solve better.
- **The opposite overreaction, moving off Slack to Notion, email or something else,** is expensive, and the problem comes with you. The tool isn't the cause. The lack of separation between broadcasts and discussion is.
