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

    literal: pp.QuotedString = literal_spec()

    # TODO - Flesh out the grammar

    Grammar = literal
    Grammar.ignore(pp.pythonStyleComment)

    return Grammar


### HELPERS ###


def filter_comments(line: str) -> str:
    """Filter Python-style comments from a line of text."""

    filtered: pp.ParserElement = pp.Regex(r"#.*")

    filtered = filtered.suppress()
    qs: pp.ParserElement = pp.QuotedString('"') | pp.QuotedString("'")
    filtered = filtered.ignore(qs)

    return filtered.transform_string(line)


def literal_spec() -> pp.QuotedString:
    """A literal string, either single or double quoted."""

    return pp.QuotedString('"', unquote_results=False) | pp.QuotedString(
        "'", unquote_results=False
    )


### END ###
