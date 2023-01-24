#!/usr/bin/env python3

"""
HELPER UTILITIES
"""

from pyparsing import ParseResults
from typing import Any

import src.globals as G
from .reserved import *
from .constants import *


### EMIT HELPERS ###


def word_act(toks: ParseResults, translation: str, comment: str) -> str:
    if G.EMIT_MODE == G.Mode.TOKENS:
        return toks[0]

    if G.EMIT_MODE == G.Mode.REGEX:
        return translation

    if G.EMIT_MODE == G.Mode.FREE_SPACED_REGEX:
        return free_space(translation, comment)

    raise ValueError("Invalid emit mode")


def beg_paired_act(toks: ParseResults, translation: str, comment: str) -> str:
    """Open pair action template."""

    if G.EMIT_MODE == G.Mode.TOKENS:
        return toks

    if G.EMIT_MODE == G.Mode.REGEX:
        return translation

    if G.EMIT_MODE == G.Mode.FREE_SPACED_REGEX:
        return free_space(translation, comment, tab_inc=1)

    raise ValueError("Invalid emit mode")


def end_paired_act(toks: ParseResults, translation: str, comment: str) -> str:
    """Close pair action template."""

    if G.EMIT_MODE == G.Mode.TOKENS:
        return toks

    if G.EMIT_MODE == G.Mode.REGEX:
        return translation

    if G.EMIT_MODE == G.Mode.FREE_SPACED_REGEX:
        return free_space(translation, comment, tab_inc=-1)

    raise ValueError("Invalid emit mode")


def unpack_token(toks: ParseResults, grouped: bool = False) -> Any:
    """Unpack the token from ParseResults object."""

    token: str = list(toks[0])[0] if grouped else toks[0]
    return token


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


### END ###
