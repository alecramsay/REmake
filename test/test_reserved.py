#!/usr/bin/env python3
#
# TEST GRAMMAR
#

from pyparsing import ParseResults
from typing import Any

from src.reserved import *
from src.utils import *


class TestReservedWords:
    def test_keywords(self) -> None:
        Grammar: Any = reserved_words
        expected: list[str] = reserved_word_names

        for i, word in enumerate(reserved_word_names):
            results: ParseResults = Grammar.parseString(word)
            assert list(results)[0] == expected[i]

        assert True

    def test_character_word_translations(self) -> None:
        atomic_words: list[str] = [
            "line_start",
            "string_start",
            "line_end",
            "string_end",
            "digit",
            "word_character",
            "whitespace",
            "word_boundary",
            "any_character",
            "dollar_sign",
            "left_paren",
            "right_paren",
            "asterisk",
            "plus_sign",
            "period",
            "question_mark",
            "left_bracket",
            "right_bracket",
            "caret",
            "left_brace",
            "right_brace",
            "pipe",
            "bell",
            "escape",
            "form_feed",
            "newline",
            "carriage_return",
            "horizontal_tab",
            "vertical_tab",
            "not_digit",
            "not_word_character",
            "not_whitespace",
            "not_word_boundary",
            "preceded_by",
            "followed_by",
        ]

        for word in atomic_words:
            translation: str = translate_word(word)
            # print(f"{word} -> {translation}")

            assert translation == reserved_word_dict[word]


### END ###
