#!/usr/bin/env python3

"""
ANCHORS
"""

import pyparsing as pp
from typing import Any

from .settings import *
from .utils import *


start_of_line_def: pp.CaselessKeyword = pp.CaselessKeyword("LineStart")


@start_of_line_def.set_parse_action
def start_of_line_act(toks: pp.ParseResults) -> str:
    global EMIT_MODE
    global EMIT_FLAVOR

    if EMIT_MODE == Mode.TOKENS:
        return toks[0]

    translation: str = "^"

    if EMIT_MODE == Mode.REGEX:
        return translation

    if EMIT_MODE == Mode.FREE_SPACED_REGEX:
        return free_space(translation, "Start of line")

    raise ValueError("Invalid emit mode")


end_of_line_def: pp.CaselessKeyword = pp.CaselessKeyword("LineEnd")


@end_of_line_def.set_parse_action
def end_of_line_act(toks: pp.ParseResults) -> str:
    global EMIT_MODE
    global EMIT_FLAVOR

    if EMIT_MODE == Mode.TOKENS:
        return toks[0]

    translation: str = "$"

    if EMIT_MODE == Mode.REGEX:
        return translation

    if EMIT_MODE == Mode.FREE_SPACED_REGEX:
        return free_space(translation, "End of line")

    raise ValueError("Invalid emit mode")


start_of_string_def: pp.CaselessKeyword = pp.CaselessKeyword("StringStart")


@start_of_string_def.set_parse_action
def start_of_string_act(toks: pp.ParseResults) -> str:
    global EMIT_MODE
    global EMIT_FLAVOR

    if EMIT_MODE == Mode.TOKENS:
        return toks[0]

    translation: str = "\A"

    if EMIT_MODE == Mode.REGEX:
        return translation

    if EMIT_MODE == Mode.FREE_SPACED_REGEX:
        return free_space(translation, "Start of string")

    raise ValueError("Invalid emit mode")


end_of_string_def: pp.CaselessKeyword = pp.CaselessKeyword("StringEnd")


@end_of_string_def.set_parse_action
def end_of_string_act(toks: pp.ParseResults) -> str:
    global EMIT_MODE
    global EMIT_FLAVOR

    if EMIT_MODE == Mode.TOKENS:
        return toks[0]

    translation: str = "\Z"

    if EMIT_MODE == Mode.REGEX:
        return translation

    if EMIT_MODE == Mode.FREE_SPACED_REGEX:
        return free_space(translation, "End of string")

    raise ValueError("Invalid emit mode")


start_anchor: pp.ParserElement = start_of_line_def | start_of_string_def
end_anchor: pp.ParserElement = end_of_line_def | end_of_string_def

### END ###
