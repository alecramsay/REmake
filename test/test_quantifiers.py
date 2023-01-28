#!/usr/bin/env python3
#
# TEST QUANTIFIERS
#

from src.quantifiers import *


class TestQuantifiers:
    def test_quantifiers(self) -> None:
        Grammar: Any = quantifier_def

        input: str = "* 10"
        results: ParseResults = Grammar.parseString(input)
        assert list(results) == ["10"]

        input: str = "* 0, ..."
        results: ParseResults = Grammar.parseString(input)
        assert list(results) == ["0", "..."]

        input: str = "* 1,3"
        results: ParseResults = Grammar.parseString(input)
        assert list(results) == ["1", "3"]

        input: str = "* 1,3 lazy"
        results: ParseResults = Grammar.parseString(input)
        assert list(results) == ["1", "3", "lazy"]


### END ###
