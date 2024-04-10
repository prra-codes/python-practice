# 15. Replace all vowel to exclamation mark in the sentence, Tue, 9/04/23

# Description:

# Replace all vowel to exclamation mark in the sentence. aeiouAEIOU is vowel.

# Examples

# replace("Hi!") === "H!!"
# replace("!Hi! Hi!") === "!H!! H!!"
# replace("aeiou") === "!!!!!"
# replace("ABCDE") === "!BCD!"

def replace_exclamation(st):
    replaced = st.replace("a", "!").replace("e", "!").replace("i", "!").replace("o", "!").replace("u", "!").replace("A", "!").replace("E", "!").replace("I", "!").replace("O", "!").replace("U", "!")
    return replaced