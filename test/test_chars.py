#!/usr/bin/env python3
#
# TEST CHARACTERS
#

from src.chars import *
from src.readwrite import *
from src.parser import *


class TestCharacters:
    def test_char_def(self) -> None:
        Grammar: Any = char_def

        input: str = '"a"'
        results: pp.ParseResults = Grammar.parseString(input)
        assert list(results) == ['"a"']

        input: str = "'a'"
        results: pp.ParseResults = Grammar.parseString(input)
        assert list(results) == ["'a'"]

    def test_string_def(self) -> None:
        Grammar: Any = string_def

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
