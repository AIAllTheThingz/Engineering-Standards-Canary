# Canary Agent Instructions

This repository is a public, synthetic, non-production downstream governance
consumer. It extends the central Engineering Standards
`agents/AGENTS_Base.md` and `agents/AGENTS_Integration.md` requirements at
the immutable workflow revision recorded in
`.github/workflows/governance.yml`.

Agents must keep the repository free of secrets, production identifiers,
customer data, endpoints, infrastructure, and copied central validator
directories. Do not add top-level or nested directories named `scripts`,
`actions`, `tests`, or `examples`.

Workflow permissions must remain `contents: read`. Do not add secrets,
environments, write permissions, `pull_request_target`, mutable workflow
references, or caller-controlled standards repository and SHA inputs.

Normal pull-request and default-branch validation must stay green. Negative
scenarios are synthetic, manually dispatched, and must fail for their named
governance reason while still uploading evidence.

Before completion, validate JSON contracts, YAML syntax, Markdown links,
required documentation, workflow permissions, immutable SHA pinning, repository
shape, expected GitHub conclusions, and downloaded artifacts. Report statuses
only as `Passed`, `Failed`, `Blocked`, `NotRun`, or `NotApplicable`.
