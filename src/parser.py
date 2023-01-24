#!/usr/bin/env python3

"""
PARSER
"""

from pyparsing import ParseResults
from typing import Any

import src.globals as G
from .readwrite import *
from .comments import *
from .grammar import *
from .constants import *
from .utils import *


def parse_lines(
    lines: list[str],
    *,
    mode: G.Mode = G.Mode.TOKENS,
    flavor: G.Flavor = G.Flavor.PYTHON,
    verbose: bool = False,
) -> ParseResults:
    """Parse multiple lines of source code & emit mode+flavor output."""

    G.EMIT_MODE = mode
    G.EMIT_FLAVOR = flavor
    G.GROUP_IDS = dict()

    # Remove Python-style comments
    filtered: list[str] = list()
    for line in lines:
        no_comments: str = remove_comments(line)
        filtered.append(no_comments)

    # Reconstitute the source code as a string
    source: str = "".join(filtered)

    results: ParseResults = remake_spec.parseString(source)

    if verbose:
        print(results)

    # Restore the default modes
    G.EMIT_MODE = G.Mode.TOKENS
    G.EMIT_FLAVOR = G.Flavor.PYTHON
    G.GROUP_IDS = dict()

    return results


### END ###
