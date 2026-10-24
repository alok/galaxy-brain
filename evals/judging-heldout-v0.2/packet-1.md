# Item `oss-triage`

## User message

Our open-source library gets about 50 new GitHub issues a week and our two maintainers are burning out. We're thinking of hiring a part-time contractor to triage issues. Good idea? Give me the non-obvious take.

## Response A

**Short version:** a triage contractor helps only if you also give them the authority to close things. Before you spend the money, check whether triage is what's burning your maintainers out. Often it isn't. (About 65% confident in this framing.)

**Why triage time probably isn't the problem.** Fifty issues a week at five to ten minutes each is roughly 4–8 hours a week, split between two people. That's real time, but it's rarely the part that burns people out. The usual causes are elsewhere:

- **The decisions.** "Is this a bug or intended?", "Will we ever support this?", "Do we take this PR?" A contractor can't make these calls. So triage tends to end with "needs maintainer input", and the same queue lands back on the same two people, now with labels on it.
- **The open-ended obligation.** A backlog that only grows feels like debt you never finish paying, however well it's sorted. Sorting doesn't make it smaller.
- **The social load.** Entitled or angry users, and being pinged constantly.

A contractor without decision rights also adds work at first. For the first month or two your maintainers will be answering the contractor's questions and checking their judgment. So expect things to get worse before they get better.

**What actually works:**

1. **Write a triage policy before hiring anyone.** For example: we close feature requests outside scope X. Issues with no reproduction get a request and auto-close after 14 days. Usage questions go to Discussions. We don't promise a response time. Writing this down is the valuable part. It turns maintainer judgment into rules someone else can apply. Then the contractor, a bot, or a volunteer can close issues without asking first. Without the policy, the contractor is just a router.
2. **Reduce inflow before you add capacity.** Require a reproduction in the issue template. Send questions to Discussions, since in many libraries a large share of "issues" are support requests. Use a bot to close issues marked needs-repro. Have maintainers triage once a week instead of continuously. All of this is cheap and easy to undo.
3. **Treat the issue count as data.** Fifty a week may mean a few root causes are generating most of them: a confusing API, a docs gap, a bad error message, a breaking change. Cluster your last 200 issues. If a handful of clusters account for 40% or more, one better error message or docs page beats a year of triage.

**The check (about two weeks, almost free):** have both maintainers log their issue-related time in four buckets: sorting/labeling/asking for repros, answering support questions, making decisions, and actually fixing things. At the same time, categorize your last 100 issues.

- If sorting plus support is most of the time, and questions or duplicates make up most of the issues, hire the contractor, with written close authority.
- If decisions and fixing dominate, a triager won't help much. Spend the money on a contractor who fixes bugs and handles the review work the maintainers dislike. Or use it to buy maintainers' time away from their day jobs.

**Options I'd rule out:**

- **Recruiting unpaid community triagers instead.** This moves the burnout onto volunteers and adds coordination work, which is the scarce thing.
- **"Just close everything and declare the project done."** That answers a different question unless you actually want to cut the project's scope. If you do, that's a legitimate choice and worth making on purpose.
- **Hiring on a one-off grant with no plan for renewal.** When the money runs out, the problem comes back, and users will by then expect fast responses.


## Response B

**Short version:** It can work, but probably not the way you're imagining. If you hire someone to "triage," meaning label, route and ask for more info, you may end up with *more* maintainer load, not less. The hire pays off only if you change what the job is and what the contractor is allowed to decide.

## Why the obvious version often backfires

