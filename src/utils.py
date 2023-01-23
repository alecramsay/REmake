#!/usr/bin/env python3

"""
HELPER UTILITIES
"""

from pyparsing import Keyword, Suppress, ParserElement

import src.globals as G
from .constants import *


def free_space(translation: str, comment: str, tab_inc: int = 0) -> str:
    """Return a free-spaced regex translation with a documentation comment."""
    spaces: str = " " * (COMMENT_TAB - len(translation))

    indent: str = " " * (TAB_SIZE * G.INDENT_LEVEL) if G.INDENT_LEVEL > 0 else ""
    # Apply the tab increment for the next comment(s)
    G.INDENT_LEVEL += tab_inc

    return translation + spaces + "# " + indent + comment + "\n"


def keyword_to_words(name: str) -> str:
    """Convert keyword format to spaced, lowercase words."""
    result: str = name[0].lower()

    for char in name[1:]:
        if char.isupper():  # Camel casing
            result += " "
            result += char.lower()
        elif char == "_":  # Snake casing
            result += " "
        else:
            result += char

    return result


# TODO - DELETE
def make_keyword_fn(name: str) -> ParserElement:
    """Define a keyword function."""

    return Keyword(name) + Suppress("()")


### END ###
