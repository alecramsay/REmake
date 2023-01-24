#!/usr/bin/env python3

"""
ANCHORS
"""

from pyparsing import Keyword, Group, ParserElement, ParseResults, Suppress
from typing import Any

import src.globals as G
from .reserved import *
from .constants import *
from .utils import *


start_of_line_def: Keyword = Group(line_start_word + Suppress("()"))


@start_of_line_def.set_parse_action
def start_of_line_act(toks: ParseResults) -> str:
    if G.EMIT_MODE == G.Mode.TOKENS:
        return toks[0]

    token: str = unpack_token(toks, grouped=True)
    translation: str = reserved_word_dict[token]

    if G.EMIT_MODE == G.Mode.REGEX:
        return translation

    if G.EMIT_MODE == G.Mode.FREE_SPACED_REGEX:
        return free_space(translation, "Start of line")

    raise ValueError("Invalid emit mode")


end_of_line_def: Keyword = Group(line_end_word + Suppress("()"))


@end_of_line_def.set_parse_action
def end_of_line_act(toks: ParseResults) -> str:
    if G.EMIT_MODE == G.Mode.TOKENS:
        return toks[0]

    token: str = unpack_token(toks, grouped=True)
    translation: str = reserved_word_dict[token]

    if G.EMIT_MODE == G.Mode.REGEX:
        return translation

    if G.EMIT_MODE == G.Mode.FREE_SPACED_REGEX:
        return free_space(translation, "End of line")

    raise ValueError("Invalid emit mode")


start_of_string_def: Keyword = Group(string_start_word + Suppress("()"))


@start_of_string_def.set_parse_action
def start_of_string_act(toks: ParseResults) -> str:
    if G.EMIT_MODE == G.Mode.TOKENS:
        return toks[0]

    token: str = unpack_token(toks, grouped=True)
    translation: str = reserved_word_dict[token]

    if G.EMIT_MODE == G.Mode.REGEX:
        return translation

    if G.EMIT_MODE == G.Mode.FREE_SPACED_REGEX:
        return free_space(translation, "Start of string")

    raise ValueError("Invalid emit mode")


end_of_string_def: Keyword = Group(string_end_word + Suppress("()"))


@end_of_string_def.set_parse_action
def end_of_string_act(toks: ParseResults) -> str:
    if G.EMIT_MODE == G.Mode.TOKENS:
        return toks[0]

    token: str = unpack_token(toks, grouped=True)
    translation: str = reserved_word_dict[token]

    if G.EMIT_MODE == G.Mode.REGEX:
        return translation

    if G.EMIT_MODE == G.Mode.FREE_SPACED_REGEX:
        return free_space(translation, "End of string")

    raise ValueError("Invalid emit mode")


### IMPORT THESE ###

start_anchor: ParserElement = start_of_line_def | start_of_string_def
end_anchor: ParserElement = end_of_line_def | end_of_string_def

### END ###
