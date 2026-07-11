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

`091841c94fba6039443a40b7c4a28e5b9a3af2d2`

That SHA is the authoritative merge commit for Engineering Standards PR #29.
Moving branches, tags, shortened SHAs, and caller-selected standards references
are not permitted.

## Validation

The central reusable workflow validates this repository as caller data and
uploads governance evidence. The caller-owned repository-shape job separately
proves that prohibited central implementation directories are absent.

See [Canary Operations](docs/CANARY_OPERATIONS.md) for success, controlled
failure, negative scenarios, evidence verification, pin rotation, rollback, and
release-gate procedures.

## Ownership and limitations

Engineering Standards maintainers own the canary. It validates the GitHub.com
cross-repository workflow interface only; GitHub Enterprise Server is not
supported because it does not expose the immutable reusable-workflow identity
used by the trusted checkout.
