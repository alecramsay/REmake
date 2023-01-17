#!/usr/bin/env python3
#

"""
Make a regular expression from the REmake grammar.

For example:

scripts/REmake.py -f foo.re

For documentation, type:

scripts/REmake.py -h

"""

import argparse
from argparse import ArgumentParser, Namespace

from src import *


### PARSE ARGUMENTS ###


def parse_args() -> Namespace:
    parser: ArgumentParser = argparse.ArgumentParser(
        description="Make a regular expression from the REmake grammar."
    )
    parser.add_argument("-f", "--file", help="Source file of REmake commands", type=str)
    parser.add_argument(
        "-v", "--verbose", dest="verbose", action="store_true", help="Verbose mode"
    )

    args: Namespace = parser.parse_args()
    return args


def main() -> None:
    args: Namespace = parse_args()

    source: str = args.file
    verbose: bool = args.verbose

    # FOR DEBUGGING
    source = "test/examples/section2_1a.re"
    verbose = True

    # PARSE SOURCE FILE & GENERATE REGEX
    lines: list[str] = read_source_file(source)
    tokens: list = parse_lines(lines, verbose)

    pass

    print()
    print("TODO: emit regex")
    print()


if __name__ == "__main__":
    main()

### END ###
