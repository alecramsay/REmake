#!/usr/bin/env python3

"""
SCANNER
"""

import pyparsing as pp
from typing import Any


def parse_lines(lines: list[str], verbose: bool = False) -> list:
    """Tokenize multiple lines of source code."""

    Grammar: Any = define_grammar()

    results: list = list()

    for line in lines:
        new_results = parse_line(line, Grammar, verbose)

        if new_results:
            results.extend(new_results)

    return results


def parse_line(line: str, Grammar, verbose: bool = False) -> pp.ParseResults:
    """Tokenize a line of source code, ignoring Python-style # comments."""

    filtered: str = filter_comments(line)
    if filtered == "" or filtered == "\n":
        return []

    results: pp.ParseResults = Grammar.parseString(filtered)

    if verbose:
        print(results)

    return results


def define_grammar() -> Any:
    """Define the grammar for transparently specifying regular expressions."""

    literal: pp.QuotedString = literal_tok()

    # TODO - Flesh out the grammar

    Grammar = literal
    Grammar.ignore(pp.pythonStyleComment)

    return Grammar


### COMMENTS ###


def filter_comments(line: str) -> str:
    """Filter Python-style comments from a line of text."""

    filtered: pp.ParserElement = pp.Regex(r"#.*")

    filtered = filtered.suppress()
    qs: pp.ParserElement = pp.QuotedString('"') | pp.QuotedString("'")
    filtered = filtered.ignore(qs)

    return filtered.transform_string(line)


### LITERALS ###


def literal_tok() -> pp.QuotedString:
    """A literal string, either single or double quoted."""

    return pp.QuotedString('"', unquote_results=False) | pp.QuotedString(
        "'", unquote_results=False
    )


### RESERVED WORDS ###


def reserved_words() -> pp.Literal:
    """Reserved words (for testing)."""

    return (
        start_of_line_tok()
        | end_of_line_tok()
        | word_boundary_tok()
        | digit_tok()
        | whitespace_tok()
        | any_char_tok()
        | not_tok()
    )


def start_of_line_tok() -> pp.Literal:
    """The start of a line."""

    return pp.Literal("start_of_line")


def end_of_line_tok() -> pp.Literal:
    """The end of a line."""

    return pp.Literal("end_of_line")


def word_boundary_tok() -> pp.Literal:
    """A word boundary."""

    return pp.Literal("word_boundary")


def digit_tok() -> pp.Literal:
    """A digit."""

    return pp.Literal("digit")


def whitespace_tok() -> pp.Literal:
    """Whitespace."""

    return pp.Literal("whitespace")


def any_char_tok() -> pp.Literal:
    """Any character."""

    return pp.Literal("any_char")


def not_tok() -> pp.Literal:
    """Negation."""

    return pp.Literal("not")


### END ###
