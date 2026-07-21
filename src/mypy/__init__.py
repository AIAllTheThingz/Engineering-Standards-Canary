"""Caller shadow sentinel; trusted mypy must never import this package."""

raise RuntimeError("caller mypy shadow executed")
