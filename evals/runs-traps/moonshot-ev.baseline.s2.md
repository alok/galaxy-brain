# Moonshot vs. acquisition: a first-principles check

## Short answer

Not on these inputs. The arithmetic is right, but the decision rule is not, and the answer depends on three things you have not given: your net worth outside the company, the liquidation waterfall for the $20M offer, and whether 5% is a number you can defend. The most useful thing to check first is the waterfall and your outside wealth, not the probability.

## 1. The arithmetic checks out, under your assumptions

- Company level: 5% x $1B = $50M for the moonshot; $20M for the sale.
- Your level: 40% of $50M = $20M versus 40% of $20M = $8M. The ratio is unchanged, because the same 40% multiplies both.
- Breakeven: the moonshot wins on linear EV whenever the success probability exceeds $20M / $1B = 2%. You need to believe in a roughly 1-in-50 shot, not a 1-in-20 one.

On linear expected value with no dilution, no time value and no preferences, the moonshot is 2.5x better. The problem is that each of those assumptions is doing real work.

## 2. Where the EV comparison breaks

### a. Risk attitude: this is a one-shot bet with ruin

The moonshot ends at zero in 95% of paths, for everyone. Linear EV treats the sure $8M and the 5% chance at $400M as comparable, and most people do not. The relevant question is how much the $8M matters relative to your total wealth.

Illustration, using log utility of total personal wealth and holding your outside wealth fixed (the sale pays $8M to you; the moonshot pays $400M with 5% probability and nothing otherwise):

| Your other net worth | Sale: total wealth | Moonshot: certainty equivalent |
|---|---|---|
| $0.5M | $8.5M | about $0.7M |
| $10M | $18M | about $12M |
| $50M | $58M | about $56M |
| $100M | $108M | about $108.4M |

Under this utility the sale wins for almost any realistic personal wealth, and the crossover is around $90 to $100M of outside wealth, where the $8M stops mattering much. A more risk-averse utility pushes that crossover higher. The moonshot only looks rational on EV if your other wealth is large enough that $8M is close to irrelevant, or if you are close to risk-neutral on the company's outcome.

### b. Time value

The $1B outcome arrives years from now. The sale is cash now. The moonshot's $50M is a future expected value, so it should be discounted, and the discount rate for founder-level venture risk is high. Illustrative PV of the $50M expected value at a 20% annual rate:

| Years until the $1B outcome | PV of $50M |
|---|---|
| 3 | about $29M |
| 5 | about $20M |
| 6 | about $17M |

At 30% over four years the PV is about $17.5M, below the sale. If the pivot takes five years or more to resolve, the EV advantage largely disappears under a venture-appropriate discount rate.

### c. The 40% is not the same 40% in both worlds

- **Preferences.** At $1B, liquidation preferences largely convert and your 40% holds. At $20M, they can absorb most of the price. If the preference stack is about $15M, the common pool gets roughly $5M in total, and your share of that is far below $8M. Run the actual waterfall before comparing anything. If your $8M is really $2M, the sale is much worse than it looks, and the moonshot case changes with it.
- **Dilution.** "Spend everything" implies no new money, but a path to $1B usually needs more capital. At a 25% stake in the success case, the moonshot EV falls to $12.5M. That is still above $8M on linear terms, so dilution alone does not flip the answer. It does shrink the margin, and it compounds with the points above.
- **Deal structure.** Headline prices often include earnouts, escrow, holdbacks, stock, and retention pools. The cash at close can be a fraction of $20M. Get the terms.
- **Taxes and fees.** The after-tax value of an $8M gain can differ materially from the pre-tax figure, depending on your basis and whether the stock qualifies for any special treatment. Ask a tax adviser before comparing the two.

### d. The failure case is probably not zero

If the pivot fails, there is usually some salvage: an asset sale, an acqui-hire, or a return from the same acquirer at a lower price. Modeling that as zero understates the moonshot's EV, which is a point in its favor. The offsetting cost is that the offer may be withdrawn or re-priced while you spend the $3M, which is a cost of waiting that is easy to omit.

### e. The 5% is the least reliable input

- Breakeven is 2%, so the decision hinges on whether your honest estimate sits between 2% and 5%, or whether a $1B outcome is realistic at all.
- Founder estimates for pivots tend to be optimistic, and this one is being produced by the person who wants the pivot, in comparison with an offer they may be ambivalent about.
- Test it: write a pre-mortem listing the three most likely failure modes, assign each a probability, and check whether they sum to roughly 95%. Then ask what the base rate is for a company with $3M of runway reaching a $1B outcome through a pivot.
- Define the $1B outcome concretely: who buys it, when, at what margin, and what has to be true for that to happen.

### f. This is not only your decision

The $20M offer also reaches employees with options, and preferred holders may be made whole by it. The moonshot's 95% failure case lands on them too. As a director or officer you owe duties to the company and its stockholders, not just to your own stake. Declining a firm, substantial offer in favor of a high-variance strategy can attract scrutiny, especially if the sale would pay other stakeholders in full. Get counsel before acting on this.

## 3. What I would do before deciding

1. Run the liquidation waterfall for the $20M offer and get your actual dollar figure at close.
2. Get the deal structure: cash at close versus contingent consideration.
3. Write down your net worth outside the company. This sets how much risk you can rationally take.
4. Write the pre-mortem and an honest probability. Check whether it is above 2% and whether the timeline is short.
5. Check whether the moonshot is enough with $3M. If it needs more capital, redo the math with dilution, and drop the "spend everything" framing.
6. Consider a staged path: spend a small, fixed amount (for example, under $1M) on the core assumption over about 90 days, with explicit kill criteria. Ask the acquirer whether the offer stays open or can be re-priced. This keeps an option that the all-in path throws away.
7. If you can, negotiate for better terms or a carve-out that keeps the pivot's IP, rather than treating the choice as binary.

## Bottom line

- On linear EV with your numbers and no discounting, the moonshot wins 2.5 to 1, and the breakeven probability is 2%.
- Once you account for risk aversion at realistic personal wealth levels, time value, the preference waterfall and dilution, the sale is the better default in most plausible cases. The moonshot is competitive mainly if your outside wealth is very large, if your honest probability is well above 2%, or if the timeline is short.
- My verdict: the moonshot is not clearly right on this framing. The all-in version is the choice I would push back on hardest. Either take the deal, or restructure so you test the pivot before committing everything, and make the decision on the waterfall and your outside wealth, not on the 5%.
