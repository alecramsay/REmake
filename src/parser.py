#!/usr/bin/env python3

"""
PARSER
"""

import pyparsing as pp
from typing import Any

from .readwrite import *
from .comments import *
from .grammar import *
from .settings import *
from .utils import *


def parse_lines(
    lines: list[str],
    *,
    mode: Mode = Mode.TOKENS,
    flavor: Flavor = Flavor.PYTHON,
    verbose: bool = False,
) -> pp.ParseResults:
    """Parse multiple lines of source code & emit mode+flavor output."""

    global EMIT_MODE
    global EMIT_FLAVOR
    EMIT_MODE = mode
    EMIT_FLAVOR = flavor

    # Remove Python-style comments
    filtered: list[str] = list()
    for line in lines:
        no_comments: str = remove_comments(line)
        filtered.append(no_comments)

    # Reconstitute the source code as a string
    source: str = "".join(filtered)

    results: pp.ParseResults = remake_spec.parseString(source)

    if verbose:
        print(results)

    # Restore the default modes
    EMIT_MODE = Mode.TOKENS
    EMIT_FLAVOR = Flavor.PYTHON

    return results


### END ###
