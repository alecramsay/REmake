#!/usr/bin/env python3

"""
QUANTIFIERS
"""

from pyparsing import (
    Keyword,
    Word,
    nums,
    Literal,
    Suppress,
    Opt,
    ParseResults,
    ParserElement,
)
from typing import Any

import src.globals as G
from .constants import *
from .utils import *


ellipsis: Literal = Literal("...")
quantifier_def: ParserElement = (
    Suppress("*")
    + (
        Word(nums)("mincount") + Suppress(",") + Word(nums)("maxcount")
        | Word(nums)("mincount") + Suppress(",") + ellipsis
        | ellipsis + Suppress(",") + Word(nums)("maxcount")
        | Word(nums)("count")
    )
    + Opt(Keyword("least"))("lazy")
)


@quantifier_def.set_parse_action
def quantifier_act(toks: ParseResults) -> str:
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


### IMPORT THESE ###

quantifier: ParserElement = quantifier_def

### END ###
