#!/usr/bin/env python3

"""
HELPER UTILITIES
"""


def is_quoted_string(token: str) -> bool:
    """Return True if token is a quoted string, False otherwise."""

    return (token.startswith('"') and token.endswith('"')) or (
        token.startswith("'") and token.endswith("'")
    )


### END ###
