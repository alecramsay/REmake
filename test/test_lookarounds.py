#!/usr/bin/env python3
#
# TEST LOOKAROUNDS
#

from typing import Any

from src.lookarounds import *
from src.readwrite import read_source_file


class TestLookarounds:
    def test_groups(self) -> None:
        Grammar: Any = lookaround_pattern

        # input: str = 'not followed_by(\nnot_word_character()\n"cat"word_boundary)\n'

        strings: list[str] = [
            'followed_by(\n"cat")\n',
            'not followed_by(\n"cat")\n',
            'preceded_by(\n"cat")\n',
            'not preceded_by(\n"cat")\n',
            'followed_by(\n"foo" "bar" "bas")\n',
        ]
        expected: list = [
            ['"cat"'],
            ["not", '"cat"'],
            ['"cat"'],
            ["not", '"cat"'],
            ['"foo"', '"bar"', '"bas"'],
        ]

        for i, input in enumerate(strings):
            results: ParseResults = Grammar.parseString(input)
            assert list(results) == expected[i]


### END ###
