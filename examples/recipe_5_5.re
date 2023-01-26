# 5.5 Find Any Word Not Followed by a Specific Word
#
# Regex: \b\w+\b(?!\W+cat\b)
# Flavor: Python

word_boundary()
word_character() * 1, ...
word_boundary()
not followed_by(
  not_word_character() * 1, ...
  "cat"
  word_boundary()
)