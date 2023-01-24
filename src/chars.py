#!/usr/bin/env python3

"""
CHARACTERS
"""

from pyparsing import (
    Keyword,
    Char,
    printables,
    Combine,
    Literal,
    QuotedString,
    Suppress,
    delimited_list,
    ParseResults,
    ParserElement,
)

import src.globals as G
from .reserved import *
from .quantifiers import quantifier
from .constants import *
from .utils import *


### META CHARACTERS ###

meta_chars: str = "$()*+.?[]^}{|"
meta_char_words: Keyword = [
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
    right_brace_word,
    left_brace_word,
    pipe_word,
]

(
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
    right_brace_def,
    left_brace_def,
    pipe_def,
) = map(append_suppress, meta_char_words)

meta_char_def: Keyword = (
    dollar_sign_def
    | left_paren_def
    | right_paren_def
    | asterisk_def
    | plus_sign_def
    | period_def
    | question_mark_def
    | left_bracket_def
    | right_bracket_def
    | caret_def
    | right_brace_def
    | left_brace_def
    | pipe_def
)


@meta_char_def.set_parse_action
def meta_char_act(toks: ParseResults) -> str:
    token: str = unpack_token(toks)
    translation: str = translate_word(token)
    friendly_name: str = keyword_to_words(token)
    article: str = "An" if friendly_name[0].lower() in "aeiou" else "A"
    comment: str = f"{article} {friendly_name} (escaped)"

    return modal_act(toks, translation, comment)


### PRINTABLE CHARACTERS ###

char: Char = Char(printables, exclude_chars=meta_chars)
double_quote: Literal = Literal('"')
single_quote: Literal = Literal("'")

char_def: Char = Combine(double_quote + char + double_quote) | Combine(
    single_quote + char + single_quote
)

# For ranges
range_char: Char = char_def.copy()


@char_def.set_parse_action
def char_act(toks: ParseResults) -> str:
    translation: str = unpack_token(toks)[1:-1]
    comment: str = f"The character '{translation}'"

    return modal_act(toks, translation, comment)


### NON-PRINTABLE CHARACTERS ###

non_printable_char_words: Keyword = [
    bell_word,
    escape_word,
    form_feed_word,
    newline_word,
    carriage_return_word,
    horizontal_tab_word,
    vertical_tab_word,
]

(
    bell_def,
    escape_def,
    form_feed_def,
    newline_def,
    carriage_return_def,
    horizontal_tab_def,
    vertical_tab_def,
) = map(append_suppress, non_printable_char_words)

non_printable_char_def: Keyword = (
    bell_def
    | escape_def
    | form_feed_def
    | newline_def
    | carriage_return_def
    | horizontal_tab_def
    | vertical_tab_def
)


@non_printable_char_def.set_parse_action
def non_printable_char_act(toks: ParseResults) -> str:
    token: str = unpack_token(toks)
    translation: str = translate_word(token)
    comment: str = f"The {keyword_to_words(unpack_token(toks))} character"

    return modal_act(toks, translation, comment)


### MULTI-CHARACTER STRINGS ###

# TODO - This doesn't work, for some reason.
# string: Word = Word(
#     printables, exclude_chars=meta_chars, min=2, as_keyword=True
# )
# double_quoted_string: ParserElement = Combine(
#     double_quote + string + double_quote
# )
# single_quoted_string: ParserElement = Combine(
#     single_quote + string + single_quote
# )
# string_def: ParserElement = (
#     double_quoted_string | single_quoted_string
# )
string_def: QuotedString = QuotedString('"', unquote_results=False) | QuotedString(
    "'", unquote_results=False
)


@string_def.set_parse_action
def string_act(toks: ParseResults) -> str:
    translation: str = unpack_token(toks)[1:-1]
    comment: str = f"The character string '{translation}'"

    return modal_act(toks, translation, comment)


### CHARACTER SHORTHANDS ###

digit_def: Keyword = digit_word + Suppress("()")


@digit_def.set_parse_action
def digit_act(toks: ParseResults) -> str:
    token: str = unpack_token(toks)
    translation: str = translate_word(token)
    comment: str = "A digit"

    return modal_act(toks, translation, comment)


word_char_def: Keyword = word_character_word + Suppress("()")


@word_char_def.set_parse_action
def word_char_act(toks: ParseResults) -> str:
    token: str = unpack_token(toks)
    translation: str = translate_word(token)
    comment: str = "A word character"

    return modal_act(toks, translation, comment)


whitespace_def: Keyword = whitespace_word + Suppress("()")


@whitespace_def.set_parse_action
def whitespace_act(toks: ParseResults) -> str:
    token: str = unpack_token(toks)
    translation: str = translate_word(token)
    comment: str = "A whitespace character"

    return modal_act(toks, translation, comment)


### BOUNDARIES ###

word_boundary_def: Keyword = word_boundary_word + Suppress("()")


@word_boundary_def.set_parse_action
def word_boundary_act(toks: ParseResults) -> str:
    token: str = unpack_token(toks)
    translation: str = translate_word(token)
    comment: str = "Word boundary"

    return modal_act(toks, translation, comment)


### ANY CHARACTER ###

any_char_def: Keyword = any_character_word + Suppress("()")


@any_char_def.set_parse_action
def any_char_act(toks: ParseResults) -> str:
    token: str = unpack_token(toks)
    translation: str = translate_word(token)
    comment: str = "Any character (except newline)"

    return modal_act(toks, translation, comment)


### CHARACTER CLASSES ###

char_range_def: ParserElement = (
    range_char("from_char") + Suppress("-") + range_char("to_char")
)


@char_range_def.set_parse_action
def char_range_act(toks: ParseResults) -> str:
    if ord(toks.to_char[1:-1]) <= ord(toks.from_char[1:-1]):
        raise ValueError("Invalid range: order of characters is reversed.")

    translation: str = f"{toks.from_char[1:-1]}-{toks.to_char[1:-1]}"
    comment: str = f"Characters in the range '{translation}'"

    return modal_act(toks, translation, comment, tok_list=True)


beg_char_class_def: ParserElement = Suppress(any_word) + Suppress("(")
end_char_class_def: ParserElement = Suppress(")")


@beg_char_class_def.set_parse_action
def beg_char_class_act(toks: ParseResults) -> str:
    return modal_act(
        toks, "[", f"Any character in the class:", tab_inc=1, tok_list=True
    )


@end_char_class_def.set_parse_action
def end_char_class_act(toks: ParseResults) -> str:
    return modal_act(toks, "]", f"End of character class", tab_inc=-1, tok_list=True)


char_class_def: ParserElement = (
    beg_char_class_def
    + delimited_list((char_range_def | char_def), delim="|")
    + end_char_class_def
)


### IMPORT THESE ###

consuming_char: ParserElement = (
    char_def
    | digit_def
    | word_char_def
    | whitespace_def
    | any_char_def
    | non_printable_char_def
    | meta_char_def
    | char_class_def
    | string_def
)

non_consuming_char: ParserElement = word_boundary_def

### END ###
