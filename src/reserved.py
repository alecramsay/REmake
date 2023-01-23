#!/usr/bin/env python3

"""
RESERVERD WORDS
"""

from pyparsing import Keyword, ParserElement


kw_dict: dict[str, str] = {
    # Anchors
    "start_of_line": "^",
    "start_of_string": "\\A",
    "end_of_line": "$",
    "end_of_string": "\\Z",
    # Character shorthands
    "digit": "\\d",
    "word_char": "\\w",
    "whitespace": "\\s",
    "word_boundary": "\\b",
    "any_char": ".",
    # Metacharacters
    "dollar_sign": "$",
    "left_paren": "(",
    "right_paren": ")",
    "asterisk": "*",
    "plus_sign": "+",
    "period": ".",
    "question_mark": "?",
    "left_bracket": "[",
    "right_bracket": "]",
    "caret": "^",
    "left_brace": "{",
    "right_brace": "}",
    "pipe": "|",
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

kw_names: list[str] = list(kw_dict.keys())

(
    start_of_line_def,
    start_of_string_def,
    end_of_line_def,
    end_of_string_def,
    digit_def,
    word_char_def,
    whitespace_def,
    word_boundary_def,
    any_char_def,
    dollar_sign_def,
    left_paren_def,
    right_paren_def,
    asterisk_def,
    plus_sign_def,
    period_def,
    question_mark_def,
    left_bracket_def,
    right_bracket_def,
    caret_def,
    left_brace_def,
    right_brace_def,
    pipe_def,
    bell_def,
    escape_def,
    form_feed_def,
    newline_def,
    carriage_return_def,
    horizontal_tab_def,
    vertical_tab_def,
    least_def,
    any_def,
    all_def,
    as_def,
    not_def,
) = map(Keyword, kw_names)


reserved_words: ParserElement = (
    start_of_line_def
    | start_of_string_def
    | end_of_line_def
    | end_of_string_def
    | digit_def
    | word_char_def
    | whitespace_def
    | word_boundary_def
    | any_char_def
    | dollar_sign_def
    | left_paren_def
    | right_paren_def
    | asterisk_def
    | plus_sign_def
    | period_def
    | question_mark_def
    | left_bracket_def
    | right_bracket_def
    | caret_def
    | left_brace_def
    | right_brace_def
    | pipe_def
    | bell_def
    | escape_def
    | form_feed_def
    | newline_def
    | carriage_return_def
    | horizontal_tab_def
    | vertical_tab_def
    | least_def
    | any_def
    | all_def
    | as_def
    | not_def
)


### END ###
