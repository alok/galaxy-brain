Probably not. My non-obvious take is that the summary bot would make the problem worse, and the reason is the channel count you mentioned.

**Check the numbers first.** 140 channels for 8 people is about 17 channels per person. That's not a reading problem. It means your workspace has no clear sense of where things belong. A team your size usually needs 10–20 channels. People don't miss announcements because they read too slowly. They miss them because the announcements land in a spot nobody would think to look.

**Why a digest backfires:**

1. **You'd be compressing noise, not filtering it.** A summary of 140 channels is a long, flat list where "Dana's out Friday" and "we're switching payroll providers, everyone re-enter your bank info by the 30th" look about the same. The bot ends up deciding what's important, and that's exactly the judgment that's already failing.

2. **Summaries lose the details that matter most.** LLM summaries are good at the general drift and bad at the one-off item that needs action, like the deploy-process change mentioned in reply #14 of a thread about something else. Worse, you won't notice. Today people at least know they're behind. With a digest they'll believe they're caught up when they aren't. Being confidently wrong is worse than knowing you're behind.

3. **It gives everyone an excuse to keep the sprawl.** Once "the bot covers it," nobody has a reason to archive channels or post in the right place. Channel 141 is the digest, and in about three weeks it'll be one more channel people skim and ignore.

4. **You're fixing it on the wrong end.** A missed announcement is usually the poster's mistake: they put it in the wrong place or didn't flag it. Fix that when the message is written. Patching it afterward for 8 readers every day costs more and works worse.

**What I'd do instead:**

- **Archive hard this week.** Archive any channel with no posts in the last 30 days. Fold the rest into roughly a dozen. With 8 people, all of this takes an afternoon.
- **Make one `#announcements` channel the only place official news goes.** If it isn't posted there, it wasn't announced. Every post gets read and acknowledged with a ✅, and the poster follows up with anyone who hasn't reacted. That gives you a confirmation loop, which no digest can.
- **Talk in person about anything important.** If a decision affects everyone at an 8-person company, it belongs in standup or a weekly written update from a founder, not left for people to find in Slack.
- **If you want AI, use it when messages are posted, not to summarize them later.** For example, a bot that spots messages that look like announcements or decisions in other channels and asks the poster: "This looks like it affects other people. Cross-post to #announcements?" Or one that pulls together the items that need *your* action, like @-mentions and questions directed at you. Narrow, targeted pulls beat summarizing everything.
- **If you still want digests after all that, buy them.** Slack already sells AI recaps. An 8-person startup building its own Slack tooling is another warning sign.

**A cheap test before you build anything:** look at the last 5 announcements people missed and note where each one was posted.

- If most were outside any announcements channel, you have a routing problem. The fixes above solve it, and a bot isn't needed.
- If they *were* in the right place and still got missed, you have a problem with attention or habits. Ask why people aren't reading the one channel that matters. A digest won't fix that either.
- Give `#announcements` plus the ✅ rule two weeks. If people are still missing things after that, then it's worth talking about tooling, and you'll know exactly what the tool has to catch.
