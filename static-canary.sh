#!/usr/bin/env bash
# Synthetic caller data; execution must fail, while static validation must pass.
set -euo pipefail
value='synthetic caller data'
printf '%s\n' "$value"
exit 99
