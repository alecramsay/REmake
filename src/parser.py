#!/usr/bin/env python3

"""
SCANNER
"""

import pyparsing as pp
from typing import Any


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


### RESERVED WORDS ###


start_of_line_def: pp.Literal = pp.Literal("start_of_line")

end_of_line_def: pp.Literal = pp.Literal("end_of_line")

word_boundary_def: pp.Literal = pp.Literal("word_boundary")

digit_def: pp.Literal = pp.Literal("digit")

whitespace_def: pp.Literal = pp.Literal("whitespace")

any_char_def: pp.Literal = pp.Literal("any_char")

not_def: pp.Literal = pp.Literal("not")

pattern_def: pp.Literal = (
    literal_def | word_boundary_def | digit_def | whitespace_def | any_char_def
)

reserved_words: pp.Literal = (
    start_of_line_def
    | end_of_line_def
    | word_boundary_def
    | digit_def
    | whitespace_def
    | any_char_def
    | not_def
)


remake_spec: pp.ParserElement = pattern_def()


### PARSING ###


def parse_lines(lines: list[str], verbose: bool = False) -> list:
    """Tokenize multiple lines of source code."""

    results: list = list()

    for line in lines:
        new_results: pp.ParseResults = parse_line(line, verbose)

        if new_results:
            results.extend(new_results)

    return results


def parse_line(line: str, verbose: bool = False) -> pp.ParseResults:
    """Tokenize a line of source code, ignoring Python-style # comments."""

    filtered: str = remove_comments(line)
    if filtered == "" or filtered == "\n":
        return []

    results: pp.ParseResults = remake_spec.parseString(filtered)

    if verbose:
        print(results)

    return results


### END ###
