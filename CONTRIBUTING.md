# Contributing

Python changes must keep the runtime dependency lock application-only and must
not add validator packages. Validate both governance and Python functional jobs
against the same exact Engineering Standards candidate SHA.

Changes must preserve this repository as a minimal public downstream governance
consumer. Keep normal pull-request and `main` validation passing, retain the
immutable Engineering Standards workflow pin, and avoid copied central
implementation directories.

Use a pull request for substantive changes. Explain the candidate standards SHA,
scenario impact, security impact, validation commands, hosted run IDs, artifact
digests, rollback, and remaining limitations.

Negative scenarios may change only their isolated fixture or dispatch mapping.
They must remain manually triggered and must fail for the documented reason.
Do not weaken central governance or add exceptions merely to make a scenario
green.

Before requesting review:

1. Validate the manifest and governance configuration.
2. Parse workflow YAML.
3. Confirm permissions are exactly `contents: read`.
4. Confirm the workflow reference is a full 40-character SHA.
5. Confirm no `scripts`, `actions`, `tests`, or `examples` directory exists.
6. Run the success canary and inspect its downloaded evidence.
7. Run deliberate negative scenarios and confirm their exact failure reasons.
