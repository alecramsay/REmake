#!/usr/bin/env python3
#

"""
Make a regular expression from the REmake grammar.

For example:

scripts/REmake.py sample.re

For documentation, type:

scripts/REmake.py -h

"""

import argparse
from argparse import ArgumentParser, Namespace
from pyparsing import ParseResults

from src import *


### PARSE ARGUMENTS ###


def parse_args() -> Namespace:
    parser: ArgumentParser = argparse.ArgumentParser(
        description="Compile a regular expression from a REmake program."
    )
    parser.add_argument(
        "file", help="Source file containing a REmake program", type=str
    )
    parser.add_argument(
        "-v", "--verbose", dest="verbose", action="store_true", help="Verbose mode"
    )

    args: Namespace = parser.parse_args()
    return args


def main() -> None:
    args: Namespace = parse_args()

    source: str = args.file
    verbose: bool = args.verbose

    # PARSE SOURCE FILE & GENERATE REGEX
    lines: list[str] = read_source_file(source)

    results: ParseResults = parse_lines(lines, mode=G.Mode.REGEX)
    single_line: str = "".join(list(results))

    results: ParseResults = parse_lines(
        lines, mode=G.Mode.FREE_SPACED_REGEX, verbose=verbose
    )
    free_spaced: str = "".join(list(results))

    print()
    print(f"Single-line regex:")
    print(f"{single_line}")
    print()
    print(f"Free-spaced regex:")
    print(f"{free_spaced}")
    print()

    pass


if __name__ == "__main__":
    main()

### END ###
