#!/usr/bin/env python3

"""
PARSER
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


### NAMES ###

name: pp.Word = pp.Word(pp.alphas, pp.alphanums + "_")


### KEYWORDS ###


start_of_line_def: pp.Keyword = pp.Keyword("LineStart")

end_of_line_def: pp.Keyword = pp.Keyword("LineEnd")

start_of_string_def: pp.Keyword = pp.Keyword("StringStart")

end_of_string_def: pp.Keyword = pp.Keyword("StringEnd")

word_boundary_def: pp.Keyword = pp.Keyword("WordBoundary")

digit_def: pp.Keyword = pp.Keyword("Digit")

whitespace_def: pp.Keyword = pp.Keyword("Whitespace")

any_char_def: pp.Keyword = pp.Keyword("AnyCharacter")

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


def parse_lines(lines: list[str], verbose: bool = False) -> pp.ParseResults:
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
