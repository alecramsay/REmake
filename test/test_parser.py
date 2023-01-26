#!/usr/bin/env python3
#
# TEST GRAMMAR
#

import os
from pyparsing import ParseResults

import src.globals as G
from src.readwrite import read_source_file, FileSpec
from src.parser import parse_lines


class TestParser:
    def test_something(self) -> None:
        examples_dir: str = "examples/"
        examples: list[str] = os.listdir(examples_dir)

        for example in examples:
            rel_path: str = examples_dir + example

            if FileSpec(rel_path).extension != ".re":
                continue

            try:
                lines: list[str] = read_source_file(rel_path)

                expected: str = ""
                for line in lines:
                    if line.startswith("# Regex:"):
                        expected = line[9:].strip()
                        break

                results: ParseResults = parse_lines(lines, mode=G.Mode.REGEX)
                actual: str = "".join(list(results))

                assert actual == expected

            except:
                assert False


### END ###
