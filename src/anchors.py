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


start_of_line_def: ParserElement = Group(line_start_word + Suppress("()"))


@start_of_line_def.set_parse_action
def start_of_line_act(toks: ParseResults) -> str | list[str]:
    token: str = unpack_token(toks, grouped=True)
    translation: str = translate_word(token)
    comment: str = f"Start of line"

    return modal_act(toks, translation, comment)


end_of_line_def: ParserElement = Group(line_end_word + Suppress("()"))


@end_of_line_def.set_parse_action
def end_of_line_act(toks: ParseResults) -> str | list[str]:
    token: str = unpack_token(toks, grouped=True)
    translation: str = translate_word(token)
    comment: str = f"End of line"

    return modal_act(toks, translation, comment)


start_of_string_def: ParserElement = Group(string_start_word + Suppress("()"))


@start_of_string_def.set_parse_action
def start_of_string_act(toks: ParseResults) -> str | list[str]:
    token: str = unpack_token(toks, grouped=True)
    translation: str = translate_word(token)
    comment: str = f"Start of string"

    return modal_act(toks, translation, comment)


end_of_string_def: ParserElement = Group(string_end_word + Suppress("()"))


@end_of_string_def.set_parse_action
def end_of_string_act(toks: ParseResults) -> str | list[str]:
    token: str = unpack_token(toks, grouped=True)
    translation: str = translate_word(token)
    comment: str = f"End of string"

    return modal_act(toks, translation, comment)


### IMPORT THESE ###

start_anchor: ParserElement = start_of_line_def | start_of_string_def
end_anchor: ParserElement = end_of_line_def | end_of_string_def

### END ###
