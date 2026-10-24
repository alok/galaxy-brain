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
