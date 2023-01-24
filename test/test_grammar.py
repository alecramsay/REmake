#!/usr/bin/env python3
#
# TEST GRAMMAR
#

from pyparsing import ParseResults, ParserElement
from typing import Any

from src.grammar import *
from src.readwrite import read_source_file
from src.comments import remove_comments
from src.anchors import start_anchor, end_anchor
from src.chars import consuming_char, non_consuming_char


class TestParser:
    def test_something(self) -> None:
        pass


### END ###
