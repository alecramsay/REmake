#!/usr/bin/env python3

"""
HELPER UTILITIES
"""

from .constants import *


def free_space(translation: str, comment: str) -> str:
    """Return a free-spaced regex translation with a documentation comment."""
    spaces: str = " " * (COMMENT_TAB - len(translation))

    return translation + spaces + "# " + comment + "\n"


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
