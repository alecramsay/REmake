#!/usr/bin/env python3

"""
GLOBAL SETTINGS
"""

from enum import Enum
from typing import Any


Mode: Any = Enum("Mode", ["TOKENS", "REGEX", "FREE_SPACED_REGEX"])
EMIT_MODE: Mode = Mode.TOKENS

Flavor: Any = Enum("Flavor", ["PYTHON"])
EMIT_FLAVOR: Flavor = Flavor.PYTHON

COMMENT_TAB: int = 20

### END ###
