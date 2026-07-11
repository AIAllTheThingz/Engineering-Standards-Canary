# Security

## Scope

This repository contains only public synthetic governance-canary content. It
must not contain credentials, tokens, private keys, production endpoints,
customer data, regulated data, internal infrastructure identifiers, or
secret-bearing evidence.

## Workflow security

GitHub Actions permissions are limited to `contents: read`. The canary sends
no secrets to the reusable workflow, uses no protected environments, avoids
`pull_request_target`, and pins the central workflow to a full immutable
commit SHA.

The reusable workflow treats this repository as untrusted caller data. Trusted
validators come from the pinned Engineering Standards checkout, and generated
evidence is written to a separate workspace.

## Reporting

Report suspected vulnerabilities privately through the security reporting
channel on the Engineering Standards repository. Do not place credentials or
sensitive reproduction data in public issues, pull requests, logs, or
artifacts.

## Response

If sensitive material appears, stop canary execution, revoke or rotate the
affected credential, remove exposed artifacts where authorized, preserve
incident evidence through the approved process, and do not claim the canary
passed.
