#!/usr/bin/env python3

"""
SCANNER
"""

import pyparsing as pp
from typing import Any


def parse_lines(lines: list[str], verbose: bool = False) -> None:
    Grammar: Any = define_grammar()

    for line in lines:
        tokens: list[str] = parse_line(line, Grammar, verbose)

        pass


def parse_line(line: str, Grammar, verbose: bool = False) -> list[str]:
    filtered: str = filter_comments(line)
    if filtered == "" or filtered == "\n":
        return []

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


# TODO - Use pp.ParseFile
