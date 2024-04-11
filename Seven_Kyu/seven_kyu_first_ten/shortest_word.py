#25. Shortest Word, Wed, 10/04/23

# Simple, given a string of words, return the length of the shortest word(s).

# String will never be empty and you do not need to account for different data types.

def find_short(s):
   word_list = s.split()

   shortest_word = word_list[0]

   for word in word_list:
      if len(word) < len(shortest_word):
         shortest_word = word

   return len(shortest_word)

print(find_short("Superman will be him"))