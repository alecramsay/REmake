#!/usr/bin/env python3

"""
CHARACTERS
"""

import pyparsing as pp
from typing import Any

from .settings import *
from .utils import *


def remove_comments(line: str) -> str:
    """Filter Python-style comments from a line of text."""

    filtered: pp.ParserElement = pp.Regex(r"#.*")

    filtered = filtered.suppress()
    qs: pp.ParserElement = pp.QuotedString('"') | pp.QuotedString("'")
    filtered = filtered.ignore(qs)

    return filtered.transform_string(line)


### END ###
