#!/usr/bin/env python3
#
# TEST PARSER
#

from src import *


class TestParser:
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

        source: str = "test/examples/comments.re"
        lines: list[str] = read_source_file(source)
        results: pp.ParseResults = parse_lines(lines, Emit.TOKENS)

        assert list(results) == ['"foobar"']

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
        results: pp.ParseResults = parse_lines(lines, Emit.TOKENS)

        assert list(results) == ['"foobar"', '"bas"']

    def test_keywords(self) -> None:
        Grammar: Any = keywords

        source: str = "test/examples/keywords.re"
        lines: list[str] = read_source_file(source)

        tokens: list[str] = list()
        for line in lines:
            filtered: str = remove_comments(line)
            if filtered == "" or filtered == "\n":
                continue
            results: pp.ParseResults = Grammar.parseString(filtered)
            tokens.extend(list(results))

        expected: list[str] = [
            "LineStart",
            "WordBoundary",
            "Digit",
            "Whitespace",
            "AnyCharacter",
            "Not",
            "LineEnd",
        ]
        assert tokens == expected

    def test_line_anchors(self) -> None:
        # Both start and end of line anchors
        source: str = "test/examples/line_anchors.re"
        lines: list[str] = read_source_file(source)
        results: pp.ParseResults = parse_lines(lines, Emit.TOKENS)

        assert list(results) == ["LineStart", '"foo"', "LineEnd"]

        # Only start of line anchor
        source: str = "test/examples/line_anchors2.re"
        lines: list[str] = read_source_file(source)
        results: pp.ParseResults = parse_lines(lines, Emit.TOKENS)

        assert list(results) == ["LineStart", '"foo"']

        # Only end of line anchor
        source: str = "test/examples/line_anchors3.re"
        lines: list[str] = read_source_file(source)
        results: pp.ParseResults = parse_lines(lines, Emit.TOKENS)

        assert list(results) == ['"foo"', "LineEnd"]

    def test_quantifiers(self) -> None:
        Grammar: Any = quantifier_def

        input: str = "* 10"
        results: pp.ParseResults = Grammar.parseString(input)
        assert list(results) == ["10"]

        input: str = "* 0, ..."
        results: pp.ParseResults = Grammar.parseString(input)
        assert list(results) == ["0", "..."]

        input: str = "* ..., 3"
        results: pp.ParseResults = Grammar.parseString(input)
        assert list(results) == ["...", "3"]

        input: str = "* 1,3"
        results: pp.ParseResults = Grammar.parseString(input)
        assert list(results) == ["1", "3"]


### END ###
