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
meta_char_def: Keyword = (
    dollar_sign_word
    | left_paren_word
    | right_paren_word
    | asterisk_word
    | plus_sign_word
    | period_word
    | question_mark_word
    | left_bracket_word
    | right_bracket_word
    | caret_word
    | right_brace_word
    | left_brace_word
    | pipe_word
)


@meta_char_def.set_parse_action
def meta_char_act(toks: ParseResults) -> str:
    if G.EMIT_MODE == G.Mode.TOKENS:
        return toks[0]

    translation: str = reserved_word_dict[toks[0]]
    # translation: str = "\\" + reserved_word_dict[toks[0]]

    if G.EMIT_MODE == G.Mode.REGEX:
        return translation

    if G.EMIT_MODE == G.Mode.FREE_SPACED_REGEX:
        comment: str = f"A {keyword_to_words(toks[0])} (escaped)"
        return free_space(translation, comment)

    raise ValueError("Invalid emit mode")


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
    if G.EMIT_MODE == G.Mode.TOKENS:
        return toks[0]

    translation: str = toks[0][1:-1]

    if G.EMIT_MODE == G.Mode.REGEX:
        return translation

    if G.EMIT_MODE == G.Mode.FREE_SPACED_REGEX:
        return free_space(translation, f"The character '{translation}'")

    raise ValueError("Invalid emit mode")


### NON-PRINTABLE CHARACTERS ###

non_printable_char_def: Keyword = (
    bell_word
    | escape_word
    | form_feed_word
    | newline_word
    | carriage_return_word
    | horizontal_tab_word
    | vertical_tab_word
)


@non_printable_char_def.set_parse_action
def non_printable_char_act(toks: ParseResults) -> str:
    if G.EMIT_MODE == G.Mode.TOKENS:
        return toks[0]

    translation: str = reserved_word_dict[toks[0]]

    if G.EMIT_MODE == G.Mode.REGEX:
        return translation

    if G.EMIT_MODE == G.Mode.FREE_SPACED_REGEX:
        comment: str = f"The {keyword_to_words(toks[0])} character"
        return free_space(translation, comment)

    raise ValueError("Invalid emit mode")


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
    if G.EMIT_MODE == G.Mode.TOKENS:
        return toks[0]

    translation: str = toks[0][1:-1]

    if G.EMIT_MODE == G.Mode.REGEX:
        return translation

    if G.EMIT_MODE == G.Mode.FREE_SPACED_REGEX:
        return free_space(translation, f"The character string '{translation}'")

    raise ValueError("Invalid emit mode")


### CHARACTER SHORTHANDS ###

digit_def: Keyword = digit_word + Suppress("()")


@digit_def.set_parse_action
def digit_act(toks: ParseResults) -> str:
    if G.EMIT_MODE == G.Mode.TOKENS:
        return toks[0]

    translation: str = reserved_word_dict[toks[0]]

    if G.EMIT_MODE == G.Mode.REGEX:
        return translation

    if G.EMIT_MODE == G.Mode.FREE_SPACED_REGEX:
        return free_space(translation, "A digit")

    raise ValueError("Invalid emit mode")


word_char_def: Keyword = word_character_word + Suppress("()")


@word_char_def.set_parse_action
def word_char_act(toks: ParseResults) -> str:
    if G.EMIT_MODE == G.Mode.TOKENS:
        return toks[0]

    translation: str = reserved_word_dict[toks[0]]

    if G.EMIT_MODE == G.Mode.REGEX:
        return translation

    if G.EMIT_MODE == G.Mode.FREE_SPACED_REGEX:
        return free_space(translation, "A word character")

    raise ValueError("Invalid emit mode")


whitespace_def: Keyword = whitespace_word + Suppress("()")


@whitespace_def.set_parse_action
def whitespace_act(toks: ParseResults) -> str:
    if G.EMIT_MODE == G.Mode.TOKENS:
        return toks[0]

    translation: str = reserved_word_dict[toks[0]]

    if G.EMIT_MODE == G.Mode.REGEX:
        return translation

    if G.EMIT_MODE == G.Mode.FREE_SPACED_REGEX:
        return free_space(translation, "A whitespace character")

    raise ValueError("Invalid emit mode")


### BOUNDARIES ###

word_boundary_def: Keyword = word_boundary_word + Suppress("()")


@word_boundary_def.set_parse_action
def word_boundary_act(toks: ParseResults) -> str:
    if G.EMIT_MODE == G.Mode.TOKENS:
        return toks[0]

    translation: str = reserved_word_dict[toks[0]]

    if G.EMIT_MODE == G.Mode.REGEX:
        return translation

    if G.EMIT_MODE == G.Mode.FREE_SPACED_REGEX:
        return free_space(translation, "Word boundary")

    raise ValueError("Invalid emit mode")


### ANY CHARACTER ###

any_char_def: Keyword = any_character_word + Suppress("()")


@any_char_def.set_parse_action
def any_char_act(toks: ParseResults) -> str:
    if G.EMIT_MODE == G.Mode.TOKENS:
        return toks[0]

    translation: str = reserved_word_dict[toks[0]]

    if G.EMIT_MODE == G.Mode.REGEX:
        return translation

    if G.EMIT_MODE == G.Mode.FREE_SPACED_REGEX:
        return free_space(translation, "Any character (except newline)")

    raise ValueError("Invalid emit mode")


### CHARACTER CLASSES ###

char_range_def: ParserElement = (
    range_char("from_char") + Suppress("-") + range_char("to_char")
)


@char_range_def.set_parse_action
def char_range_act(toks: ParseResults) -> str:
    if G.EMIT_MODE == G.Mode.TOKENS:
        return toks

    translation: str = f"{toks.from_char[1:-1]}-{toks.to_char[1:-1]}"

    if G.EMIT_MODE == G.Mode.REGEX:
        if ord(toks.to_char[1:-1]) > ord(toks.from_char[1:-1]):
            return translation
        else:
            raise ValueError("Invalid range: order of characters is reversed.")

    if G.EMIT_MODE == G.Mode.FREE_SPACED_REGEX:
        comment: str = f"Characters in the range '{translation}'"
        return free_space(translation, comment)

    raise ValueError("Invalid emit mode")


beg_char_class_def: ParserElement = Suppress(Keyword("any")) + Suppress("(")
end_char_class_def: ParserElement = Suppress(")")


@beg_char_class_def.set_parse_action
def beg_char_class_act(toks: ParseResults) -> str:
    if G.EMIT_MODE == G.Mode.TOKENS:
        return toks

    translation: str = "["

    if G.EMIT_MODE == G.Mode.REGEX:
        return translation

    if G.EMIT_MODE == G.Mode.FREE_SPACED_REGEX:
        comment: str = f"Any character in the class:"
        return free_space(translation, comment, tab_inc=1)

    raise ValueError("Invalid emit mode")


@end_char_class_def.set_parse_action
def end_char_class_act(toks: ParseResults) -> str:
    if G.EMIT_MODE == G.Mode.TOKENS:
        return toks

    translation: str = "]"

    if G.EMIT_MODE == G.Mode.REGEX:
        return translation

    if G.EMIT_MODE == G.Mode.FREE_SPACED_REGEX:
        comment: str = f"End of character class"
        return free_space(translation, comment, tab_inc=-1)

    raise ValueError("Invalid emit mode")


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
