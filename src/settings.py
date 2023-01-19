#!/usr/bin/env python3

"""
GLOBAL SETTINGS
"""

from enum import Enum
from typing import Any


Emit: Any = Enum("Emit", ["TOKENS", "REGEX", "FREE_SPACED_REGEX"])

EMIT_MODE: Emit = Emit.TOKENS

### END ###
