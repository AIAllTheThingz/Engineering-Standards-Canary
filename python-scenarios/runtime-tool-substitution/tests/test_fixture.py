"""Synthetic test that must never execute because the runtime lock is invalid."""


def test_unreachable() -> None:
    assert True
