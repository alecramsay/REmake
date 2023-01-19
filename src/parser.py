#!/usr/bin/env python3

"""
PARSER
"""

import pyparsing as pp
from typing import Any

from .settings import *
from .utils import *


### COMMENTS ###


def remove_comments(line: str) -> str:
    """Filter Python-style comments from a line of text."""

    filtered: pp.ParserElement = pp.Regex(r"#.*")

    filtered = filtered.suppress()
    qs: pp.ParserElement = pp.QuotedString('"') | pp.QuotedString("'")
    filtered = filtered.ignore(qs)

    return filtered.transform_string(line)


### LITERALS ###

literal_def: pp.QuotedString = pp.QuotedString(
    '"', unquote_results=False
) | pp.QuotedString("'", unquote_results=False)


@literal_def.set_parse_action
def literal_act(toks: pp.ParseResults) -> str:
    global EMIT_MODE
    global EMIT_FLAVOR

    translation: str = toks[0][1:-1]

    if EMIT_MODE == Mode.TOKENS:
        return toks[0]
    elif EMIT_MODE == Mode.REGEX:
        return translation
    elif EMIT_MODE == Mode.FREE_SPACED_REGEX:
        return free_space(translation, "Specific character(s)")

    raise ValueError("Invalid emit mode")


### NAMES ###

# TODO
name: pp.Word = pp.Word(pp.alphas, pp.alphanums + "_")


### KEYWORDS ###


start_of_line_def: pp.Keyword = pp.Keyword("LineStart")


@start_of_line_def.set_parse_action
def start_of_line_act(toks: pp.ParseResults) -> str:
    global EMIT_MODE
    global EMIT_FLAVOR

    translation: str = "^"

    if EMIT_MODE == Mode.TOKENS:
        return toks[0]
    elif EMIT_MODE == Mode.REGEX:
        return translation
    elif EMIT_MODE == Mode.FREE_SPACED_REGEX:
        return free_space(translation, "Start of line")

    raise ValueError("Invalid emit mode")


end_of_line_def: pp.Keyword = pp.Keyword("LineEnd")


@end_of_line_def.set_parse_action
def end_of_line_act(toks: pp.ParseResults) -> str:
    global EMIT_MODE
    global EMIT_FLAVOR

    translation: str = "$"

    if EMIT_MODE == Mode.TOKENS:
        return toks[0]
    elif EMIT_MODE == Mode.REGEX:
        return translation
    elif EMIT_MODE == Mode.FREE_SPACED_REGEX:
        return free_space(translation, "End of line")

    raise ValueError("Invalid emit mode")


# TODO
start_of_string_def: pp.Keyword = pp.Keyword("StringStart")

# TODO
end_of_string_def: pp.Keyword = pp.Keyword("StringEnd")

word_boundary_def: pp.Keyword = pp.Keyword("WordBoundary")


@word_boundary_def.set_parse_action
def word_boundary_act(toks: pp.ParseResults) -> str:
    global EMIT_MODE
    global EMIT_FLAVOR

    translation: str = "\b"

    if EMIT_MODE == Mode.TOKENS:
        return toks[0]
    elif EMIT_MODE == Mode.REGEX:
        return translation
    elif EMIT_MODE == Mode.FREE_SPACED_REGEX:
        return free_space(translation, "Word boundary")

    raise ValueError("Invalid emit mode")


digit_def: pp.Keyword = pp.Keyword("Digit")


@digit_def.set_parse_action
def digit_act(toks: pp.ParseResults) -> str:
    global EMIT_MODE
    global EMIT_FLAVOR

    translation: str = "\d"

    if EMIT_MODE == Mode.TOKENS:
        return toks[0]
    elif EMIT_MODE == Mode.REGEX:
        return translation
    elif EMIT_MODE == Mode.FREE_SPACED_REGEX:
        return free_space(translation, "A digit")

    raise ValueError("Invalid emit mode")


whitespace_def: pp.Keyword = pp.Keyword("Whitespace")


@whitespace_def.set_parse_action
def whitespace_act(toks: pp.ParseResults) -> str:
    global EMIT_MODE
    global EMIT_FLAVOR

    translation: str = "\s"

    if EMIT_MODE == Mode.TOKENS:
        return toks[0]
    elif EMIT_MODE == Mode.REGEX:
        return translation
    elif EMIT_MODE == Mode.FREE_SPACED_REGEX:
        return free_space(translation, "A whitespace character")

    raise ValueError("Invalid emit mode")


any_char_def: pp.Keyword = pp.Keyword("AnyCharacter")


@any_char_def.set_parse_action
def any_char_act(toks: pp.ParseResults) -> str:
    global EMIT_MODE
    global EMIT_FLAVOR

    translation: str = "."

    if EMIT_MODE == Mode.TOKENS:
        return toks[0]
    elif EMIT_MODE == Mode.REGEX:
        return translation
    elif EMIT_MODE == Mode.FREE_SPACED_REGEX:
        return free_space(translation, "Any character")

    raise ValueError("Invalid emit mode")


# TODO
not_def: pp.Keyword = pp.Keyword("Not")

pattern_def: pp.ParserElement = (
    literal_def | word_boundary_def | digit_def | whitespace_def | any_char_def
)

keywords: pp.ParserElement = (
    start_of_line_def
    | end_of_line_def
    | start_of_string_def
    | end_of_string_def
    | word_boundary_def
    | digit_def
    | whitespace_def
    | any_char_def
    | not_def
)

remake_spec: pp.ParserElement = (
    pp.Opt(start_of_line_def) + pp.OneOrMore(pattern_def) + pp.Opt(end_of_line_def)
)


### QUANTIFIERS ###

# times: pp.Literal = pp.Literal("*")
ellipsis: pp.Literal = pp.Literal("...")
quantifier_def: pp.ParserElement = pp.Suppress("*") + (
    pp.Word(pp.nums)("mincount") + pp.Suppress(",") + pp.Word(pp.nums)("maxcount")
    | pp.Word(pp.nums)("mincount") + pp.Suppress(",") + ellipsis
    | ellipsis + pp.Suppress(",") + pp.Word(pp.nums)("maxcount")
    | pp.Word(pp.nums)("count")
)


### PARSING ###


def parse_lines(
    lines: list[str],
    *,
    mode: Mode = Mode.TOKENS,
    flavor: Flavor = Flavor.PYTHON,
    verbose: bool = False
) -> pp.ParseResults:
    """Parse multiple lines of source code."""

    global EMIT_MODE
    global EMIT_FLAVOR
    EMIT_MODE = mode
    EMIT_FLAVOR = flavor

    # Remove Python-style comments
    filtered: list[str] = list()
    for line in lines:
        no_comments: str = remove_comments(line)
        filtered.append(no_comments)

    # Reconstitute the source code as a string
    source: str = "".join(filtered)

    results: pp.ParseResults = remake_spec.parseString(source)

    if verbose:
        print(results)

    # Restore the default modes
    EMIT_MODE = Mode.TOKENS
    EMIT_FLAVOR = Flavor.PYTHON

    return results


### END ###
