# 2.3 Match One of Many Characters
#
# Regex: c[ae]l[ae]nd[ae]r
# Flavor: Python

"c"
alternative("a" | "e")
"l"
alternative("a" | "e")
"nd"
alternative("a" | "e")
"r"