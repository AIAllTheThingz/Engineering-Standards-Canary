"""Inert maintained Python source for downstream static canary coverage."""


def canary_identity(candidate_sha: str) -> str:
    """Return an exact validated lowercase commit identity."""
    invalid_character = any(
        character not in "0123456789abcdef" for character in candidate_sha
    )
    if len(candidate_sha) != 40 or invalid_character:
        raise ValueError("candidate SHA must be exactly 40 lowercase hexadecimal characters")
    return candidate_sha
