#!/usr/bin/env python3

"""
HELPER UTILITIES
"""

from pyparsing import ParseResults, Suppress
from typing import Any

import src.globals as G
from .reserved import *
from .constants import *


### EMIT HELPERS ###


def modal_act(
    toks: ParseResults,
    translation: str,
    comment: str,
    *,
    tab_inc: int = 0,
    tok_list: bool = False
) -> str:
    """Emit raw tokens, a single-line regex, or a free-spaced regex."""

    if G.EMIT_MODE == G.Mode.TOKENS:
        # NOTE - tab_inc is zero for atomic words, +/– for paired items
        return toks if tok_list else toks[0]

    if G.EMIT_MODE == G.Mode.REGEX:
        return translation

    if G.EMIT_MODE == G.Mode.FREE_SPACED_REGEX:
        return free_space(translation, comment, tab_inc=tab_inc)

    raise ValueError("Invalid emit mode")


def unpack_token(toks: ParseResults, grouped: bool = False) -> Any:
    """Unpack the token from ParseResults object."""

    token: str = list(toks[0])[0] if grouped else toks[0]
    return token


def translate_word(word: str) -> str:
    """Lookup the atomic word in the dictionary."""

    return reserved_word_dict[word]


def free_space(translation: str, comment: str, tab_inc: int = 0) -> str:
    """Return a free-spaced regex translation with a documentation comment."""

    indent: str = " " * (TAB_SIZE * G.INDENT_LEVEL) if G.INDENT_LEVEL > 0 else ""

    if COMMENT_TAB < (len(translation) + len(indent)):
        raise ValueError("Comment tab is too small")

    spaces: str = " " * (COMMENT_TAB - len(translation) - len(indent))

    # Apply the tab increment for the next comment(s)
    G.INDENT_LEVEL += tab_inc

    return indent + translation + spaces + "# " + comment + "\n"


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


def append_suppress(word: Keyword) -> Keyword:
    """Append a Suppress to a reserved keyword."""

    return word + Suppress("()")


### END ###
