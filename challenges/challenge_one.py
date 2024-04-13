# Write a function that takes a list of words and returns a
# report of all the words that are longer than 10 characters
# but don't contain a hyphen. If those words are longer than
# 15 characters, then they should be shortened to 15
# characters and have an ellipsis (...) added to the end.

# For example, if the input is:
# [
#   'hello',
#   'nonbiological',
#   'Kay',
#   'this-is-a-long-word',
#   'antidisestablishmentarianism'
# ]
# then the output should be:
# "These words are quite long: nonbiological, antidisestablis..."

def report_long_words(words):
 
    long_words = []
    for word in words:
        if len(word) > 10:
          long_words.append(word)

    unhypenated_words = []
    for word in long_words:
        if "-" not in word:
            unhypenated_words.append(word)
    
    processed_words = []

    for word in unhypenated_words:
      if len(word) > 15:
       longer_word = word[0:15] + "..."
       processed_words.append(longer_word)
      else:
       processed_words.append(word)

    report = "These words are quite long: "
    report = report + ", ".join(processed_words)

    return report
  


print(report_long_words([
    'hello',
    'nonbiological',
    'Kay',
    'this-is-a-long-word',
    'antidisestablishmentarianism'
  ]))

print(report_long_words([
    'cat',
    "dog",
    'rhinosaurus',
    'rhinosaurus-rex',
    'frog',
  ]))

print(
  report_long_words([
    'cat'
  ])
)
