#!/usr/bin/env python3

"""
LOOKAROUNDS
"""

from pyparsing import (
    Suppress,
    Opt,
    ParseResults,
    ParserElement,
)

import src.globals as G
from .reserved import *
from .constants import *
from .utils import *


"""
not* followed_by ( <pattern> )
"""

beg_lookahead_def: ParserElement = (
    Opt(not_word)("negated") + Suppress(followed_by_word) + Suppress("(")
)
end_lookahead_def: ParserElement = Suppress(")")


@beg_lookahead_def.set_parse_action
def beg_lookahead_act(toks: ParseResults) -> str:
    translation: str = "(?!" if toks.negated else "(?="
    qualifier: str = " (negative)" if toks.negated else ""
    comment: str = f"Begin lookhead{qualifier}:"

    return modal_act(
        toks,
        translation,
        comment,
        tab_inc=1,
        tok_list=True,
    )


@end_lookahead_def.set_parse_action
def end_lookahead_act(toks: ParseResults) -> str:
    return modal_act(toks, ")", f"End of lookhead", tab_inc=-1, tok_list=True)


lookahead_pattern: ParserElement = beg_lookahead_def + pattern + end_lookahead_def


"""
not* preceded_by ( <pattern> )
"""

beg_lookbehind_def: ParserElement = (
    Opt(not_word)("negated") + Suppress(preceded_by_word) + Suppress("(")
)
end_lookbehind_def: ParserElement = Suppress(")")


@beg_lookbehind_def.set_parse_action
def beg_lookbehind_act(toks: ParseResults) -> str:
    translation: str = "(?<!" if toks.negated else "(?<="
    qualifier: str = " (negative)" if toks.negated else ""
    comment: str = f"Begin lookbehind{qualifier}:"

    return modal_act(
        toks,
        translation,
        comment,
        tab_inc=1,
        tok_list=True,
    )


@end_lookbehind_def.set_parse_action
def end_lookbehind_act(toks: ParseResults) -> str:
    return modal_act(toks, ")", f"End of lookbehind", tab_inc=-1, tok_list=True)


lookbehind_pattern: ParserElement = beg_lookbehind_def + pattern + end_lookbehind_def


### IMPORT THESE ###

lookaround_pattern: ParserElement = lookahead_pattern | lookbehind_pattern

### END ###