**1. Sorting is rarely what's burning people out.** 50 issues a week is about 7 a day. Labeling and deduping that many takes a few hours a week. What wears maintainers down is usually something else:
- the *decisions* (is this a bug, intended behavior, or out of scope?)
- the *reproduction work* (an hour spent reconstructing someone's environment)
- the *emotional labor* (entitled or angry reporters, guilt about the open-issue count)
- the *context switching* (every notification breaks focus)

A triager who can't make decisions only handles the cheap part. Every judgment call still goes up to the maintainers, who now also have a new "triaged, awaiting maintainer" queue and a contractor to manage.

**2. Triage needs the most context of any job on the project.** "Won't fix, that's by design" is a call only someone who knows the codebase and roadmap well can make. That's the opposite of what a new part-time contractor brings. For the first 2–3 months they will need your maintainers' time to get up to speed, so expect the load to rise before it falls.

**3. Contractors leave and take what they learned with them.** Part-time contractors turn over. Each one who leaves takes the judgment you spent months teaching them.

## What tends to actually work

**Hire a reproduction engineer, not a triager.** Make the job "turn every bug report into a minimal failing test case or close it." A maintainer who gets a confirmed repro, or better a failing test in a PR, can often fix the bug in 15 minutes. That's where the real hours are saved. It also trains the contractor on the codebase much faster than labeling does.

**Write down what the contractor can decide on their own, or don't hire.** They should be able to close issues without asking:
- duplicates
- support questions (redirect them to Discussions or a forum)
- issues waiting on the reporter for more than N days
- anything clearly outside a documented scope

That means you need a short written "what this project is and isn't" document first. Writing it is valuable even if you never hire anyone.

**Shrink the inflow before you staff it.** At 50 a week, a big share is usually questions, duplicates and low-effort reports. Some fixes:
- issue templates that require a version and a repro
- routing questions to Discussions
- auto-closing issues stuck on "needs-info"
- automated dedup/labeling bots (LLM-based ones are now cheap enough for a first pass)

These often cut the volume by a third to a half, and they cost nothing per month.

**Change the deal you have with users.** A lot of burnout comes from feeling responsible for every open issue. A public statement like "we don't guarantee a response; issues without a repro may be closed" lets maintainers stop feeling guilty, and that can matter as much as the actual hours.

**Ask your maintainers what drains them. It may not be issues.** Sometimes the draining part is releases, CI breakage, dependency bumps or security reports, and issues just get blamed because they're the most visible. If so, pay a contractor to own the boring infrastructure and let the maintainers keep the issue work they actually like.

**Use the contractor to grow volunteer triagers.** Make part of the job finding and coaching 2–3 regular community members who can get GitHub's Triage role. That way, if the contractor leaves, the knowledge stays with people who are still around.

## Before you spend the money

Run it as an experiment, not a commitment:
1. **Two weeks of time logging.** Each maintainer roughly tracks hours by category: sorting, reproducing, deciding, fixing, reviewing, infra, and dealing with people. That shows you what to hire for.
2. **Fix the inflow first** (templates, Discussions, bots, scope doc) and measure again.
3. **Then a 3-month contract** with criteria set in advance. For example: maintainer hours on issues drop by at least 30%, median time to first response is under 48h, and maintainers *say* they feel better. If it's not working by month 3, stop.

**Bottom line:** the money is well spent if it buys reproductions and authority to close issues, and badly spent if it buys a labeling layer. Also, the problem may be the maintainers' sense that they owe every reporter an answer, more than their hours. No contractor fixes that. A scope document and an explicit "we may not respond" policy can.


---

# Item `det-product`

## User message

Why is det(AB) = det(A) det(B)? I know the proof via elementary matrices. Give me the deepest explanation, the one that makes it feel inevitable.

## Response A

**Short answer:** the determinant is the number by which a linear map scales the top exterior power, a space of dimension one. A linear map on a one-dimensional space is just multiplication by a number. Composing two such maps multiplies their numbers. So once you see what det is, $\det(AB)=\det A\,\det B$ says that 1×1 matrices multiply like numbers. I'm confident this is the explanation most algebraists would call the real reason.

## Start with 2×2

Let $\omega(x,y) = x_1y_2 - x_2y_1$ be the signed-area form on $k^2$. Work out $\omega(Ax, Ay)$ for $A = \begin{pmatrix} a & b \\ c & d\end{pmatrix}$ and you get

$$\omega(Ax,Ay) = (ad-bc)\,\omega(x,y).$$

That is the definition: $\det A$ is the factor by which $A$ rescales $\omega$. Now apply $AB$:

$$\omega(ABx, ABy) = \det A\cdot\omega(Bx,By) = \det A\cdot\det B\cdot\omega(x,y).$$

Comparing with $\omega(ABx,ABy) = \det(AB)\,\omega(x,y)$ finishes the proof. Nothing was computed except the definition.

## The general statement

Let $V$ have dimension $n$. The space of **alternating $n$-linear forms** on $V$ (equivalently $\Lambda^n V^*$) is **one-dimensional**. Any linear $T : V \to V$ pulls such a form back:
$$(T^*\omega)(v_1,\dots,v_n) = \omega(Tv_1,\dots,Tv_n),$$
and the result is again alternating and $n$-linear. Since the space is a line, $T^*\omega = c\,\omega$ for one scalar $c$, the same for every $\omega$. That scalar is $\det T$, defined with no basis and no formula.

Multiplicativity is then just functoriality:
$$(ST)^* = T^* \circ S^* \quad\Longrightarrow\quad \det(ST) = \det T\cdot\det S.$$
(Order doesn't matter at the end because scalars commute. That is also why $\det$ ignores the noncommutativity of matrices.)

## Where the actual work goes

All the content sits in one fact: **alternating $n$-forms in dimension $n$ form a line.**
- *At most one-dimensional:* expand $\omega(\sum a_{i1}e_i, \dots)$ multilinearly. Terms with a repeated basis vector vanish. Each surviving term is $\pm\,\omega(e_1,\dots,e_n)$ with the sign of a permutation. So $\omega$ is fixed by its value on one basis.
- *At least one-dimensional:* the Leibniz formula $\sum_\sigma \operatorname{sgn}(\sigma)\prod a_{\sigma(i)i}$ gives a nonzero example. This needs the sign homomorphism to be well defined.

Your elementary-matrix proof proves this same fact in disguise. Each row operation checks that $B \mapsto \det(EB)$ behaves like an alternating multilinear function of the rows. The cleanest coordinate version makes this explicit. Fix $A$. Then $B \mapsto \det(AB)$ is alternating and multilinear in the columns of $B$, so it equals $c\cdot\det B$, and setting $B=I$ gives $c=\det A$. That is the argument above with a basis chosen.

## The converse: det is the only multiplicative invariant

The fact above shows why det *is* multiplicative. A second fact shows why det is the *only* multiplicative invariant. For any field $k$, apart from the single case $n=2$, $k=\mathbb F_2$, the commutator subgroup of $GL_n(k)$ is exactly $SL_n(k)$. So every homomorphism from $GL_n(k)$ to an abelian group factors through $\det$. If you want a scalar invariant of invertible matrices that respects products, you are forced to take det or a function of det. Uniqueness of alternating forms makes det multiplicative. Abelianization says nothing else could be.

## A check you can run

Try the argument over $\mathbb Z/6$ or $\mathbb F_2$, where "volume" means nothing. The theorem still holds. The exterior-power proof still works word for word, because over any commutative ring $\Lambda^n R^n$ is free of rank one. The volume proof does not. This test separates the real reason from its most popular shadow.

## Explanations that sound deeper but aren't the reason

- **"Det is the volume scaling factor, and scaling factors compose."** True over $\mathbb R$, and a good picture. But it needs measure theory to make rigorous, treats sign as an afterthought, and says nothing over finite fields. It is the real-number picture of the exterior-power argument, so it can't be the reason itself.
- **"Det is the product of the eigenvalues."** This goes nowhere. The eigenvalues of $AB$ are not products of the eigenvalues of $A$ and $B$. To make it work you have to prove multiplicativity some other way first.
- **"Det is a natural transformation $GL_n \to \mathbb G_m$" / "$K_1$ of a field is its unit group."** Correct and useful for generalizing, for example to the Dieudonné determinant or the Berezinian. For matrices, though, it is the same functoriality stated at higher altitude. It adds generality but no extra understanding of *why*.


## Response B

The short version: **the determinant is what a linear map does to a one-dimensional space, and the maps from a one-dimensional space to itself are just multiplication by scalars. Composing two of them multiplies the scalars.** Once you see det that way, the product rule follows directly. Everything hard about determinants sits in one fact, that this space is one-dimensional, and the product rule isn't part of the hard work.

Here it is properly, starting with a concrete case.

## 1. A worked 2×2 example

Take a linear map $f:\mathbb{R}^2\to\mathbb{R}^2$ with matrix $\begin{pmatrix} a & b \\ c & d\end{pmatrix}$, so $f(e_1) = ae_1 + ce_2$ and $f(e_2) = be_1 + de_2$.

Now compute the *oriented area* of the image of the unit square. To do that, use a product $\wedge$ with two rules: it is bilinear, and $v\wedge v = 0$ (a degenerate parallelogram has no area). From those two rules you also get $w\wedge v = -v\wedge w$. Then

$$
f(e_1)\wedge f(e_2) = (ae_1+ce_2)\wedge(be_1+de_2) = ad\,e_1\wedge e_2 + cb\,e_2\wedge e_1 = (ad-bc)\,e_1\wedge e_2.
$$

You never chose the formula $ad-bc$. It came out of bilinearity plus "degenerate means zero". The key point is that **every** wedge $v\wedge w$ of two vectors in $\mathbb{R}^2$ is a multiple of the single element $e_1\wedge e_2$. So $f$ acts on the space of such wedges by multiplication by one number, and that number is the determinant.

## 2. The general statement

For an $n$-dimensional vector space $V$, form the top exterior power $\Lambda^n V$. This space is spanned by the formal products $v_1\wedge\cdots\wedge v_n$, which are multilinear and vanish whenever two of the factors are equal.

Two facts:

1. **Functoriality.** A linear map $f:V\to V$ induces $\Lambda^n f:\Lambda^n V\to\Lambda^n V$ by
 $v_1\wedge\cdots\wedge v_n \mapsto f v_1\wedge\cdots\wedge f v_n$. This rule is so obviously compatible with composition that checking it is barely a step:
 $$\Lambda^n(f\circ g) = \Lambda^n f\circ \Lambda^n g.$$
 (Apply $g$ to each factor and then $f$ to each factor, or apply $fg$ to each factor. Same thing.)

2. **One-dimensionality.** $\dim \Lambda^n V = 1$.

A linear endomorphism of a one-dimensional space is multiplication by a unique scalar. **Define** $\det f$ to be that scalar:
$$\Lambda^n f = \det(f)\cdot \mathrm{id}.$$
Then
$$\det(fg)\cdot\mathrm{id} = \Lambda^n(fg) = \Lambda^n f\circ\Lambda^n g = \det(f)\det(g)\cdot\mathrm{id}.$$

That completes the proof. Notice what kind of statement it is: $\det$ is a functor $\Lambda^n$ applied to a map, followed by the identification $\mathrm{End}(\text{line}) = k$. Functors preserve composition, and in $k$ composition is multiplication. So **multiplicativity holds by construction**.

Some things come for free with this definition:
- $\det$ is defined without choosing a basis, so $\det(PAP^{-1}) = \det A$ needs no proof.
- $\det f \neq 0 \iff f$ is invertible. If $f$ kills some vector, extend that vector to a basis $v_1,\dots,v_n$; then the generator $v_1\wedge\cdots\wedge v_n$ of $\Lambda^n V$ maps to $0$.
- The geometric reading: $\Lambda^n V$ is the space of "oriented $n$-volumes", and $\det f$ is the factor by which $f$ scales every one of them. Scaling all volumes by $\lambda$ and then by $\mu$ scales them by $\lambda\mu$. The algebra above is the precise form of that sentence.

## 3. Where the real work is

The proof in §2 skips nothing, but it puts all the content into fact 2: $\dim\Lambda^n V = 1$, and in particular $\Lambda^n V \neq 0$.

- **At most 1 dimension** is easy. Expand $v_1\wedge\cdots\wedge v_n$ in a basis. Any term with a repeated basis vector dies, and each surviving term is $\pm e_1\wedge\cdots\wedge e_n$ after reordering. This is the same computation as the 2×2 case.
- **Not zero** is the hard part. You need the sign you pick up from reordering to be *well-defined*: a permutation cannot be both an even and an odd number of transpositions. Equivalently, the Leibniz formula $\sum_\sigma \operatorname{sgn}(\sigma)\prod_i a_{i\sigma(i)}$ really is an alternating multilinear form and isn't identically zero.

So the sign homomorphism $S_n\to\{\pm1\}$ is the actual combinatorial input. The elementary-matrix proof mixes this input in with the multiplicativity. The exterior-power proof separates them: existence and uniqueness of the volume form is the theorem, and the product rule follows from it in one line.

The dual phrasing is also useful. Alternating multilinear $n$-forms on $V$ make up a one-dimensional space, so for any nonzero such form $\omega$, the pulled-back form $\omega(f\,\cdot,\dots,f\,\cdot)$ must equal $c\,\omega$, and that $c$ is $\det f$. This is the "uniqueness of the normalized alternating form" characterization in many textbooks, minus the normalization, which you don't need.

## 4. Why det is more or less the only option

There is a second sense in which the result is unavoidable. It answers the question "why this function and not some other?"

$\det: GL_n(k)\to k^\times$ is a group homomorphism to an abelian group. Every such homomorphism must vanish on commutators $ABA^{-1}B^{-1}$. For a field $k$, the commutator subgroup of $GL_n(k)$ is exactly $SL_n(k)$, with the single exception $n=2$, $k=\mathbb{F}_2$. So
$$GL_n(k)^{\mathrm{ab}} \;\cong\; k^\times \quad\text{via } \det.$$

This means **every** multiplicative invariant of invertible matrices with values in a commutative group factors through the determinant. Any rule that assigns a number to a matrix and is multiplicative must be a function of $\det$. Multiplicativity doesn't just happen to hold for det. Det is the universal multiplicative invariant, and $\Lambda^n$ is how you build it explicitly.

## Summary

- **Algebraic:** $\det f$ is the action of $f$ on the line $\Lambda^n V$. Functoriality plus "endomorphisms of a line are scalars" gives multiplicativity in one step.
- **Geometric:** $\det f$ is the factor by which $f$ scales oriented volume. Scale factors compose by multiplication.
- **Group-theoretic:** $\det$ is the abelianization of $GL_n$. Any multiplicative scalar invariant has to go through it.
- **Where the effort really goes:** proving that the line $\Lambda^n V$ is nonzero, i.e., that the sign of a permutation is well-defined. Elementary-matrix proofs hide this step inside row-operation bookkeeping, which is why they feel like an accident.


---

# Item `ab-peeking`

## User message

Our A/B test of a new checkout flow shows a 4% conversion lift at p = 0.04. We checked the dashboard every day and stopped the test the first day it crossed significance, which was day 6. Ship it? Give me the non-obvious take.

## Response A

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


## Response B

**Not on this evidence. The non-obvious part is that peeking damages two things, and they deserve different responses: your claim that the lift is 4%, and your decision about whether to ship.**

**The claim is badly damaged.** You looked once a day and stopped the first time p dipped under 0.05. Run that procedure on two identical checkout flows with six daily looks and it "finds" a winner roughly 15% of the time, not 5%. If you would have kept going past day 6, the rate is even higher. The 4% is also biased upward. Stopping at the first crossing means you stopped on the day the noise was most in your favor, so the true lift is probably well under 4%, possibly 0. For calibration: a sequential design built for daily looks (Pocock boundaries over 6 looks) would have needed a nominal p of about 0.015 on day 6. An O'Brien-Fleming design planned over two weeks would have needed about 0.001. Your 0.04 clears neither. Six days also doesn't cover a full weekly cycle, and a new checkout flow can show early novelty or confusion effects that fade.

**The decision is only mildly damaged.** The data still say the new flow is unlikely to be worse. What they don't say is how much better it is. Waiting costs very little: half your traffic is already on the new flow, so a couple more weeks gives up at most half of a lift that is probably small. That asymmetry makes waiting the right call (about 75% confident):

1. **Keep the test running to a fixed end date you commit to now.** That means at least 2 full weeks, with a sample size powered for a realistic lift of 1–2%, not 4%. Analyze once, at the end.
2. **The cheapest check:** treat the data from day 7 onward as a replication. If the lift is real, it shows up again in fresh data you didn't stop on. If it was luck or novelty, it shrinks toward zero. This also tells you whether the effect fades over time.
3. **Decide on revenue per visitor, not conversion rate.** A checkout change can raise conversion while lowering order value, or pull purchases earlier without adding new ones. Also confirm the traffic split actually came out at the intended ratio (a sample ratio mismatch check), since a broken split invalidates everything else.

If you're under real pressure and the flow is cheap to roll back, shipping now is defensible. In that case, record the lift as "probably positive, size unknown, likely below 4%", not as +4%. The worse outcome of shipping now isn't a bad checkout. It's a fake 4% going into the forecast and the team learning that stopping at the first significant day works.

**Clever-sounding alternatives, and why they don't rescue the result:**
- *"Switch to a Bayesian analysis, where the stopping rule doesn't matter."* That's technically true. But it only holds up with an honest prior, and an honest prior for checkout changes (most produce lifts near zero) shrinks 4% down hard anyway. You end up in the same place.
- *"Ship with a 5% holdback group and measure later."* A holdback that small takes a long time to detect a 1–2% lift. It works as a fallback, not as a substitute for the test.
- *"Just ban looking at the dashboard."* Nobody follows that rule. The lasting fix is a sequential testing method (always-valid p-values, or alpha-spending boundaries) so people can look every day without inflating false positives. Set that up before the next test.


---

# Item `sql-count`

## User message

In SQL, how do I count the number of rows per customer_id in an orders table? Give me the non-obvious take.

## Response A

The query is the boring one, and it's correct:

```sql
SELECT customer_id, COUNT(*) AS order_count
FROM orders
GROUP BY customer_id
ORDER BY order_count DESC;
```

The non-obvious part is the meaning, not the syntax. This query gives the right answer to "rows per customer_id" and can still be wrong about "orders per customer" in three common ways:

**1. Customers with zero orders are missing.** `GROUP BY` only produces groups that exist. If you need every customer, including those with 0, start from the customers table:

```sql
SELECT c.customer_id, COUNT(o.customer_id) AS order_count
FROM customers c
LEFT JOIN orders o ON o.customer_id = c.customer_id
GROUP BY c.customer_id;
```

Use `COUNT(o.customer_id)` here, not `COUNT(*)`. `COUNT(*)` counts the NULL-padded row from the LEFT JOIN, so every zero-order customer would show 1.

**2. NULL `customer_id` becomes its own group.** Guest checkouts or broken imports all land in one `NULL` row, which can quietly be your "biggest customer." Filter it out with `WHERE customer_id IS NOT NULL` or label it, but decide on purpose.

**3. A row may not be an order.** Tables called `orders` are often really order *lines* (one row per item), or they include cancelled, test or duplicate rows. In that case you want something like:

```sql
SELECT customer_id, COUNT(DISTINCT order_id) AS order_count
FROM orders
WHERE status <> 'cancelled'
GROUP BY customer_id;
```

**The cheap check:** run `SELECT COUNT(*), COUNT(DISTINCT order_id) FROM orders;`. If the two numbers differ, the table isn't one row per order and the plain `COUNT(*)` is overcounting.

Two related tools worth knowing:

- If you want the count next to each order row instead of collapsing the rows, use a window function: `COUNT(*) OVER (PARTITION BY customer_id)`.
- On a big table, an index on `customer_id` lets most databases answer the `GROUP BY` from the index alone. A precomputed counter column or materialized view is only worth its upkeep if this query runs on a hot path, since it adds a way for the count to drift.


## Response B

The obvious answer:

```sql
SELECT customer_id, COUNT(*) AS n_orders
FROM orders
GROUP BY customer_id;
```

That query is correct. The non-obvious part is that it answers a slightly different question from the one you probably mean. Here's where it goes wrong.

**1. Customers with zero orders don't show up.**
`GROUP BY` can only make groups out of rows that exist. A customer who never ordered isn't missing a count of 0. They're just absent from the result. If you want "orders per customer" and not "customers who have orders, with their counts," start from the customers table:

```sql
SELECT c.customer_id, COUNT(o.order_id) AS n_orders
FROM customers c
LEFT JOIN orders o ON o.customer_id = c.customer_id
GROUP BY c.customer_id;
```

**2. In that LEFT JOIN, `COUNT(*)` is a bug.**
A customer with no orders still produces one joined row, with NULLs on the orders side. `COUNT(*)` counts that row, so the customer gets 1. `COUNT(o.order_id)` skips NULLs and correctly gives 0. Rule: `COUNT(*)` counts rows, `COUNT(col)` counts non-NULL values. After an outer join, those two numbers are different.

**3. `NULL` customer_id becomes its own group.**
Orders with no customer (guest checkout, bad data) collapse into a single `NULL` row in the first query. Decide on purpose whether to keep it or filter it out with `WHERE customer_id IS NOT NULL`.

**4. "Rows" may not mean "orders."**
If the table really holds one row per line item, `COUNT(*)` counts items. Use `COUNT(DISTINCT order_id)` to count orders. The same problem appears quietly whenever you join another one-to-many table (payments, shipments) before grouping. The join multiplies rows, and every count goes up with no error to warn you.

**5. If you need the count next to each row, use a window function:**

```sql
SELECT o.*, COUNT(*) OVER (PARTITION BY customer_id) AS customer_order_count
FROM orders o;
```

This keeps every order row and adds the per-customer total, with no self-join.

**6. Conditional counts in one pass:**

```sql
SELECT customer_id,
       COUNT(*) AS total,
       COUNT(*) FILTER (WHERE status = 'refunded') AS refunded
FROM orders
GROUP BY customer_id;
```

`FILTER` works in Postgres and SQLite. Elsewhere, use `SUM(CASE WHEN status = 'refunded' THEN 1 ELSE 0 END)`. To filter on the count itself, use `HAVING COUNT(*) > 5`. `WHERE` runs before grouping, so it can't see the count.

**7. Performance:** an index on `orders(customer_id)` lets most engines answer the basic query from the index alone, without reading the table. On a large table that's the difference between a full table scan and a cheap read of the index.

**Bottom line:** the counting is the easy part. What matters is which entity's rows you're counting (orders, line items, or customers) and what you start from: start from `customers` if zero-order customers should appear, and from `orders` if they shouldn't.


---
