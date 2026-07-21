"""Caller shadow sentinel; trusted pytest must never import this package."""

raise RuntimeError("caller pytest shadow executed")
