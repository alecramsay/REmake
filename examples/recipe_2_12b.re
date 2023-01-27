# 2.12 Repeat Part of the Regex a Certain Number of Times
# Hexadecimal number
#
# Regex: \b[a-f0-9]{1,8}\b
# Flavor: Python

word_boundary()
any ("a"-"f" | "0"-"9") * 1, 8
word_boundary()