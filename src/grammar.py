#!/usr/bin/env python3

"""
GRAMMAR
"""

from pyparsing import (
    Opt,
    Word,
    alphas,
    alphanums,
    CaselessKeyword,
    ParserElement,
)

from .groups import pattern
from .anchors import start_anchor, end_anchor
from .constants import *
from .utils import *


# A simple flat list for now
remake_spec: ParserElement = Opt(start_anchor) + pattern + Opt(end_anchor)


### TODO - NYI SCRAPS ###

name: Word = Word(alphas, alphanums + "_")

not_def: CaselessKeyword = CaselessKeyword("Not")


### END ###
