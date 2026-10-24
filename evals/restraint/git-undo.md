```sh
git reset --soft HEAD~1
```

That's the answer. `--soft` moves the branch pointer back one commit and leaves both the index and the working tree alone, so everything from the commit is staged again. You haven't pushed, so no one else's history changes.

Honestly, there isn't a clever reframe here. This is a narrow question and the obvious answer is correct. What I can give you is a few edge cases that catch people out:

- **You might want `git commit --amend` instead.** If the plan is "undo, tweak, recommit", amending does all of that in one step: stage the fix, then `git commit --amend` (add `--no-edit` to keep the message).
- **Getting it back is easy.** Right after the reset, `ORIG_HEAD` points at the commit you just undid, so `git reset --soft ORIG_HEAD` puts it back. Later on, `git reflog` still has it.
- **Anything you staged after the commit gets merged in.** The index ends up holding the old commit's changes plus whatever you staged since, with nothing marking which is which. If you need them kept apart, run `git stash` before the reset.
- **It fails on the first commit in a repo.** `HEAD~1` doesn't exist there. Use `git update-ref -d HEAD`, which keeps the index, so the files stay staged.
- **Don't use `--mixed` (the default) or `--hard`.** `--mixed` unstages the changes and `--hard` deletes them. Only `--soft` matches what you asked for.
