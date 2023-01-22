#!/usr/bin/env python3

"""
HELPER UTILITIES
"""

import src.globals as G
from .constants import *


def free_space(translation: str, comment: str) -> str:
    """Return a free-spaced regex translation with a documentation comment."""
    spaces: str = " " * (COMMENT_TAB - len(translation))

    tab: str = " " * TAB_SIZE if G.INDENT_LEVEL > 0 else ""

    return translation + spaces + "# " + tab + comment + "\n"


def keyword_to_words(name: str) -> str:
    """Convert keyword format to spaced, lowercase words."""
    result: str = name[0].lower()

    for char in name[1:]:
        if char.isupper():
            result += " "
            result += char.lower()
        else:
            result += char

    return result


### END ###
