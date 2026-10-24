**Short answer:** don't ship it *as a 4% win*. You may still want to ship it, but for a different reason and with a different number in the forecast.

## The obvious part (quickly)

Checking every day and stopping at the first p < 0.05 inflates your false-positive rate. With about 6 looks, the real chance of a false positive is around 12–15%, not 5% (Armitage et al.: 5 looks ≈ 14%). The more looks you would have taken before giving up, the higher it gets. The nominal p = 0.04 doesn't mean what it says. Under a proper 6-look sequential design (Pocock), you'd have needed roughly p < 0.015 at the look where you stopped. You didn't get there.

Most people stop at that point. The more useful points follow.

## The non-obvious part

### 1. The stopping rule produced the "4%", not the new flow

If you stop the first time z crosses ~1.96, then at that moment the observed lift is about 2 standard errors by construction. On day 6 your SE was about 4% / 2.05 ≈ 2 percentage points (relative). So "4% lift" mostly tells you how noisy day 6 was. Whatever the true effect was, 0%, 1% or 4%, you'd have seen about 4% on the day you stopped. Crossing on day 6 rather than day 2 carries a little information, but the estimate is badly biased upward (winner's curse / truncation bias). A reasonable shrunk guess is low single digits, possibly about 0.

**Practical consequence:** if someone puts "+4% checkout conversion" into a revenue forecast, that's the real damage. Don't let it happen.

### 2. The confirmation test is much bigger than you'd guess

Say the true lift is 2%, not 4%. Sample size scales with 1/δ². For 80% power at δ = 2% you need SE ≈ 0.7pp, versus the ~2pp you had. That's about **7–8× the traffic**: roughly 6–7 weeks at your current rate, not "a few more days." If that isn't feasible, admit that the test can only detect large effects. Then decide on priors and costs, not on p-values.

### 3. Day 6 means less than one full weekly cycle

You've under-sampled at least one weekday/weekend mix. Weekend shoppers, mobile share and intent can differ a lot. Checkout changes also have time dynamics. Returning users can show a *primacy* dip at first (broken muscle memory) or a novelty bump. Six days can't separate either from the steady state.

### 4. "Conversion" may not be the outcome you care about

Checkout redesigns commonly move conversion by changing *what counts* or *who gets through*:
- Did the conversion event's firing point move (e.g., earlier in the flow)?
- Average order value, attach rate, upsells: a smoother flow often cuts add-ons.
- Payment failures, fraud/chargebacks, refunds and returns over the next 30 days.
- Sample ratio mismatch: check that the split is actually 50/50. Checkout tests often break assignment through redirects or payment providers.

A real +1% conversion with −2% AOV is a loss.

### 5. The ship decision isn't a significance test, and that can work in your favor

Ask what happens if you're wrong. A false positive here most likely means you shipped something neutral. Your data does reasonably rule out "the new flow is much worse." If the new flow is cheaper to maintain, aligns with your roadmap, or unblocks other work, then "probably not worse, maybe somewhat better" can be enough to ship. Just say that's the reason. "We proved a 4% lift" is not.

## What I'd actually do

1. **Ship to ~90% with a 10% holdback** of the old flow for a pre-registered fixed period: at least 2 full weeks, sized for a 1–2% effect. You get most of any upside now and a clean, unbiased estimate later. Use only *new* data for the estimate. Pooling it with the peeked data brings the bias back.
2. Track AOV, payment failures and 30-day refunds/chargebacks as guardrails, not just conversion.
3. Going forward, if people are going to look at the dashboard daily (they will), use a method that allows it: an always-valid / mSPRT sequential test, or group-sequential boundaries (O'Brien–Fleming). Either one makes peeking legitimate instead of forbidden.

**Bottom line:** the evidence supports "probably not harmful, possibly a modest gain." It doesn't support "+4%." Ship with a holdback if the downside is cheap, and don't book the 4%.
