"""Caller shadow sentinel; trusted pip-audit must never import this package."""

raise RuntimeError("caller pip-audit shadow executed")
