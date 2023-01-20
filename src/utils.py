#!/usr/bin/env python3

"""
HELPER UTILITIES
"""

from .settings import *


def free_space(translation: str, comment: str) -> str:
    """Return a free-spaced regex translation with a documentation comment."""
    spaces: str = " " * (COMMENT_TAB - len(translation))

    return translation + spaces + "# " + comment + "\n"


### END ###
