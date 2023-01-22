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

# from .chars import non_consuming_char, consuming_char, char_class
from .chars import quantified_char, non_consuming_char
from .anchors import start_anchor, end_anchor
from .quantifiers import quantifier
from .constants import *
from .utils import *


# A simple flat list for now
pattern_def: ParserElement = non_consuming_char | quantified_char | quantifier

remake_spec: ParserElement = (
    Opt(start_anchor) + OneOrMore(pattern_def) + Opt(end_anchor)
)


### TODO - NYI SCRAPS ###

name: Word = Word(alphas, alphanums + "_")

not_def: CaselessKeyword = CaselessKeyword("Not")


### FOR TESTING ###

keywords: ParserElement = (
    start_anchor | end_anchor | non_consuming_char | quantified_char | not_def
)

### END ###
