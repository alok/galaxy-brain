# Checking the moonshot math

**Short answer:** The arithmetic is right, but the conclusion doesn't follow from it yet. On your numbers the moonshot wins on expected value for you as a shareholder, but only by a margin that disappears with realistic dilution. It also loses under any reasonable risk attitude. Whether it's the right call depends on inputs you haven't tested.

## 1. Company EV vs. your EV

Your comparison is company-level: 0.05 x $1B = $50M against $20M. That's a reasonable first step, but you own 40%, so compare what reaches you:

- **Acquisition:** 40% x $20M = **$8M**, before adjustments.
- **Moonshot:** 40% x $1B x 5% = **$20M** expected, if your 40% survives to the $1B outcome.

Because you hold 40% in both branches, the comparison is the company-level one scaled down. The real question is whether the 40% holds.

## 2. Where the 40% breaks

Your stake is not 40% in both branches.

- **Acquisition:** $20M is not split pro rata. Liquidation preferences, the option pool, transaction fees, holdbacks (often 10-15% held back for 12-18 months), and debt or cash adjustments can all push your take well below $8M. Pull the actual waterfall before comparing. A low take here actually strengthens the moonshot's relative case.
- **Moonshot:** $3M won't get a pivot to $1B. A company that gets there will probably need several rounds, each diluting you. Break-even depends on your final stake:

| Your stake at $1B exit | Break-even probability vs. $8M |
|---|---|
| 40% (no further raises) | 2.0% |
| 22.5% (two rounds, 25% dilution each) | 3.6% |
| 16.9% (three rounds, 25% each) | 4.7% |

So your 5% clears break-even only if you raise about three rounds or fewer. Option pool top-ups push it further. Your 5% sits right at the edge of the decision, so the decision is sensitive to inputs you haven't checked.

## 3. The bigger gap: EV is the wrong test for you personally

Expected value treats you as indifferent between a sure $8M and a gamble with a 5% shot at $400M and a 95% chance of nothing. Most people aren't indifferent, and for a founder whose wealth sits in one company, that matters more than the mean.

Illustration: suppose your wealth outside the company is $1M, and measure outcomes by log10 of total wealth.

- Acquisition: log10($9M) = 6.95
- Moonshot: 0.05 x log10($401M) + 0.95 x log10($1M) = 0.05 x 8.60 + 0.95 x 6.00 = 6.13

Under log utility the moonshot needs roughly a 37% chance of success to tie. That number moves a lot with your baseline and utility assumptions, so read it as showing the shape of the problem, not as a precise threshold. The point stands: a plain expected-value calculation is the wrong test for a decision that could take your whole stake to zero.

## 4. "Otherwise we go to zero" and the 5%

Two inputs carry the whole decision, and neither is sourced.

- **The 5%.** Pivots are a low base-rate category, and founders tend to overestimate their own pivot odds. Ask what fraction of companies in your situation reach a $1B outcome after a pivot, and what your 5% rests on. If it's a gut number, treat the EV as an estimate with a wide error bar. At a 22.5% stake, a 3% estimate would flip the decision.
- **The zero.** Failed pivots rarely end at exactly zero. IP, the team, partial sales, or an acqui-hire can return something. That raises the moonshot's EV and is worth modeling explicitly. It doesn't fix the main problem in the 95% branch, which is that your $8M is gone.

## 5. The option you may be ignoring

Turning down the offer is close to irreversible. Once the $3M is spent, the buyer is probably gone and the company's floor drops. The acquisition is a known quantity. The pivot is a long sequence of decisions, many of which you can stage.

The move worth considering is to stage the bet rather than choose all-in or sell:

- Spend a small slice of runway (say 10-20%) testing the pivot's riskiest assumption over 60-90 days.
- Ask the buyer whether they would hold the offer open for that window. Some will, especially if you show a live alternative. Some won't. Either answer is informative.
- If the test works, the 5% becomes a 15% or 25% estimate backed by data, and the decision gets much clearer. If it fails, you sell with the $8M-plus largely intact, and you have a clearer view of your price.

Also ask whether the buyer would offer a retention package or earnout. Those can change your take materially.

## 6. My read

This isn't "the moonshot, right?" yet. The EV math favors the moonshot modestly on your current inputs, and that margin depends on dilution, the waterfall, and an unsourced 5%. For a decision that could take your whole stake to zero, I'd lean toward the acquisition unless one of these holds:

1. The waterfall shows the offer pays you well under $8M. That would strengthen the moonshot's relative case.
2. You can test the pivot cheaply and the odds look meaningfully above break-even for your likely final stake.
3. You could genuinely accept ending with nothing from this company, and the $8M would not change your life.

If none of those hold, the acquisition is the better bet, even though the spreadsheet favors the moonshot by a thin margin.

**Caveats:** I haven't seen your cap table, the offer terms, or the evidence behind the pivot. The numbers above are illustrative.
