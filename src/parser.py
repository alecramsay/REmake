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

remake_spec = (
    pp.Opt(start_of_line_def) + pp.OneOrMore(pattern_def) + pp.Opt(end_of_line_def)
)

### PARSING ###


def parse_lines(lines: list[str], verbose: bool = False) -> list:
    """Parse multiple lines of source code."""

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

    return results


### END ###
