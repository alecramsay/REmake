#!/usr/bin/env python3

"""
SCANNER
"""

import pyparsing as pp
from typing import Any


def parse_lines(lines: list[str], verbose: bool = False) -> None:
    Grammar: Any = define_grammar()

    tokens: list = list()

    for line in lines:
        new_tokens: list = parse_line(line, Grammar, verbose)

        if new_tokens:
            tokens.extend(new_tokens)

    return tokens


def parse_line(line: str, Grammar, verbose: bool = False) -> list[str]:

    # Filter out Python-style comments
    filtered: str = filter_comments(line)
    if filtered == "" or filtered == "\n":
        return []

    # Tokenize the rest of the line, if any
    tokens: list[str] = Grammar.parseString(filtered)

    if verbose:
        print(tokens)

    return tokens


def define_grammar() -> Any:
    literal: pp.QuotedString = pp.QuotedString('"', unquote_results=False)

    Grammar = literal
    Grammar.ignore(pp.pythonStyleComment)

    return Grammar


def filter_comments(line: str) -> str:
    """Filter Python-style comments from a line of text."""

    filtered: pp.ParserElement = pp.Regex(r"#.*")

    filtered = filtered.suppress()
    qs: pp.ParserElement = pp.QuotedString('"') | pp.QuotedString("'")
    filtered = filtered.ignore(qs)

    return filtered.transform_string(line)


### END ###
