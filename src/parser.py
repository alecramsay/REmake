#!/usr/bin/env python3

"""
PARSER
"""

import pyparsing as pp
from typing import Any

import src.globals
from .readwrite import *
from .comments import *
from .grammar import *
from .constants import *
from .utils import *


def parse_lines(
    lines: list[str],
    *,
    mode: src.globals.Mode = src.globals.Mode.TOKENS,
    flavor: src.globals.Flavor = src.globals.Flavor.PYTHON,
    verbose: bool = False,
) -> pp.ParseResults:
    """Parse multiple lines of source code & emit mode+flavor output."""

    src.globals.EMIT_MODE = mode
    src.globals.EMIT_FLAVOR = flavor

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
    src.globals.EMIT_MODE = src.globals.Mode.TOKENS
    src.globals.EMIT_FLAVOR = src.globals.Flavor.PYTHON

    return results


### END ###
