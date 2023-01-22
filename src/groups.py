#!/usr/bin/env python3

"""
GROUPS
"""

# TODO - Add emit actions

from pyparsing import (
    Forward,
    Suppress,
    CaselessKeyword,
    delimited_list,
    Word,
    alphas,
    ParseResults,
    ParserElement,
)

import src.globals as G
from .chars import quantified_char, non_consuming_char
from .quantifiers import quantifier
from .constants import *
from .utils import *


### PATTERN ###

pattern: Forward = Forward()


### NON-GROUP PATTERNS ###

simple_pattern: ParserElement = quantified_char | non_consuming_char


### ALTERNATION ###

"""
Any { pattern1 | pattern2 | ... | patternN }
"""

beg_alt_def: ParserElement = Suppress(CaselessKeyword("Any")) + Suppress("{")
end_alt_def: ParserElement = Suppress("}")


@beg_alt_def.set_parse_action
def beg_alt_act(toks: ParseResults) -> str:
    if G.EMIT_MODE == G.Mode.TOKENS:
        return toks

    translation: str = "("

    if G.EMIT_MODE == G.Mode.REGEX:
        return translation

    if G.EMIT_MODE == G.Mode.FREE_SPACED_REGEX:
        comment: str = f"One alternative:"
        return free_space(translation, comment)

    raise ValueError("Invalid emit mode")


@end_alt_def.set_parse_action
def end_alt_act(toks: ParseResults) -> str:
    if G.EMIT_MODE == G.Mode.TOKENS:
        return toks

    translation: str = ")"

    if G.EMIT_MODE == G.Mode.REGEX:
        return translation

    if G.EMIT_MODE == G.Mode.FREE_SPACED_REGEX:
        comment: str = f"End of alternatives"
        return free_space(translation, comment)

    raise ValueError("Invalid emit mode")


alt_pattern: ParserElement = (
    beg_alt_def + delimited_list(pattern, delim="|") + end_alt_def
)

### NON-CAPTURING GROUPS (UNNAMED SEQUENCES) ###

"""
All [ pattern1, pattern2, ... , patternN ]
"""

beg_noncapturing_def: ParserElement = Suppress(CaselessKeyword("All")) + Suppress("[")
end_noncapturing_def: ParserElement = Suppress("]")


@beg_noncapturing_def.set_parse_action
def beg_noncapturing_act(toks: ParseResults) -> str:
    if G.EMIT_MODE == G.Mode.TOKENS:
        return toks

    translation: str = "("

    if G.EMIT_MODE == G.Mode.REGEX:
        return translation

    if G.EMIT_MODE == G.Mode.FREE_SPACED_REGEX:
        comment: str = f"All sequentially:"
        return free_space(translation, comment)

    raise ValueError("Invalid emit mode")


@end_noncapturing_def.set_parse_action
def end_noncapturing_act(toks: ParseResults) -> str:
    if G.EMIT_MODE == G.Mode.TOKENS:
        return toks

    translation: str = ")"

    if G.EMIT_MODE == G.Mode.REGEX:
        return translation

    if G.EMIT_MODE == G.Mode.FREE_SPACED_REGEX:
        comment: str = f"End of sequence"
        return free_space(translation, comment)

    raise ValueError("Invalid emit mode")


noncapturing_pattern: ParserElement = (
    beg_noncapturing_def + delimited_list(pattern, delim=",") + end_noncapturing_def
)


### CAPTURING GROUPS (NAMED SEQUENCES) ###

"""
AllAs name[ pattern1, pattern2, ... , patternN ]
"""

beg_capturing_def: ParserElement = (
    Suppress(CaselessKeyword("AllAs")) + Word(alphas)("id") + Suppress("[")
)
end_capturing_def: ParserElement = Suppress("]")


@beg_capturing_def.set_parse_action
def beg_capturing_act(toks: ParseResults) -> str:
    if G.EMIT_MODE == G.Mode.TOKENS:
        return toks

    name: str = toks["id"]
    translation: str = f"(?<{name}>"

    if G.EMIT_MODE == G.Mode.REGEX:
        return translation

    if G.EMIT_MODE == G.Mode.FREE_SPACED_REGEX:
        comment: str = f"All sequentially as '{name}':"
        return free_space(translation, comment)

    raise ValueError("Invalid emit mode")


@end_capturing_def.set_parse_action
def end_capturing_act(toks: ParseResults) -> str:
    if G.EMIT_MODE == G.Mode.TOKENS:
        return toks

    translation: str = ")"

    if G.EMIT_MODE == G.Mode.REGEX:
        return translation

    if G.EMIT_MODE == G.Mode.FREE_SPACED_REGEX:
        comment: str = f"End of capturing group"
        return free_space(translation, comment)

    raise ValueError("Invalid emit mode")


capturing_pattern: ParserElement = (
    beg_capturing_def + delimited_list(pattern, delim=",") + end_capturing_def
)


pattern_list: ParserElement = pattern[...]


### IMPORT THIS ###

pattern <<= (
    alt_pattern
    | noncapturing_pattern
    | capturing_pattern
    | simple_pattern
    | pattern_list
)


### END ###
