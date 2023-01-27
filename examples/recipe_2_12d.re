# 2.12 Repeat Part of the Regex a Certain Number of Times
# Floating-point number
# Modified group to be non-capturing
#
# Regex: \d*\.\d+(?:e\d+)?
# Flavor: Python

digit() * 0, ...
period()
digit() * 1, ...
all (
  "e"
  digit() * 1, ...
) * 0, 1