#!/usr/bin/env python3

"""
CHARACTERS
"""

import pyparsing as pp
from typing import Any

import src.globals as G
from .constants import *
from .utils import *


### META CHARACTERS ###

meta_chars: str = "$()*+.?[]^}{|"
meta_char_def: pp.Char = pp.Char(meta_chars)
# TODO - HERE

### INDIVIDUAL CHARACTERS ###

char: pp.Char = pp.Char(pp.printables, exclude_chars=meta_chars)
double_quote: pp.Literal = pp.Literal('"')
single_quote: pp.Literal = pp.Literal("'")

char_def: pp.Char = pp.Combine(double_quote + char + double_quote) | pp.Combine(
    single_quote + char + single_quote
)


@char_def.set_parse_action
def char_act(toks: pp.ParseResults) -> str:
    if G.EMIT_MODE == G.Mode.TOKENS:
        return toks[0]

    translation: str = toks[0][1:-1]

    if G.EMIT_MODE == G.Mode.REGEX:
        return translation

    if G.EMIT_MODE == G.Mode.FREE_SPACED_REGEX:
        return free_space(translation, "One '{translation}' character}")

    raise ValueError("Invalid emit mode")


### MULTI-CHARACTER STRINGS ###

# TODO - Build this on top of char
# string: pp.Word = pp.Word(
#     pp.printables, exclude_chars=meta_chars, min=2, as_keyword=True
# )
# double_quoted_string: pp.ParserElement = pp.Combine(
#     double_quote + string + double_quote
# )
# single_quoted_string: pp.ParserElement = pp.Combine(
#     single_quote + string + single_quote
# )
# string_def: pp.ParserElement = (
#     double_quoted_string | single_quoted_string
# )  # This doesn't work!
string_def: pp.QuotedString = pp.QuotedString(
    '"', unquote_results=False
) | pp.QuotedString("'", unquote_results=False)


@string_def.set_parse_action
def string_act(toks: pp.ParseResults) -> str:
    if G.EMIT_MODE == G.Mode.TOKENS:
        return toks[0]

    translation: str = toks[0][1:-1]

    if G.EMIT_MODE == G.Mode.REGEX:
        return translation

    if G.EMIT_MODE == G.Mode.FREE_SPACED_REGEX:
        return free_space(translation, "Specific character(s)")

    raise ValueError("Invalid emit mode")


### CHARACTER SHORTHANDS ###

digit_def: pp.CaselessKeyword = pp.CaselessKeyword("Digit")


@digit_def.set_parse_action
def digit_act(toks: pp.ParseResults) -> str:
    if G.EMIT_MODE == G.Mode.TOKENS:
        return toks[0]

    translation: str = "\d"

    if G.EMIT_MODE == G.Mode.REGEX:
        return translation

    if G.EMIT_MODE == G.Mode.FREE_SPACED_REGEX:
        return free_space(translation, "A digit")

    raise ValueError("Invalid emit mode")


word_char_def: pp.CaselessKeyword = pp.CaselessKeyword("WordCharacter")


@word_char_def.set_parse_action
def word_char_act(toks: pp.ParseResults) -> str:
    if G.EMIT_MODE == G.Mode.TOKENS:
        return toks[0]

    translation: str = "\w"

    if G.EMIT_MODE == G.Mode.REGEX:
        return translation

    if G.EMIT_MODE == G.Mode.FREE_SPACED_REGEX:
        return free_space(translation, "A word character")

    raise ValueError("Invalid emit mode")


whitespace_def: pp.CaselessKeyword = pp.CaselessKeyword("Whitespace")


@whitespace_def.set_parse_action
def whitespace_act(toks: pp.ParseResults) -> str:
    if G.EMIT_MODE == G.Mode.TOKENS:
        return toks[0]

    translation: str = "\s"

    if G.EMIT_MODE == G.Mode.REGEX:
        return translation

    if G.EMIT_MODE == G.Mode.FREE_SPACED_REGEX:
        return free_space(translation, "A whitespace character")

    raise ValueError("Invalid emit mode")


### BOUDNARIES ###

word_boundary_def: pp.CaselessKeyword = pp.CaselessKeyword("WordBoundary")


@word_boundary_def.set_parse_action
def word_boundary_act(toks: pp.ParseResults) -> str:
    if G.EMIT_MODE == G.Mode.TOKENS:
        return toks[0]

    translation: str = "\b"

    if G.EMIT_MODE == G.Mode.REGEX:
        return translation

    if G.EMIT_MODE == G.Mode.FREE_SPACED_REGEX:
        return free_space(translation, "Word boundary")

    raise ValueError("Invalid emit mode")


### MISC ###

any_char_def: pp.CaselessKeyword = pp.CaselessKeyword("AnyCharacter")


@any_char_def.set_parse_action
def any_char_act(toks: pp.ParseResults) -> str:
    if G.EMIT_MODE == G.Mode.TOKENS:
        return toks[0]

    translation: str = "."

    if G.EMIT_MODE == G.Mode.REGEX:
        return translation

    if G.EMIT_MODE == G.Mode.FREE_SPACED_REGEX:
        return free_space(translation, "Any character (except newline)")

    raise ValueError("Invalid emit mode")


### END ###
