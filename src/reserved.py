#!/usr/bin/env python3

"""
RESERVERD WORDS
"""

from pyparsing import Keyword, ParserElement


reserved_word_dict: dict[str, str] = {
    # Anchors
    "line_start": "^",
    "string_start": "\\A",
    "line_end": "$",
    "string_end": "\\Z",
    # Character shorthands
    "digit": "\\d",
    "word_character": "\\w",
    "whitespace": "\\s",
    "word_boundary": "\\b",
    "any_character": ".",
    # Metacharacters
    "dollar_sign": "\\$",
    "left_paren": "\\(",
    "right_paren": "\\)",
    "asterisk": "\\*",
    "plus_sign": "\\+",
    "period": "\\.",
    "question_mark": "\\?",
    "left_bracket": "\\[",
    "right_bracket": "\\]",
    "caret": "\\^",
    "left_brace": "\\{",
    "right_brace": "\\}",
    "pipe": "\\|",
    # Non-printable characters
    "bell": "\\a",
    "escape": "\\e",
    "form_feed": "\\f",
    "newline": "\\n",
    "carriage_return": "\\r",
    "horizontal_tab": "\\t",
    "vertical_tab": "\\v",
    # Quantifiers
    "least": "",
    # Groups
    "any": "",
    "all": "",
    "as": "",
    # Miscellaneous
    "not": "^",
}

reserved_word_names: list[str] = list(reserved_word_dict.keys())

(
    line_start_word,
    string_start_word,
    line_end_word,
    string_end_word,
    digit_word,
    word_character_word,
    whitespace_word,
    word_boundary_word,
    any_character_word,
    dollar_sign_word,
    left_paren_word,
    right_paren_word,
    asterisk_word,
    plus_sign_word,
    period_word,
    question_mark_word,
    left_bracket_word,
    right_bracket_word,
    caret_word,
    left_brace_word,
    right_brace_word,
    pipe_word,
    bell_word,
    escape_word,
    form_feed_word,
    newline_word,
    carriage_return_word,
    horizontal_tab_word,
    vertical_tab_word,
    lazy_word,
    any_word,
    all_word,
    as_word,
    not_word,
) = map(Keyword, reserved_word_names)

reserved_words: ParserElement = (
    line_start_word
    | string_start_word
    | line_end_word
    | string_end_word
    | digit_word
    | word_character_word
    | whitespace_word
    | word_boundary_word
    | any_character_word
    | dollar_sign_word
    | left_paren_word
    | right_paren_word
    | asterisk_word
    | plus_sign_word
    | period_word
    | question_mark_word
    | left_bracket_word
    | right_bracket_word
    | caret_word
    | left_brace_word
    | right_brace_word
    | pipe_word
    | bell_word
    | escape_word
    | form_feed_word
    | newline_word
    | carriage_return_word
    | horizontal_tab_word
    | vertical_tab_word
    | lazy_word
    | any_word
    | all_word
    | as_word
    | not_word
)


def translate_character_word(word: str) -> str:
    return reserved_word_dict[word]


### END ###
