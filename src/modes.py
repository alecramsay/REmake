#!/usr/bin/env python3

"""
MODES
"""

from pyparsing import (
    Suppress,
    delimited_list,
    Opt,
    Group,
    ParseResults,
    ParserElement,
)

import src.globals as G
from .reserved import *
from .constants import *
from .utils import *


"""
Inline mode modifiers, i.e., toggle on/off for the remainder of the expression:
ignore_case, multi_line, dot_all, free_space 

modes (on: <mode>, <mode>, ... <mode>, off: <mode>, <mode>, ... <mode>)
"""

mode: ParserElement = (
    ignore_case_word | multi_line_word | dot_all_word | free_space_word
)
on_group_def: ParserElement = Group(
    on_word("on") + Suppress(":") + delimited_list(mode)
)
off_group_def: ParserElement = Group(
    off_word("off") + Suppress(":") + delimited_list(mode)
)
mode_groups_def: ParserElement = (
    on_group_def
    ^ off_group_def
    ^ Group(on_group_def + Suppress(",") + off_group_def, aslist=True)
)

beg_modes_def: ParserElement = Suppress(modes_word) + Suppress("(")
end_modes_def: ParserElement = Suppress(")")

# TODO
# @beg_modes_def.set_parse_action
# def beg_modes_act(toks: ParseResults) -> str:
#     translation: str = "(?:"
#     comment: str = f"Begin inline mode modifiers:"

#     return modal_act(
#         toks,
#         translation,
#         comment,
#         tab_inc=1,
#         tok_list=True,
#     )


# TODO
# @end_modes_def.set_parse_action
# def end_modes_act(toks: ParseResults) -> str:
#     return modal_act(
#         toks, ")", f"End of inline mode modifiers", tab_inc=-1, tok_list=True
#     )


def translate_modes(toks) -> str:
    """Translate a combined list of on/off modes to a regex string."""

    translation: str = ""

    if isinstance(toks[0], str):  # Either all on or all off
        translation = "(?" + translate_mode_list(toks) + ")"

    else:  # Mixed on/off
        translation = (
            "(?" + translate_mode_list(toks[0]) + translate_mode_list(toks[1]) + ")"
        )

    return translation


def translate_mode_list(toks) -> str:
    """Translate a list of either on or off modes to a portion of a regex string."""

    translation: str = ""
    translation += "" if toks[0] == "on" else "-"
    for tok in toks[1:]:
        # token: str = unpack_token(toks, grouped=True)
        translation += translate_word(tok)

    return translation


# TODO
@mode_groups_def.set_parse_action
def mode_groups_act(toks: list) -> str:
    translation: str = "TODO"
    comment: str = "TODO"

    # translation: str = translate_modes(toks)
    # comment: str = f"Inline mode modifiers"
    return modal_act(toks, translation, comment)


modes_pattern_def: ParserElement = beg_modes_def + mode_groups_def + end_modes_def


### IMPORT THESE ###

modes_pattern: ParserElement = modes_pattern_def

### END ###
