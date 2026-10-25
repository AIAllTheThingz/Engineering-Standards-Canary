"""Synthetic caller data that trusted validation must never execute."""

raise RuntimeError("Caller code must remain inert during static validation.")
