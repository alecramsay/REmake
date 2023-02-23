# 2.9 Group and Capture Parts of the Match
#
# Regex: \b(?:Mary|Jane|Sue)\b
# Flavor: Python

word_boundary()
alternative("Mary" | "Jane" | "Sue")
word_boundary()