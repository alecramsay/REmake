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
    Char,
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
any ( <pattern> | <pattern> | ... | <pattern> )
any as <name> ( <pattern> | <pattern> | ... | <pattern> )
"""

beg_alt_def: ParserElement = Suppress(any_word) + Suppress("(")
alt_delim_def: ParserElement = Char("|")
end_alt_def: ParserElement = Suppress(")")


@beg_alt_def.set_parse_action
def beg_alt_act(toks: ParseResults) -> str:
    return modal_act(toks, "(?:", f"Begin alternatives:", tab_inc=1, tok_list=True)


@alt_delim_def.set_parse_action
def alt_delim_act(toks: ParseResults) -> str:
    return modal_act(toks, "|", f"-or-")


@end_alt_def.set_parse_action
def end_alt_act(toks: ParseResults) -> str:
    return modal_act(toks, ")", f"End of alternatives", tab_inc=-1, tok_list=True)


alt_pattern: ParserElement = (
    beg_alt_def + pattern + (alt_delim_def + pattern)[1, ...] + end_alt_def
)


### GROUPS - CAPTURING AND NON-CAPTURING SEQUENCES ###

"""
all ( <pattern>, <pattern>, ..., <pattern> )
all as <name> ( <pattern>, <pattern>, ..., <pattern> )
"""

beg_group_def: ParserElement = (
    Suppress(all_word)
    + Opt(Suppress(as_word) + Word(identchars, identbodychars)("id"))
    + Suppress("(")
)
end_group_def: ParserElement = Suppress(")")


@beg_group_def.set_parse_action
def beg_group_act(toks: ParseResults) -> str:
    translation: str = "(?:"
    comment: str = f"Begin group (not captured):"

    if "id" in toks:
        name: str = toks["id"]

        if name in G.GROUP_IDS:
            raise ValueError(f"Duplicate group name '{name}'")
        else:
            G.GROUP_IDS[name] = "DEFINED"

        translation = f"(?<{name}>"
        f"Begin group (captured in '{name}'):"

    return modal_act(
        toks,
        translation,
        comment,
        tab_inc=1,
        tok_list=True,
    )


@end_group_def.set_parse_action
def end_group_act(toks: ParseResults) -> str:
    return modal_act(toks, ")", f"End of group", tab_inc=-1, tok_list=True)


capturing_pattern: ParserElement = (
    beg_group_def + delimited_list(pattern, delim=",") + end_group_def
)


# A REFERENCE TO A NAMED CAPTURING GROUP

id_def: Word = ~reserved_words + Word(identchars, identbodychars)


@id_def.set_parse_action
def id_act(toks: ParseResults) -> str:
    id: str = unpack_token(toks)
    translation: str = f"(?P={id})"
    comment: str = f"Reference to '{id}' capturing group"

    if id not in G.GROUP_IDS:
        raise ValueError(f"Undefined group name '{id}'")

    return modal_act(toks, translation, comment)


### IMPORT THESE ###

atomic_pattern: ParserElement = (
    (alt_pattern + Opt(quantifier))
    ^ (capturing_pattern + Opt(quantifier))
    ^ (consuming_char + Opt(quantifier))
    ^ (id_def + Opt(quantifier))
    ^ non_consuming_char
)  # This is not an atomic *group*.

### END ###
