#!/usr/bin/env python3

"""
SCANNER
"""

import pyparsing as pp
from typing import Any


def parse_lines(lines: list[str], verbose: bool = False) -> None:
    REgrammar: Any = define_RE_grammar()

    for line in lines:
        tokens: list[str] = parse_line(line, REgrammar, verbose)

        pass


def parse_line(line: str, grammar, verbose: bool = False) -> list[str]:
    tokens: list[str] = grammar.parseString(line)

    if verbose:
        print(tokens)

    return tokens


def define_RE_grammar() -> Any:
    literal: pp.QuotedString = pp.QuotedString('"', unquote_results=False)

    REgrammar = literal
    REgrammar.ignore(pp.pythonStyleComment)

    return REgrammar


# TODO - Abstract specification of grammar from parsing using it
# TODO - Use pp.ParseFile
