#!/usr/bin/env python3
#
# TEST GRAMMAR
#

from src import *


class TestParser:
    def test_keywords(self) -> None:
        Grammar: Any = keywords

        source: str = "test/examples/keywords.re"
        lines: list[str] = read_source_file(source)

        tokens: list[str] = list()
        for line in lines:
            filtered: str = remove_comments(line)
            if filtered == "" or filtered == "\n":
                continue
            results: pp.ParseResults = Grammar.parseString(filtered)
            tokens.extend(list(results))

        expected: list[str] = [
            "LineStart",
            "WordBoundary",
            "Digit",
            "Whitespace",
            "AnyCharacter",
            "Not",
            "LineEnd",
        ]
        assert tokens == expected


### END ###
