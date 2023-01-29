#!/usr/bin/env python3
#
# TEST CHARACTERS
#

from src.chars import *
from src.readwrite import read_source_file
from src.parser import parse_lines
from src.comments import remove_comments


class TestCharacters:
    def test_char_def(self) -> None:
        Grammar: Any = char_def

        input: str = '"a"'
        results: ParseResults = Grammar.parseString(input)
        assert list(results) == ['"a"']

        input: str = "'a'"
        results: ParseResults = Grammar.parseString(input)
        assert list(results) == ["'a'"]

    def test_string_def(self) -> None:
        Grammar: Any = string_def

        input: str = '"foobar"'
        results: ParseResults = Grammar.parseString(input)
        assert list(results) == ['"foobar"']

        input: str = "'foobar'"
        results: ParseResults = Grammar.parseString(input)
        assert list(results) == ["'foobar'"]

        source: str = "test/files/strings.re"
        lines: list[str] = read_source_file(source)
        results: ParseResults = parse_lines(lines)

        assert list(results) == ['"foobar"', '"bas"']

    def test_meta_char_def(self) -> None:
        teststrings: list[str] = [
            "dollar_sign",
            "left_paren",
            "right_paren",
            "asterisk",
            "plus_sign",
            "period",
            "question_mark",
            "left_bracket",
            "right_bracket",
            "caret",
            "left_brace",
            "right_brace",
            "pipe",
        ]
        expected: list[str] = teststrings

        for i, teststring in enumerate(teststrings):
            result: str = remove_comments(teststring)
            assert result == expected[i]

    def test_non_printable_char_def(self) -> None:
        teststrings: list[str] = [
            "bell",
            "escape",
            "form_feed",
            "new_line",
            "carriage_return",
            "horizontal_tab",
            "vertical_tab",
        ]
        expected: list[str] = teststrings

        for i, teststring in enumerate(teststrings):
            result: str = remove_comments(teststring)
            assert result == expected[i]

    def test_char_ranges(self) -> None:
        Grammar: Any = char_range_def | char_def
        input: str = "'a'-'z'"
        expected: str = ["'a'", "'z'"]

        results: ParseResults = Grammar.parseString(input)
        assert list(results) == expected

        input: str = "'a' - 'z'"
        expected: str = ["'a'", "'z'"]

        results: ParseResults = Grammar.parseString(input)
        assert list(results) == expected

    def test_char_classes(self) -> None:
        Grammar: Any = char_class_def
        input: str = "any ('a' - 'z')"
        expected: str = ["'a'", "'z'"]

        results: ParseResults = Grammar.parseString(input)
        assert list(results) == expected

        input: str = "any ('a' - 'z' | 'A' - 'Z')"
        expected: str = ["'a'", "'z'", "'A'", "'Z'"]

        results: ParseResults = Grammar.parseString(input)
        assert list(results) == expected

        input: str = "any not ('a' - 'z')"
        expected: str = ["not", "'a'", "'z'"]

        results: ParseResults = Grammar.parseString(input)
        assert list(results) == expected

    def test_quotes(self) -> None:
        source: str = "test/files/quotes.re"
        lines: list[str] = read_source_file(source)
        results: ParseResults = parse_lines(lines)

        assert list(results) == ["double_quote", '"foo"', "double_quote"]

    def test_hashes(self) -> None:
        source: str = "test/files/hashes.re"
        lines: list[str] = read_source_file(source)
        results: ParseResults = parse_lines(lines)

        assert list(results) == ["hash", '"foo"', "hash"]


### END ###
