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

The separate Bash functional canary exercises the central immutable Bash
reusable workflow against `bash-functional/`. Pull requests and pushes run only
the passing scenario. Manual dispatch selects exactly one of success,
ShellCheck failure, formatting failure, Bats failure, or caller-configuration
bypass so each run receives its own identity-bound evidence artifact.

## Immutable workflow under test

The workflow is pinned to:

`6c0050de328ac083e69fbac8971a317689c2c1d6`

That SHA is the Engineering Standards `1.2.0` release candidate validated by
this canary. It becomes an authoritative released revision only after the
required protected review, release approval, tag, and GitHub Release lifecycle
complete. Moving branches, tags, shortened SHAs, and caller-selected standards
references are not permitted.

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
