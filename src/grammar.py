#!/usr/bin/env python3

"""
GRAMMAR
"""

import pyparsing as pp
from typing import Any

from .chars import *
from .anchors import *
from .quantifiers import *
from .constants import *
from .utils import *


# A simple flat list for now
pattern_def: pp.ParserElement = non_consuming_char | consuming_chars | quantifier_def

remake_spec: pp.ParserElement = (
    pp.Opt(start_anchor) + pp.OneOrMore(pattern_def) + pp.Opt(end_anchor)
)


### TODO - NYI SCRAPS ###

name: pp.Word = pp.Word(pp.alphas, pp.alphanums + "_")

not_def: pp.CaselessKeyword = pp.CaselessKeyword("Not")


### FOR TESTING ###

keywords: pp.ParserElement = (
    start_anchor | end_anchor | non_consuming_char | consuming_chars | not_def
)

### END ###
