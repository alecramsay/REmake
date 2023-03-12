#!/usr/bin/env python3
#
# TEST GROUPS
#

from typing import Any

from src.groups import *
from src.readwrite import read_source_file


class TestGroups:
    def test_groups(self) -> None:
        Grammar: Any = atomic_pattern

        source: str = "test/files/groups.re"
        lines: list[str] = read_source_file(source)

        expected: list[list[str]] = [
            ["magic", "digit", "digit"],
            ['"Alice"', "|", '"Bob"', "|", '"Carol"'],
            ['"foo"', '"bar"', '"bas"'],
        ]

        for i, line in enumerate(lines):
            results: ParseResults = Grammar.parseString(line)
            assert list(results) == expected[i]

        Grammar: Any = id_def
        input: str = "magic"
        results: ParseResults = Grammar.parseString(input)

        assert list(results) == ["magic"]


### END ###
