#!/usr/bin/env python3
#
# TEST GRAMMAR
#

from pyparsing import ParseResults, ParserElement
from typing import Any

from src.readwrite import read_source_file
from src.grammar import not_def  # TODO: remove
from src.comments import remove_comments
from src.anchors import start_anchor, end_anchor
from src.chars import quantified_char, non_consuming_char


class TestParser:
    def test_keywords(self) -> None:
        keywords: ParserElement = (
            start_anchor | end_anchor | non_consuming_char | quantified_char | not_def
        )
        Grammar: Any = keywords

        source: str = "test/examples/keywords.re"
        lines: list[str] = read_source_file(source)

        tokens: list[str] = list()
        for line in lines:
            filtered: str = remove_comments(line)
            if filtered == "" or filtered == "\n":
                continue
            results: ParseResults = Grammar.parseString(filtered)
            tokens.extend(list(results))

        expected: list[str] = [
            "LineStart",
            "WordBoundary",
            "Digit",
            "WordCharacter",
            "Whitespace",
            "AnyCharacter",
            "Not",
            "LineEnd",
        ]
        assert tokens == expected


### END ###
