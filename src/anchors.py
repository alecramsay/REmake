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


# TODO
start_of_string_def: pp.CaselessKeyword = pp.CaselessKeyword("StringStart")

# TODO
end_of_string_def: pp.CaselessKeyword = pp.CaselessKeyword("StringEnd")


### END ###
