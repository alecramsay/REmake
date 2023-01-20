#!/usr/bin/env python3

"""
CHARACTERS
"""

import pyparsing as pp
from typing import Any

from .settings import *
from .utils import *


### LITERAL STRINGS ###

literal_def: pp.QuotedString = pp.QuotedString(
    '"', unquote_results=False
) | pp.QuotedString("'", unquote_results=False)


@literal_def.set_parse_action
def literal_act(toks: pp.ParseResults) -> str:
    global EMIT_MODE
    global EMIT_FLAVOR

    if EMIT_MODE == Mode.TOKENS:
        return toks[0]

    translation: str = toks[0][1:-1]

    if EMIT_MODE == Mode.REGEX:
        return translation

    if EMIT_MODE == Mode.FREE_SPACED_REGEX:
        return free_space(translation, "Specific character(s)")

    raise ValueError("Invalid emit mode")


### CHARACTER SHORTHANDS ###

digit_def: pp.CaselessKeyword = pp.CaselessKeyword("Digit")


@digit_def.set_parse_action
def digit_act(toks: pp.ParseResults) -> str:
    global EMIT_MODE
    global EMIT_FLAVOR

    if EMIT_MODE == Mode.TOKENS:
        return toks[0]

    translation: str = "\d"

    if EMIT_MODE == Mode.REGEX:
        return translation

    if EMIT_MODE == Mode.FREE_SPACED_REGEX:
        return free_space(translation, "A digit")

    raise ValueError("Invalid emit mode")


word_char_def: pp.CaselessKeyword = pp.CaselessKeyword("WordCharacter")


@word_char_def.set_parse_action
def word_char_act(toks: pp.ParseResults) -> str:
    global EMIT_MODE
    global EMIT_FLAVOR

    if EMIT_MODE == Mode.TOKENS:
        return toks[0]

    translation: str = "\w"

    if EMIT_MODE == Mode.REGEX:
        return translation

    if EMIT_MODE == Mode.FREE_SPACED_REGEX:
        return free_space(translation, "A word character")

    raise ValueError("Invalid emit mode")


whitespace_def: pp.CaselessKeyword = pp.CaselessKeyword("Whitespace")


@whitespace_def.set_parse_action
def whitespace_act(toks: pp.ParseResults) -> str:
    global EMIT_MODE
    global EMIT_FLAVOR

    if EMIT_MODE == Mode.TOKENS:
        return toks[0]

    translation: str = "\s"

    if EMIT_MODE == Mode.REGEX:
        return translation

    if EMIT_MODE == Mode.FREE_SPACED_REGEX:
        return free_space(translation, "A whitespace character")

    raise ValueError("Invalid emit mode")


### BOUDNARIES ###

word_boundary_def: pp.CaselessKeyword = pp.CaselessKeyword("WordBoundary")


@word_boundary_def.set_parse_action
def word_boundary_act(toks: pp.ParseResults) -> str:
    global EMIT_MODE
    global EMIT_FLAVOR

    if EMIT_MODE == Mode.TOKENS:
        return toks[0]

    translation: str = "\b"

    if EMIT_MODE == Mode.REGEX:
        return translation

    if EMIT_MODE == Mode.FREE_SPACED_REGEX:
        return free_space(translation, "Word boundary")

    raise ValueError("Invalid emit mode")


### MISC ###

any_char_def: pp.CaselessKeyword = pp.CaselessKeyword("AnyCharacter")


@any_char_def.set_parse_action
def any_char_act(toks: pp.ParseResults) -> str:
    global EMIT_MODE
    global EMIT_FLAVOR

    if EMIT_MODE == Mode.TOKENS:
        return toks[0]

    translation: str = "."

    if EMIT_MODE == Mode.REGEX:
        return translation

    if EMIT_MODE == Mode.FREE_SPACED_REGEX:
        return free_space(translation, "Any character (except newline)")

    raise ValueError("Invalid emit mode")


### END ###
