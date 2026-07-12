# Canary Operations

## Purpose

This repository is the public external-consumer acceptance canary for
`AIAllTheThingz/Engineering-Standards`. It proves the documented downstream
interface against an exact immutable Engineering Standards SHA without copied
central validator implementation.

## Ownership

Engineering Standards maintainers own workflow-pin updates, scenario execution,
artifact verification, failure triage, and rollback. The repository is
non-production and requires no credentials or external endpoints.

## Normal success

Pull requests and pushes to `main` run the root project with governance version
`1.1.0`. A successful run must pass the repository-shape job and reusable
governance job, upload `governance-evidence-<run-id>`, and record the caller
repository/commit plus the Engineering Standards repository/workflow SHA.

A manual success proof uses:

```powershell
gh workflow run governance.yml --repo AIAllTheThingz/Engineering-Standards-Canary --ref <reviewed-ref> -f scenario=success
```

## Controlled failure

Dispatch `controlled-failure` only as a deliberate proof. Normal Contract
validation must complete, evidence must be generated and uploaded, and the job
must fail only at final mandatory enforcement.

```powershell
gh workflow run governance.yml --repo AIAllTheThingz/Engineering-Standards-Canary --ref <reviewed-ref> -f scenario=controlled-failure
```

## Negative scenarios

The closed dispatch choices are:

- `governance-version-mismatch`: expects `1.0.0` while the root manifest declares `1.1.0`.
- `missing-required-file`: validates a committed fixture that intentionally omits required `SECURITY.md`; the expected diagnostic identifies `SECURITY.md` as nonexistent beneath the selected project.
- `mandatory-control-disablement`: validates a committed fixture with a synthetic nonempty `mandatoryControlsDisabled`.

Each scenario must fail for its named reason. The root project and default branch
remain unchanged and passing. Do not edit or remove default-branch files to
exercise a negative test.

## Artifact verification

For every run, record the caller SHA, standards SHA, run and job IDs, expected
and actual conclusion, artifact ID/name/digest, and intended failure message.
Download artifacts into isolated temporary directories. Use the central
`scripts/Test-WorkflowEvidenceArtifact.ps1` at the reviewed Engineering
Standards checkout to verify identity, conclusion, referenced hashes and sizes,
path safety, credential patterns, and unexpected executable files.

For every negative scenario, confirm the downloaded artifact itself contains
the exact sanitized diagnostic. Workflow logs alone are not acceptance evidence.

At minimum, independently verify success and controlled-failure artifacts.
Negative artifacts should also be inspected when retained.

## Candidate pin updates and release gate

To test a candidate release, change the reusable-workflow reference only to the
exact reviewed 40-character candidate SHA, open a canary pull request, and run
all five scenarios. Record the resulting evidence in the Engineering Standards
release pull request.

A release that modifies the reusable governance workflow, its public downstream
interface, or an authoritative reusable-workflow pin is blocked unless this
external canary succeeds against the exact candidate SHA and the controlled and
policy-negative scenarios fail for their intended reasons. Documentation-,
policy-, schema-, or metadata-only releases that do not change those workflow
surfaces do not require a new canary run. Never substitute a moving branch, tag,
local fixture, or same-repository self-CI run for the required gate.

## Troubleshooting

Confirm the caller SHA, reusable workflow SHA, selected project path, manifest
version, required documents, and mandatory-control configuration. Confirm no
central implementation directories were added. A negative scenario that fails
for a different reason is not valid proof and must be corrected and rerun.

## Rollback

Revert the canary pin commit or its merge commit to restore the last verified
immutable SHA. Do not rewrite `main` or published evidence. If a candidate
fails, keep the prior verified pin and block release until remediation succeeds.

## Known limitations

The canary validates GitHub.com reusable-workflow behavior. It does not validate
GitHub Enterprise Server, production infrastructure, vendor endpoints, secrets,
or application runtime behavior.
