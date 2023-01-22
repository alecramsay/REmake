#!/usr/bin/env python3

"""
GRAMMAR
"""

from pyparsing import (
    Opt,
    OneOrMore,
    Word,
    alphas,
    alphanums,
    CaselessKeyword,
    ParserElement,
)
from typing import Any

from .chars import non_consuming_char, consuming_chars, char_class
from .anchors import start_anchor, end_anchor
from .quantifiers import quantifier
from .constants import *
from .utils import *


# A simple flat list for now
pattern_def: ParserElement = (
    non_consuming_char | consuming_chars | quantifier | char_class
)

remake_spec: ParserElement = (
    Opt(start_anchor) + OneOrMore(pattern_def) + Opt(end_anchor)
)


### TODO - NYI SCRAPS ###

name: Word = Word(alphas, alphanums + "_")

not_def: CaselessKeyword = CaselessKeyword("Not")


### FOR TESTING ###

keywords: ParserElement = (
    start_anchor | end_anchor | non_consuming_char | consuming_chars | not_def
)

### END ###
