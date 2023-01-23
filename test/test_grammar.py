#!/usr/bin/env python3
#
# TEST GRAMMAR
#

from pyparsing import ParseResults, ParserElement
from typing import Any

from src.grammar import *
from src.readwrite import read_source_file
from src.comments import remove_comments
from src.anchors import start_anchor, end_anchor
from src.chars import consuming_char, non_consuming_char


class TestParser:
    def test_keywords(self) -> None:
        atomic_keywords: ParserElement = (
            start_anchor | end_anchor | non_consuming_char | consuming_char | not_def
        )
        Grammar: Any = atomic_keywords

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
            "digit",
            "WordCharacter",
            "Whitespace",
            "AnyCharacter",
            "Not",
            "LineEnd",
        ]
        assert tokens == expected


### END ###
