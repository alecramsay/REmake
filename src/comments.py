#!/usr/bin/env python3

"""
COMMENTS
"""

from pyparsing import Regex, QuotedString, ParserElement

from .constants import *
from .utils import *


def remove_comments(line: str) -> str:
    """Filter Python-style comments from a line of text."""

    filtered: ParserElement = Regex(r"#.*")

    filtered = filtered.suppress()
    qs: ParserElement = QuotedString('"') | QuotedString("'")
    filtered = filtered.ignore(qs)

    return filtered.transform_string(line)


### END ###
