# 2.3 Match One of Many Characters
# Example: c[ae]l[ae]nd[ae]r

["c", {"a", "e"}, "l", {"a", "e"}, "n", "d", {"a", "e"}, "r"]

# \d and \D: digits

digit()
not digit()

# \w and \W: word characters

word_char()
not word_char()

# \s and \S: whitespace

whitespace()
not whitespace()