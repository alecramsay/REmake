#!/usr/bin/env python3

"""
GLOBALS
"""

from enum import Enum
from typing import Any

Mode: Any = Enum("Mode", ["TOKENS", "REGEX", "FREE_SPACED_REGEX"])
EMIT_MODE: str = Mode.TOKENS

Flavor: Any = Enum("Flavor", ["PYTHON"])
EMIT_FLAVOR: str = Flavor.PYTHON

GROUP_IDS: dict[str, str] = dict()

INDENT_LEVEL: int = 0

### END ###
