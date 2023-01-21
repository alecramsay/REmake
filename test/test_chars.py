#!/usr/bin/env python3
#
# TEST CHARACTERS
#

from src.chars import *
from src.readwrite import *
from src.parser import *


class TestCharacters:
    def test_char_def(self) -> None:
        Grammar: Any = char_def

        input: str = '"a"'
        results: pp.ParseResults = Grammar.parseString(input)
        assert list(results) == ['"a"']

        input: str = "'a'"
        results: pp.ParseResults = Grammar.parseString(input)
        assert list(results) == ["'a'"]

    def test_string_def(self) -> None:
        Grammar: Any = string_def

        input: str = '"foobar"'
        results: pp.ParseResults = Grammar.parseString(input)
        assert list(results) == ['"foobar"']

        input: str = "'foobar'"
        results: pp.ParseResults = Grammar.parseString(input)
        assert list(results) == ["'foobar'"]

        source: str = "test/examples/literals.re"
        lines: list[str] = read_source_file(source)
        results: pp.ParseResults = parse_lines(lines)

        assert list(results) == ['"foobar"', '"bas"']

    def test_meta_char_def(self) -> None:
        teststrings: list[str] = meta_names
        expected: list[str] = meta_names

        for i, teststring in enumerate(teststrings):
            result: str = remove_comments(teststring)
            assert result == expected[i]

    def test_non_printable_char_def(self) -> None:
        teststrings: list[str] = non_printable_names
        expected: list[str] = non_printable_names

        for i, teststring in enumerate(teststrings):
            result: str = remove_comments(teststring)
            assert result == expected[i]


### END ###
