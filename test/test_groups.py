#!/usr/bin/env python3
#
# TEST GROUPS
#

from typing import Any

from src.groups import *

# from src.comments import *
from src.readwrite import *


class TestGroups:
    def test_groups(self) -> None:
        Grammar: Any = pattern

        source: str = "test/examples/groups.re"
        lines: list[str] = read_source_file(source)

        expected: list[str] = [
            ['"Alice"', '"Bob"', '"Carol"'],
            ['"foo"', '"bar"', '"bas"'],
            ["magic", "Digit", "Digit"],
        ]

        for i, line in enumerate(lines):
            results: ParseResults = Grammar.parseString(line)
            print(list(results))
            assert list(results) == expected[i]


### END ###
