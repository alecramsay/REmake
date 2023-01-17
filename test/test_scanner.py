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


### END ###
