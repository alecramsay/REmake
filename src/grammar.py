#!/usr/bin/env python3

"""
GRAMMAR
"""

import pyparsing as pp
from typing import Any

from .chars import *
from .anchors import *
from .quantifiers import *
from .settings import *
from .utils import *


# A simple flat list for now
pattern_def: pp.ParserElement = (
    literal_def
    | word_boundary_def
    | digit_def
    | whitespace_def
    | any_char_def
    | quantifier_def
)

remake_spec: pp.ParserElement = (
    pp.Opt(start_of_line_def) + pp.OneOrMore(pattern_def) + pp.Opt(end_of_line_def)
)


### TODO - NYI SCRAPS ###

name: pp.Word = pp.Word(pp.alphas, pp.alphanums + "_")

not_def: pp.CaselessKeyword = pp.CaselessKeyword("Not")


### FOR TESTING ###

keywords: pp.ParserElement = (
    start_of_line_def
    | end_of_line_def
    | start_of_string_def
    | end_of_string_def
    | word_boundary_def
    | digit_def
    | whitespace_def
    | any_char_def
    | not_def
)

### END ###
