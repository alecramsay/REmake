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
        results: pp.ParseResults = parse_lines(lines)

        assert list(results) == ['"foobar"']

    def test_literal_def(self) -> None:
        Grammar: Any = literal_def()

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

    def test_reserved_words(self) -> None:
        Grammar: Any = reserved_words()

        source: str = "test/examples/reserved_words.re"
        lines: list[str] = read_source_file(source)

        tokens: list[str] = list()
        for line in lines:
            filtered: str = remove_comments(line)
            if filtered == "" or filtered == "\n":
                continue
            results: pp.ParseResults = Grammar.parseString(filtered)
            tokens.extend(list(results))

        # results: pp.ParseResults = parse_lines(lines)

        expected: list[str] = [
            "start_of_line",
            "word_boundary",
            "digit",
            "whitespace",
            "any_char",
            "not",
            "end_of_line",
        ]
        assert tokens == expected


### END ###
