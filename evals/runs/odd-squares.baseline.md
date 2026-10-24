**Short version:** the odd numbers are the gaps between consecutive squares. If you add up all the gaps from $0$ to $n^2$, you get $n^2$. There's nothing else to it. The induction proof contains this too, but it only shows it one step at a time.

## Start with the grid

Label each cell $(i,j)$ of an $n \times n$ grid with $\max(i,j)$. For $n = 4$:

```
4 4 4 4
3 3 3 4
2 2 3 4
1 2 3 4
```

The cells labeled $k$ form an L-shape (a gnomon). It has $k$ cells along the top row, $k$ along the right column, and they share one corner, so it has $2k-1$ cells. Every cell gets exactly one label, so

$$n^2 = |[n]\times[n]| = \sum_{k=1}^{n} \#\{\max = k\} = \sum_{k=1}^{n} (2k-1).$$

This is a bijective proof: the identity just says the level sets of $\max$ partition the square. The $k$-th odd number is the $k$-th shell of an onion.

## Why it has to work: discrete calculus

The real statement is $k^2 - (k-1)^2 = 2k-1$. Once you have that, the sum telescopes:

$$\sum_{k=1}^n \big(f(k) - f(k-1)\big) = f(n) - f(0).$$

That's the fundamental theorem of calculus for sequences. The odd numbers are $\nabla(k^2)$, the backward difference of the squares. Summing a difference gives back the function. So asking "why do the odd numbers sum to squares?" is like asking why $\int_0^n 2x\,dx = n^2$. The answer is the same in both cases: you're integrating a derivative.

The comparison holds up in detail. In the gnomon:
- **$2k$** is the two edges of length $k$. This is the $2x\,dx$ term.
- **$-1$** is the corner cell those edges share. This is the $(dx)^2$ term, the second-order piece of the binomial expansion.

Shrink the grid to mesh $1/N$ with $N$ hyperfinite. You get $\sum_{k\le N} (2k-1)/N^2 = 1$ exactly. The corner cells add up to $N \cdot (1/N^2) = 1/N$, which is infinitesimal. Take the standard part and you get $\int_0^1 2x\,dx = 1$. So the odd-number identity is the exact discrete version of that integral, and the "$-1$" is the correction that vanishes in the limit.

## Why the odd numbers specifically: forced by uniqueness

Turn the question around. If the partial sums are to be $n^2$, the terms must be $n^2 - (n-1)^2 = 2n-1$. No other sequence works. You can also see it through the mean. The sum of an arithmetic progression is (number of terms) × (mean of the endpoints). For $a, a+d, \dots$ with $n$ terms, the mean is $a + (n-1)d/2$. This equals $n$ for every $n$ only when $a=1$ and $d=2$. The odd numbers are the only arithmetic progression whose mean always equals its length. That's Gauss's pairing trick: $1 + (2n-1) = 2n$, and there are $n/2$ such pairs.

## A rigidity version (less illuminating, but airtight)

$S(n) = \sum_{k \le n}(2k-1)$ is a polynomial of degree 2. The difference $S(n) - n^2$ is a quadratic with zeros at $n=0,1,2$, so it is identically zero. This shows the result couldn't be otherwise, but it doesn't explain anything.

## Checks that you've really got it

- **Other ways to cut the same grid.** Group cells by $i+j$ and you get $n^2 = 1 + 2 + \dots + n + \dots + 2 + 1$, which is $T_n + T_{n-1}$. Grouping by $\min$ gives the odd numbers in reverse order. Same square, different partitions.
- **One dimension up.** Group $[n]^3$ by $\max$. The shells are $k^3 - (k-1)^3 = 3k^2 - 3k + 1 = 1, 7, 19, 37, \dots$. Each shell is three faces, minus the three edges counted twice, plus the corner counted three times (inclusion–exclusion). These are the centered hexagonal numbers. Look at a cube down its main diagonal and the outer shell does look like a hexagon. In dimension $d$, the shells are $\nabla(k^d)$.
- **Physics.** Galileo found that a falling body covers distances in the ratio $1:3:5:7$ over successive equal time intervals. Distance grows like $t^2$, so the distance covered in each interval is the backward difference of the squares. "Constant acceleration" is "constant second difference" in physical form.

## Which explanation is deepest

I'd rank them: **discrete FTC = gnomon = $\max$-partition** (one idea written three ways) > the mean-equals-length uniqueness argument > polynomial rigidity. Induction isn't really a separate proof. It's the telescoping argument checked one term at a time, and its inductive step, $n^2 + (2n+1) = (n+1)^2$, is the whole content.
