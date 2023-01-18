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

    filtered: str = remove_comments(line)
    if filtered == "" or filtered == "\n":
        return []

    results: pp.ParseResults = Grammar.parseString(filtered)

    if verbose:
        print(results)

    return results


def define_grammar() -> Any:
    """Define the grammar for transparently specifying regular expressions."""

    # TODO - Flesh out the grammar

    expr = pattern_def()
    expr.ignore(pp.pythonStyleComment)

    return expr


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

### END ###
