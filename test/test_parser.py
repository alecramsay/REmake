#!/usr/bin/env python3
#
# TEST PARSER
#

from src import *


class TestParser:
    def test_filter_comments(self) -> None:
        teststrings: list[str] = [
            "# this is comment",
            'Option "sadsadlsad#this is not a comment"',
            "Option 'sadsadlsad#this is not a comment'",
            "Option 'sadsadlsad'#this is a comment",
        ]
        expected: list[str] = [
            "",
            'Option "sadsadlsad#this is not a comment"',
            "Option 'sadsadlsad#this is not a comment'",
            "Option 'sadsadlsad'",
        ]

        for i, teststring in enumerate(teststrings):
            result: str = filter_comments(teststring)
            assert result == expected[i]

    def test_literal_spec(self) -> None:
        Grammar: Any = literal_spec()

        input: str = '"foobar"'
        results: pp.ParseResults = Grammar.parseString(input)
        assert list(results) == ['"foobar"']

        input: str = "'foobar'"
        results: pp.ParseResults = Grammar.parseString(input)
        assert list(results) == ["'foobar'"]

    def test_parse_line(self) -> None:
        source: str = "test/examples/section2_1a.re"
        lines: list[str] = read_source_file(source)
        results: pp.ParseResults = parse_lines(lines)

        assert list(results) == ['"foobar"']

        source: str = "test/examples/section2_1.re"
        lines: list[str] = read_source_file(source)
        results: pp.ParseResults = parse_lines(lines)

        assert list(results) == ['"foobar"', '"bas"']


### END ###
