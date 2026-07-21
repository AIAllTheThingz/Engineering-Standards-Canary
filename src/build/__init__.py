"""Caller shadow sentinel; trusted build must never import this package."""

raise RuntimeError("caller build shadow executed")
