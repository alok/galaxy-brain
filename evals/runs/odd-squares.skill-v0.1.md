Start with n = 4. Label each cell (i, j) of a 4×4 grid by max(i, j):

```
3 3 3 3
2 2 2 3
1 1 2 3
0 1 2 3
```

The label k shows up 2k+1 times: once on the diagonal, plus k cells along each of its two arms. The cells labeled k form an L-shape (Euclid called it a gnomon). It is exactly what you add to a k×k square to get a (k+1)×(k+1) one. So the grid is 1 + 3 + 5 + 7, and the sum equals 16 because it is just the grid counted shell by shell.

## The reason, in one line

The question is set up backwards. It's not that the odd numbers happen to add up to squares. The odd numbers *are* the gaps between consecutive squares:

(k+1)² − k² = 2k + 1

Add up all the gaps from 0 to n and you get n² − 0². That's telescoping, and the identity has no other content. Your induction proof does the same thing: the inductive step is "add the next L." For any sequence, Σ Δf = f(n) − f(0). The only fact about squares you need is Δ(k²) = 2k+1, and that fact is the L-shape: two arms of length k and one corner.

You can check this by running the same template on other powers. The gaps between cubes are 3k² + 3k + 1 = 1, 7, 19, 37, … (the centered hexagonal numbers). Their running sums are 1, 8, 27, 64. You can see it the same way, by splitting an n×n×n cube into shells by max(i, j, k). Nothing here is special to odd numbers.

## Where the "+1" goes in calculus

Continuous version: d(x²) = 2x dx, so ∫₀ˣ 2t dt = x². The "+1" disappears, and nonstandard analysis shows exactly where it goes. Split [0, x] into N steps of size h = x/N, with N hyperfinite. The k-th gnomon has area (2k+1)h² = 2(kh)·h + h². Over all N gnomons:

- The arms add up to Σ 2(kh)·h, which is a Riemann sum for ∫ 2t dt.
- The corners add up to N·h² = x·h, which is infinitesimal.

The total is exactly x². So the integral is the standard part of the odd-number identity: the corner term is the "+1", and you're allowed to drop it once it's infinitesimal. The discrete identity is the exact statement. The calculus fact is its shadow.

## Deeper, but not more inevitable

This next part gives the identity more structure. It doesn't make it any more forced.

Read the grid as n×n matrices, End(V), where V is the n-dimensional irreducible representation of sl₂. Give the matrix unit E_ij the weight j − i. Now look at the gnomon max(i, j) = m:

- Its row half has weights −m, …, 0.
- Its column half has weights 0, …, m.
- They share the corner, so 0 is counted once.

So each gnomon has weights −m through m, once each. That is exactly the weight string of the (2m+1)-dimensional irreducible representation. The gnomon decomposition is the character-level shadow of Clebsch–Gordan:

V ⊗ V* ≅ V₀ ⊕ V₂ ⊕ … ⊕ V₂ₙ₋₂, with dimensions 1, 3, …, 2n−1.

Keeping track of the weights turns this into a q-identity: [n]_q² = Σ_{m<n} [2m+1]_q, using symmetric q-integers. Set q = 1 and you get the original sum.

This is why the identity keeps turning up in physics:

- Two spin-j particles, with n = 2j+1, have total spin 0 through 2j.
- Hydrogen's level n has n² orbitals, with l = 0, …, n−1 and 2l+1 values of m each. That gives the shell sizes 2, 8, 18, 32 once you double for spin. The degeneracy comes from the hidden SO(4) symmetry. Level n is V_j ⊠ V_j, and restricting it to the diagonal SO(3) is exactly the Clebsch–Gordan decomposition above.
- Polynomial functions of degree ≤ n−1 on S² split into spherical harmonics of dimension 2l+1. Their total dimension is C(n+2, 3) − C(n, 3) = n².

## Bottom line

The inevitability comes from telescoping: a square is the sum of its own increments, and an increment of a square is an L with two arms and a corner. The representation theory explains why nature keeps using the identity. But its dimension count rests on the same L-shapes, now graded by weight. If the explanation that feels deepest doesn't reduce to "count the grid by max(i, j)," it's adding decoration, not explanation.
