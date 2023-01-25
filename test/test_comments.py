#!/usr/bin/env python3
#
# TEST COMMENTS
#

from src import *


class TestComments:
    def test_remove_comments(self) -> None:
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
            result: str = remove_comments(teststring)
            assert result == expected[i]

        source: str = "test/files/comments.re"
        lines: list[str] = read_source_file(source)
        results: ParseResults = parse_lines(lines)

        assert list(results) == ['"foobar"']


### END ###
