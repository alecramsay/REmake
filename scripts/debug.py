#!/usr/bin/env python3
#

"""
DEBUG REmake
"""

from src import *


### ARGUMENTS ###

# source: str = "test/files/sample.re"
# source: str = "test/files/sample2.re"
# source: str = "test/files/atomic_words.re"
# source: str = "test/files/lookarounds.re"
source: str = "examples/recipe_2_11d.re"

verbose: bool = True


def main() -> None:

    # <deleted>

    # PARSE SOURCE FILE & GENERATE REGEX
    lines: list[str] = read_source_file(source)

    results: ParseResults = parse_lines(lines, mode=G.Mode.REGEX)
    single_line: str = "".join(list(results))

    results: ParseResults = parse_lines(lines, mode=G.Mode.FREE_SPACED_REGEX)
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
