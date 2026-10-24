`=` assigns, it doesn't compare. Use `===`:

```js
if (x === 5) { ... }
```

You asked for the non-obvious take. Here the obvious answer is the correct one, and stacking clever reframes on top would just be noise. What I can offer is the mechanism, which explains more than "wrong operator" does.

**Why the branch always runs.** In JavaScript, assignment is an expression that evaluates to the value it assigned. So `x = 5` evaluates to `5`, `if` coerces that to boolean, and `5` is truthy. The condition doesn't depend on what `x` was before. It depends only on the literal on the right side:

```js
let x = 3;
if (x = 5) {}   // runs: 5 is truthy
if (x = 0) {}   // never runs: 0 is falsy
if (x = "") {}  // never runs
```

**The worse part is the side effect.** The bug isn't only that the branch runs. Every pass through that line also overwrites `x` with `5`. Code after the `if` sees `x === 5` even though it was 3, so the symptom can appear far from the cause. If anything downstream is acting strangely, this line is the reason.

**Why the language allows it.** Assignment-as-expression is inherited from C. It makes idioms like `while ((m = re.exec(s)) !== null)` and `a = b = 0` possible. The tradeoff is that `=` and `==` sit one keystroke apart, and both forms parse.

**How to make it impossible to repeat:**
- ESLint's `no-cond-assign` is in `eslint:recommended` and flags this. Its default mode (`"except-parens"`) allows `if ((x = 5))` with double parentheses. That is the conventional way to say "yes, I mean to assign here," so a deliberate assignment stays possible while a typo gets caught.
- Yoda conditions (`if (5 === x)`) were the old defense, because `5 = x` is a syntax error. Once you have a linter, they're just harder to read. Skip them.
- Use `===` rather than `==` while you're fixing this. That's a separate issue from this bug, but it's the comparison you actually want.
