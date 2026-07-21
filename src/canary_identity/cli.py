"""Safe console entry point for installed-wheel smoke validation."""

from __future__ import annotations

import argparse


def main() -> int:
    """Parse the synthetic command without external effects."""
    parser = argparse.ArgumentParser(description="Validate a synthetic candidate SHA.")
    parser.add_argument("candidate_sha", nargs="?")
    parser.parse_args()
    return 0
