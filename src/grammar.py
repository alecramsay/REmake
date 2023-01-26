#!/usr/bin/env python3

"""
GRAMMAR
"""

from pyparsing import (
    Opt,
    Keyword,
    ParserElement,
)

from .reserved import *
from .constants import *
from .utils import *
from .groups import pattern, atomic_pattern
from .anchors import start_anchor, end_anchor


# NOTE - The forward declaration of 'pattern' is in utils.py,
#   so groups & lookarounds can be defined in terms of patterns.

pattern_list: ParserElement = pattern[...]

pattern <<= atomic_pattern[...] | pattern_list


### IMPORT THIS ###

remake_spec: ParserElement = Opt(start_anchor) + pattern + Opt(end_anchor)

### END ###
