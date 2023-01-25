# Recipe 5.5

word_boundary()
word_character() * 1, ...
word_boundary()
not followed_by(
  not_word_character() * 1, ...
  "cat"
  word_boundary()
)