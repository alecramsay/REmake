#!/usr/bin/env python3
#
# TEST ANCHORS
#

from src import *


class TestAnchors:
    def test_line_anchors(self) -> None:
        # Both start and end of line anchors
        source: str = "test/examples/line_anchors.re"
        lines: list[str] = read_source_file(source)
        results: pp.ParseResults = parse_lines(lines)

        assert list(results) == ["LineStart", '"foo"', "LineEnd"]

        # Only start of line anchor
        source: str = "test/examples/line_anchors2.re"
        lines: list[str] = read_source_file(source)
        results: pp.ParseResults = parse_lines(lines)

        assert list(results) == ["LineStart", '"foo"']

        # Only end of line anchor
        source: str = "test/examples/line_anchors3.re"
        lines: list[str] = read_source_file(source)
        results: pp.ParseResults = parse_lines(lines)

        assert list(results) == ['"foo"', "LineEnd"]

        # Both start and end of string anchors
        source: str = "test/examples/line_anchors4.re"
        lines: list[str] = read_source_file(source)
        results: pp.ParseResults = parse_lines(lines)

        assert list(results) == ["StringStart", '"foo"', "StringEnd"]


### END ###
