#!/usr/bin/env python3

"""
EMITTER
"""

import pyparsing as pp
from typing import Any


def is_quoted_string(token: str) -> bool:
    """Return True if token is a quoted string, False otherwise."""

    return (token.startswith('"') and token.endswith('"')) or (
        token.startswith("'") and token.endswith("'")
    )


def emit(results: pp.ParseResults) -> tuple[str, str]:
    """Emit single-line & free-spaced regex from a parse tree."""

    single_line: str = ""
    free_spaced: str = ""

    for result in results:
        translation: str
        comment: str = (result.replace("_", " ")).capitalize()

        if result == "start_of_line":
            translation = "^"

        elif result == "end_of_line":
            translation = "$"

        elif result == "word_boundary":
            translation = "\b"

        elif result == "digit":
            translation = "\d"

        elif result == "whitespace":
            translation = "\s"

        elif result == "any_char":
            translation = "."
            comment = "Any character"

        # Literal text
        elif is_quoted_string(result):
            translation = result[1:-1]
            comment = "Literal text"

        else:
            raise NotImplementedError(f"Unimplemented result: {result}")

        single_line += translation

        spaces: str = " " * (20 - len(translation))
        free_spaced += translation + spaces + "# " + comment + "\n"

    return single_line, free_spaced
