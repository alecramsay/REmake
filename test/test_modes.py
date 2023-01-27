#!/usr/bin/env python3
#
# TEST MODES
#

from typing import Any

from src.modes import *

# from src.readwrite import read_source_file


class TestModes:
    def test_groups(self) -> None:
        Grammar: Any = modes_pattern

        lines: list[str] = [
            "modes (on: ignore_case)",
            "modes (on: ignore_case, dot_all)",
            "modes (on: ignore_case, off: dot_all)",
            "modes (off: ignore_case, dot_all)",
        ]

        expected: list[list[str]] = [
            ["on", "ignore_case"],
            ["on", "ignore_case", "dot_all"],
            [["on", "ignore_case"], ["off", "dot_all"]],
            ["off", "ignore_case", "dot_all"],
        ]

        for i, line in enumerate(lines):
            results: ParseResults = Grammar.parseString(line)
            assert list(results) == expected[i]


### END ###
