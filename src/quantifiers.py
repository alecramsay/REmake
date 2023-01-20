#!/usr/bin/env python3

"""
QUANTIFIERS
"""

import pyparsing as pp
from typing import Any

import src.globals as G
from .constants import *
from .utils import *


ellipsis: pp.Literal = pp.Literal("...")
quantifier_def: pp.ParserElement = (
    pp.Suppress("*")
    + (
        pp.Word(pp.nums)("mincount") + pp.Suppress(",") + pp.Word(pp.nums)("maxcount")
        | pp.Word(pp.nums)("mincount") + pp.Suppress(",") + ellipsis
        | ellipsis + pp.Suppress(",") + pp.Word(pp.nums)("maxcount")
        | pp.Word(pp.nums)("count")
    )
    + pp.Opt(pp.CaselessKeyword("Least"))("lazy")
)


@quantifier_def.set_parse_action
def quantifier_act(toks: pp.ParseResults) -> str:
    if G.EMIT_MODE == G.Mode.TOKENS:
        return toks

    translation: str
    comment: str

    lazy: str = "?" if "lazy" in toks else ""
    style: str = "lazy" if "lazy" in toks else "greedy"

    if "count" in toks:
        if int(toks.count) >= 1:
            translation = f"{{{toks.count}}}{lazy}"
            comment = f"Exactly {translation} times ({style})"
        else:
            raise ValueError("Invalid quantifier: repetitions must be positive")

    elif "mincount" in toks and "maxcount" in toks:
        if int(toks.mincount) == 0 and int(toks.maxcount) == 1:
            translation = f"?{lazy}"
            comment = f"Optionally ({style})"
        elif int(toks.mincount) < int(toks.maxcount):
            translation = f"{{{toks.mincount},{toks.maxcount}}}{lazy}"
            comment = f"Between {toks.mincount} and {toks.maxcount} times ({style})"
        else:
            raise ValueError(
                "Invalid quantifier: min repetitions must be less than max repetitions"
            )

    elif "mincount" in toks:
        if int(toks.mincount) == 0:
            translation = f"*{lazy}"
            comment = f"Zero or more times ({style})"
        elif int(toks.mincount) == 1:
            translation = f"+{lazy}"
            comment = f"One or more times ({style})"
        elif int(toks.mincount) > 1:
            translation = f"{{{toks.mincount},}}{lazy}"
            comment = f"At least {toks.mincount} times ({style})"
        else:
            raise ValueError("Invalid quantifier: repetitions must be positive")

    else:
        raise ValueError("Invalid quantifier")

    if G.EMIT_MODE == G.Mode.REGEX:
        return translation

    if G.EMIT_MODE == G.Mode.FREE_SPACED_REGEX:
        return free_space(translation, comment)

    raise ValueError("Invalid emit mode")


### END ###
