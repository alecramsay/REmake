#!/usr/bin/env python3

"""
SCANNER
"""

import pyparsing as pp


def parse() -> None:
    greet = pp.Word(pp.alphas) + "," + pp.Word(pp.alphas) + "!"
    for greeting_str in [
        "Hello, World!",
        "Bonjour, Monde!",
        "Hola, Mundo!",
        "Hallo, Welt!",
    ]:
        greeting = greet.parse_string(greeting_str)
        print(greeting)
