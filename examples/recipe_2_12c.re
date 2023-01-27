# 2.12 Repeat Part of the Regex a Certain Number of Times
# Hexadecimal number with optional suffix
#
# Regex: \b[a-f0-9]{1,8}h?\b
# Flavor: Python

word_boundary()
any ("a"-"f" | "0"-"9") * 1, 8
"h" * 0, 1
word_boundary()