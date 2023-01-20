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
meta_names: list[str] = [
    "DollarSign",
    "LeftParen",
    "RightParen",
    "Asterisk",
    "PlusSign",
    "Period",
    "QuestionMark",
    "LeftBracket",
    "RightBracket",
    "Caret",
    "LeftBrace",
    "RightBrace",
    "Pipe",
]
meta_dict: dict[str, str] = dict(zip(meta_names, meta_chars))

(
    dollar_sign,
    left_paren,
    right_paren,
    asterisk,
    plus_sign,
    period,
    question_mark,
    left_bracket,
    right_bracket,
    caret,
    left_brace,
    right_brace,
    pipe,
) = map(pp.CaselessKeyword, meta_names)

meta_char_def: pp.CaselessKeyword = (
    dollar_sign
    | left_paren
    | right_paren
    | asterisk
    | plus_sign
    | period
    | question_mark
    | left_bracket
    | right_bracket
    | caret
    | right_brace
    | left_brace
    | pipe
)


@meta_char_def.set_parse_action
def meta_char_act(toks: pp.ParseResults) -> str:
    if G.EMIT_MODE == G.Mode.TOKENS:
        return toks[0]

    translation: str = "\\" + meta_dict[toks[0]]
    comment: str = f"A {keyword_to_words(toks[0])} (escaped)"

    if G.EMIT_MODE == G.Mode.REGEX:
        return translation

    if G.EMIT_MODE == G.Mode.FREE_SPACED_REGEX:
        return free_space(translation, comment)

    raise ValueError("Invalid emit mode")


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
        return free_space(translation, f"One '{translation}' character")

    raise ValueError("Invalid emit mode")


### MULTI-CHARACTER STRINGS ###

# TODO - This doesn't work, for some reason.
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
# )
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
        return free_space(translation, f"The character string '{translation}'")

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


### ANY CHARACTER ###

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


### FOR EXPORT ###

consuming_chars: pp.ParserElement = (
    char_def
    | digit_def
    | word_char_def
    | whitespace_def
    | any_char_def
    | meta_char_def
    | string_def
)

non_consuming_char: pp.ParserElement = word_boundary_def


### END ###
