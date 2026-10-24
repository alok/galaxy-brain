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
