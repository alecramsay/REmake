#!/usr/bin/env python3

"""
READ/WRITE ROUTINES
"""

import os

# import readline


def read_source(rel_path) -> list[str]:
    """
    Read a source file into a list of strings.
    """

    abs_path: str = FileSpec(rel_path).abs_path

    try:
        with open(abs_path, "r") as f:
            lines: list = list()
            line: str = f.readline()

            lines.append(line)

        return lines

    except:
        raise Exception("Exception reading source file.")


class FileSpec:
    def __init__(self, path: str, name=None) -> None:
        file_name: str
        file_extension: str
        file_name, file_extension = os.path.splitext(path)

        self.rel_path: str = path
        self.abs_path: str = os.path.abspath(path)
        self.name: str = name.lower() if (name) else os.path.basename(file_name).lower()
        self.extension: str = file_extension


### END ###
