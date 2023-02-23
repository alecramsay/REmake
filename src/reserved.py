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
    "lazy": "",
    # Groups
    "alternative": "",
    "group": "",
    "as": "",
    # Miscellaneous
    "not": "^",
    # Negations
    "not_digit": "\\D",
    "not_word_character": "\\W",
    "not_whitespace": "\\S",
    "not_word_boundary": "\\B",
    # Lookarounds
    "preceded_by": "",
    "followed_by": "",
    # Modes
    "modes": "",
    "on": "",
    "off": "",
    "ignore_case": "i",
    "multi_line": "m",
    "dot_all": "s",
    # "free_space": "x", # NOTE - This would be very meta
    # Special characters
    "single_quote": "'",
    "double_quote": '"',
    "hash": "#",
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
    alternative_word,
    group_word,
    as_word,
    not_word,
    not_digit_word,
    not_word_character_word,
    not_whitespace_word,
    not_word_boundary_word,
    preceded_by_word,
    followed_by_word,
    modes_word,
    on_word,
    off_word,
    ignore_case_word,
    multi_line_word,
    dot_all_word,
    # free_space_word,
    single_quote_word,
    double_quote_word,
    hash_word,
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
    | alternative_word
    | group_word
    | as_word
    | not_word
    | not_digit_word
    | not_word_character_word
    | not_whitespace_word
    | not_word_boundary_word
    | preceded_by_word
    | followed_by_word
    | modes_word
    | on_word
    | off_word
    | ignore_case_word
    | multi_line_word
    | dot_all_word
    # | free_space_word
    | single_quote_word
    | double_quote_word
    | hash_word
)

### END ###
