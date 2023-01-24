#!/usr/bin/env python3

"""
GROUPS
"""

from pyparsing import (
    Forward,
    Suppress,
    delimited_list,
    Word,
    identchars,
    identbodychars,
    Opt,
    ParseResults,
    ParserElement,
)

import src.globals as G
from .reserved import *
from .constants import *
from .utils import *
from .chars import consuming_char, non_consuming_char
from .quantifiers import quantifier


### PATTERN ###

pattern: Forward = Forward()


### ALTERNATION ###

"""
any ( pattern1 | pattern2 | ... | patternN )
"""

beg_alt_def: ParserElement = Suppress(any_word) + Suppress("(")
end_alt_def: ParserElement = Suppress(")")


@beg_alt_def.set_parse_action
def beg_alt_act(toks: ParseResults) -> str:
    return modal_act(toks, "(", f"One alternative:", tab_inc=1)


@end_alt_def.set_parse_action
def end_alt_act(toks: ParseResults) -> str:
    return modal_act(toks, ")", f"End of alternatives", tab_inc=-1)


alt_pattern: ParserElement = (
    beg_alt_def + delimited_list(pattern, delim="|") + end_alt_def
)

### NON-CAPTURING GROUPS (UNNAMED SEQUENCES) ###

"""
all ( pattern1, pattern2, ... , patternN )
"""

beg_noncapturing_def: ParserElement = Suppress(all_word) + Suppress("(")
end_noncapturing_def: ParserElement = Suppress(")")


@beg_noncapturing_def.set_parse_action
def beg_noncapturing_act(toks: ParseResults) -> str:
    return modal_act(toks, "(", f"All sequentially (not captured):", tab_inc=1)


@end_noncapturing_def.set_parse_action
def end_noncapturing_act(toks: ParseResults) -> str:
    return modal_act(toks, ")", f"End of non-capturing group", tab_inc=-1)


noncapturing_pattern: ParserElement = (
    beg_noncapturing_def + delimited_list(pattern, delim=",") + end_noncapturing_def
)


### CAPTURING GROUPS (NAMED SEQUENCES) ###

"""
all as name ( pattern1, pattern2, ... , patternN )
"""

beg_capturing_def: ParserElement = (
    Suppress(all_word)
    + Suppress(as_word)
    + Word(identchars, identbodychars)("id")
    + Suppress("(")
)
end_capturing_def: ParserElement = Suppress(")")


@beg_capturing_def.set_parse_action
def beg_capturing_act(toks: ParseResults) -> str:
    name: str = toks["id"]
    translation: str = f"(?<{name}>"

    return modal_act(
        toks, translation, f"All sequentially (captured in '{name}'):", tab_inc=1
    )


@end_capturing_def.set_parse_action
def end_capturing_act(toks: ParseResults) -> str:
    return modal_act(toks, ")", f"End of capturing group", tab_inc=-1)


capturing_pattern: ParserElement = (
    beg_capturing_def + delimited_list(pattern, delim=",") + end_capturing_def
)


# A REFERENCE TO A NAMED CAPTURING GROUP

# TODO - ADD SYMBOL TABLE LOOKUP

id_def: Word = ~reserved_words + Word(identchars, identbodychars)


@id_def.set_parse_action
def name_act(toks: ParseResults) -> str:
    if G.EMIT_MODE == G.Mode.TOKENS:
        return toks

    name: str = toks[0]
    translation: str = f"(?P={name})"

    if G.EMIT_MODE == G.Mode.REGEX:
        return translation

    if G.EMIT_MODE == G.Mode.FREE_SPACED_REGEX:
        comment: str = f"Reference to '{name}' capturing group"
        return free_space(translation, comment)

    raise ValueError("Invalid emit mode")


### IMPORT THESE ###

atomic_pattern: ParserElement = (
    (alt_pattern + Opt(quantifier))
    ^ (noncapturing_pattern + Opt(quantifier))
    ^ (capturing_pattern + Opt(quantifier))
    ^ (consuming_char + Opt(quantifier))
    ^ (id_def + Opt(quantifier))
    ^ non_consuming_char
)  # This is not an atomic *group*.

### END ###
