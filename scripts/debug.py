#!/usr/bin/env python3
#

"""
DEBUG REmake
"""

import argparse
from argparse import ArgumentParser, Namespace

from src import *


### ARGUMENTS ###

source: str = "test/examples/sample.re"
verbose: bool = True


def main() -> None:

    # <deleted>

    # PARSE SOURCE FILE & GENERATE REGEX
    lines: list[str] = read_source_file(source)

    results: pp.ParseResults = parse_lines(lines, mode=Mode.REGEX)
    single_line: str = "".join(list(results))

    results: pp.ParseResults = parse_lines(lines, mode=Mode.FREE_SPACED_REGEX)
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
