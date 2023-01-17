#!/usr/bin/env python3
#
# TEST SCANNER
#

from src import *


class TestScanner:
    def test_filter_comments(self) -> None:
        teststrings = [
            "# this is comment",
            'Option "sadsadlsad#this is not a comment"',
            "Option 'sadsadlsad#this is not a comment'",
            "Option 'sadsadlsad'#this is a comment",
        ]
        expected = [
            "",
            'Option "sadsadlsad#this is not a comment"',
            "Option 'sadsadlsad#this is not a comment'",
            "Option 'sadsadlsad'",
        ]

        for i, teststring in enumerate(teststrings):
            result: str = filter_comments(teststring)
            assert result == expected[i]

    def test_parse_line(self) -> None:
        source: str = "test/examples/section2_1a.re"
        lines: list[str] = read_source_file(source)
        tokens: list = parse_lines(lines)

        assert tokens == ['"foobar"']

        source: str = "test/examples/section2_1.re"
        lines: list[str] = read_source_file(source)
        tokens: list = parse_lines(lines)

        assert tokens == ['"foobar"', '"bas"']


### END ###
