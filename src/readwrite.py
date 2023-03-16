#!/usr/bin/env python3

"""
READ/WRITE ROUTINES
"""

import os
from pyutils import FileSpec


def read_source_file(rel_path) -> list[str]:
    """Read a source file into a list of strings."""

    abs_path: str = FileSpec(rel_path).abs_path

    try:
        with open(abs_path, "r") as f:
            lines: list = list()
            line: str = f.readline()
            while line:
                lines.append(line)

                line = f.readline()

        return lines

    except:
        raise Exception("Exception reading source file.")


### END ###
