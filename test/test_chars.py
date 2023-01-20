#!/usr/bin/env python3
#
# TEST CHARACTERS
#

from src import *


class TestCharacters:
    def test_literal_def(self) -> None:
        Grammar: Any = literal_def

        input: str = '"foobar"'
        results: pp.ParseResults = Grammar.parseString(input)
        assert list(results) == ['"foobar"']

        input: str = "'foobar'"
        results: pp.ParseResults = Grammar.parseString(input)
        assert list(results) == ["'foobar'"]

        source: str = "test/examples/literals.re"
        lines: list[str] = read_source_file(source)
        results: pp.ParseResults = parse_lines(lines)

        assert list(results) == ['"foobar"', '"bas"']


### END ###