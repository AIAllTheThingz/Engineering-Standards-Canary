"""Installed-wheel behavior tests."""

import pytest
from canary_identity import canary_identity


def test_valid_identity() -> None:
    candidate = "a" * 40
    assert canary_identity(candidate) == candidate


@pytest.mark.parametrize("candidate", ["a" * 39, "A" * 40, "g" * 40])
def test_invalid_identity(candidate: str) -> None:
    with pytest.raises(ValueError, match="40 lowercase hexadecimal"):
        canary_identity(candidate)
