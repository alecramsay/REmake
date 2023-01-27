#!/usr/bin/env python3
#

"""
GENERATE RAILROAD DIAGRAM
"""

from pyparsing import ParserElement
from src import *


def main() -> None:

    Grammar: ParserElement = remake_spec

    Grammar.create_diagram("temp/railroad_diagram.html")


if __name__ == "__main__":
    main()

### END ###
