# Engineering Standards Canary

This public, non-production repository is a real downstream consumer of the
`AIAllTheThingz/Engineering-Standards` reusable governance workflow. It proves
that central validators execute from an immutable Engineering Standards commit
without copying central `scripts/`, `actions/`, `tests/`, or `examples/`
into the caller repository.

The canary models a synthetic integration project. It has no production
endpoints, infrastructure, customer data, environments, or secrets. Its normal
pull-request and `main` workflows are expected to pass. Deliberate negative
scenarios run only through a closed `workflow_dispatch` choice.

## Immutable workflow under test

The workflow is pinned to:

`04b3bd4d63c4fc1abf5febbe98016adeef67d1b6`

That SHA is the exact validator candidate approved for testing in Engineering
Standards PR #128. This branch records acceptance evidence for its self-CI
promotion. It does not publish a release or authorize a merge. Moving branches, tags, shortened SHAs, and caller-selected standards
references are not permitted.

## Validation

The central reusable workflow validates this repository as caller data and
uploads governance evidence. The caller-owned repository-shape job separately
proves that prohibited central implementation directories are absent.

See [Canary Operations](docs/CANARY_OPERATIONS.md) for success, controlled
failure, negative scenarios, evidence verification, pin rotation, rollback, and
release-gate procedures.

## Additional static acceptance for PR #128

The root Python and Bash files are synthetic, inert caller data. They are valid
for static analysis and deliberately fail if executed. The trusted reusable
workflow must analyze them without running them. This proof targets Linux static
analysis with Ruff 0.17.1 and ShellCheck 0.11.0; it makes no functional or
cross-platform execution claim.

The normal pull-request run must pass both language validators. Two isolated
manual-only branches each alter one source file: one introduces undefined Python
name F821 with a noqa suppression, and one removes a Bash assignment to trigger
SC2154. The caller-owned Ruff configuration excludes all files and ignores F821;
the ShellCheck configuration disables SC2154. Trusted validation must ignore
those suppressions and reject the corresponding source while the other language
and Contract still pass. Each negative uses the existing `success` dispatch
choice against intentionally invalid caller data; no default branch or normal
pull-request fixture is changed. No caller source is executed.

Run, caller commit, artifact and hash records are maintained in the draft canary
pull request. The five separate Contract/interface scenarios remain recorded in
Canary PR #8 against the same immutable standards candidate.

## Ownership and limitations

Engineering Standards maintainers own the canary. It validates the GitHub.com
cross-repository workflow interface only; GitHub Enterprise Server is not
supported because it does not expose the immutable reusable-workflow identity
used by the trusted checkout.
