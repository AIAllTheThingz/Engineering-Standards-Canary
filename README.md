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

`7d15ec8be6d8c3cdca35061728901584437e4a50`

That SHA is the immutable commit of the already-published Engineering Standards
`v1.2.1` release. All five acceptance calls use this exact revision. These runs
validate the released commit as a downstream consumer; they do not replace the
separate published-tag PostRelease certificate. Moving branches, tags, shortened SHAs, and caller-selected standards
references are not permitted.

## Validation

The central reusable workflow validates this repository as caller data and
uploads governance evidence. The caller-owned repository-shape job separately
proves that prohibited central implementation directories are absent.

See [Canary Operations](docs/CANARY_OPERATIONS.md) for success, controlled
failure, negative scenarios, evidence verification, pin rotation, rollback, and
release-gate procedures.

Only the success case runs for normal pull requests and pushes to `main`.
The four deliberate failures remain isolated choices in the existing closed
manual dispatcher. Their failed conclusions are accepted only when the
downloaded evidence proves the exact intended reason.

The [historical v1.2.0 record](.github/postrelease-canary-v1.2.0.md) retains the
failed annotated-tag observation. The immutable `v1.2.1` acceptance runs do not
relabel that older release as passing or modify either published tag.

## Ownership and limitations

Engineering Standards maintainers own the canary. It validates the GitHub.com
cross-repository workflow interface only; GitHub Enterprise Server is not
supported because it does not expose the immutable reusable-workflow identity
used by the trusted checkout.
