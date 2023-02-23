# 2.10 Match Previously Matched Text Again
#
# Modified to use explicit named capture vs. implicit numbered capture.
#
# Regex: \b\d\d(?P<magic>\d\d)-(?P=magic)-(?P=magic)\b
# Flavor: Python

word_boundary()
digit()
digit()
group as magic (
  digit()
  digit()
)
"-"
magic
"-"
magic
word_boundary()
