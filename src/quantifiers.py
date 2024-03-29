#!/usr/bin/env python3

"""
QUANTIFIERS
"""

from pyparsing import (
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
from .reserved import *
from .constants import *
from .utils import *


ellipsis: Literal = Literal("...")
quantifier_def: ParserElement = (
    Suppress("*")
    + (
        Word(nums)("mincount") + Suppress(",") + Word(nums)("maxcount")
        | Word(nums)("mincount") + Suppress(",") + ellipsis
        # | ellipsis + Suppress(",") + Word(nums)("maxcount")
        | Word(nums)("count")
    )
    + Opt(lazy_word)("lazy")
)


@quantifier_def.set_parse_action
def quantifier_act(toks: ParseResults) -> str | list[str]:
    translation: str
    comment: str

    lazy: str = "?" if "lazy" in toks else ""
    style: str = "lazy" if "lazy" in toks else "greedy"

    if "count" in toks:
        if int(str(toks.count)) >= 1:
            translation = f"{{{toks.count}}}{lazy}"
            comment = f"Exactly {translation} times ({style})"
        else:
            raise ValueError("Invalid quantifier: repetitions must be positive")

    elif "mincount" in toks and "maxcount" in toks:
        if int(str(toks.mincount)) == 0 and int(str(toks.maxcount)) == 1:
            translation = f"?{lazy}"
            comment = f"Optionally ({style})"
        elif int(str(toks.mincount)) < int(str(toks.maxcount)):
            translation = f"{{{toks.mincount},{toks.maxcount}}}{lazy}"
            comment = f"Between {toks.mincount} and {toks.maxcount} times ({style})"
        else:
            raise ValueError(
                "Invalid quantifier: min repetitions must be less than max repetitions"
            )

    elif "mincount" in toks:
        if int(str(toks.mincount)) == 0:
            translation = f"*{lazy}"
            comment = f"Zero or more times ({style})"
        elif int(str(toks.mincount)) == 1:
            translation = f"+{lazy}"
            comment = f"One or more times ({style})"
        elif int(str(toks.mincount)) > 1:
            translation = f"{{{toks.mincount},}}{lazy}"
            comment = f"At least {toks.mincount} times ({style})"
        else:
            raise ValueError("Invalid quantifier: repetitions must be positive")

    else:
        raise ValueError("Invalid quantifier")

    return modal_act(toks, translation, comment, tok_list=True)


### IMPORT THESE ###

quantifier: ParserElement = quantifier_def

### END ###
