#!/usr/bin/env python3

"""
CHARACTERS
"""

from pyparsing import (
    CaselessKeyword,
    Char,
    printables,
    Combine,
    Literal,
    QuotedString,
    Suppress,
    delimited_list,
    Opt,
    ParseResults,
    ParserElement,
)

import src.globals as G
from .quantifiers import quantifier
from .constants import *
from .utils import *


### META CHARACTERS ###

meta_chars: str = "$()*+.?[]^}{|"
meta_names: list[str] = [
    "DollarSign",
    "LeftParen",
    "RightParen",
    "Asterisk",
    "PlusSign",
    "Period",
    "QuestionMark",
    "LeftBracket",
    "RightBracket",
    "Caret",
    "LeftBrace",
    "RightBrace",
    "Pipe",
]
meta_dict: dict[str, str] = dict(zip(meta_names, meta_chars))

(
    dollar_sign,
    left_paren,
    right_paren,
    asterisk,
    plus_sign,
    period,
    question_mark,
    left_bracket,
    right_bracket,
    caret,
    left_brace,
    right_brace,
    pipe,
) = map(CaselessKeyword, meta_names)

meta_char_def: CaselessKeyword = (
    dollar_sign
    | left_paren
    | right_paren
    | asterisk
    | plus_sign
    | period
    | question_mark
    | left_bracket
    | right_bracket
    | caret
    | right_brace
    | left_brace
    | pipe
)


@meta_char_def.set_parse_action
def meta_char_act(toks: ParseResults) -> str:
    if G.EMIT_MODE == G.Mode.TOKENS:
        return toks[0]

    translation: str = "\\" + meta_dict[toks[0]]

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

non_printable_chars: list[str] = [
    "\\a",
    "\\e",
    "\\f",
    "\\n",
    "\\r",
    "\\t",
    "\\v",
]
non_printable_names: list[str] = [
    "Bell",
    "Escape",
    "FormFeed",
    "NewLine",
    "CarriageReturn",
    "HorizontalTab",
    "VerticalTab",
]
non_printable_dict: dict[str, str] = dict(zip(non_printable_names, non_printable_chars))

(
    bell,
    escape,
    form_feed,
    newline,
    carriage_return,
    horizontal_tab,
    vertical_tab,
) = map(CaselessKeyword, non_printable_names)

non_printable_char_def: CaselessKeyword = (
    bell
    | escape
    | form_feed
    | newline
    | carriage_return
    | horizontal_tab
    | vertical_tab
)


@non_printable_char_def.set_parse_action
def non_printable_char_act(toks: ParseResults) -> str:
    if G.EMIT_MODE == G.Mode.TOKENS:
        return toks[0]

    translation: str = non_printable_dict[toks[0]]

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

digit_def: CaselessKeyword = CaselessKeyword("Digit")


@digit_def.set_parse_action
def digit_act(toks: ParseResults) -> str:
    if G.EMIT_MODE == G.Mode.TOKENS:
        return toks[0]

    translation: str = "\d"

    if G.EMIT_MODE == G.Mode.REGEX:
        return translation

    if G.EMIT_MODE == G.Mode.FREE_SPACED_REGEX:
        return free_space(translation, "A digit")

    raise ValueError("Invalid emit mode")


word_char_def: CaselessKeyword = CaselessKeyword("WordCharacter")


@word_char_def.set_parse_action
def word_char_act(toks: ParseResults) -> str:
    if G.EMIT_MODE == G.Mode.TOKENS:
        return toks[0]

    translation: str = "\w"

    if G.EMIT_MODE == G.Mode.REGEX:
        return translation

    if G.EMIT_MODE == G.Mode.FREE_SPACED_REGEX:
        return free_space(translation, "A word character")

    raise ValueError("Invalid emit mode")


whitespace_def: CaselessKeyword = CaselessKeyword("Whitespace")


@whitespace_def.set_parse_action
def whitespace_act(toks: ParseResults) -> str:
    if G.EMIT_MODE == G.Mode.TOKENS:
        return toks[0]

    translation: str = "\s"

    if G.EMIT_MODE == G.Mode.REGEX:
        return translation

    if G.EMIT_MODE == G.Mode.FREE_SPACED_REGEX:
        return free_space(translation, "A whitespace character")

    raise ValueError("Invalid emit mode")


### BOUNDARIES ###

word_boundary_def: CaselessKeyword = CaselessKeyword("WordBoundary")


@word_boundary_def.set_parse_action
def word_boundary_act(toks: ParseResults) -> str:
    if G.EMIT_MODE == G.Mode.TOKENS:
        return toks[0]

    translation: str = "\b"

    if G.EMIT_MODE == G.Mode.REGEX:
        return translation

    if G.EMIT_MODE == G.Mode.FREE_SPACED_REGEX:
        return free_space(translation, "Word boundary")

    raise ValueError("Invalid emit mode")


### ANY CHARACTER ###

any_char_def: CaselessKeyword = CaselessKeyword("AnyCharacter")


@any_char_def.set_parse_action
def any_char_act(toks: ParseResults) -> str:
    if G.EMIT_MODE == G.Mode.TOKENS:
        return toks[0]

    translation: str = "."

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


beg_char_class_def: ParserElement = Suppress(CaselessKeyword("Any")) + Suppress("{")
end_char_class_def: ParserElement = Suppress("}")


@beg_char_class_def.set_parse_action
def beg_char_class_act(toks: ParseResults) -> str:
    if G.EMIT_MODE == G.Mode.TOKENS:
        return toks

    translation: str = "["

    if G.EMIT_MODE == G.Mode.REGEX:
        return translation

    if G.EMIT_MODE == G.Mode.FREE_SPACED_REGEX:
        comment: str = f"Any character in the class:"
        return free_space(translation, comment)

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
        return free_space(translation, comment)

    raise ValueError("Invalid emit mode")


char_class_def: ParserElement = (
    beg_char_class_def
    + delimited_list((char_range_def | char_def), delim="|")
    + end_char_class_def
)


### IMPORT THESE ###

quantified_char: ParserElement = (
    # A consuming character, optionally quantified
    char_def
    | digit_def
    | word_char_def
    | whitespace_def
    | any_char_def
    | non_printable_char_def
    | meta_char_def
    | char_class_def
    | string_def
) + Opt(quantifier)

non_consuming_char: ParserElement = word_boundary_def

### END ###
