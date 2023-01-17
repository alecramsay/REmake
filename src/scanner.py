#!/usr/bin/env python3

"""
SCANNER
"""

import pyparsing as pp


def parse_lines(lines: list[str], verbose: bool = False) -> None:
    for line in lines:
        tokens: list[str] = parse_line(line, verbose)

        pass


def parse_line(line: str, verbose: bool = False) -> list[str]:
    literal: pp.QuotedString = pp.QuotedString('"', unquote_results=False)

    REgrammar = literal
    tokens: list[str] = REgrammar.parseString(line)

    if verbose:
        print(tokens)

    return tokens
