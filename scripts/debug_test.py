#!/usr/bin/env python3
#

"""
DEBUG test example
"""

from pyparsing import ParseResults

import src.globals as G
from src.readwrite import *
from src.parser import parse_lines


source: str = "examples/recipe_2_10.re"
verbose: bool = True


def main() -> None:

    lines: list[str] = read_source_file(source)

    expected: str = ""
    for line in lines:
        if line.startswith("# Regex:"):
            expected = line[9:].strip()
            break

    print()
    print(f"Expected regex: {expected}")

    results: ParseResults = parse_lines(lines, mode=G.Mode.REGEX)
    actual: str = "".join(list(results))

    print(f"Actual regex:   {actual}")

    assert actual == expected


pass


if __name__ == "__main__":
    main()

### END ###
