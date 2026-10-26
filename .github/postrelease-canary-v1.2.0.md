# Historical v1.2.0 PostRelease Canary

The original published-ref success run
[31652545960](https://github.com/AIAllTheThingz/Engineering-Standards-Canary/actions/runs/31652545960)
failed because `v1.2.0` compared annotated tag object
`42fa18ed9744fa98ce1f9048e3610f7ed6ff7507` directly with peeled standards commit
`6c0050de328ac083e69fbac8971a317689c2c1d6`. Its result remains Failed. The old
artifact collection is now empty and is not claimed independently reverified.

The replacement acceptance matrix uses the already-published `v1.2.1` commit
`7d15ec8be6d8c3cdca35061728901584437e4a50` in all five calls of the existing
closed manual dispatcher. Normal pull requests run only its success case.
There are no separate automatic negative workflows.

These are immutable-commit downstream acceptance tests. They do not certify a
new PostRelease tag test or relabel the old `v1.2.0` failure. Published tags,
releases, permissions and scenario expectations are not changed.

This validation-only pull request must remain unmerged. Current run, artifact,
hash and reviewer records are maintained in its description. Reverting the
correction commit restores the prior branch files; no published history is
rewritten.
