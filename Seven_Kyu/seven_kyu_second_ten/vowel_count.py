#33. Vowel Count, Thu, 11/04/23

# Return the number (count) of vowels in the given string.

# We will consider a, e, i, o, u as vowels for this Kata (but not y).

# The input string will only consist of lower case letters and/or spaces.

def get_count(sentence):
    lowercase = sentence.lower()
    sentence_list = list(sentence)
   
    vowels = ["a", "e", "i", "o", "u"]

    vowel_count = 0

    for char in sentence_list:
        if char in vowels:
            vowel_count = vowel_count + 1

    return vowel_count

print(get_count("I am the Dragon King"))