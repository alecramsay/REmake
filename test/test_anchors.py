#!/usr/bin/env python3
#
# TEST ANCHORS
#

from src.readwrite import *
from src.parser import *


class TestAnchors:
    def test_line_anchors(self) -> None:
        # Both start and end of line anchors
        source: str = "test/files/line_anchors.re"
        lines: list[str] = read_source_file(source)
        results: ParseResults = parse_lines(lines)

        assert list(results) == ["line_start", '"foo"', "line_end"]

        # Only start of line anchor
        source: str = "test/files/line_anchors2.re"
        lines: list[str] = read_source_file(source)
        results: ParseResults = parse_lines(lines)

        assert list(results) == ["line_start", '"foo"']

        # Only end of line anchor
        source: str = "test/files/line_anchors3.re"
        lines: list[str] = read_source_file(source)
        results: ParseResults = parse_lines(lines)

        assert list(results) == ['"foo"', "line_end"]

        # Both start and end of string anchors
        source: str = "test/files/line_anchors4.re"
        lines: list[str] = read_source_file(source)
        results: ParseResults = parse_lines(lines)

        assert list(results) == ["string_start", '"foo"', "string_end"]


### END ###
