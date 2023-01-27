# 2.16 Test for a Match Without Adding It to the Overall Match
#
# Regex: (?<=<b>)\w+(?=</b>)
# Flavor: Python

preceded_by("<b>")
word_character() * 1, ...
followed_by("</b>")