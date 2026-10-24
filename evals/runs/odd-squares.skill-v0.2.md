Take a 4×4 grid and label each cell (i, j). Then sort the cells by max(i, j):

```
4 4 4 4
3 3 3 4
2 2 3 4
1 2 3 4
```

The cells with max = k form an L-shaped shell. It has k cells along the top, k along the side, and they share 1 corner cell, so the shell has 2k − 1 cells. Every cell of the n×n grid sits in exactly one shell, so n² = Σ (2k − 1). Nothing was summed. One set was split into pieces.

**The deeper point: the question has the arrow backwards.** The odd numbers don't happen to add up to squares. They are what squares are made of. 2k − 1 is by definition k² − (k−1)², the amount you add to go from one square to the next. So the sum is Σ (k² − (k−1)²), which telescopes to n². It could not be anything else. Telescoping is the algebra and the L-shaped shells are the picture. They are the same proof.

So the only real fact in the identity is this: the step k² − (k−1)² = (k − (k−1))(k + (k−1)) = 2k − 1 comes out linear, with slope 2. That happens because x² has degree 2. Its first difference has degree 1, and the leading coefficient doubles. Every closed-form identity Σ p(k) = q(n) works this way: p is the difference of q. The odd numbers are the one case where the difference is simple enough to recognize at a glance. The "surprise" lives in the fact that you meet the sequence 1, 3, 5, 7 before you meet it as the differences of 0, 1, 4, 9, 16.

I'm confident this is the right level. The other explanations below are either this one in different words, or they work only because the degree happens to be 1.

**A test that shows which explanation is the real one: go up a degree.** Use cubes instead of squares. The shell explanation carries over unchanged. Sort the cells of an n×n×n cube by max(i, j, k). The k-th shell has k³ − (k−1)³ = 3k² − 3k + 1 cells, the centered hexagonal numbers. So Σ (3k² − 3k + 1) = n³, for exactly the same reason.

The calculus explanation does not carry over (see below). The midpoint value of 3x² on [k−1, k] is 3k² − 3k + 3/4. That misses the shell size by exactly 1/4 per term, which is the midpoint rule's error f″h³/24 = 6/24. So the shell/difference explanation is the general truth, and the calculus one is a happy accident.

**Other explanations, and where each falls short:**

- **Calculus and Galileo.** 2k − 1 = 2(k − ½) is the value of 2x at the midpoint of [k−1, k]. The midpoint rule is exact for linear functions, so Σ (2k − 1) = ∫₀ⁿ 2x dx = n² exactly, not just approximately. Galileo's 1 : 3 : 5 : 7 rule for distances fallen in successive seconds is this same statement for constant acceleration. It's lovely, but as the cube test shows, it is exact only because 2x is linear. It's a degree-1 coincidence sitting on top of the difference explanation.
- **Gauss pairing.** Pair the first and last terms: (1 + (2n−1)) · n/2 = n². This is the trapezoid rule, which is also exact only for linear functions. It checks the answer without explaining why it has to be a square.
- **Two triangles.** n² = T(n) + T(n−1). True, but it just moves the question to triangular numbers.
- **Generating functions or finite-calculus machinery.** These say the same difference/sum story more formally, and add nothing that makes it feel more inevitable.
