#!/usr/bin/env python3

"""
GRAMMAR
"""

from pyparsing import (
    StringStart,
    StringEnd,
    Opt,
    Keyword,
    ParserElement,
)

from .groups import pattern, atomic_pattern
from .anchors import start_anchor, end_anchor
from .constants import *
from .utils import *


# NOTE - The forward declaration of 'pattern' is in groups.py,
#   so groups can be defined in terms of patterns.

pattern_list: ParserElement = pattern[...]

pattern <<= atomic_pattern[...] | pattern_list

# TODO
# remake_spec: ParserElement = (
#     StringStart() + Opt(start_anchor) + pattern + Opt(end_anchor) + StringEnd()
# )
remake_spec: ParserElement = Opt(start_anchor) + pattern + Opt(end_anchor)

### TODO - NYI SCRAPS ###

not_def: Keyword = Keyword("not")


### END ###
