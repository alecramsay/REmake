# 2.3 Match One of Many Characters
#
# Regex: c[ae]l[ae]nd[ae]r
# Flavor: Python

"c"
any("a" | "e")
"l"
any("a" | "e")
"nd"
any("a" | "e")
"r"

# TODO - These are being parsed as alternative as opposed to character classes.