#!/usr/bin/env python3

"""
HELPER UTILITIES
"""

from .settings import *


def free_space(translation: str, comment: str) -> str:
    """Return a free-spaced regex translation with a documentation comment."""
    spaces: str = " " * (COMMENT_TAB - len(translation))

    return translation + spaces + "# " + comment + "\n"


# TODO - DELETE
# def is_quoted_string(token: str) -> bool:
#     """Return True if token is a quoted string, False otherwise."""

#     return (token.startswith('"') and token.endswith('"')) or (
#         token.startswith("'") and token.endswith("'")
#     )


### END ###
